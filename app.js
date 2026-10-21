import { QUIZ_STEPS } from "./quiz_data.js";

// Inlead Quiz Funnel Engine — Resumen Cronológico de la Biblia
(function() {
  if (window.location.pathname.startsWith('/appbiblia')) {
    window.location.replace('/appbiblia/index.html');
    return;
  }
  let currentStepIndex = 0;
  let historyStack = [];
  let userScore = 0;
  let questionScores = {}; // questionIndex -> score (prevents double counting on back)
  let userGender = 'Cristiano';
  let userAge = '18 a 34';
  let multiSelectionsByStep = {};
  let loadingInterval = null;

  const appEl = document.getElementById('app');

  // Base checkout URL
  const BASE_CHECKOUT_URL = "https://checkout.kashpay.com/checkout/checkout-1792201272859";

  // Salvar parâmetros de rastreamento (UTMs, subids, click IDs)
  function captureTrackingParams() {
    try {
      const current = new URLSearchParams(window.location.search);
      let stored = JSON.parse(localStorage.getItem('latram_utm_params') || '{}');
      let changed = false;

      current.forEach((val, key) => {
        if (val) {
          stored[key] = val;
          changed = true;
        }
      });

      // Capturar cookies úteis se existirem (_fbp, _fbc)
      document.cookie.split(';').forEach(c => {
        const parts = c.trim().split('=');
        const k = parts[0];
        const v = parts.slice(1).join('=');
        if (['_fbp', '_fbc'].includes(k) && v && !stored[k]) {
          stored[k] = v;
          changed = true;
        }
      });

      if (changed) {
        localStorage.setItem('latram_utm_params', JSON.stringify(stored));
      }
    } catch(e) {}
  }
  captureTrackingParams();

  function getDynamicCheckoutUrl() {
    try {
      const url = new URL(BASE_CHECKOUT_URL);
      let stored = {};
      try {
        stored = JSON.parse(localStorage.getItem('latram_utm_params') || '{}');
      } catch(e) {}

      // Injeta os salvos no localStorage
      Object.keys(stored).forEach(key => {
        if (stored[key]) url.searchParams.set(key, stored[key]);
      });

      // Prioriza a URL atual
      const currentParams = new URLSearchParams(window.location.search);
      currentParams.forEach((val, key) => {
        if (val) url.searchParams.set(key, val);
      });

      // Auto-preencher src e sck para Kashpay se não estiverem explícitos
      if (!url.searchParams.get('src')) {
        const srcVal = url.searchParams.get('utm_source') || url.searchParams.get('utm_campaign');
        if (srcVal) url.searchParams.set('src', srcVal);
      }
      if (!url.searchParams.get('sck')) {
        const sckVal = [
          url.searchParams.get('utm_source'),
          url.searchParams.get('utm_medium'),
          url.searchParams.get('utm_campaign')
        ].filter(Boolean).join('|');
        if (sckVal) url.searchParams.set('sck', sckVal);
      }

      return url.toString();
    } catch(e) {
      return BASE_CHECKOUT_URL;
    }
  }

  function cleanHtml(html) {
    if (!html) return '';
    return html
      .replace(/&nbsp;/g, ' ')
      .replace(/\u00a0/g, ' ')
      .replace(/{{score}}/g, userScore)
      .replace(/{{idade}}/g, userAge);
  }

  function goToStep(index, isBack = false) {
    if (loadingInterval) {
      clearInterval(loadingInterval);
      loadingInterval = null;
    }

    if (!isBack && currentStepIndex !== index) {
      historyStack.push(currentStepIndex);
    }
    currentStepIndex = index;
    render();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  window.__goToStep = goToStep;

  function goBack() {
    if (historyStack.length > 0) {
      const prev = historyStack.pop();
      goToStep(prev, true);
    }
  }

  function goToNextStep() {
    if (currentStepIndex < QUIZ_STEPS.length - 1) {
      goToStep(currentStepIndex + 1);
    }
  }

  function render() {
    const step = QUIZ_STEPS[currentStepIndex];
    if (!step) return;

    // Header logic
    const isIntro = currentStepIndex === 0;
    const isLoading = currentStepIndex === 19; // Step 20
    const isResults = currentStepIndex === 20; // Step 21
    const isVsl = currentStepIndex === 21; // Step 22

    const showBack = step.show_back && !isIntro && !isLoading && !isResults && !isVsl && historyStack.length > 0;
    const showProgress = step.show_progress && !isIntro && !isResults && !isVsl;
    const showLogo = !!step.show_logo;
    const showHeader = showBack || showProgress || showLogo;

    let progressPercent = 0;
    if (currentStepIndex > 0 && currentStepIndex <= 19) {
      progressPercent = Math.min(100, Math.round((currentStepIndex / 19) * 100));
    } else if (currentStepIndex >= 19) {
      progressPercent = 100;
    }

    let html = '';

    // Render Header
    if (showHeader) {
      html += `
        <header class="quiz-header">
          <div class="header-top">
            ${showBack ? `
              <button class="back-btn" id="btnBack" aria-label="Volver">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M19 12H5M12 19l-7-7 7-7"/>
                </svg>
              </button>
            ` : '<div class="header-empty"></div>'}
            
            ${showLogo ? `
              <img src="/images/img_04_xviyW-logo-palabra-invertida.png" alt="Instituto La Palabra" class="header-logo" onerror="this.style.display='none'">
            ` : '<div class="header-empty"></div>'}

            <div class="header-empty"></div>
          </div>
          ${showProgress ? `
            <div class="progress-track">
              <div class="progress-bar" style="width: ${progressPercent}%"></div>
            </div>
          ` : ''}
        </header>
      `;
    }

    // Step Container
    html += `<main class="step-container fade-in" id="stepContent">`;

    step._chartRendered = false;

    // Process Layers
    step.layers.forEach((layer, layerIdx) => {
      if (isVsl) {
        // Step 22 (VSL & Offer) Custom clean order
        if (layerIdx === 0) {
          // Headline
          html += `<div class="content-text">${cleanHtml(layer.text)}</div>`;
        } else if (layerIdx === 1) {
          // VTurb Player
          const checkoutUrl = getDynamicCheckoutUrl();
          html += `
            <div class="vsl-wrap">
              <vturb-smartplayer id="vid-6ad85eba93921d34e88abd88" style="display: block; margin: 0 auto; width: 100%; max-width: 400px;">
                <div class="vturb-player-placeholder" style="position: relative; width: 100%; padding: 133.33333333333331% 0 0; z-index: 0; background-color: black;"></div>
              </vturb-smartplayer>
            </div>

            <!-- Delayed Offer Content (Oculto até 615s de VSL) -->
            <div id="vslDelayedSection" class="vsl-delayed-section" style="display: none;">
              <div style="text-align:center; margin: 8px 0 4px;">
                <div class="badge-urgency">⏰ ¡Último día a este precio!</div>
              </div>
              <a id="botaoComprar" href="${checkoutUrl}" target="_self">
                <div class="offer-wrapper">
                  <div class="offer-button">
                    Haz clic aquí para asegurar tu material
                  </div>
                  <div class="offer-card">
                    <div class="offer-header">Recibe ahora!</div>
                    <div class="offer-body">
                      <div class="offer-info">
                        <div class="offer-title">Resumen Cronologico</div>
                        <div class="offer-gift">+ 9 regalos especiales</div>
                      </div>
                      <div class="offer-price-box">
                        <div class="old-price">De <s>US$188</s> por</div>
                        <div class="new-price">US$ <strong>17.90</strong></div>
                        <div class="note">solo hoy</div>
                      </div>
                    </div>
                  </div>
                </div>
              </a>
              <div class="guarantees-row">
                <span><strong style="color: #16a34a;">✓</strong> Acceso de por vida</span>
                <span><strong style="color: #16a34a;">✓</strong> Garantía de 30 días</span>
              </div>
              <div class="step-img-wrap" style="margin-top: 14px;">
                <img class="step-img" src="/images/img_54_TUIaS-checkout.png" alt="Garantía" loading="lazy">
              </div>
            </div>
          `;
        }
        return; // done for VSL
      }

      // Normal steps (1 to 21)
      if (layer.type === 'text') {
        html += `<div class="content-text">${cleanHtml(layer.text)}</div>`;
      } 
      else if (layer.type === 'image') {
        html += `
          <div class="step-img-wrap">
            <img class="step-img" src="${layer.src}" alt="${layer.alt || 'Ilustración'}" loading="lazy">
          </div>
        `;
      } 
      else if (layer.type === 'options') {
        const isMulti = !!layer.multi;
        const gridClass = layer.grid || 'grid-cols-1';
        const orientation = layer.orientation || (gridClass === 'grid-cols-2' ? 'vertical' : 'horizontal');
        const showIcon = layer.icon === 'right';
        const currentStepMulti = isMulti && multiSelectionsByStep[currentStepIndex] ? multiSelectionsByStep[currentStepIndex] : null;

        html += `<div class="options-grid ${gridClass}">`;
        layer.options.forEach((opt, optIdx) => {
          const isChecked = isMulti && currentStepMulti ? currentStepMulti.has(optIdx) : false;
          const hasImage = !!opt.image && !!opt.image.src;
          const isEmoji = hasImage && opt.image.type === 'emoji';

          if (orientation === 'vertical') {
            html += `
              <div class="option-card vertical ${isChecked ? 'checked' : ''}" data-opt-idx="${optIdx}" data-score="${opt.score || 0}">
                ${hasImage ? `
                  <div class="opt-img-box">
                    <img src="${opt.image.src}" alt="Imagem" class="opt-img" loading="lazy">
                  </div>
                ` : ''}
                <div class="opt-text-box">${cleanHtml(opt.label)}</div>
              </div>
            `;
          } else {
            // Horizontal card
            html += `
              <div class="option-card horizontal ${isChecked ? 'checked' : ''}" data-opt-idx="${optIdx}" data-score="${opt.score || 0}">
                ${hasImage ? `
                  ${isEmoji ? `
                    <div class="opt-thumb-box"><span class="opt-emoji">${opt.image.src}</span></div>
                  ` : `
                    <div class="opt-thumb-box"><img src="${opt.image.src}" alt="Imagem" class="opt-thumb" loading="lazy"></div>
                  `}
                ` : ''}
                <div class="opt-text-box">${cleanHtml(opt.label)}</div>
                ${showIcon ? `
                  <div class="opt-arrow-circle">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                      <path d="m9 18 6-6-6-6"/>
                    </svg>
                  </div>
                ` : ''}
                ${isMulti ? `
                  <div class="option-checkbox">
                    ${isChecked ? `
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="20 6 9 17 4 12"/>
                      </svg>
                    ` : ''}
                  </div>
                ` : ''}
              </div>
            `;
          }
        });
        html += `</div>`;
      } 
      else if (layer.type === 'button') {
        const pulseClass = layer.pulse ? 'pulse' : '';
        html += `
          <button class="btn-primary ${pulseClass}" id="btnAction" data-dest="${layer.destination}">
            ${layer.label}
          </button>
        `;
      } 
      else if (layer.type === 'loading') {
        html += `
          <div class="loading-box">
            <h2>${layer.title || 'Analizando tus respuestas...'}</h2>
            <div class="loading-bar-wrap">
              <div class="loading-bar-fill" id="loadingBarFill"></div>
            </div>
            <div class="loading-percent" id="loadingPercent">0%</div>
          </div>
        `;
      } 
      else if (layer.type === 'alert' && isResults) {
        const isLowScoreAlert = layer.id === 'FxZ8ey';
        const isHighScoreAlert = layer.id === 'HoMuSm';

        if ((userScore <= 6 && isLowScoreAlert) || (userScore > 6 && isHighScoreAlert)) {
          html += `<div class="alert-box">${cleanHtml(layer.text)}</div>`;
        }
      } 
      else if (layer.type === 'charts' && isResults) {
        if (!step._chartRendered) {
          step._chartRendered = true;
          let userPct = 58;
          if (userScore >= 8) userPct = 85;
          else if (userScore < 5) userPct = 27;

          const diff = 100 - userPct;

          html += `
            <div class="chart-card">
              <div class="chart-title">Personas de ${userAge} Años</div>
              <div class="chart-bars">
                <div class="chart-row">
                  <div class="chart-label-row">
                    <span>Usted</span>
                    <span>${userPct}%</span>
                  </div>
                  <div class="chart-bar-bg">
                    <div class="chart-bar-user" style="width: ${userPct}%"></div>
                  </div>
                </div>
                <div class="chart-row">
                  <div class="chart-label-row">
                    <span>Promedio de aciertos</span>
                    <span>100%</span>
                  </div>
                  <div class="chart-bar-bg">
                    <div class="chart-bar-average" style="width: 100%"></div>
                  </div>
                </div>
              </div>
            </div>
            <div class="alert-box" style="margin-top: 4px; text-align: center;">
              <p><strong>Lamentablemente, quedaste un ${diff}% por debajo del promedio de las personas de tu edad en conocimiento bíblico.</strong></p>
            </div>
          `;
        }
      } 
      else if (layer.type === 'arguments') {
        if (layer.arguments && layer.arguments.length > 0) {
          html += `<div class="pitch-box">${cleanHtml(layer.arguments[0].text)}</div>`;
        }
      }
    });

    html += `</main>`;
    appEl.innerHTML = html;

    // Attach Event Listeners
    attachEvents(step, isLoading, isVsl);
  }

  function attachEvents(step, isLoading, isVsl) {
    // Back button
    const btnBack = document.getElementById('btnBack');
    if (btnBack) {
      btnBack.addEventListener('click', goBack);
    }

    // Single action button
    const btnAction = document.getElementById('btnAction');
    if (btnAction) {
      btnAction.addEventListener('click', () => {
        goToNextStep();
      });
    }

    // Options selection
    const optionCards = document.querySelectorAll('.option-card');
    const optionsLayer = step.layers.find(l => l.type === 'options');
    const isMulti = optionsLayer && optionsLayer.multi;

    optionCards.forEach(card => {
      card.addEventListener('click', () => {
        const optIdx = parseInt(card.getAttribute('data-opt-idx'), 10);
        const score = parseInt(card.getAttribute('data-score'), 10) || 0;

        if (isMulti) {
          if (!multiSelectionsByStep[currentStepIndex]) {
            multiSelectionsByStep[currentStepIndex] = new Set();
          }
          const currentStepMulti = multiSelectionsByStep[currentStepIndex];
          if (currentStepMulti.has(optIdx)) {
            currentStepMulti.delete(optIdx);
            card.classList.remove('checked');
            const checkbox = card.querySelector('.option-checkbox');
            if (checkbox) checkbox.innerHTML = '';
          } else {
            currentStepMulti.add(optIdx);
            card.classList.add('checked');
            const checkbox = card.querySelector('.option-checkbox');
            if (checkbox) {
              checkbox.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>`;
            }
          }
        } else {
          // Single select
          optionCards.forEach(c => c.classList.remove('selected'));
          card.classList.add('selected');

          // Save special profile answers
          const optText = card.querySelector('.opt-text-box').textContent.trim();
          if (step.id === '6VJqSa') { // Gender step
            userGender = optText.includes('Cristiana') ? 'Cristiana' : 'Cristiano';
          } else if (step.id === 'LsctZR') { // Age step
            userAge = optText;
          }

          // Scoring logic for quiz questions (Step index 9 to 18)
          if (currentStepIndex >= 9 && currentStepIndex <= 18) {
            questionScores[currentStepIndex] = score;
            // Recalculate total score
            userScore = Object.values(questionScores).reduce((a, b) => a + b, 0);
          }

          // Auto-advance
          setTimeout(() => {
            goToNextStep();
          }, 180);
        }
      });
    });

    // Loading Step (Step 20)
    if (isLoading) {
      const fill = document.getElementById('loadingBarFill');
      const text = document.getElementById('loadingPercent');
      let progress = 0;
      const duration = 4000; // 4 seconds
      const intervalTime = 40;
      const stepIncrement = 100 / (duration / intervalTime);

      loadingInterval = setInterval(() => {
        progress += stepIncrement;
        if (progress >= 100) {
          progress = 100;
          clearInterval(loadingInterval);
          loadingInterval = null;
          if (fill) fill.style.width = '100%';
          if (text) text.textContent = '100%';
          setTimeout(() => {
            goToNextStep();
          }, 350);
        } else {
          if (fill) fill.style.width = `${Math.round(progress)}%`;
          if (text) text.textContent = `${Math.round(progress)}%`;
        }
      }, intervalTime);
    }

    // Step 22 (VSL) Delay Logic
    if (isVsl) {
      // Inject VTurb smartplayer script if not already present
      if (!document.getElementById('vturb-script')) {
        const s = document.createElement('script');
        s.id = 'vturb-script';
        s.src = "https://scripts.converteai.net/ab5fe3da-5afb-4db2-bf3c-fc0652a82946/players/6ad85eba93921d34e88abd88/v4/player.js";
        s.async = true;
        document.head.appendChild(s);
      }

      const DELAY_SECONDS = 615; // 10 minutos e 15 segundos (pitch do vídeo na VTurb)
      const delayedSection = document.getElementById('vslDelayedSection');
      const urlParams = new URLSearchParams(window.location.search);
      const skipDelay = urlParams.get('delay') === 'false' || urlParams.get('test') === 'true';
      const alreadyRevealed = localStorage.getItem('vsl_offer_revealed') === 'true';

      function showDelayedContent() {
        if (!delayedSection) return;
        delayedSection.style.display = 'flex';
        try {
          localStorage.setItem('vsl_offer_revealed', 'true');
        } catch(e) {}
      }

      // Função global acessível no console para testes imediatos
      window.__showOffer = showDelayedContent;

      if (skipDelay || alreadyRevealed) {
        showDelayedContent();
      } else {
        // 1. Escutar evento nativo de pitch do VTurb SmartPlayer
        document.addEventListener('smartplayer:pitch', showDelayedContent);
        document.addEventListener('pitch:time', showDelayedContent);

        // 2. Escutar evento customizado de timeupdate do VTurb SmartPlayer
        document.addEventListener('smartplayer:timeupdate', (e) => {
          if (e && e.detail && e.detail.currentTime >= DELAY_SECONDS) {
            showDelayedContent();
          }
        });

        // 3. Monitoramento direto na instância do player
        let checkInterval = setInterval(() => {
          try {
            if (window.smartplayer && window.smartplayer.instances && window.smartplayer.instances.length > 0) {
              const player = window.smartplayer.instances[0];
              const currentTime = (player.video && typeof player.video.currentTime === 'number') 
                ? player.video.currentTime 
                : (typeof player.currentTime === 'number' ? player.currentTime : 0);
              
              if (currentTime >= DELAY_SECONDS) {
                showDelayedContent();
                clearInterval(checkInterval);
                checkInterval = null;
              }
            }
          } catch(e) {}
        }, 1000);
      }
    }
  }

  // Listener do clique no botão de compra (Pixel InitiateCheckout + garantia de UTMs)
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('#botaoComprar, .offer-button, .offer-card, .offer-wrapper, [class*="smartplayer-button"], [class*="smartplayer-callaction"]');
    if (btn) {
      if (typeof window.fbq === 'function') {
        window.fbq('track', 'InitiateCheckout', {
          value: 17.90,
          currency: 'USD',
          content_name: 'Resumen Cronológico de la Biblia',
          content_ids: ['checkout-1792201272859']
        });
      }

      const link = btn.closest('a') || document.getElementById('botaoComprar');
      if (link && !link.closest('vturb-smartplayer')) {
        link.href = getDynamicCheckoutUrl();
      }
    }
  });

  // Proteção Global Anti-Hijack: Impede desvio de vendas por qualquer link não autorizado
  document.addEventListener('click', (e) => {
    const link = e.target.closest('a');
    if (link && link.href) {
      if (link.href.includes('hotmart.com')) {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        console.warn('[Segurança] Bloqueada tentativa de redirecionamento:', link.href);
        window.open(getDynamicCheckoutUrl(), '_blank');
        return false;
      }
    }
  }, true);

  // Interceptar chamadas diretas a window.open com domínios suspeitos
  const _originalOpen = window.open;
  window.open = function(url, target, features) {
    if (typeof url === 'string' && (url.includes('hotmart.com') || url.includes('vturb_thumbnail'))) {
      console.warn('[Segurança] Redirecionamento suspeito interceptado para o checkout oficial:', url);
      return _originalOpen.call(window, getDynamicCheckoutUrl(), target, features);
    }
    return _originalOpen.apply(window, arguments);
  };

  // Initialize
  render();
})();
