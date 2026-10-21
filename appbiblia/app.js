// URL del PDF
const PDF_URL = '/pdf/La_Gran_Historia_de_la_Biblia_Ilustrada.pdf';

// Configuración de Estado
let pdfDoc = null;
let currentPage = 1;
let totalPages = 223;
let pageRendering = false;
let pageNumPending = null;
let scale = 1.0;
let autoFit = true;
let currentRenderTask = null;

// Referencias del DOM
const canvas = document.getElementById('pdfCanvas');
const ctx = canvas.getContext('2d');
const pageInput = document.getElementById('pageInput');
const pageRange = document.getElementById('pageRange');
const totalPagesText = document.getElementById('totalPagesText');
const zoomPercent = document.getElementById('zoomPercent');
const loadingOverlay = document.getElementById('loadingOverlay');
const loadingStatusText = document.getElementById('loadingStatusText');
const viewerContainer = document.getElementById('viewerContainer');
const tocSidebar = document.getElementById('tocSidebar');

// Configuración PDF.js Worker
if (window.pdfjsLib) {
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
}

/**
 * Renderiza la página solicitada en el canvas con alta resolución (HiDPI)
 */
async function renderPage(num) {
  if (!pdfDoc) return;
  if (pageRendering) {
    pageNumPending = num;
    return;
  }
  pageRendering = true;

  try {
    const page = await pdfDoc.getPage(num);

    // Calcular escala automática si autoFit está activo
    if (autoFit && viewerContainer) {
      const containerWidth = viewerContainer.clientWidth - 48; // padding
      const unscaledViewport = page.getViewport({ scale: 1 });
      const fitScale = Math.min(Math.max(containerWidth / unscaledViewport.width, 0.45), 2.2);
      scale = fitScale;
    }

    const dpr = window.devicePixelRatio || 1;
    const viewport = page.getViewport({ scale: scale });

    // Ajustar dimensiones internas del canvas (multiplicado por DPR para nitidez retina)
    canvas.width = Math.floor(viewport.width * dpr);
    canvas.height = Math.floor(viewport.height * dpr);

    // Ajustar tamaño CSS mostrado en pantalla
    canvas.style.width = `${Math.floor(viewport.width)}px`;
    canvas.style.height = `${Math.floor(viewport.height)}px`;

    const renderContext = {
      canvasContext: ctx,
      viewport: viewport,
      transform: dpr !== 1 ? [dpr, 0, 0, dpr, 0, 0] : null
    };

    if (currentRenderTask) {
      try {
        currentRenderTask.cancel();
      } catch (e) {}
    }

    currentRenderTask = page.render(renderContext);
    await currentRenderTask.promise;

    pageRendering = false;

    if (pageNumPending !== null) {
      const nextNum = pageNumPending;
      pageNumPending = null;
      renderPage(nextNum);
    }
  } catch (err) {
    if (err && err.name !== 'RenderingCancelledException') {
      console.error('Error renderizando página:', err);
    }
    pageRendering = false;
  }

  // Actualizar UI
  updateControls();
}

/**
 * Pasa de página de forma segura
 */
function queueRenderPage(num) {
  if (!pdfDoc) return;
  const target = Math.max(1, Math.min(num, totalPages));
  currentPage = target;
  localStorage.setItem('latram_last_biblia_page', target.toString());

  if (pageRendering) {
    pageNumPending = target;
  } else {
    renderPage(target);
  }
}

function prevPage() {
  if (currentPage <= 1) return;
  queueRenderPage(currentPage - 1);
}

function nextPage() {
  if (currentPage >= totalPages) return;
  queueRenderPage(currentPage + 1);
}

/**
 * Actualiza los indicadores visuales y controles
 */
function updateControls() {
  if (pageInput) pageInput.value = currentPage;
  if (pageRange) pageRange.value = currentPage;
  if (totalPagesText) totalPagesText.textContent = totalPages;
  if (zoomPercent) zoomPercent.textContent = `${Math.round(scale * 100)}%`;

  // Botones anterior / siguiente
  const btnPrev = document.getElementById('btnPrevPage');
  const btnNext = document.getElementById('btnNextPage');
  if (btnPrev) btnPrev.disabled = currentPage <= 1;
  if (btnNext) btnNext.disabled = currentPage >= totalPages;

  // Actualizar item activo en Índice
  document.querySelectorAll('.toc-item').forEach(item => {
    const pageTarget = parseInt(item.getAttribute('data-page'), 10);
    if (pageTarget === currentPage) {
      item.classList.add('active');
    } else {
      item.classList.remove('active');
    }
  });

  // Actualizar botones de salto rápido
  document.querySelectorAll('.quick-jump-btn').forEach(btn => {
    const pageTarget = parseInt(btn.getAttribute('data-page'), 10);
    if (pageTarget === currentPage) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });
}

/**
 * Inicialización y Carga del Documento
 */
async function loadPdf() {
  if (!window.pdfjsLib) {
    console.warn('PDF.js no cargó, reintentando...');
    setTimeout(loadPdf, 500);
    return;
  }

  try {
    const loadingTask = pdfjsLib.getDocument({
      url: PDF_URL,
      cMapUrl: 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/cmaps/',
      cMapPacked: true,
    });

    loadingTask.onProgress = function(progressData) {
      if (progressData.total > 0) {
        const percent = Math.min(100, Math.round((progressData.loaded / progressData.total) * 100));
        if (loadingStatusText) {
          loadingStatusText.textContent = `Descargando guía ilustrada (${percent}%)...`;
        }
      }
    };

    pdfDoc = await loadingTask.promise;
    totalPages = pdfDoc.numPages;

    if (pageInput) pageInput.max = totalPages;
    if (pageRange) pageRange.max = totalPages;

    // Recuperar última página leída
    const savedPage = parseInt(localStorage.getItem('latram_last_biblia_page'), 10);
    if (savedPage && savedPage >= 1 && savedPage <= totalPages) {
      currentPage = savedPage;
    } else {
      currentPage = 1;
    }

    // Ocultar overlay
    if (loadingOverlay) {
      loadingOverlay.style.opacity = '0';
      setTimeout(() => loadingOverlay.style.display = 'none', 300);
    }

    renderPage(currentPage);
  } catch (error) {
    console.error('Error cargando PDF:', error);
    if (loadingStatusText) {
      loadingStatusText.innerHTML = `
        <span class="text-rose-400 font-medium">No se pudo cargar el visor directo.</span><br>
        <a href="${PDF_URL}" download class="inline-block mt-3 px-4 py-2 bg-amber-500 text-black font-bold rounded-lg">
          Descargar PDF directamente aquí
        </a>
      `;
    }
  }
}

/**
 * Event Listeners
 */
function setupEvents() {
  // Paginación botones
  document.getElementById('btnPrevPage')?.addEventListener('click', prevPage);
  document.getElementById('btnNextPage')?.addEventListener('click', nextPage);
  document.getElementById('floatingPrev')?.addEventListener('click', prevPage);
  document.getElementById('floatingNext')?.addEventListener('click', nextPage);

  // Input de número de página
  pageInput?.addEventListener('change', (e) => {
    const val = parseInt(e.target.value, 10);
    if (!isNaN(val)) queueRenderPage(val);
  });
  pageInput?.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      const val = parseInt(e.target.value, 10);
      if (!isNaN(val)) queueRenderPage(val);
    }
  });

  // Slider de página
  pageRange?.addEventListener('input', (e) => {
    const val = parseInt(e.target.value, 10);
    if (!isNaN(val)) queueRenderPage(val);
  });

  // Zoom
  document.getElementById('btnZoomIn')?.addEventListener('click', () => {
    autoFit = false;
    scale = Math.min(scale * 1.25, 3.0);
    renderPage(currentPage);
  });

  document.getElementById('btnZoomOut')?.addEventListener('click', () => {
    autoFit = false;
    scale = Math.max(scale / 1.25, 0.4);
    renderPage(currentPage);
  });

  document.getElementById('btnFitWidth')?.addEventListener('click', () => {
    autoFit = true;
    renderPage(currentPage);
  });

  // Pantalla Completa
  document.getElementById('btnFullscreen')?.addEventListener('click', () => {
    if (!document.fullscreenElement) {
      viewerContainer?.requestFullscreen().catch(err => {
        console.warn('Error solicitando fullscreen:', err);
      });
    } else {
      document.exitFullscreen();
    }
  });

  // Drawer / Índice Lateral
  const toggleToc = () => {
    if (tocSidebar) {
      if (window.innerWidth < 768) {
        tocSidebar.classList.toggle('open');
      } else {
        tocSidebar.classList.toggle('hidden');
      }
    }
  };
  document.getElementById('btnToggleToc')?.addEventListener('click', toggleToc);
  document.getElementById('btnCloseToc')?.addEventListener('click', toggleToc);

  // Clicks en elementos del índice
  document.querySelectorAll('.toc-item').forEach(item => {
    item.addEventListener('click', () => {
      const target = parseInt(item.getAttribute('data-page'), 10);
      if (!isNaN(target)) {
        queueRenderPage(target);
        if (window.innerWidth < 768 && tocSidebar) {
          tocSidebar.classList.remove('open');
        }
      }
    });
  });

  // Clicks en botones de salto rápido
  document.querySelectorAll('.quick-jump-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = parseInt(btn.getAttribute('data-page'), 10);
      if (!isNaN(target)) {
        queueRenderPage(target);
      }
    });
  });

  // Teclado
  window.addEventListener('keydown', (e) => {
    if (['input', 'textarea'].includes(document.activeElement.tagName.toLowerCase())) return;
    if (e.key === 'ArrowRight' || e.key === ' ') {
      e.preventDefault();
      nextPage();
    } else if (e.key === 'ArrowLeft') {
      e.preventDefault();
      prevPage();
    }
  });

  // Gestos táctiles (Swipe)
  let touchStartX = 0;
  let touchStartY = 0;
  viewerContainer?.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
    touchStartY = e.changedTouches[0].screenY;
  }, { passive: true });

  viewerContainer?.addEventListener('touchend', (e) => {
    const diffX = e.changedTouches[0].screenX - touchStartX;
    const diffY = e.changedTouches[0].screenY - touchStartY;
    // Solo si el movimiento horizontal supera al vertical y pasa el umbral de 60px
    if (Math.abs(diffX) > 60 && Math.abs(diffX) > Math.abs(diffY)) {
      if (diffX < 0) {
        nextPage();
      } else {
        prevPage();
      }
    }
  }, { passive: true });

  // Resize ventana (reajustar si autoFit está activo)
  let resizeTimeout;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      if (autoFit && pdfDoc) {
        renderPage(currentPage);
      }
    }, 150);
  });
}

// Iniciar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
  setupEvents();
  loadPdf();
});
