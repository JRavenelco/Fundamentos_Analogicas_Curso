# Semana 1: diagnostico y base electrica minima

Curso: Fundamentos de Sistemas Electronicos Analogicos, Ingenieria Aeroespacial.

Carga: 4 horas de teoria y 2 horas de practica.

## Resultado de aprendizaje

Al terminar la semana, el estudiante podra calcular corriente, caidas de
tension y potencia en una red resistiva de bajo voltaje, verificarla con
medicion y simulacion SPICE, y decidir con criterio de derating si cada
componente tiene margen termico suficiente para una aplicacion aeroespacial.

## Pregunta rectora

Un resistor que "funciona" en el calculo basico, ¿sobrevivira diez años en
orbita sin conveccion, con vibracion y con ciclos termicos?

## Diagnostico inicial

Antes de la teoria, aplicar el diagnostico de 8 preguntas (10 a 15 minutos,
individual, sin calificar). Cubre Ley de Ohm, divisor serie, potencia,
KVL, KCL, energia y criterio de derating. Se repite al cierre de la semana
para medir avance. Instrumento completo con clave de respuestas:

- `editorial/notebooklm_reviewed/clase_1_fundamentos_aeroespaciales_reviewed.json`

## Bloque 1: magnitudes electricas y Ley de Ohm

La tension es diferencia de potencial (energia por unidad de carga), la
corriente es flujo de carga por unidad de tiempo y la resistencia modela la
oposicion al movimiento de esa carga:

```text
V = I * R
```

Ideas clave:

- tension en voltios (V), corriente en amperios (A), resistencia en ohmios
- la Ley de Ohm es el primer puente entre fenomeno fisico, ecuacion y medicion
- toda magnitud calculada debe poder medirse con el multimetro

## Bloque 2: Leyes de Kirchhoff (KVL y KCL)

La Ley de Ohm describe un componente; Kirchhoff describe la red completa:

```text
KVL: suma de tensiones en una malla cerrada = 0
KCL: suma de corrientes que entran a un nodo = suma de las que salen
```

Ideas clave:

- en serie la corriente es unica y las caidas de tension suman Vin
- en paralelo la tension es comun y las corrientes se reparten
- KVL y KCL se verifican con medicion real y con simulacion `.op`

## Bloque 3: potencia, energia y calor

```text
P = V * I = I^2 * R = V^2 / R
E = P * t
```

Ideas clave:

- la potencia indica que tan rapido se transforma energia en calor
- el efecto Joule existe incluso en practicas de bajo voltaje
- la potencia crece con el cuadrado de la tension: subir Vin de 12 V a 14 V
  aumenta la disipacion un 36%

## Bloque 4: resistores reales

El resistor ideal no existe. El componente real se selecciona con tres
parametros ademas del valor en ohmios:

- tolerancia: 5% (banda dorada), 1% (serie E96) o 0.1% para instrumentacion
- TCR (coeficiente de temperatura): 100 a 200 ppm/°C en pelicula de carbon,
  50 ppm/°C o menos en pelicula metalica; critico en sensores
- potencia nominal: 1/8 W, 1/4 W, 1/2 W; definida a una temperatura ambiente
  y reducida por derating al subir la temperatura

El valor exacto calculado casi nunca existe: se elige el valor normalizado
mas cercano (series E12/E24/E96) y se mide el valor real antes de usarlo.

## Bloque 5: lectura aeroespacial y derating

En vacio no hay conveccion: la disipacion depende de conduccion y radiacion.
Por eso se aplica derating, tipicamente operar a 50% o menos de la potencia
nominal:

```text
P_derated_max = 0.5 * P_nominal
margen = P_derated_max / P_disipada
```

Un resistor que disipa 56 W con nominal de 60 W funciona en el papel, pero se
rechaza por margen insuficiente: se sube la potencia nominal, se distribuye
la disipacion o se cambia la topologia.

## Ejemplo numerico resuelto

Red serie de R1 = 1 kohm, R2 = 2.2 kohm y R3 = 3.3 kohm con Vin = 12 V
(la misma red del ejercicio guiado y del laboratorio):

```text
Rt = 1k + 2.2k + 3.3k = 6.5 kohm
I  = 12 V / 6.5 kohm = 1.846 mA

V1 = 1.846 V   V2 = 4.062 V   V3 = 6.092 V
V1 + V2 + V3 = 12.000 V   (confirma KVL)

P1 = 3.41 mW   P2 = 7.50 mW   P3 = 11.26 mW
Pt = 22.15 mW = 12 V * 1.846 mA   (balance de potencia)
```

Con resistores de 1/4 W y derating de 50%, el limite es 125 mW. El peor caso
(P3 = 11.26 mW) usa menos del 10% de ese limite: aceptado con amplio margen.

## Actividades de teoria activa

1. Calcular Rt, I, caidas de tension y potencias de la red serie antes de
   ver el ejemplo resuelto.
2. Predecir que cambia si Vin sube de 12 V a 14 V (corriente y potencia).
3. Medir tres resistores reales y calcular su error porcentual contra el
   valor nominal.
4. Decidir, con derating de 50%, si un resistor de 1/4 W acepta 0.2 W
   continuos y justificar la respuesta.
5. Explicar por que una red de 2 + 3 + 1 ohm a 12 V (2 A, 24 W) no es apta
   para protoboard.

## Evidencia y evaluacion

Entregable: diagnostico inicial y de salida, mas tabla de margen de potencia
de la red serie medida (plantilla en `docs/labs/semana_1_laboratorio.md`).

| Criterio | Peso |
| --- | ---: |
| Mediciones completas y ordenadas | 20% |
| Calculos correctos de Ohm, Kirchhoff y potencia | 25% |
| Simulacion y comparacion contra medicion | 20% |
| Analisis de derating y decision de seguridad | 25% |
| Claridad del reporte | 10% |

## Recursos web de apoyo

Lista completa validada en `docs/resources/recursos_didacticos.md`.

- PhET - Ley de Ohm:
  `https://phet.colorado.edu/sims/html/ohms-law/latest/ohms-law_en.html`
- PhET - Kit de circuitos DC:
  `https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html`
- Falstad Circuit Simulator: `https://www.falstad.com/circuit/`
- NASA S3VI - Diseño de circuitos para aplicaciones espaciales (PDF):
  `https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/electronic-circuit-design-and-analysis-for-space-applications.pdf`
- NASA LLIS - EEE Parts Derating (NASA-LLIS-0676):
  `https://llis.nasa.gov/lesson/676`
- EEVblog #819 - Leyes de Kirchhoff (video):
  `https://www.youtube.com/watch?v=WBfAEeEzDlg`

Sugerencias de uso:

- PhET Ley de Ohm: actividad de apertura de 5 minutos en el Bloque 2.
- PhET Kit DC: laboratorio virtual previo a la practica fisica.
- Falstad: apoyo visual a KCL/KVL antes de pasar a LTspice.
- NASA S3VI: lectura del docente para el Bloque 4 y ejemplo del regulador.
- NASA LLIS: respaldo oficial de la regla de derating de 50%.
- EEVblog #819: tarea de repaso tras ver Kirchhoff en teoria.

## Materiales de la semana

- Guia de laboratorio: `docs/labs/semana_1_laboratorio.md`
- Actividades de normas de resistores: `docs/labs/semana_1_actividades_normas_resistores.md`
- Respuestas de las actividades (docente): `docs/labs/semana_1_actividades_normas_resistores_respuestas.md`
- Presentacion de actividades (con enlaces): `docs/presentations/semana_1_actividades_normas_resistores.tex`
- Secuencia de simulaciones: `docs/labs/semana_1_simulaciones_ltspice.md`
- Teoria S1.2 (serie, KVL, balance de potencia): `docs/labs/semana_1_teoria_s12_serie_kvl_balance.md`
- Teoria S1.3 (paralelo, KCL, resistencia equivalente): `docs/labs/semana_1_teoria_s13_paralelo_kcl.md`
- Diapositivas: `docs/presentations/semana_1_diapositivas.md`
- Presentacion Beamer S1.2 (serie, KVL, balance): `docs/presentations/semana_1_s12_serie_kvl_balance.tex`
- Presentacion Beamer S1.3 (paralelo, KCL): `docs/presentations/semana_1_s13_paralelo_kcl.tex`
- Presentacion Beamer S1.4 (potencia y derating): `docs/presentations/semana_1_s14_potencia_derating.tex`
- Presentacion Beamer S1.5 (fuente real y falla): `docs/presentations/semana_1_s15_fuente_y_falla.tex`
- Presentacion Beamer S1.6 (divisor cargado): `docs/presentations/semana_1_s16_divisor_cargado.tex`
- Modulo editorial revisado:
  `editorial/notebooklm_reviewed/clase_1_fundamentos_aeroespaciales_reviewed.json`
- Circuitos LTspice: `Simulaciones Ltspice/sim/semana1_01` a `semana1_06`
- Recursos web: `docs/resources/recursos_didacticos.md`

## Fuentes base del repositorio

- Plan rector: `docs/weekly_course_plan_16_weeks_unam_aligned.md`
- Clase 1 extraida: `extracted_courses/57_FZ92uwT8/course_notes.md`
- Ampliacion aeroespacial: `extracted_courses/57_FZ92uwT8/aerospace_enrichment.md`
