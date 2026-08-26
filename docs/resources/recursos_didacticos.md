# Recursos Didacticos para Fundamentos de Electronica Analogica

Material web complementario para la Semana 1 (diagnostico y base electrica
minima). Cada enlace fue validado y se mapea al bloque de clase y a los
entregables del curso.

## Simuladores interactivos

| # | Titulo | Plataforma | Enlace | Uso en clase |
| --- | --- | --- | --- | --- |
| 1 | Ley de Ohm - Simulacion interactiva | PhET (Univ. de Colorado) | https://phet.colorado.edu/sims/html/ohms-law/latest/ohms-law_en.html | Bloque 2: manipular V y R y ver V = I x R y la densidad de portadores en vivo |
| 2 | Kit de construccion de circuitos DC | PhET (Univ. de Colorado) | https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html | Pre-lab: armar serie/paralelo y medir con voltimetro y amperimetro virtuales |
| 3 | Simulador animado de circuitos en tiempo real | Falstad | https://www.falstad.com/circuit/ | Bloque 2: flujo de electrones, bifurcacion de corrientes (KCL) y caidas de potencial (KVL) |

Descripcion didactica:

- **PhET - Ley de Ohm:** deslizadores de voltaje y resistencia muestran en
  tiempo real el cambio en la ecuacion y la densidad de particulas
  conductoras. Ideal como actividad de apertura de 5 minutos.
- **PhET - Kit de Circuitos DC:** laboratorio virtual previo al fisico.
  Permite circuitos serie/paralelo, bombillas reales (no ohmicas) y
  mediciones seguras con instrumentos virtuales.
- **Falstad:** muestra electrones amarillos en movimiento; facilita la
  comprension intuitiva de KCL y KVL. Usar junto a la secuencia LTspice
  (`docs/labs/semana_1_simulaciones_ltspice.md`).

## Guias y estandares de diseno aeroespacial

| # | Titulo | Autor / Organizacion | Enlace | Uso en clase |
| --- | --- | --- | --- | --- |
| 4 | Electronic Circuit Design and Analysis for Space Applications | NASA S3VI / SSRI | https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/electronic-circuit-design-and-analysis-for-space-applications.pdf | Bloque 4: disipacion en resistores, TCR, margen de temperatura, WCCA y radiacion |
| 5 | EEE Parts Derating (NASA-LLIS-0676) | NASA LLIS | https://llis.nasa.gov/lesson/676 | Bloque 4: tabla oficial de limites de derating y justificacion de confiabilidad |
| 6 | EEE-INST-002 - Derating Pages (suplementario) | NASA (espejo MIT) | https://snebulos.mit.edu/projects/reference/NASA-Generic/EEE-INST-002-DeratingPages.pdf | Criterio de seleccion de partes EEE con la tabla de derating por componente |

Descripcion:

- **NASA S3VI:** documento tecnico pedagogico que resuelve con ejemplos reales
  (regulador LT1086) el calculo de disipacion, la influencia del TCR y el
  procedimiento de WCCA frente a radiacion y envejecimiento.
- **NASA LLIS - Derating de partes:** leccion oficial que respalda la regla
  de operar resistores al 50-60% de su potencia nominal. Se menciona en la
  clase como respaldo a la regla practica `P_disipada <= 0.5 * P_nominal`.
- **EEE-INST-002:** referencia de diseno del programa NASA; uti para el
  docente y lecturas avanzadas, no obligatoria para estudiantes.

## Videotutoriales de fundamentos

| # | Titulo | Canal | Enlace | Uso en clase |
| --- | --- | --- | --- | --- |
| 7 | DC Fundamentals Part 4: Kirchhoff's Laws (EEVblog #819) | EEVblog | https://www.youtube.com/watch?v=WBfAEeEzDlg | Bloque 2: KCL y KVL con demostraciones de banca, complemento al video de teori de Kirchhoff |

## Temas clave que cubren

- Visualizacion intuitiva del flujo electrico (PhET y Falstad).
- Rigor en el analisis de peor caso WCCA (guias NASA).
- Conciliacion entre simulacion, medicion y criterio de diseno
  (los simuladores + las guias junto a la practica de laboratorio).

## Otros materiales de la Semana 1

- Guia docente: `docs/semana_1_guia_docente.md`
- Laboratorio: `docs/labs/semana_1_laboratorio.md`
- Secuencia de simulaciones LTspice: `docs/labs/semana_1_simulaciones_ltspice.md`
- Diapositivas: `docs/presentations/semana_1_diapositivas.md`
- Modulo editorial: `editorial/notebooklm_reviewed/clase_1_fundamentos_aeroespaciales_reviewed.json`