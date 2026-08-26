# Material didáctico — VectorLab: Acondicionamiento de señales para instrumentación aeroespacial

Paquete didáctico completo para el laboratorio **"Acondiciona una galga para vuelo"**.
Cubre las seis capas del curso (Física → Dispositivo → Circuito → Sistema → Misión → Verificación)
con mini-clases, ejercicios resueltos, rúbricas, preguntas socráticas y un guion de laboratorio.

> **Uso en NotebookLM:** súbelo como fuente de texto. Cada mini-clase y ejercicio está escrito
> para que el cuaderno pueda generar resúmenes, audio-overviews y preguntas a partir de él.
> **Uso en el sitio:** los bloques están pensados para copiarse a las secciones existentes.

---

## PARTE A · Mini-clases (una por módulo)

### A1 · Física: portadores, unión PN y ruido — *¿de dónde sale la señal y el ruido?*

Antes de cablear nada, conviene recordar qué ocurre dentro del material. En un semiconductor la
conducción la realizan dos tipos de portadores: electrones (carga negativa) y huecos (ausencia de
electrón, carga positiva efectiva). El dopado introduce impurezas que aportan portadores: tipo N
(donadores, exceso de electrones) y tipo P (aceptores, exceso de huecos).

Al unir material P y N se forma la **unión PN**: los portadores difunden, se recombinan en la
frontera y dejan una zona de carga espacial (zona de deplexión) que genera una barrera de potencial.
Esa barrera es la que explica el comportamiento rectificador del diodo y la dependencia exponencial
corriente-tensión. Un dato clave para instrumentación: la tensión de la unión cae ~2 mV por cada °C
de aumento de temperatura, lo que convierte a cualquier unión en un termómetro involuntario y es la
raíz de la **deriva térmica** que después hay que compensar.

El **ruido** no es un defecto evitable, es física. Aparecen al menos tres mecanismos: ruido térmico
(Johnson-Nyquist), proporcional a la raíz de la temperatura, la resistencia y el ancho de banda
(v_n = √(4kTRB)); ruido de disparo (shot), asociado al cruce discreto de portadores por la unión; y
ruido 1/f (flicker), dominante a bajas frecuencias. La consecuencia de diseño es directa: la
resistencia de la primera etapa y su ancho de banda fijan el piso de ruido de toda la cadena.

**Idea fuerza:** la temperatura aparece dos veces —como deriva de la unión y como ruido térmico—,
así que "controlar la temperatura" no es un lujo, es parte del diseño de la medición.

---

### A2 · Dispositivo: diodos, BJT, FET y op-amp — *el sensor no es una fuente de voltaje ideal*

Cada dispositivo activo resuelve un problema distinto del acondicionamiento. El **diodo** rectifica y
protege (recorte de sobretensiones, descarga de transitorios). El **BJT** es un amplificador
controlado por corriente, con buena transconductancia pero corriente de base no nula. El **FET**
(JFET/MOSFET) es controlado por tensión y presenta una impedancia de entrada altísima, lo que lo
hace ideal para no cargar sensores de alta impedancia. El **amplificador operacional** integra
muchos transistores para ofrecer una ganancia enorme, dos entradas diferenciales y una salida de
baja impedancia.

El error conceptual más común —y que el sitio señala bien— es tratar todos los sensores como fuentes
de voltaje ideales. No lo son: una galga es una **resistencia variable**, un NTC/RTD es una
**resistencia dependiente de la temperatura**, y un piezoeléctrico se modela como una **fuente de
carga en paralelo con una capacitancia**, no como una fuente de tensión. El modelo correcto del
sensor determina qué dispositivo de entrada usar: divisor/puente para resistivos, buffer FET para
alta impedancia, amplificador de carga para piezoeléctricos.

**Idea fuerza:** primero modela el sensor (¿resistencia, corriente o carga?), y de ahí se deduce el
dispositivo de entrada, no al revés.

---

### A3 · Circuito: ganancia, filtro y protección — *la primera etapa define casi todo*

La interfaz analógica tiene tres tareas que a menudo compiten: amplificar la señal útil, rechazar lo
común (interferencia que entra por ambos cables) y no saturarse. El **amplificador de instrumentación
(INA)** es la herramienta canónica: tres op-amps que ofrecen alta impedancia en ambas entradas, una
ganancia fijada por una sola resistencia (RG) y un alto **CMRR** (rechazo de modo común). Con cables
largos y sensores diferenciales, el CMRR es lo que separa una medición usable de ruido puro.

Dos parámetros consumen margen de forma silenciosa: el **offset** (tensión de salida cuando la
entrada debería ser cero) y la **deriva térmica** de ese offset. Ambos gastan rango del ADC y pueden
enterrar señales pequeñas. Por eso la regla práctica: la primera etapa define gran parte del ruido,
la deriva y la capacidad de recuperarse ante sobrecarga. Equivocarse aquí no se arregla después.

La **protección** (diodos de recorte, resistencias serie, limitación de corriente) no es opcional en
entornos con transitorios. Y el **filtro** no es decorativo: limita el ancho de banda al rango con
significado físico, pero mal elegido puede borrar información mecánica real.

**Idea fuerza:** diseña la primera etapa para el peor caso de modo común y sobrecarga, no para el
caso nominal.

---

### A4 · Sistema: ADC, cableado y alimentación — *la cadena vale lo que vale su eslabón más ruidoso*

El **filtro anti-aliasing** es la frontera entre el mundo analógico continuo y el muestreado. El
teorema de Nyquist exige muestrear a más del doble de la frecuencia máxima con significado; cualquier
energía por encima de Nyquist se "pliega" (aliasing) y aparece disfrazada de señal lenta, imposible
de distinguir después. Por eso el filtro va **antes** del ADC, no después.

El **ADC** traduce tensión a números. Su resolución (bits) fija el **LSB** (el escalón mínimo
distinguible): un ADC de N bits con fondo de escala V_FS tiene LSB = V_FS / 2^N. Referido a la
entrada, ese LSB se divide entre la ganancia, así que la ganancia previa determina cuán fina es la
medición real. El objetivo es usar bien el rango: amplificar para acercarse al fondo de escala sin
saturar, dejando un margen de seguridad (típicamente 10 %).

El **cableado y la alimentación** son donde el circuito se vuelve físico: retornos de corriente,
lazos de masa, acoplamientos capacitivos, ruido de la fuente. Separar masas analógica, digital y de
potencia, y cuidar por dónde vuelve cada corriente, suele importar más que elegir un op-amp "mejor".

**Idea fuerza:** primero define qué frecuencia tiene significado físico; eso fija a la vez el filtro,
la tasa de muestreo y la interpretación de los datos.

---

### A5 · Misión aeroespacial: derating, WCCA y entorno — *un diseño existe cuando se puede defender*

El entorno aeroespacial cambia las prioridades. Hay vibración (que excita resonancias mecánicas y de
cableado), cables largos (más captación de interferencia), transitorios y picos de alimentación,
redes de 400 Hz, rangos de temperatura amplios y, en órbita, radiación. La norma **DO-160** define
las condiciones ambientales y los ensayos para equipos aerotransportados; las normas **ECSS** y las
guías **NASA** cumplen un papel análogo para espacio.

El **derating** consiste en usar los componentes por debajo de sus límites máximos (tensión,
corriente, potencia, temperatura) para ganar fiabilidad y vida útil. El **WCCA** (análisis de peor
caso) demuestra que el circuito cumple sus requisitos aun cuando todas las tolerancias, el
envejecimiento y la temperatura se combinan en contra. Hay tres métodos habituales: extremos (suma
de los peores casos, conservador), RSS (raíz de la suma de cuadrados, estadístico) y Monte Carlo
(simulación de la distribución real).

**Idea fuerza:** en vuelo, la deriva térmica y las tolerancias pueden pesar tanto como el error
inicial; el margen no se supone, se calcula y se documenta.

---

### A6 · Ejemplo integrador: galga de 2 mV/V con excitación de 5 V

Este es el hilo conductor del laboratorio. Un puente de galga con sensibilidad 2 mV/V, excitado a
5 V, entrega a plena escala 2 mV/V × 5 V = **10 mV diferenciales**. Para un ADC de 3.3 V de fondo de
escala, reservando 10 % de margen, el objetivo de salida es 2.97 V. La ganancia necesaria es
2.97 V / 10 mV = **297 V/V**. Con un INA826, cuya ganancia es G = 1 + 49.4 kΩ/RG, despejar para
G = 297 da RG ≈ 49.4 kΩ / 296 ≈ **167 Ω**. Para un filtro anti-aliasing de 50 Hz con C = 100 nF,
R = 1 / (2π·f·C) ≈ **31.8 kΩ**.

Pero el diseño no termina en el número: antes de fabricar hay que revisar modo común (¿satura el INA
aunque la diferencia sea pequeña?), offset, ruido referido a entrada y tolerancias de todos los
componentes. Ese paso de revisión es lo que distingue un cálculo de un diseño.

---

## PARTE B · Ejercicios (con solución)

**B1 (Física/Sistema).** Un ADC de 12 bits tiene fondo de escala de 3.3 V. (a) ¿Cuánto vale el LSB a
la entrada del ADC? (b) Si la ganancia de la cadena es 297 V/V, ¿cuánto vale el LSB referido a la
entrada del sensor?
*Solución:* (a) LSB = 3.3 / 2¹² = 3.3 / 4096 ≈ 0.806 mV. (b) Referido a entrada: 0.806 mV / 297 ≈
**2.7 µV**. Interpretación: cada escalón del ADC equivale a ~2.7 µV en la galga, así que ruidos por
encima de eso degradan la resolución efectiva.

**B2 (Circuito).** Se quiere una ganancia de 200 V/V con un INA826 (G = 1 + 49.4 kΩ/RG). Calcula RG.
*Solución:* 200 = 1 + 49.4 kΩ/RG → RG = 49.4 kΩ / 199 ≈ **248 Ω**.

**B3 (Sistema).** Un filtro RC pasa-bajos debe cortar a 1 kHz. Si C = 10 nF, ¿qué R se necesita?
*Solución:* f = 1/(2πRC) → R = 1/(2π·1000·10⁻⁸) ≈ **15.9 kΩ**.

**B4 (Sistema/Nyquist).** Una vibración tiene contenido útil hasta 2 kHz. ¿A qué frecuencia mínima
hay que muestrear y por qué conviene un margen mayor?
*Solución:* Nyquist exige f_s > 2 × 2 kHz = **4 kHz**. En la práctica se sobremuestrea (p. ej. 8–10
kHz) para relajar la pendiente del filtro anti-aliasing y reducir el plegado de ruido.

**B5 (Misión/Derating).** Un capacitor está especificado para 50 V. Con un criterio de derating del
60 % de la tensión nominal, ¿cuál es la tensión máxima de trabajo recomendada?
*Solución:* 0.60 × 50 V = **30 V** máximos en operación.

**B6 (Física/Deriva).** La unión de un diodo deriva ~ -2 mV/°C. Si la temperatura sube 40 °C,
¿cuánto cambia la tensión de unión y por qué importa en una galga?
*Solución:* ΔV ≈ -2 mV/°C × 40 °C = **-80 mV**. Importa porque esa deriva, si entra sin compensar al
front-end, puede ser mucho mayor que los 10 mV de señal útil del puente.

**B7 (WCCA, abierto).** El objetivo de ganancia es 297 V/V usando RG = 167 Ω con tolerancia ±1 % y la
red interna de 49.4 kΩ con ±0.5 %. Estima el rango de ganancia por el método de extremos.
*Pista de solución:* combina los extremos peores: RG mínimo (165.3 Ω) con red máxima (49.65 kΩ) da la
ganancia más alta, y al revés la más baja. Calcula G = 1 + R_int/RG en ambos extremos y compara el
margen contra el 10 % reservado del ADC.

---

## PARTE C · Rúbrica de evaluación (defensa de diseño)

Evalúa la entrega "Defiende tu diseño" en cuatro criterios, cada uno de 0 a 4 puntos
(0 ausente · 1 insuficiente · 2 suficiente · 3 sólido · 4 ejemplar).

**C1 · Objetivo y requisitos.** ¿Define magnitud física, rango, ancho de banda y restricciones del
ADC? *Ejemplar (4):* requisitos cuantificados y trazables a la misión; *Suficiente (2):* objetivo
correcto pero sin cifras de rango/ancho de banda; *Insuficiente (1):* descripción vaga del problema.

**C2 · Justificación de la topología.** ¿Explica por qué INA/buffer/amplificador de carga y cómo se
fijan ganancia y filtro? *Ejemplar (4):* elección razonada desde el modelo del sensor, con cálculo de
RG y del filtro; *Suficiente (2):* topología correcta pero justificada por costumbre, no por el
sensor; *Insuficiente (1):* topología sin relación con el sensor.

**C3 · Riesgos aeroespaciales y mitigación.** ¿Identifica modo común, deriva térmica, vibración,
transitorios, EMI y propone mitigaciones? *Ejemplar (4):* riesgos priorizados con mitigación
concreta y referencia a derating/DO-160/ECSS; *Suficiente (2):* lista riesgos sin mitigación clara;
*Insuficiente (1):* ignora el entorno.

**C4 · Plan de verificación.** ¿Propone evidencia DC, AC, transitorio, ruido, tolerancias, WCCA y
temperatura? *Ejemplar (4):* plan completo con criterios de aceptación y método WCCA elegido;
*Suficiente (2):* algunas pruebas sin criterios; *Insuficiente (1):* "lo probaré" sin plan.

**Interpretación:** 14–16 listo para revisión de hardware · 10–13 sólido con ajustes · 6–9 revisar
front-end y verificación · <6 rehacer desde requisitos.

---

## PARTE D · Preguntas socráticas (para guiar, no para responder en seco)

Sobre el sensor: ¿tu sensor entrega voltaje, corriente o carga? ¿Cómo cambia tu front-end si te
equivocas en ese modelo? ¿Qué pasa con la sensibilidad de un piezoeléctrico si alargas el cable?

Sobre la primera etapa: ¿por qué el CMRR importa más con cables largos? Si la diferencia entre tus
entradas es de 10 mV pero el modo común es de 2 V, ¿puede saturar tu INA? ¿Cómo lo verificarías
antes de fabricar?

Sobre el filtro y el ADC: ¿qué frecuencia de tu señal tiene significado físico y cuál es solo
interferencia? Si subes la ganancia para llenar el ADC, ¿qué le pasa al ruido? ¿Dónde colocas el
filtro y por qué no después del ADC?

Sobre temperatura y deriva: si la unión deriva 2 mV/°C, ¿cuánto error térmico tolera tu presupuesto?
¿Qué pesa más en tu caso, el error inicial o la deriva en vuelo?

Sobre la misión: ¿qué tres condiciones del entorno aeroespacial cambiarían tu diseño respecto a un
banco de laboratorio? ¿Cómo demuestras —no afirmas— que te queda margen? ¿Qué método de WCCA es
honesto para tu nivel de información: extremos, RSS o Monte Carlo?

---

## PARTE E · Guion de laboratorio — "Acondiciona una galga para vuelo"

**Objetivo.** Diseñar y justificar un canal de medición de deformación estructural, desde el puente
de galga hasta la entrada del ADC, apto para un ensayo de vibración aeroespacial.

**Materiales/recursos.** Modelo del puente de galga (2 mV/V), excitación 5 V, INA826 (o INA de
instrumentación equivalente), red RC para filtro anti-aliasing, ADC de referencia (3.3 V), y la
**calculadora "Ventana de diseño"** del sitio para validar números.

**Procedimiento.**
1. *Definir el fenómeno.* Establece magnitud (deformación), rango esperado y ancho de banda mecánico
   con significado físico. Anota la frecuencia máxima útil.
2. *Modelar el sensor.* Confirma que la galga es resistiva y calcula la salida diferencial a plena
   escala (sensibilidad × excitación).
3. *Dimensionar la ganancia.* Fija el fondo de escala del ADC y el margen (10 %). Calcula la ganancia
   objetivo y la RG del INA. Verifica con la calculadora del sitio.
4. *Diseñar el filtro anti-aliasing.* Elige la frecuencia de corte según el paso 1 y calcula R para el
   C disponible. Justifica por qué esa banda separa señal de interferencia.
5. *Revisar el peor caso.* Comprueba modo común, offset, ruido referido a entrada y tolerancias.
   Haz un WCCA por extremos de la ganancia (ejercicio B7).
6. *Documentar y defender.* Redacta objetivo, justificación de topología, riesgos aeroespaciales con
   mitigación y plan de verificación. Esto alimenta la rúbrica de la Parte C.

**Extensión (simulación piezoeléctrica).** Compara dos formas de leer un sensor piezoeléctrico: en
**modo tensión** (la sensibilidad depende de la capacitancia total, incluida la del cable, así que
alargar el cable atenúa la señal) frente a un **amplificador de carga** (la sensibilidad la fija la
capacitancia de realimentación Cf y es prácticamente inmune a la longitud del cable). Discute por qué
en aeroespacial, con cables largos, el amplificador de carga suele ganar.

**Criterio de cierre.** El laboratorio se aprueba cuando el estudiante puede *defender* cada decisión
con un número, un riesgo identificado y una prueba que lo verificaría, no solo cuando el circuito
"funciona" en simulación.

---

## PARTE F · Prompts listos para NotebookLM

Copia y pega estos prompts en tu NotebookLM (con este material y la bibliografía cargados como
fuentes) para seguir generando contenido coherente con el curso:

1. *Mini-clase:* "Genera una mini-clase de 400 palabras sobre [módulo] dirigida a estudiantes de
   ingeniería de 3.º año, con una idea fuerza al final y un error típico a evitar."
2. *Ejercicios:* "Crea 5 ejercicios numéricos sobre dimensionamiento de ganancia y filtro
   anti-aliasing, con solución paso a paso y unidades explícitas."
3. *Rúbrica:* "Convierte los cuatro criterios de la defensa de diseño en una rúbrica de 0–4 con
   descriptores observables por nivel."
4. *Preguntas socráticas:* "Dame 8 preguntas socráticas que ayuden a un estudiante a descubrir por
   qué el CMRR importa con cables largos, sin darle la respuesta directa."
5. *Laboratorio:* "Redacta una práctica guiada para acondicionar una galga de 2 mV/V hasta un ADC de
   3.3 V, con pasos, criterios de aceptación y un WCCA por extremos."
6. *Repaso:* "Resume las seis capas del curso en un mapa conceptual textual que conecte cada capa con
   su pregunta guía y su evidencia mínima."
