# Diagnóstico de conocimientos previos

**Fundamentos de Sistemas Electrónicos Analógicos**
UNAM · ENES Juriquilla · Ingeniería Aeroespacial
Semestre 2027-1 · Semana 1: 17–23 de agosto de 2026
M. en C. José de Jesús Santana Ramírez

> Fuente editable de `Diagnostico_Conocimientos_Previos_Fundamentos_Analogicas_2027-1.docx`.
> Regenerar el Word con `tools/build_diagnostico_docx.py` después de editar este archivo.

Este instrumento mide **antecedentes de semestres anteriores**; no sustituye las
actividades diagnósticas ni los contenidos propios de la Semana 1.

---

## Qué mide

Verifica el dominio de los antecedentes que se usarán desde la Unidad I.
Se asigna una puntuación únicamente para interpretar el diagnóstico; esa
puntuación no forma parte de la calificación final. El resultado indica cuánto
repaso de prerrequisitos conviene antes de polarizar transistores.

| Aspecto | Indicación |
| --- | --- |
| Duración | 45 minutos en total. Trabajo orientativo: A 10 min · B 8 min · C 8 min · D 11 min · E 4 min; los 4 min restantes son para encuadre y cierre. |
| Modalidad | Individual, sin apuntes. Calculadora científica sí; teléfono no. |
| Forma | Procedimiento a la vista. Toda cantidad con unidad (mA, kΩ, µF, Hz). |
| Si no recuerdas | Escribe «no lo recuerdo». También es un dato útil. |

---

## Sección A · Redes en DC y teoremas (4 × 7 = 28 pts)

Antecedente: Análisis de Circuitos Eléctricos (5.º). Se usa en polarización,
efecto de carga entre etapas y el equivalente visto por la base.

**A1.** Un divisor con R1 = 10 kΩ y R2 = 10 kΩ se alimenta con 12 V. Calcula la tensión de salida en vacío y cuando se conecta una carga de 10 kΩ en paralelo con R2.

**A2.** Obtén el equivalente de Thévenin (Vth y Rth) visto desde la unión de R1 y R2, con Vcc = 12 V, R1 = 8.2 kΩ hacia Vcc y R2 = 3.3 kΩ hacia tierra.

**A3.** Un circuito conectado y planar tiene 4 nodos y 6 ramas. ¿Cuántas ecuaciones independientes se plantean por análisis nodal y cuántas por análisis de mallas?

**A4.** Enuncia el principio de superposición: ¿en qué circuitos es válido y cómo se anula una fuente de tensión y una de corriente?

## Sección B · Capacitancia, inductancia y transitorios (3 × 7 = 21 pts)

Antecedente: Electricidad y Magnetismo (4.º) y Ecuaciones Diferenciales (3.º).
Se usa en acoplamiento, desacoplo y respuesta en baja frecuencia.

**B1.** Un capacitor de 100 nF se carga a través de 10 kΩ. Calcula la constante de tiempo, el porcentaje de carga alcanzado en 1τ y el tiempo para llegar a más del 99 %.

**B2.** Calcula la reactancia de un capacitor de 100 nF a 1 kHz. Indica además cómo se comporta un capacitor en DC y en muy alta frecuencia.

**B3.** Escribe la relación tensión-corriente de un inductor, calcula la energía almacenada por un inductor de 10 mH con 0.5 A y explica su comportamiento en DC.

## Sección C · Régimen senoidal, fasores y decibeles (3 × 7 = 21 pts)

Antecedente: Análisis de Circuitos (5.º), Señales (4.º) y Álgebra Lineal (2.º).
Se usa en ganancia, ancho de banda, filtros y osciladores.

**C1.** Una señal senoidal de 10 Vpp está montada sobre un nivel de 2 V DC. Determina el valor pico de la componente alterna, su valor eficaz (RMS) y el valor medio de la señal total.

**C2.** Una etapa tiene ganancia de tensión de 100. Exprésala en decibeles. Indica también a qué factor de tensión y de potencia corresponde −3 dB.

**C3.** Un resistor de 1 kΩ está en serie con un capacitor de 100 nF a 1 kHz. Escribe la impedancia en forma rectangular y en forma polar (magnitud y ángulo).

## Sección D · Dispositivos semiconductores (4 × 6 = 24 pts)

Antecedente: Dispositivos y Circuitos Electrónicos (6.º), seriación obligatoria.
Sin esto no arranca la Unidad I.

**D1.** Indica la caída típica de un diodo de silicio en conducción y su comportamiento en polarización inversa. En un rectificador de media onda con 12 V pico de entrada, ¿cuál es la tensión pico de salida?

**D2.** Con Vcc = 12 V y Rc = 2.2 kΩ, determina los dos puntos extremos de la recta de carga en el plano Ic–Vce y explica qué representa el punto Q sobre ella.

**D3.** Nombra las tres regiones de operación de un transistor bipolar e indica la condición de polarización de sus dos uniones en la región activa. Si β = 100 e IB = 20 µA, calcula IC e IE.

**D4.** En un MOSFET de canal n de enriquecimiento, explica qué es la tensión de umbral y en qué se diferencia el control de un MOSFET respecto al de un transistor bipolar.

## Sección E · Notación, instrumentos y simulación (2 × 3 = 6 pts)

Antecedente: laboratorios previos. Se usa desde la primera práctica.

**E1.** Escribe en notación de ingeniería con prefijo: 0.0000047 F, 4700 Ω y 0.00025 A.

**E2.** Indica cómo se conecta un amperímetro y cómo un voltímetro, y qué análisis de SPICE usarías para punto de operación, para respuesta en frecuencia y para transitorio.

## Experiencia previa (no puntúa)

Marca 1 = nulo, 2 = bajo, 3 = medio, 4 = alto.

- Análisis de circuitos: ____
- Diodos y transistores: ____
- Fasores y filtros: ____
- SPICE / LTspice: ____
- Instrumentos de laboratorio: ____

¿Cuánto tiempo ha pasado desde que cursaste Dispositivos y Circuitos Electrónicos? __________

¿Qué tema previo sientes más olvidado? __________

---

# Solo para el docente — no fotocopiar al grupo

## 1. Mapa: antecedente → dónde se ocupa en el curso

| Sección | Asignatura antecedente | Semestre | Dónde se ocupa aquí |
| --- | --- | --- | --- |
| A | Análisis de Circuitos Eléctricos: divisores, carga, Thévenin, nodos, mallas, superposición | 5.º | Polarización; carga entre etapas; Thévenin en la base; estabilidad del punto Q. |
| B | Electricidad y Magnetismo y Ecuaciones Diferenciales: RC, RL, energía | 4.º y 3.º | Acoplamiento y desacoplo; respuesta en baja frecuencia; constantes de tiempo. |
| C | Circuitos, Señales y Álgebra Lineal: fasores, complejos, decibeles | 5.º, 4.º y 2.º | Ganancia, ancho de banda, Bode, filtros activos, Barkhausen. |
| D | Dispositivos y Circuitos Electrónicos (seriación, 10 créditos) | 6.º | Todo el curso. Sin recta de carga y regiones no inicia la Unidad I. |
| E | Laboratorios previos: notación, instrumentos, SPICE | 2.º a 6.º | Prácticas desde el primer laboratorio. |

El bloque móvil del plan 2020 permite llegar a esta materia con hasta tres
semestres de distancia respecto de Dispositivos. No conviene suponer que
se cursó el semestre inmediato anterior.

## 2. Tiempos (45 minutos)

| Minuto | Actividad | Acción del docente |
| --- | --- | --- |
| 0–3 | Encuadre | Explicar que mide antecedentes y que la puntuación no afecta la calificación final. |
| 3–13 | Sección A | Anotar quién se detiene en el divisor con carga. |
| 13–21 | Sección B | Recorrer el aula. No dar fórmulas. |
| 21–29 | Sección C | Avisar que quedan 16 minutos. |
| 29–40 | Sección D | Sección decisiva por la seriación. Avisar el tiempo en el minuto 38. |
| 40–44 | Sección E | Instrumentos, notación y SPICE. |
| 44–45 | Cierre | Recoger el instrumento. El espacio en blanco también es información diagnóstica. |

Las Semanas 1 y 2 del plan (Ohm, derating, divisores) **no se omiten**
aunque el grupo salga alto. Este diagnóstico solo indica cuánto repaso
de prerrequisitos hay que insertar antes de polarización.

## 3. Clave

**A1.** Vacío: 6 V. Con carga: R2 ∥ RL = 5 kΩ → 4 V. El divisor cae 33 %.

**A2.** Vth = 3.443 V. Rth = 2.353 kΩ. Es el cálculo del divisor de base.

**A3.** Al ser conectado y planar: nodal, 3 ecuaciones (N − 1); mallas, 3 ecuaciones independientes (B − N + 1).

**A4.** Válido en circuitos lineales; no aplica directo a la potencia.
Fuente de tensión → cortocircuito. Fuente de corriente → abierto.

**B1.** τ = 1 ms. En 1τ: 63.2 %. En 5τ = 5 ms se supera el 99 %.

**B2.** Xc = 1.59 kΩ. DC: abierto. Alta frecuencia: cortocircuito.

**B3.** v = L·di/dt. E = 1.25 mJ. En DC estacionario: cortocircuito.

**C1.** Vpico AC = 5 V. Vrms = 3.54 V. Valor medio = 2 V (el nivel DC).

**C2.** 40 dB. −3 dB → 0.707 en tensión y 0.5 en potencia.

**C3.** Z = 1000 − j1592 Ω. \|Z\| = 1.88 kΩ. Ángulo = −57.9°.

**D1.** 0.6 a 0.7 V en directa. En inversa solo circula fuga mientras no se alcance la tensión de ruptura.
Salida pico ≈ 11.3 V.

**D2.** (12 V, 0) corte y (0, 5.45 mA) saturación. Q es el reposo sin señal.

**D3.** Corte, activa, saturación. Activa: BE directa, BC inversa.
IC = 2 mA. IE = 2.02 mA.

**D4.** VGS(th) es la tensión a partir de la cual comienza la conducción bajo
una corriente de drenaje especificada; no es la tensión de encendido pleno.
MOSFET: control por tensión, corriente de puerta ≈ 0 en régimen estacionario.
TBJ: requiere corriente de base.

**E1.** 4.7 µF, 4.7 kΩ, 250 µA.

**E2.** Amperímetro en serie; voltímetro en paralelo.
SPICE: `.op`, `.ac`, `.tran`.

## 4. Lectura de la puntuación diagnóstica

| Resultado | Lectura | Qué hacer |
| --- | --- | --- |
| ≥ 80 % | Antecedentes vigentes | Semanas 1 y 2 según el plan, con énfasis aeroespacial. |
| 60–79 % | Olvido normal | Repaso dirigido de los reactivos fallados. Calendario igual. |
| 40–59 % | Base frágil | Más ejercicios de carga, Thévenin y recta de carga en Semanas 1–2. |
| < 40 % en D | Seriación no consolidada | Prioridad: Boylestad (diodos y polarización) y reevaluación al cierre de Semana 2. |

## 5. Registro

Anotar aciertos por reactivo (A1–E2) al inicio y al reaplicar al cierre
de la Semana 2.
