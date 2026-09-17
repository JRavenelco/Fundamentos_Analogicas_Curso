import React, { useMemo, useState } from 'react'
import { QUESTIONS, TOTAL } from './questions.js'

const LETTER = (i) => String.fromCharCode(65 + i)

export default function App() {
  const [answers, setAnswers] = useState({})   // { index: valor }
  const [graded, setGraded] = useState(false)

  const score = useMemo(() => {
    if (!graded) return null
    let pts = 0
    QUESTIONS.forEach((it, i) => {
      if (!it.t) return
      const v = answers[i]
      if (it.t === 'mc') { if (v === it.a) pts++ }
      else { const n = parseFloat(v); if (!isNaN(n) && Math.abs(n - it.a) <= (it.tol || 0)) pts++ }
    })
    return { pts, pct: Math.round((1000 * pts) / TOTAL) / 10 }
  }, [graded, answers])

  const setAns = (i, v) => setAnswers((a) => ({ ...a, [i]: v }))
  const reset = () => { setAnswers({}); setGraded(false) }

  const isOk = (it, v) => {
    if (it.t === 'mc') return v === it.a
    const n = parseFloat(v)
    return !isNaN(n) && Math.abs(n - it.a) <= (it.tol || 0)
  }
  const correctText = (it) =>
    it.t === 'mc' ? `${LETTER(it.a)}) ${it.o[it.a]}` : `${it.a} ${it.unit || ''}`

  const answered = Object.keys(answers).length

  return (
    <>
      <header>
        <h1>Examen de repaso · Fundamentos de Sistemas Electrónicos Analógicos</h1>
        <p>Semanas 1–4 (resistores, divisores, TBJ, MOSFET y PWM) · Licenciatura en Ingeniería Aeroespacial · UNAM</p>
      </header>

      <main>
        <div className="card">
          <b>Instrucciones.</b> Contesta y presiona <b>Calificar</b>. Las de opción se califican solas; las
          numéricas aceptan tolerancia (redondeo). Verás tu puntaje y la explicación de cada respuesta.
          <div className="fine" style={{ marginTop: 8 }}>
            {TOTAL} preguntas · 45 min · usa <i>V = I·R</i> y <i>P = V·I = I²R = V²/R</i>.
            Respondidas: <b>{answered}/{TOTAL}</b>
          </div>
        </div>

        {QUESTIONS.map((it, i) => {
          if (it.s) return <div className="sec" key={`s${i}`}>{it.s}</div>
          const v = answers[i]
          const ok = graded ? isOk(it, v) : null
          return (
            <div className="card q" key={i}>
              <h3>{i}. {it.q}</h3>
              {it.t === 'mc' ? (
                <div className="opts">
                  {it.o.map((op, j) => (
                    <label key={j}>
                      <input
                        type="radio"
                        name={`q${i}`}
                        checked={v === j}
                        onChange={() => setAns(i, j)}
                      />{' '}
                      {LETTER(j)}) {op}
                    </label>
                  ))}
                </div>
              ) : (
                <div>
                  <input
                    type="number"
                    step="any"
                    value={v ?? ''}
                    onChange={(e) => setAns(i, e.target.value)}
                  />
                  <span className="unit">{it.unit}</span>
                </div>
              )}
              {graded && (
                <div className={`fb ${ok ? 'good' : 'bad'}`}>
                  {ok
                    ? <>✔ Correcto<br />{it.e}</>
                    : <>✘ Correcta: <b>{correctText(it)}</b><br />{it.e}</>}
                </div>
              )}
            </div>
          )
        })}
      </main>

      <div className="bar">
        <span className="score">
          {score
            ? `Puntaje: ${score.pts}/${TOTAL} (${score.pct} %) — ${score.pct >= 80 ? '¡Excelente!' : score.pct >= 60 ? 'Vas bien: repasa lo rojo.' : 'Repasa y vuelve a intentar.'}`
            : 'Sin calificar'}
        </span>
        <span>
          <button onClick={() => { setGraded(true); window.scrollTo({ top: 0, behavior: 'smooth' }) }}>Calificar</button>{' '}
          <button className="ghost" onClick={reset}>Reiniciar</button>
        </span>
      </div>
    </>
  )
}
