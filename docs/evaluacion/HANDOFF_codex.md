# Handoff para Codex — Examen en línea del curso (React + Netlify)

Documento de traspaso. Aquí está **qué ya existe, cómo funciona, cómo se publica y
qué falta por mejorar**. Objetivo: que Codex pueda iterar el examen sin
reconstruir contexto.

---

## 1. Repositorios y rama

| Rol | Remoto | Notas |
| --- | --- | --- |
| **Principal (privado)** | `https://github.com/JRavenelco/Fundamentos_Analogicas.git` | Todo el material del curso (incluye libros con derechos). Rama `main`. |
| **Público (curso)** | `https://github.com/JRavenelco/Fundamentos_Analogicas_Curso.git` | Solo material del curso (para enlaces de Gemini/Live). Rama `main`. |

Convención: se trabaja en el **principal** y se **copia a mano** al público lo que
deba ser público (no hay submódulo; el público es un repo espejo parcial en
`C:\Users\jesus\Documents\_curso_public`).

Commits recientes relevantes:

```text
7cf4a29 docs(evaluacion): agrega package-lock del examen
bfb5659 docs(evaluacion): examen en linea del curso (React+Vite listo para Netlify)
1e04722 docs(semana4): revision de pizarrones (15 laminas: T1-T3 en TikZ)
d02ade4 docs(semana4): generador PWM con TL494 (modelo educativo) ...
```

---

## 2. Qué se construyó

### 2.1 Examen en línea — React + Vite (la app principal)

Ruta: `docs/evaluacion/examen_react/`

```text
examen_react/
├─ index.html            # entrada Vite
├─ package.json          # React 18 + Vite 5 (scripts: dev, build, preview)
├─ package-lock.json     # build reproducible
├─ vite.config.js        # base:'./' y outDir:'dist'
├─ netlify.toml          # build = npm run build · publish = dist · SPA redirect + headers
├─ .gitignore            # node_modules/, dist/, .netlify/
├─ README.md             # cómo correr y desplegar (3 caminos)
└─ src/
   ├─ main.jsx           # createRoot
   ├─ App.jsx            # UI + calificación + retroalimentación
   ├─ questions.js       # ← BANCO DE PREGUNTAS (editar aquí)
   └─ styles.css         # paleta del curso (navy/gold)
```

**Funcionalidad actual**
- 34 reactivos en 4 secciones (semanas 1–4): resistores y medición, divisores y
  equivalentes, TBJ, MOSFET/PWM.
- Dos tipos de pregunta:
  ```js
  { t:'mc',  q:'...', o:['A','B','C','D'], a:1, e:'explicación' }        // opción múltiple
  { t:'num', q:'...', a:0.25, tol:0.02, unit:'W', e:'explicación' }      // numérica con tolerancia
  { s:'Sección 5 · Título' }                                             // separador de sección
  ```
- Botón **Calificar** → puntaje `pts/34`, porcentaje, mensaje según rango, y
  retroalimentación por pregunta (correcta vs. correcta-esperada + explicación).
- Contador de respondidas, botón **Reiniciar**, barra fija inferior, estilos
  responsivos y `@media print`.
- **Cálculo de puntaje**: `src/App.jsx` → `score` con `useMemo`; MC compara índice;
  numérica compara `Math.abs(v - a) <= tol`. Las no respondidas cuentan como error.
- Los números del examen provienen de los ejercicios y simulaciones reales del
  curso (divisor 12 V, paralelo 5 V → 8.788 mA/43.94 mW, TBJ VS=5.7 V,
  IRF640N 0.15 Ω → 24 mW, TL494 a 100 kHz).

### 2.2 Versión sin build (respaldo / offline)

`docs/evaluacion/examen_curso_online.html` — el mismo examen en **un solo archivo**
(HTML+CSS+JS, sin dependencias). Útil si no hay Node o para abrir con doble clic.
Al cambiar el banco de preguntas, hay que actualizar **ambos** (o generar el HTML
desde `questions.js`).

### 2.3 Material de la semana 4 relacionado (contexto del examen)

- Presentaciones: `docs/presentations/clase_4_pizarrones.pdf` (15 láminas),
  `clase_4_mosfet.pdf`, `clase_4_conmutador_hard_sat.pdf`, `clase_4_tl494_pwm.pdf`.
- Simulaciones LTspice (verificadas con LTspice XVII):
  `Simulaciones Ltspice/sim/semana4_01…05*.cir`, `semana4_irf640n_educativo.lib`,
  `tl494_educativo.sub`, `semana4_README.md`.
- Labs: `docs/labs/semana_4_*.md`. Guía: `docs/semana_4_guia_docente.md`.

---

## 3. Publicación (ya está en línea)

- **URL:** https://examen-analogicas-juriquilla.netlify.app
- **Site ID:** `78bc69f7-3da2-4b4e-8af4-b6a2bc10fa09`
- **Proyecto Netlify:** https://app.netlify.com/projects/examen-analogicas-juriquilla
- **Cuenta Netlify:** `jravenelco` (CLI ya instalada y autenticada en esta máquina).

Actualizar (dos comandos):

```powershell
cd docs\evaluacion\examen_react
npm run build
netlify deploy --prod --dir=dist --site 78bc69f7-3da2-4b4e-8af4-b6a2bc10fa09
```

Nota: `netlify sites:create` requiere `--account-slug jravenelco` (el nombre del
equipo, "uaq", NO funciona como slug en la API).

---

## 4. Entorno de desarrollo

- Node 20+ (probado con Node 24), npm; `npm install` → `npm run dev` (5173) →
  `npm run build` → `npm run preview`.
- No se versionan `node_modules/` ni `dist/` (`.gitignore`).
- LTspice XVII instalado en `C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe`
  (para re-correr las simulaciones: `& $exe -b archivo.cir` y leer el `.log`).

---

## 5. Qué falta / ideas para mejorar (priorizadas)

### P1 — Registro de resultados (lo más pedido para "aplicar online")
- Capturar **nombre + grupo** y enviar el puntaje al calificar.
- Opciones: **Netlify Forms** (sin backend, 100 envíos/mes gratis) o una
  **función serverless** (`netlify/functions/enviar.mjs`) que escriba en
  **Google Sheets / Airtable / Supabase**.
- Guardar también `localStorage` para que el alumno no pierda su intento.
- Vista docente `/resultados` con tabla y exportación **CSV**.
- Criterio de aceptación: al calificar, aparece en la hoja una fila con
  `fecha, nombre, grupo, puntaje, %, duración, respuestas_incorrectas`.

### P2 — Cronómetro y reglas de aplicación
- Temporizador configurable (p. ej. 45 min) con **autoenvío** al terminar.
- Barajar **orden de preguntas y de opciones** (semilla por alumno o por sesión).
- Modo "una pregunta a la vez" opcional.
- Criterio: dos alumnos no ven el mismo orden; el tiempo restante se muestra y al
  agotarse califica automáticamente.

### P3 — Más tipos de reactivo y ponderación
- Verdadero/falso, respuesta múltiple (varias correctas), emparejar
  (magnitud ↔ sensor), y **numérica con unidades** (validar `mA` vs `A`).
- Ponderación por sección configurable y reporte por sección (fortalezas/áreas).
- Criterio: el puntaje respeta los pesos y el reporte indica el % por sección.

### P4 — Calidad técnica
- **Tests** de la lógica de calificación (`vitest`): MC, numérica con tolerancia,
  sin responder, límites de tolerancia.
- `npm run lint` (ESLint) y formateo; TypeScript opcional (`questions.ts` con tipos).
- **CI**: GitHub Action que corra `npm ci && npm run build`; conectar el sitio
  Netlify al repo (Base directory `docs/evaluacion/examen_react`,
  Build `npm run build`, Publish `dist`) para auto-deploy en cada push.
- Accesibilidad: `aria-live` para el puntaje, focus visible, navegación por teclado,
  contraste AA; modo oscuro.
- Generar `examen_curso_online.html` automáticamente desde `questions.js`
  (script `npm run build:single`) para que no se desincronicen.

### P5 — Contenido
- Ampliar el banco a ~60 reactivos (semana 1–4) y marcar dificultad por pregunta.
- Añadir sección de **semana 5** cuando exista material.
- Variantes A/B/C por alumno (subconjuntos del banco).
- Reactivos con gráfica (SVG/TikZ exportado) para no lineales y regiones del TBJ.

---

## 6. Archivos que NO tocar sin querer

- `.netlify/` (estado del link de Netlify) y `node_modules/`: ignorados por git.
- `docs/classroom/Programa_*.docx/.pdf`, `Simulaciones Ltspice/sim/Practica_transistor.asc`
  y los `.asc` de semana 3 tenían **cambios pendientes de otros procesos**;
  confirmar con el usuario antes de commitearlos.
