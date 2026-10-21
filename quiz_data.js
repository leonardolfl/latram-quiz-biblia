export const QUIZ_STEPS = [
  {
    "id": "BgXef0",
    "title": "Introdu\u00e7\u00e3o",
    "show_back": false,
    "show_progress": false,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": [],
        "text": "<h1 class=\"ql-align-center\"><strong>\u00bfCu\u00e1nto&nbsp;conoces&nbsp;la&nbsp;Palabra?</strong></h1><p class=\"ql-align-center\">Haz&nbsp;este&nbsp;test&nbsp;r\u00e1pido&nbsp;y&nbsp;descubre&nbsp;cu\u00e1l&nbsp;es&nbsp;tu&nbsp;nivel&nbsp;de&nbsp;conocimiento&nbsp;sobre&nbsp;las&nbsp;escrituras.</p><p class=\"ql-align-center\"><strong style=\"color: inherit;\">\ud83c\udf81&nbsp;</strong><strong>\u00a1Al&nbsp;final&nbsp;recibir\u00e1s&nbsp;tres&nbsp;regalos!</strong></p>"
      },
      {
        "type": "image",
        "design": {
          "basis": "80",
          "horizontalAlign": "mx-auto"
        },
        "src": "/images/img_44_hjhXK-spaceclimb-74087-a-detailed-and-beautifully-illustrated-chro-0b2efe8f-dfd3-4014-8e56-ed7c7f6533aa-0.jpg",
        "alt": ""
      },
      {
        "type": "button",
        "design": {
          "style": "success",
          "basis": 100,
          "pulse": true,
          "bubble": false,
          "fixed": false
        },
        "label": "EMPEZAR EL TEST",
        "destination": "next",
        "pulse": true
      }
    ]
  },
  {
    "id": "FnP6Ml",
    "title": "Funil - Etapa 01",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": {
          "cols": "9",
          "horizontalAlign": "mx-auto",
          "basis": "100"
        },
        "text": "<p class=\"ql-align-center\"><strong style=\"background-color: inherit; color: rgb(22, 163, 74);\">Antes,&nbsp;queremos saber un poco m\u00e1s sobre ti.</strong></p><h2 class=\"ql-align-center\"><strong>\u00bfCu\u00e1l es la forma en que m\u00e1s sueles conectarte con la Palabra de Dios?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "background": "default",
          "cols": "11",
          "horizontalAlign": "mx-auto",
          "basis": "100",
          "transparentImage": false,
          "grid": "grid-cols-2",
          "orientation": "vertical",
          "order": "default",
          "icon": "none",
          "iconPosition": "end",
          "shadow": "shadow-sm hover:shadow-md",
          "gap": "gap-2"
        },
        "multi": false,
        "grid": "grid-cols-2",
        "orientation": "vertical",
        "icon": "none",
        "options": [
          {
            "label": "<p><strong>Lecturas</strong><strong style=\"color: inherit;\">, videos o predicaciones</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_34_TOKxE-spaceclimb-74087-cartoon-illustration-of-a-young-man-studyin-40676052-3709-4bcb-8d1c-e5d63f0190bb-1.jpg"
            }
          },
          {
            "label": "<p><strong style=\"color: inherit;\">Leyendo la Biblia / devocional</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_46_mvwcv-spaceclimb-74087-a-cheerful-cartoon-style-christian-woman-re-abd8b25c-787b-4b9b-ad79-d0221834e934-1.jpg"
            }
          },
          {
            "label": "<p><strong style=\"color: inherit;\">Cultos y reuniones</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_24_7eOI6-spaceclimb-74087-a-cheerful-cartoon-style-church-service-sce-21496426-b36a-4728-8187-3be87f2b007b-3.jpg"
            }
          },
          {
            "label": "<p><strong>No estoy logrando conectarme con Dios</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_38_ZAcYi-spaceclimb-74087-a-contemplative-and-emotional-scene-of-a-pe-40ccc84c-653d-4678-b506-2236fdd0aef6-0.jpg"
            }
          }
        ]
      }
    ]
  },
  {
    "id": "jazPXm",
    "title": "Funil - Etapa 02",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "image",
        "design": {
          "basis": "75",
          "horizontalAlign": "mx-auto"
        },
        "src": "/images/img_43_gN7Tb-spaceclimb-74087-a-cute-cartoon-style-bible-lying-open-on-a-82a9b528-a785-447b-97bd-79b2cb8afef2-1.jpg",
        "alt": ""
      },
      {
        "type": "text",
        "design": [],
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfQu\u00e9 parte de la Biblia te resulta dif\u00edcil de entender?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "icon": "right",
          "background": "default",
          "border": "border",
          "shadow": "shadow-sm hover:shadow-md",
          "transparentImage": true,
          "basis": 100
        },
        "multi": false,
        "grid": "grid-cols-1",
        "orientation": "horizontal",
        "icon": "right",
        "options": [
          {
            "label": "<p>Antiguo Testamento</p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_02_w69WC-umaimagem-6.png"
            }
          },
          {
            "label": "<p>Nuevo Testamento</p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_01_8hI6J-umaimagem-5.png"
            }
          }
        ]
      }
    ]
  },
  {
    "id": "zN6ldK",
    "title": "Funil - Etapa 03",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": [],
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfC\u00f3mo te sientes al intentar entender la Biblia en su totalidad?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "icon": "none",
          "background": "default",
          "border": "border",
          "shadow": "shadow-sm hover:shadow-md",
          "transparentImage": true,
          "basis": 100,
          "orientation": "vertical",
          "grid": "grid-cols-2"
        },
        "multi": false,
        "grid": "grid-cols-2",
        "orientation": "vertical",
        "icon": "none",
        "options": [
          {
            "label": "<p>Ya lo intent\u00e9 varias veces y me rend\u00ed</p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_53_zsT4b-spaceclimb-74087-a-thoughtful-and-symbolic-illustration-of-a-abbdb02e-b160-459d-b387-539aa2bc4d54-2.jpg"
            }
          },
          {
            "label": "<p>Intento pero no lo consigo de ninguna manera</p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_35_Ti2AY-spaceclimb-74087-a-detailed-cartoon-style-illustration-of-a-d0fb6482-73b5-4430-82b0-d82458a091f3-2.jpg"
            }
          },
          {
            "label": "<p>A veces confundido/a, pero la entiendo.</p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_26_9uIWv-spaceclimb-74087-a-detailed-cartoon-style-illustration-of-a-c5047af5-d480-4463-a50a-9d5a39085687-1.jpg"
            }
          },
          {
            "label": "<p>Tranquilo/a, pero siento que puedo mejorar</p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_23_3iZaa-spaceclimb-74087-a-detailed-cartoon-style-illustration-of-an-0662196c-d82c-47f0-a83e-6ce7c754df88-3.jpg"
            }
          }
        ]
      }
    ]
  },
  {
    "id": "82kel7",
    "title": "Funil - Etapa 04",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "image",
        "design": {
          "basis": "75",
          "horizontalAlign": "mx-auto"
        },
        "src": "/images/img_42_e0E1f-spaceclimb-74087-a-cute-cartoon-style-christian-man-looking-12fcf148-7881-4c34-89bc-456922fd9859-2.jpg",
        "alt": ""
      },
      {
        "type": "text",
        "design": [],
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfCu\u00e1l es el mayor desaf\u00edo que enfrentas cuando intentas leer la Biblia?</strong></h2><p class=\"ql-align-center\">(Puedes seleccionar m\u00e1s de uno si es el caso)</p>"
      },
      {
        "type": "options",
        "design": {
          "icon": "select",
          "background": "default",
          "border": "border",
          "shadow": "shadow-sm hover:shadow-md",
          "transparentImage": true,
          "basis": 100
        },
        "multi": true,
        "grid": "grid-cols-1",
        "orientation": "horizontal",
        "icon": "select",
        "options": [
          {
            "label": "<p>No s\u00e9 por d\u00f3nde empezar</p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p>Tengo dificultad para entender</p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p>Falta de planificaci\u00f3n y organizaci\u00f3n</p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p>Siento que la lectura lleva mucho tiempo</p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p>Siento la falta de un material que me ayude en la lectura</p>",
            "score": 0,
            "destination": "next",
            "image": null
          }
        ]
      },
      {
        "type": "button",
        "design": {
          "style": "success",
          "basis": 100,
          "pulse": true,
          "bubble": false,
          "fixed": false
        },
        "label": "CONTINUAR",
        "destination": "next",
        "pulse": true
      }
    ]
  },
  {
    "id": "U3R5nC",
    "title": "Funil - Etapa (N)",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "image",
        "design": {
          "basis": "85",
          "horizontalAlign": "mx-auto"
        },
        "src": "/images/img_48_nmxzX-spaceclimb-74087-a-symbolic-and-inspirational-scene-of-a-lar-482497d8-0585-4a6a-bb73-24b84c951f64-3.jpg",
        "alt": ""
      },
      {
        "type": "text",
        "design": [],
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfHas logrado leer toda la Biblia?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "icon": "right",
          "grid": "grid-cols-1",
          "orientation": "horizontal",
          "order": "default",
          "transparentImage": true,
          "basis": 100,
          "shadow": "shadow-sm hover:shadow-md"
        },
        "multi": false,
        "grid": "grid-cols-1",
        "orientation": "horizontal",
        "icon": "right",
        "options": [
          {
            "label": "<p><strong>S\u00ed, ya lo logr\u00e9</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "emoji",
              "src": "\u2705"
            }
          },
          {
            "label": "<p><strong>No, todav\u00eda no lo logr\u00e9</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "emoji",
              "src": "\u274c"
            }
          }
        ]
      }
    ]
  },
  {
    "id": "6VJqSa",
    "title": "Funil - Etapa (N)",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": [],
        "text": "<h2 class=\"ql-align-center\"><strong>Usted es:</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "icon": "right",
          "background": "default",
          "border": "border",
          "shadow": "shadow-sm hover:shadow-md",
          "transparentImage": true,
          "basis": 100,
          "grid": "grid-cols-2",
          "orientation": "vertical"
        },
        "multi": false,
        "grid": "grid-cols-2",
        "orientation": "vertical",
        "icon": "right",
        "options": [
          {
            "label": "<p><strong>Cristiano</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_31_Kp94I-spaceclimb-74087-a-cheerful-cartoon-style-christian-man-smil-c915093e-9a70-4c1e-adc4-d08e1a97f0c8-0.jpg"
            }
          },
          {
            "label": "<p><strong>Cristiana</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_29_HxCxt-spaceclimb-74087-a-cheerful-cartoon-style-christian-woman-sm-32e43840-836d-453a-b43d-a5d040d1f9f0-1.jpg"
            }
          }
        ]
      }
    ]
  },
  {
    "id": "LsctZR",
    "title": "Funil - Etapa (N)",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": [],
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfCu\u00e1l es su edad?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "icon": "right",
          "background": "default",
          "border": "border",
          "shadow": "shadow-sm hover:shadow-md",
          "transparentImage": true,
          "basis": 100,
          "grid": "grid-cols-2",
          "orientation": "vertical"
        },
        "multi": false,
        "grid": "grid-cols-2",
        "orientation": "vertical",
        "icon": "right",
        "options": [
          {
            "label": "<p><strong>18 a 34</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_27_A9nui-spaceclimb-74087-a-cheerful-cartoon-style-18-year-old-christ-47eb831d-15f4-4ed2-b20d-c10b9e3994a9-1.jpg"
            }
          },
          {
            "label": "<p><strong>35 a 44</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_50_rmMp1-spaceclimb-74087-a-cheerful-cartoon-style-christian-adult-35-3f6ea568-7958-4548-92f7-9c1a8a2494f0-2.jpg"
            }
          },
          {
            "label": "<p><strong>45 a 54</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_32_OpCZf-spaceclimb-74087-a-cheerful-cartoon-style-christian-adult-45-b3244730-ad1e-4951-9d05-64d1b5e334d1-0.jpg"
            }
          },
          {
            "label": "<p><strong>55+</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_49_qtLJ1-spaceclimb-74087-a-gentle-cartoon-style-christian-woman-55-y-3ecca564-f044-43ac-b994-b0ac4a305494-2.jpg"
            }
          }
        ]
      }
    ]
  },
  {
    "id": "MxSrro",
    "title": "Funil - Inicio do Teste",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": [],
        "text": "<h2 class=\"ql-align-center\"><strong style=\"background-color: transparent; color: rgb(31, 41, 55);\">\u00a1</strong><strong style=\"background-color: transparent; color: inherit;\">Ahora p</strong><strong style=\"background-color: transparent; color: rgb(31, 41, 55);\">ongamos a prueba tu conocimiento sobre la Palabra de Dios! \ufeffResponde las siguientes preguntas.</strong></h2>"
      },
      {
        "type": "image",
        "design": {
          "basis": 75,
          "horizontalAlign": "mx-auto"
        },
        "src": "/images/img_47_n5haF-spaceclimb-74087-two-cheerful-cartoon-style-christian-men-st-c460fa30-af7c-4faf-859f-8c80ed144b7b-2.jpg",
        "alt": ""
      },
      {
        "type": "button",
        "design": {
          "style": "success",
          "basis": 100,
          "pulse": true,
          "bubble": false,
          "fixed": false
        },
        "label": "COMENZAR",
        "destination": "next",
        "pulse": true
      }
    ]
  },
  {
    "id": "qfWagk",
    "title": "Teste - Pergunta 01",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": {
          "cols": "9",
          "horizontalAlign": "mx-auto",
          "basis": "100"
        },
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfQui\u00e9n derrot\u00f3 a un gigante usando una honda y una piedra?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "background": "default",
          "cols": "11",
          "horizontalAlign": "mx-auto",
          "basis": "100",
          "transparentImage": false,
          "grid": "grid-cols-2",
          "orientation": "vertical",
          "order": "default",
          "icon": "right",
          "iconPosition": "end",
          "shadow": "shadow-sm hover:shadow-md",
          "gap": "gap-2"
        },
        "multi": false,
        "grid": "grid-cols-2",
        "orientation": "vertical",
        "icon": "right",
        "options": [
          {
            "label": "<p><strong>Josu\u00e9</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_19_tAI9v-spaceclimb-74087-a-cartoon-style-side-profile-portrait-of-jo-d8c249aa-673e-4ff8-91b0-67a5c0135497-1.webp"
            }
          },
          {
            "label": "<p><strong>Mois\u00e9s</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_05_4sLak-spaceclimb-74087-a-cartoon-style-side-profile-portrait-of-mo-9a7b3d27-cc2d-4f8f-a49c-4deb6578c41b-3.webp"
            }
          },
          {
            "label": "<p><strong>David</strong></p>",
            "score": "1",
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_13_WHF53-spaceclimb-74087-a-cartoon-style-side-profile-portrait-of-da-fab4a0bc-981c-441f-9c09-f4de62f7a9fa-2.webp"
            }
          },
          {
            "label": "<p><strong>Sans\u00f3n</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_20_tJ5dp-spaceclimb-74087-a-cartoon-style-side-profile-portrait-of-sa-64851776-9ccc-43c6-9b61-bb453d2d4871-0.webp"
            }
          }
        ]
      }
    ]
  },
  {
    "id": "hL2s3O",
    "title": "Teste - Pergunta 02",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "image",
        "design": {
          "basis": "75",
          "horizontalAlign": "mx-auto"
        },
        "src": "/images/img_37_XVTJi-spaceclimb-74087-a-cute-cartoon-style-scene-of-joseph-and-ma-a608d65d-6558-46ea-9373-d39fb959868b-3.jpg",
        "alt": ""
      },
      {
        "type": "text",
        "design": {
          "cols": "9",
          "horizontalAlign": "mx-auto",
          "basis": "100"
        },
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfQu\u00e9 escena muestra a Mar\u00eda, Jos\u00e9 y un beb\u00e9 en un pesebre?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "background": "default",
          "cols": "11",
          "horizontalAlign": "mx-auto",
          "basis": "100",
          "transparentImage": false,
          "grid": "grid-cols-1",
          "orientation": "horizontal",
          "order": "default",
          "icon": "right",
          "iconPosition": "end",
          "shadow": "shadow-sm hover:shadow-md",
          "gap": "gap-2"
        },
        "multi": false,
        "grid": "grid-cols-1",
        "orientation": "horizontal",
        "icon": "right",
        "options": [
          {
            "label": "<p><strong>La Transfiguraci\u00f3n</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p><strong>La Natividad</strong></p>",
            "score": "1",
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p><strong>La Anunciaci\u00f3n</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p><strong>La \u00daltima Cena</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          }
        ]
      }
    ]
  },
  {
    "id": "ZVXEti",
    "title": "Teste - Pergunta 03",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": {
          "cols": "9",
          "horizontalAlign": "mx-auto",
          "basis": "100"
        },
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfQu\u00e9 batalla fue ganada por 300 hombres usando trompetas y antorchas?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "background": "default",
          "cols": "11",
          "horizontalAlign": "mx-auto",
          "basis": "100",
          "transparentImage": false,
          "grid": "grid-cols-2",
          "orientation": "vertical",
          "order": "default",
          "icon": "right",
          "iconPosition": "end",
          "shadow": "shadow-sm hover:shadow-md",
          "gap": "gap-2"
        },
        "multi": false,
        "grid": "grid-cols-2",
        "orientation": "vertical",
        "icon": "right",
        "options": [
          {
            "label": "<p><strong>La rebeli\u00f3n de Absal\u00f3n</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_16_oGxxj-spaceclimb-74087-a-cartoon-style-illustration-of-the-biblica-e2057925-9a24-45ce-9800-814f200861b8-3.webp"
            }
          },
          {
            "label": "<p><strong>La batalla de Jeric\u00f3</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_52_wgSnO-spaceclimb-74087-a-detailed-cartoon-style-illustration-of-th-ff6d2290-7031-48c0-adf7-3574290334f3-1.jpg"
            }
          },
          {
            "label": "<p><strong>La conquista de Cana\u00e1n</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_36_Wwfo2-spaceclimb-74087-a-detailed-cartoon-style-illustration-of-th-52353f53-0d6e-430d-97ad-6b31bfbda0c1-2.jpg"
            }
          },
          {
            "label": "<p><strong>La batalla de Madi\u00e1n</strong></p>",
            "score": "1",
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_41_dJMZ5-spaceclimb-74087-a-detailed-cartoon-style-illustration-of-th-74a4efdf-dc69-448f-adf2-28b53d110f19-3.jpg"
            }
          }
        ]
      }
    ]
  },
  {
    "id": "eFneXm",
    "title": "Teste - Pergunta 04",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "image",
        "design": {
          "basis": "75",
          "horizontalAlign": "mx-auto"
        },
        "src": "/images/img_28_DKUCl-spaceclimb-74087-a-detailed-cartoon-style-illustration-of-th-611a7a9f-a099-4eec-8b5b-be4280c1417d-2.jpg",
        "alt": ""
      },
      {
        "type": "text",
        "design": {
          "cols": "9",
          "horizontalAlign": "mx-auto",
          "basis": "100"
        },
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfQu\u00e9 evento muestra los muros de una ciudad cayendo tras siete d\u00edas de marcha?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "background": "default",
          "cols": "11",
          "horizontalAlign": "mx-auto",
          "basis": "100",
          "transparentImage": false,
          "grid": "grid-cols-1",
          "orientation": "horizontal",
          "order": "default",
          "icon": "right",
          "iconPosition": "end",
          "shadow": "shadow-sm hover:shadow-md",
          "gap": "gap-2"
        },
        "multi": false,
        "grid": "grid-cols-1",
        "orientation": "horizontal",
        "icon": "right",
        "options": [
          {
            "label": "<p><strong>La fundaci\u00f3n de Jerusal\u00e9n</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p><strong>La destrucci\u00f3n de Sodoma</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p><strong>La ca\u00edda de Babilonia</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p><strong>La batalla de Jeric\u00f3</strong></p>",
            "score": "1",
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          }
        ]
      }
    ]
  },
  {
    "id": "a0FfOb",
    "title": "Teste - Pergunta 05",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "image",
        "design": {
          "basis": "75",
          "horizontalAlign": "mx-auto"
        },
        "src": "/images/img_33_PJSUn-spaceclimb-74087-a-beautiful-cartoon-style-scene-symbolizing-879c9d5d-edfd-4837-bf53-3fb83b663e88-3.jpg",
        "alt": ""
      },
      {
        "type": "text",
        "design": {
          "cols": "9",
          "horizontalAlign": "mx-auto",
          "basis": "100"
        },
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfQu\u00e9 promesa de Dios se simboliza con un arco\u00edris en el cielo?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "background": "default",
          "cols": "11",
          "horizontalAlign": "mx-auto",
          "basis": "100",
          "transparentImage": false,
          "grid": "grid-cols-1",
          "orientation": "horizontal",
          "order": "default",
          "icon": "right",
          "iconPosition": "end",
          "shadow": "shadow-sm hover:shadow-md",
          "gap": "gap-2"
        },
        "multi": false,
        "grid": "grid-cols-1",
        "orientation": "horizontal",
        "icon": "right",
        "options": [
          {
            "label": "<p><strong>El \u00e9xodo de Egipto</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p><strong>La creaci\u00f3n</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p><strong>La venida de Jes\u00fas</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p><strong>El Pacto con No\u00e9</strong></p>",
            "score": "1",
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          }
        ]
      }
    ]
  },
  {
    "id": "uRsq6T",
    "title": "Teste - Pergunta 06",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": {
          "cols": "9",
          "horizontalAlign": "mx-auto",
          "basis": "100"
        },
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfQu\u00e9 profeta subi\u00f3 al cielo en un carro de fuego?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "background": "default",
          "cols": "11",
          "horizontalAlign": "mx-auto",
          "basis": "100",
          "transparentImage": false,
          "grid": "grid-cols-2",
          "orientation": "vertical",
          "order": "default",
          "icon": "right",
          "iconPosition": "end",
          "shadow": "shadow-sm hover:shadow-md",
          "gap": "gap-2"
        },
        "multi": false,
        "grid": "grid-cols-2",
        "orientation": "vertical",
        "icon": "right",
        "options": [
          {
            "label": "<p><strong>El\u00edas</strong></p>",
            "score": "1",
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_12_RhMAB-spaceclimb-74087-a-cartoon-style-portrait-of-the-prophet-eli-39b8b5fb-c6ae-484b-babd-b7a1e351383a-2.webp"
            }
          },
          {
            "label": "<p><strong>Ezequiel</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_10_R4wJ7-spaceclimb-74087-a-cartoon-style-portrait-of-the-prophet-eze-458984a9-d373-4ba9-8add-8ebd05ad7291-1.webp"
            }
          },
          {
            "label": "<p><strong>Jerem\u00edas</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_21_x79gU-spaceclimb-74087-a-cartoon-style-portrait-of-the-prophet-jer-c5b72932-92df-4872-b42b-8fb99a2078b8-1.webp"
            }
          },
          {
            "label": "<p><strong>Isa\u00edas</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_18_rnRUH-spaceclimb-74087-a-cartoon-style-portrait-of-the-prophet-isa-52ea38c5-87ca-4786-bc4e-307177bdda3c-2.webp"
            }
          }
        ]
      }
    ]
  },
  {
    "id": "JnmVMl",
    "title": "Teste - Pergunta 07",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": {
          "cols": "9",
          "horizontalAlign": "mx-auto",
          "basis": "100"
        },
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfQu\u00e9 profeta tuvo la visi\u00f3n de un valle de huesos secos que reviv\u00edan?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "background": "default",
          "cols": "11",
          "horizontalAlign": "mx-auto",
          "basis": "100",
          "transparentImage": false,
          "grid": "grid-cols-2",
          "orientation": "vertical",
          "order": "default",
          "icon": "right",
          "iconPosition": "end",
          "shadow": "shadow-sm hover:shadow-md",
          "gap": "gap-2"
        },
        "multi": false,
        "grid": "grid-cols-2",
        "orientation": "vertical",
        "icon": "right",
        "options": [
          {
            "label": "<p><strong>Oseas</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_06_6fITI-spaceclimb-74087-a-cartoon-style-portrait-of-the-prophet-hos-45f4a60e-b3b7-41f1-a49a-80950011998d-2.webp"
            }
          },
          {
            "label": "<p><strong>Ezequiel</strong></p>",
            "score": "1",
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_10_R4wJ7-spaceclimb-74087-a-cartoon-style-portrait-of-the-prophet-eze-458984a9-d373-4ba9-8add-8ebd05ad7291-1.webp"
            }
          },
          {
            "label": "<p><strong>Daniel</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_11_RRUBH-spaceclimb-74087-a-cartoon-style-portrait-of-the-prophet-dan-721b21a4-e01c-4163-b51a-8d99851ccfeb-0.webp"
            }
          },
          {
            "label": "<p><strong>Isa\u00edas</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_18_rnRUH-spaceclimb-74087-a-cartoon-style-portrait-of-the-prophet-isa-52ea38c5-87ca-4786-bc4e-307177bdda3c-2.webp"
            }
          }
        ]
      }
    ]
  },
  {
    "id": "LlVoyJ",
    "title": "Teste - Pergunta 08",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": {
          "cols": "9",
          "horizontalAlign": "mx-auto",
          "basis": "100"
        },
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfQu\u00e9 rey quem\u00f3 un rollo con la profec\u00eda de Jerem\u00edas?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "background": "default",
          "cols": "11",
          "horizontalAlign": "mx-auto",
          "basis": "100",
          "transparentImage": false,
          "grid": "grid-cols-2",
          "orientation": "vertical",
          "order": "default",
          "icon": "right",
          "iconPosition": "end",
          "shadow": "shadow-sm hover:shadow-md",
          "gap": "gap-2"
        },
        "multi": false,
        "grid": "grid-cols-2",
        "orientation": "vertical",
        "icon": "right",
        "options": [
          {
            "label": "<p><strong>Jos\u00edas</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_07_BwS05-spaceclimb-74087-a-cartoon-style-portrait-of-king-josiah-as-6aae4517-a72c-4638-b413-94aabd4fc924-3.webp"
            }
          },
          {
            "label": "<p><strong>Manas\u00e9s</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_09_Jh8jp-spaceclimb-74087-a-cartoon-style-portrait-of-king-manasseh-s-8a939d9f-ba4d-466b-8971-d362a6cb4279-0.webp"
            }
          },
          {
            "label": "<p><strong>Sedequ\u00edas</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_17_qh8eb-spaceclimb-74087-a-cartoon-style-portrait-of-king-zedekiah-w-dec8619c-1586-40f5-8c1c-bd532587c5a2-3.webp"
            }
          },
          {
            "label": "<p><strong>Joaquim</strong></p>",
            "score": "1",
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_15_mhPMh-spaceclimb-74087-a-cartoon-style-portrait-of-king-jehoiakim-a93bd49f-4873-4e4e-9022-7273eb1aeb17-1.webp"
            }
          }
        ]
      }
    ]
  },
  {
    "id": "Ssx0Yr",
    "title": "Teste - Pergunta 09",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "image",
        "design": {
          "basis": "75",
          "horizontalAlign": "mx-auto"
        },
        "src": "/images/img_22_2Yank-spaceclimb-74087-a-detailed-cartoon-style-illustration-of-jo-5353a7a2-38c1-44d7-aad5-a65c0b0bb885-1.jpg",
        "alt": ""
      },
      {
        "type": "text",
        "design": {
          "cols": "9",
          "horizontalAlign": "mx-auto",
          "basis": "100"
        },
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfQu\u00e9 personaje es conocido por su t\u00fanica de colores y por interpretar los sue\u00f1os del fara\u00f3n?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "background": "default",
          "cols": "11",
          "horizontalAlign": "mx-auto",
          "basis": "100",
          "transparentImage": false,
          "grid": "grid-cols-1",
          "orientation": "horizontal",
          "order": "default",
          "icon": "right",
          "iconPosition": "end",
          "shadow": "shadow-sm hover:shadow-md",
          "gap": "gap-2"
        },
        "multi": false,
        "grid": "grid-cols-1",
        "orientation": "horizontal",
        "icon": "right",
        "options": [
          {
            "label": "<p><strong>Jos\u00e9</strong></p>",
            "score": "1",
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p><strong>Eliseo</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p><strong>Mois\u00e9s</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          },
          {
            "label": "<p><strong>Daniel</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": null
            }
          }
        ]
      }
    ]
  },
  {
    "id": "P72jhX",
    "title": "Teste - Pergunta 10",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": {
          "cols": "9",
          "horizontalAlign": "mx-auto",
          "basis": "100"
        },
        "text": "<h2 class=\"ql-align-center\"><strong>\u00bfCu\u00e1l fue el martirio del primer cristiano en el libro de los Hechos?</strong></h2>"
      },
      {
        "type": "options",
        "design": {
          "background": "default",
          "cols": "11",
          "horizontalAlign": "mx-auto",
          "basis": "100",
          "transparentImage": false,
          "grid": "grid-cols-2",
          "orientation": "vertical",
          "order": "default",
          "icon": "none",
          "iconPosition": "end",
          "shadow": "shadow-sm hover:shadow-md",
          "gap": "gap-2"
        },
        "multi": false,
        "grid": "grid-cols-2",
        "orientation": "vertical",
        "icon": "none",
        "options": [
          {
            "label": "<p><strong>La decapitaci\u00f3n de Juan el Bautista</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_39_bNH4b-spaceclimb-74087-a-detailed-cartoon-style-historical-scene-o-b7ca3df0-be15-4a22-a9ed-f06409d2a4ec-1.jpg"
            }
          },
          {
            "label": "<p><strong>El apedreamiento de Esteban</strong></p>",
            "score": "1",
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_25_9EEOx-spaceclimb-74087-a-detailed-cartoon-style-historical-scene-o-653beb28-e932-4a19-bf1c-5bfcd234fe2e-3.jpg"
            }
          },
          {
            "label": "<p><strong>La muerte de Jacobo</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_51_sfDF2-spaceclimb-74087-a-detailed-cartoon-style-historical-scene-o-87711d65-6511-4948-94cb-82245ea636b0-3.jpg"
            }
          },
          {
            "label": "<p><strong>La muerte de Pedro</strong></p>",
            "score": 0,
            "destination": "next",
            "image": {
              "type": "image",
              "src": "/images/img_45_mh6wj-spaceclimb-74087-a-detailed-cartoon-style-historical-scene-o-8c0b71d8-0044-4c4a-b090-1223bb65b6dc-1.jpg"
            }
          }
        ]
      }
    ]
  },
  {
    "id": "bW24vz",
    "title": "Loading 01",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "image",
        "design": {
          "basis": "75",
          "horizontalAlign": "mx-auto"
        },
        "src": "/images/img_30_Jr8Sv-spaceclimb-74087-a-detailed-cartoon-style-illustration-of-an-80339f2b-82be-4ae4-94f1-5b6dfe2ab637-1-1.jpg",
        "alt": ""
      },
      {
        "type": "clear",
        "design": [],
        "clear": "h-[1rem]"
      },
      {
        "type": "loading",
        "design": {
          "style": "default",
          "basis": "100"
        },
        "title": "Analizando tus respuestas...",
        "seconds": 4
      },
      {
        "type": "clear",
        "design": [],
        "clear": "h-[1rem]"
      }
    ]
  },
  {
    "id": "sEkxhu",
    "title": "Resultados do Teste",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": [],
        "text": "<h1 class=\"ql-align-center\"><strong>Resultados de tu Desaf\u00edo B\u00edblico</strong></h1>"
      },
      {
        "type": "image",
        "design": {
          "basis": "75",
          "horizontalAlign": "mx-auto"
        },
        "src": "/images/img_40_bzBl9-spaceclimb-74087-a-detailed-cartoon-style-illustration-of-je-7b71d104-64c6-4fb6-bcae-1b094dd53043-3.jpg",
        "alt": ""
      },
      {
        "type": "alert",
        "design": {
          "style": "danger"
        },
        "text": "<h2><strong>Acertaste {{score}} de 10 preguntas</strong></h2><p>Pero no te desanimes, <strong>no es tu culpa...</strong></p><p>Esto no es falta de fe, es una se\u00f1al de Dios para que profundices tu conocimiento.</p><p>El universo de la Biblia es vasto y complejo, y es normal tener dificultades para comprender y memorizar los detalles.</p>",
        "id": "FxZ8ey"
      },
      {
        "type": "alert",
        "design": {
          "style": "warning",
          "basis": 100,
          "contrast": false
        },
        "text": "<h2><strong>Acertaste {{score}} de 10 preguntas</strong></h2><p>\u00a1Felicidades, est\u00e1s en el camino correcto!</p><p>Parece que conoces bastante sobre la Biblia, pero siempre hay algo nuevo por aprender.</p><p>Con un poco m\u00e1s de profundidad, puedes alcanzar a\u00fan m\u00e1s claridad y comprensi\u00f3n.</p><p>El universo de la Biblia es vasto y complejo, y puede ser dif\u00edcil memorizar todos los detalles.</p>",
        "id": "HoMuSm"
      },
      {
        "type": "alert",
        "design": {
          "style": "warning",
          "basis": 100,
          "contrast": false
        },
        "text": "<h2><strong>Acertaste&nbsp;9&nbsp;de 10 preguntas</strong></h2><p>\u00a1Felicidades, est\u00e1s en el camino correcto!</p><p>Parece que conoces bastante sobre la Biblia, pero siempre hay algo nuevo por aprender.</p><p>Con un poco m\u00e1s de profundidad, puedes alcanzar a\u00fan m\u00e1s claridad y comprensi\u00f3n.</p><p>El universo de la Biblia es vasto y complejo, y puede ser dif\u00edcil memorizar todos los detalles.</p>",
        "id": "jNwshv"
      },
      {
        "type": "clear",
        "design": {
          "basis": 100
        },
        "clear": "h-[5rem]"
      },
      {
        "type": "charts",
        "design": {
          "color": "gradient-invert",
          "area": true,
          "axisY": false,
          "axisX": true,
          "gridY": false,
          "gridX": false,
          "datasets": [
            {
              "fill": "gradient",
              "colors": [
                "#c7c7c7",
                "#fbbf24",
                "#22c55e"
              ]
            },
            {
              "fill": "solid",
              "colors": [
                "#13b443"
              ]
            },
            {
              "fill": "solid",
              "colors": [
                "#71717A"
              ]
            }
          ],
          "basis": "100"
        },
        "chart": {
          "id": "eLCN0d",
          "type": "bar",
          "datasetCount": 1,
          "xAxis": [
            "Personas de {{idade}} A\u00f1os"
          ],
          "datasets": [
            {
              "id": "xmZQcN",
              "title": "Conjunto A",
              "datas": [
                {
                  "id": "cU3iHv",
                  "value": "85",
                  "tooltip": "Usted"
                }
              ]
            },
            {
              "id": "uZxWg5",
              "title": "Conjunto B",
              "datas": [
                {
                  "id": "3LNbNl",
                  "value": "100",
                  "hiddenDot": true,
                  "tooltip": "Promedio de aciertos"
                }
              ]
            },
            {
              "id": "ZcbuWa",
              "title": "Conjunto C",
              "datas": [
                {
                  "id": "vGj5NI",
                  "value": 15,
                  "hiddenDot": true
                }
              ]
            }
          ],
          "name": "AEnKoe"
        }
      },
      {
        "type": "alert",
        "design": {
          "style": "danger",
          "basis": 100,
          "contrast": false
        },
        "text": "<p class=\"ql-align-center\">Lamentablemente, quedaste un 6% por debajo del promedio de las personas de tu edad en conocimiento b\u00edblico.</p>",
        "id": "F09B98"
      },
      {
        "type": "charts",
        "design": {
          "color": "gradient-invert",
          "area": true,
          "axisY": false,
          "axisX": true,
          "gridY": false,
          "gridX": false,
          "datasets": [
            {
              "fill": "gradient",
              "colors": [
                "#c7c7c7",
                "#fbbf24",
                "#22c55e"
              ]
            },
            {
              "fill": "solid",
              "colors": [
                "#13b443"
              ]
            },
            {
              "fill": "solid",
              "colors": [
                "#71717A"
              ]
            }
          ],
          "basis": "100"
        },
        "chart": {
          "id": "hj64Nv",
          "type": "bar",
          "datasetCount": 1,
          "xAxis": [
            "Personas de {{idade}} A\u00f1os"
          ],
          "datasets": [
            {
              "id": "xmZQcN",
              "title": "Conjunto A",
              "datas": [
                {
                  "id": "cU3iHv",
                  "value": "58",
                  "tooltip": "Usted"
                }
              ]
            },
            {
              "id": "uZxWg5",
              "title": "Conjunto B",
              "datas": [
                {
                  "id": "3LNbNl",
                  "value": "100",
                  "hiddenDot": true,
                  "tooltip": "Promedio de aciertos"
                }
              ]
            },
            {
              "id": "ZcbuWa",
              "title": "Conjunto C",
              "datas": [
                {
                  "id": "vGj5NI",
                  "value": 15,
                  "hiddenDot": true
                }
              ]
            }
          ],
          "name": "HEWcgr"
        }
      },
      {
        "type": "alert",
        "design": {
          "style": "danger",
          "basis": 100,
          "contrast": false
        },
        "text": "<p class=\"ql-align-center\">Lamentablemente, quedaste un 44% por debajo del promedio de las personas de tu edad en conocimiento b\u00edblico.</p>",
        "id": "KH12TP"
      },
      {
        "type": "charts",
        "design": {
          "color": "gradient-invert",
          "area": true,
          "axisY": false,
          "axisX": true,
          "gridY": false,
          "gridX": false,
          "datasets": [
            {
              "fill": "gradient",
              "colors": [
                "#c7c7c7",
                "#fbbf24",
                "#22c55e"
              ]
            },
            {
              "fill": "solid",
              "colors": [
                "#13b443"
              ]
            },
            {
              "fill": "solid",
              "colors": [
                "#71717A"
              ]
            }
          ],
          "basis": "100"
        },
        "chart": {
          "id": "97S2kP",
          "type": "bar",
          "datasetCount": 1,
          "xAxis": [
            "Personas de {{idade}} A\u00f1os"
          ],
          "datasets": [
            {
              "id": "xmZQcN",
              "title": "Conjunto A",
              "datas": [
                {
                  "id": "cU3iHv",
                  "value": "27",
                  "tooltip": "Usted"
                }
              ]
            },
            {
              "id": "uZxWg5",
              "title": "Conjunto B",
              "datas": [
                {
                  "id": "3LNbNl",
                  "value": "100",
                  "hiddenDot": true,
                  "tooltip": "Promedio de aciertos"
                }
              ]
            },
            {
              "id": "ZcbuWa",
              "title": "Conjunto C",
              "datas": [
                {
                  "id": "vGj5NI",
                  "value": 15,
                  "hiddenDot": true
                }
              ]
            }
          ],
          "name": "vRkw5X"
        }
      },
      {
        "type": "alert",
        "design": {
          "style": "danger",
          "basis": 100,
          "contrast": false
        },
        "text": "<p class=\"ql-align-center\">Lamentablemente, quedaste un 73% por debajo del promedio de las personas de tu edad en conocimiento b\u00edblico.</p>",
        "id": "biVXQR"
      },
      {
        "type": "arguments",
        "design": {
          "basis": 100
        },
        "arguments": [
          {
            "id": "Mz0P5J",
            "text": "<h2><span style=\"color: rgb(22, 163, 74);\">\u00bfLa&nbsp;buena&nbsp;noticia?</span></h2><p>Entender&nbsp;la&nbsp;Biblia&nbsp;no&nbsp;tiene&nbsp;por&nbsp;qu\u00e9&nbsp;ser&nbsp;una&nbsp;<strong>tarea&nbsp;dif\u00edcil.</strong></p><p>La&nbsp;verdadera&nbsp;transformaci\u00f3n&nbsp;ocurre&nbsp;cuando&nbsp;logras&nbsp;absorber&nbsp;las&nbsp;ense\u00f1anzas&nbsp;de&nbsp;Dios&nbsp;con&nbsp;<strong>simplicidad&nbsp;e&nbsp;intenci\u00f3n.</strong></p><p>Y&nbsp;yo&nbsp;descubr\u00ed&nbsp;la&nbsp;forma&nbsp;m\u00e1s&nbsp;simple&nbsp;de&nbsp;hacerlo.</p><p><strong style=\"color: rgb(22, 163, 74);\">\u2728\u00a0El&nbsp;nombre&nbsp;es&nbsp;Resumen&nbsp;cronol\u00f3gico&nbsp;de&nbsp;la&nbsp;Biblia</strong></p>",
            "chosen": false,
            "selected": false
          }
        ]
      },
      {
        "type": "image",
        "design": {
          "basis": "75",
          "horizontalAlign": "mx-auto"
        },
        "src": "/images/img_14_dYhVt-untitled-design-15.webp",
        "alt": ""
      },
      {
        "type": "button",
        "design": {
          "style": "success",
          "basis": 100,
          "pulse": true,
          "bubble": false,
          "fixed": false
        },
        "label": "Haga clic para descubrir c\u00f3mo recibirlo",
        "destination": "next",
        "pulse": true
      }
    ]
  },
  {
    "id": "dZGCfD",
    "title": "Sobre o entreg\u00e1vel",
    "show_back": false,
    "show_progress": true,
    "show_logo": false,
    "layers": [
      {
        "type": "text",
        "design": [],
        "text": "<h2 class=\"ql-align-center\"><strong>Mira&nbsp;el&nbsp;video&nbsp;a&nbsp;continuaci\u00f3n&nbsp;para&nbsp;descubrir&nbsp;el&nbsp;secreto&nbsp;para&nbsp;entender&nbsp;la&nbsp;Biblia.&nbsp;\ud83d\udc47</strong></h2>"
      },
      {
        "type": "script",
        "design": [],
        "script": "<vturb-smartplayer id=\"vid-69e12fde750b24d3132d77e4\" style=\"display: block; margin: 0 auto; width: 100%; max-width: 400px;\"><div class=\"vturb-player-placeholder\" style=\"position: relative; width: 100%; padding: 133.33333333333331% 0 0; z-index: 0; background-color: black;\"></div></vturb-smartplayer> <script type=\"text/javascript\"> var s=document.createElement(\"script\"); s.src=\"https://scripts.converteai.net/31957ec3-9250-4adb-93eb-bb2b4086c66f/players/69e12fde750b24d3132d77e4/v4/player.js\", s.async=!0,document.head.appendChild(s); </script>"
      },
      {
        "type": "script",
        "design": [],
        "script": "<a\n  id=\"botaoComprar\"\n  href=\"https://checkout.kashpay.com/checkout/checkout-1792201272859\"\n  target=\"_blank\"\n  rel=\"noopener noreferrer\"\n>\n  <div class=\"offer-wrapper\">\n    <div class=\"offer-button\">\n      Haz clic aqu\u00ed para assegurar tu material\n    </div>\n\n    <div class=\"offer-card\">\n      <div class=\"offer-header\">Recibe ahora!</div>\n\n      <div class=\"offer-body\">\n        <div class=\"offer-info\">\n          <div class=\"offer-title\">Resumen Cronologico</div>\n          <div class=\"offer-gift\">+ 9 regalos especiales</div>\n        </div>\n\n        <div class=\"offer-price-box\">\n          <div class=\"old-price\">De <s>US$188</s> por</div>\n          <div class=\"new-price\">US$ <strong>17.90</strong></div>\n          <div class=\"note\">solo hoy</div>\n        </div>\n      </div>\n    </div>\n  </div>\n</a>"
      },
      {
        "type": "script",
        "design": [],
        "script": "<style>\n  * {\n    box-sizing: border-box;\n  }\n\n  #botaoComprar {\n    display: block;\n    width: 100%;\n    max-width: 420px;\n    margin: 0 auto;\n    text-decoration: none;\n  }\n\n  .offer-wrapper {\n    width: 100%;\n    padding-top: 8px;\n  }\n\n  .offer-button {\n    min-height: 58px;\n    padding: 12px 16px;\n    border: 1px solid #d9d9d9;\n    border-radius: 16px;\n    background: linear-gradient(180deg, #1fb14b, #19a745);\n    color: #fff;\n    font-size: 15px;\n    font-weight: 700;\n    text-transform: uppercase;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    text-align: center;\n    letter-spacing: 0.5px;\n    line-height: 1.2;\n    box-shadow:\n      inset 0 2px 0 rgba(255,255,255,0.25),\n      0 2px 8px rgba(0,0,0,0.15);\n    transition: all 0.25s ease;\n    animation: pulseGreen 1.2s infinite;\n  }\n\n  .offer-card {\n    margin-top: 6px;\n    border-radius: 16px;\n    overflow: hidden;\n    border: 1px solid #d9d9d9;\n    background: #fff;\n  }\n\n  .offer-header {\n    background: #8f1b1f;\n    color: #fff;\n    text-align: center;\n    font-weight: 700;\n    font-size: 14px;\n    padding: 8px 12px;\n    line-height: 1.2;\n  }\n\n  .offer-body {\n    display: flex;\n    gap: 12px;\n    padding: 14px;\n    background: #f7f7f7;\n    align-items: center;\n  }\n\n  .offer-info {\n    flex: 1 1 auto;\n    min-width: 0;\n    font-weight: 700;\n    color: #111;\n    font-size: 18px;\n    line-height: 1.2;\n  }\n\n  .offer-title,\n  .offer-gift {\n    word-break: break-word;\n  }\n\n  .offer-price-box {\n    flex: 0 0 auto;\n    min-width: 128px;\n    max-width: 150px;\n    background: #efefef;\n    border-radius: 8px;\n    padding: 8px 10px;\n    text-align: right;\n  }\n\n  .old-price {\n    font-size: 12px;\n    color: #666;\n    line-height: 1.2;\n  }\n\n  .new-price {\n    font-size: 20px;\n    font-weight: 800;\n    color: #111;\n    line-height: 1.1;\n    margin-top: 2px;\n  }\n\n  .new-price strong {\n    font-size: 1.1em;\n  }\n\n  .note {\n    font-size: 11px;\n    color: #555;\n    line-height: 1.2;\n    margin-top: 2px;\n  }\n\n  #botaoComprar:hover .offer-button {\n    transform: translateY(-2px);\n    filter: brightness(1.05);\n  }\n\n  #botaoComprar:active .offer-button {\n    transform: scale(0.98);\n  }\n\n  a {\n    text-decoration: none;\n  }\n\n  /* ANIMA\u00c7\u00c3O PULSE */\n@keyframes pulseGreen {\n  0% {\n    box-shadow:\n      0 0 0 0 rgba(34, 197, 94, 0.6),\n      inset 0 2px 0 rgba(255,255,255,0.25),\n      0 2px 8px rgba(0,0,0,0.15);\n  }\n\n  70% {\n    box-shadow:\n      0 0 0 10px rgba(34, 197, 94, 0),\n      inset 0 2px 0 rgba(255,255,255,0.25),\n      0 2px 8px rgba(0,0,0,0.15);\n  }\n\n  100% {\n    box-shadow:\n      0 0 0 0 rgba(34, 197, 94, 0),\n      inset 0 2px 0 rgba(255,255,255,0.25),\n      0 2px 8px rgba(0,0,0,0.15);\n  }\n}\n</style>"
      },
      {
        "type": "script",
        "design": [],
        "script": "<style>\n    /* TABLETS / MOBILE GRANDE */\n  @media (max-width: 480px) {\n    #botaoComprar {\n      max-width: 100%;\n    }\n\n    .offer-button {\n      min-height: 54px;\n      padding: 12px;\n      font-size: 14px;\n      border-radius: 14px;\n    }\n\n    .offer-card {\n      border-radius: 14px;\n    }\n\n    .offer-header {\n      font-size: 13px;\n      padding: 8px 10px;\n    }\n\n    .offer-body {\n      gap: 10px;\n      padding: 12px;\n    }\n\n    .offer-info {\n      font-size: 18px;\n      line-height: 1.18;\n    }\n\n    .offer-price-box {\n      min-width: 118px;\n      max-width: 138px;\n      padding: 8px 9px;\n    }\n\n    .old-price {\n      font-size: 12px;\n    }\n\n    .new-price {\n      font-size: 18px;\n    }\n\n    .note {\n      font-size: 12px;\n    }\n  }\n\n  /* MOBILE MENOR */\n  @media (max-width: 390px) {\n    .offer-body {\n      gap: 8px;\n      padding: 10px;\n    }\n\n    .offer-info {\n      font-size: 15px;\n    }\n\n    .offer-price-box {\n      min-width: 108px;\n      max-width: 128px;\n      padding: 7px 8px;\n    }\n\n    .new-price {\n      font-size: 17px;\n    }\n  }\n\n  /* TELAS MUITO PEQUENAS */\n  @media (max-width: 360px) {\n    .offer-button {\n      font-size: 13px;\n      padding: 10px 12px;\n      line-height: 1.15;\n    }\n\n    .offer-body {\n      flex-direction: column;\n      align-items: stretch;\n    }\n\n    .offer-info {\n      font-size: 15px;\n      text-align: left;\n    }\n\n    .offer-price-box {\n      width: 100%;\n      max-width: 100%;\n      min-width: 0;\n      text-align: center;\n    }\n\n    .old-price,\n    .new-price,\n    .note {\n      text-align: center;\n    }\n  }\n</style>"
      },
      {
        "type": "script",
        "design": [],
        "script": "<script>\n  var link = \"https://checkout.kashpay.com/checkout/checkout-1792201272859\";\n  var textoBotao = \"Haz clic aqu\u00ed para assegurar tu material\";\n\n  (function () {\n    var botao = document.getElementById(\"botaoComprar\");\n    if (!botao) return;\n\n    botao.setAttribute(\"href\", link);\n\n    var texto = botao.querySelector(\".offer-button\");\n    if (texto) texto.textContent = textoBotao;\n  })();\n</script>"
      },
      {
        "type": "alert",
        "design": {
          "style": "danger"
        },
        "text": "<h3 class=\"ql-align-center\"><strong style=\"color: rgb(220, 38, 38);\">\ud83d\udd57&nbsp;\u00a1\u00daltimo&nbsp;d\u00eda&nbsp;a&nbsp;este&nbsp;precio!</strong></h3>",
        "id": "G0cmul"
      },
      {
        "type": "text",
        "design": {
          "basis": 50
        },
        "text": "<p class=\"ql-align-center\"><strong style=\"color: rgb(22, 163, 74); background-color: rgb(250, 250, 249);\">\u2713</strong><strong style=\"color: rgb(87, 83, 78); background-color: rgb(250, 250, 249);\">&nbsp;Acceso&nbsp;de&nbsp;por&nbsp;vida</strong></p>"
      },
      {
        "type": "text",
        "design": {
          "basis": 50
        },
        "text": "<p class=\"ql-align-center\"><strong style=\"color: rgb(22, 163, 74); background-color: rgb(250, 250, 249);\">\u2713</strong><strong style=\"color: rgb(87, 83, 78); background-color: rgb(250, 250, 249);\">&nbsp;Garant\u00eda&nbsp;de&nbsp;30&nbsp;d\u00edas</strong></p>"
      },
      {
        "type": "image",
        "design": {
          "basis": 100
        },
        "src": "/images/img_54_TUIaS-checkout.png",
        "alt": ""
      }
    ]
  }
];
