# Examen en línea · Fundamentos de Sistemas Electrónicos Analógicos

Aplicación **React + Vite** con el examen de repaso de las **semanas 1–4**
(resistores y medición, divisores y equivalentes, TBJ, MOSFET y PWM).
Se autocorrige: opción múltiple y respuestas numéricas con tolerancia, con
explicación de cada respuesta y puntaje final.

## Contenido

- `src/questions.js` — banco de preguntas (sección, enunciado, opciones/valor, respuesta y explicación). **Aquí se edita el examen.**
- `src/App.jsx` — interfaz, calificación y retroalimentación.
- `src/styles.css` — estilo (paleta del curso: azul marino / dorado).
- `netlify.toml` — configuración de build/publicación para Netlify.
- `../examen_curso_online.html` — versión **sin build** (un solo archivo, por si no quieres Node).

## Correr en local

```powershell
cd docs\evaluacion\examen_react
npm install
npm run dev        # http://localhost:5173
npm run build      # genera dist\ listo para publicar
npm run preview    # sirve dist\ para probar el build
```

## Publicar en Netlify (3 opciones)

### 1) Arrastrar y soltar (la más rápida, sin cuenta técnica)
1. `npm run build`
2. Entra a https://app.netlify.com/drop
3. Arrastra la carpeta `dist` → Netlify te da una URL pública al instante.

### 2) Netlify CLI (permite actualizar con un comando)
```powershell
npm install -g netlify-cli
netlify login                 # abre el navegador para autorizar
netlify deploy                # prueba (draft): te da una URL temporal
netlify deploy --prod         # publica en la URL definitiva
```
La configuración de build/publicación la toma de `netlify.toml`
(`npm run build` → `dist`).

### 3) Conectado a GitHub (actualización automática)
1. Netlify → **Add new site → Import an existing project** → elige el repo.
2. Ajusta:
   - **Base directory:** `docs/evaluacion/examen_react`
   - **Build command:** `npm run build`
   - **Publish directory:** `dist`
3. Cada `git push` vuelve a publicar el examen automáticamente.

## Cómo agregar o cambiar preguntas

En `src/questions.js`, dos tipos:

```js
// opción múltiple: a = índice correcto (0 = A, 1 = B, ...)
{ t:'mc', q:'¿Cuál es la corriente…?', o:['0.5 A','2 A'], a:1, e:'I = V/R…' }

// numérica: a = valor correcto, tol = tolerancia, unit = unidades
{ t:'num', q:'¿Cuánto disipa…?', a:0.25, tol:0.02, unit:'W', e:'P = V²/R…' }
```

Para separar secciones: `{ s:'Sección 5 · Título' }`.

## Notas
- No incluir `node_modules/` ni `dist/` en git (ya están en `.gitignore`).
- El puntaje se calcula sobre el total de preguntas; las no respondidas cuentan como error.
- Todas las cifras del examen provienen de los ejercicios y simulaciones del curso
  (divisor 12 V, paralelo 5 V, TBJ VS=5.7 V, IRF640N, TL494 a 100 kHz).
