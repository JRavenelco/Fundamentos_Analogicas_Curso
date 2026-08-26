---
marp: true
theme: default
paginate: true
size: 16:9
backgroundColor: #f9fbfd
color: #2c3e50
---

# Semana 1: Diagnóstico y Base Eléctrica Mínima
## Curso: Fundamentos de Sistemas Electrónicos Analógicos
### Ingeniería Aeroespacial - UNAM

***

**Notas del expositor:**
* **Bienvenida e Introducción:** Dé la bienvenida a los estudiantes al curso de Fundamentos de Sistemas Electrónicos Analógicos de la carrera de Ingeniería Aeroespacial de la UNAM.
* **Objetivo de la sesión:** Establecer el punto de partida del curso, realizar un diagnóstico de conocimientos previos de electricidad básica y entender cómo estos conceptos se aplican bajo la rigurosa perspectiva aeroespacial.
* **Dinámica:** La clase se dividirá en 4 bloques de 1 hora cada uno, abordando desde la estructura del curso hasta las limitaciones físicas reales y la traducción de estos conceptos a condiciones de vuelo y vacío espacial.
* **Fuentes de información:** Diseñado con base en el temario UNAM, los videos de AcadeNAS (Clases 0, 1 y 2), y la metodología del laboratorio VectorLab.

---

## Bloque 1: Estructura del Curso y Enfoque de Ingeniería

### ¿Qué aprenderemos en esta asignatura?
* **Interpretar esquemas complejos:** Entender el propósito y funcionamiento de cada componente en un plano eléctrico.
* **Resolver problemas de circuitos:** Calcular tensiones, corrientes y potencias con precisión analítica y mediante simulación.
* **Calcular y adaptar componentes:** Dimensionar y elegir componentes reales para cumplir con especificaciones técnicas específicas.
* **De la teoría al hardware:** No se trata de memorizar fórmulas, sino de defender decisiones de diseño que deben funcionar en condiciones extremas.

***

**Notas del expositor:**
* **Explicación del enfoque:** Enfatice a los estudiantes que el curso no tiene como fin únicamente la resolución matemática abstracta. El objetivo principal es que adquieran las habilidades de un diseñador de hardware aeroespacial.
* **Las tres decisiones de diseño:** Cuando un ingeniero ve un circuito, debe:
  1. Interpretar qué hace (ej. acondicionar la señal de un sensor).
  2. Resolverlo matemáticamente (saber si saturará o tendrá suficiente ganancia).
  3. Adaptarlo/Calcularlo (seleccionar valores comerciales y componentes específicos para una misión).
* **Pregunta para el grupo:** *¿Qué diferencia creen que existe entre un circuito que funciona en un simulador o en un protoboard de laboratorio, y uno que vuela a bordo de un satélite?* (Permita respuestas breves para introducir el concepto de entorno aeroespacial).
* **Fuentes:** Extrayendo los objetivos y alcances definidos en la Clase 0 (`extracted_courses/KkoudrHOpGE/course_notes.md` y `course_outline.json`).

---

## El Enfoque Aeroespacial: La Cadena VectorLab

### Del fenómeno físico a la telemetría en vuelo
* **Física:** ¿Cómo se genera la señal y el ruido en el sensor? (ej. portadores, temperatura, ruido térmico).
* **Dispositivo:** El sensor no es ideal. ¿Qué dispositivo de entrada usar? (diodos, BJT, FET, Op-Amp).
* **Circuito:** Tareas del circuito: ganancia, filtrado analógico y protección contra transitorios.
* **Sistema:** Conversión digital (ADC), prevención de aliasing, distribución de potencia y ruidos de masa.
* **Misión:** Cumplimiento de estándares de vuelo (DO-160, ECSS) mediante *derating*, análisis térmico y WCCA.
* **Verificación:** Pruebas que demuestran que el diseño cumple los requisitos bajo el peor escenario posible.

***

**Notas del expositor:**
* **Explicación:** Presente las seis capas de VectorLab. Explique que en ingeniería aeroespacial no diseñamos un circuito aislado; diseñamos un eslabón dentro de una cadena de instrumentación.
* **El hilo conductor del curso:** Usaremos el ejemplo de acondicionar una galga extensométrica (sensor de deformación estructural) a lo largo del semestre para ver cómo interactúan estas seis capas.
* **Idea Fuerza:** "La cadena de instrumentación es tan fuerte como su eslabón más débil y ruidoso." Si la primera etapa (el circuito analógico) tiene deriva térmica excesiva o ruido elevado, ni el mejor microcontrolador o algoritmo digital podrá recuperar la señal.
* **Fuentes:** Basado en `Material_Didactico_VectorLab.md` (Parte A: Introducción y Ejemplo Integrador).

---

## Bloque 2: Magnitudes Eléctricas Fundamentales

### Tensión, Corriente y Resistencia
* **Tensión ($V$ / Diferencia de Potencial):**
  * La fuerza motriz o energía por unidad de carga que impulsa a los electrones a moverse.
  * Unidad: Voltio (V).
* **Corriente ($I$ / Intensidad):**
  * El flujo o tasa de movimiento de carga eléctrica a través de un conductor.
  * Unidad: Amperio (A). $1\text{ A} = 1\text{ Coulomb/segundo}$.
* **Resistencia ($R$):**
  * La oposición inherente de un material al flujo de la corriente eléctrica.
  * Unidad: Ohmio ($\Omega$).

***

**Notas del expositor:**
* **Explicación básica:** Defina con precisión las unidades. Es común que los estudiantes confundan tensión y corriente. Explique que la tensión "existe" entre dos puntos (es una diferencia de potencial), mientras que la corriente "fluye" a través de un elemento.
* **Definición de Fuerza Electromotriz (FEM):** Mencione que la FEM es la capacidad de un generador (como una batería o celda solar) de mantener una diferencia de potencial activa.
* **Instrucciones para el profesor:** Dibuje en el pizarrón un circuito simple (fuente, conductor, receptor) para preparar la transición hacia la analogía hidráulica del siguiente slide.
* **Fuentes:** Clase 1 (`extracted_courses/57_FZ92uwT8/course_notes.md` y `course_outline.json`).

---

## La Analogía Hidráulica de los Circuitos

### Visualizando el movimiento de la carga
* **La Batería $\rightarrow$ La Bomba de Agua:**
  * Crea la diferencia de presión (tensión / potencial) para mover el fluido.
* **El Conductor $\rightarrow$ La Tubería:**
  * Canaliza y transporta el agua (corriente de electrones).
* **El Resistor $\rightarrow$ La Restricción o Válvula:**
  * Reduce el diámetro del conducto, oponiéndose al flujo de agua y causando una caída de presión (tensión).
* **El Receptor $\rightarrow$ Turbina / Molino:**
  * Convierte la energía hidráulica en trabajo útil (calor, luz, movimiento).

***

**Notas del expositor:**
* **Explicación:** Utilice esta analogía clásica para consolidar el entendimiento intuitivo.
  * Mayor altura del tanque de agua o mayor potencia de la bomba = mayor voltaje.
  * Diámetro de la tubería más ancho = menor resistencia, por lo tanto fluye más agua (corriente).
  * Si cerramos una válvula (aumento de resistencia), el flujo de agua (corriente) disminuye considerablemente.
* **Pregunta socrática:** *Si cortamos un tubo por la mitad, el agua se derrama. Si cortamos un cable eléctrico por la mitad, ¿se derraman los electrones? ¿Por qué?* (El aire tiene una resistencia extremadamente alta, actuando como un aislante que detiene la corriente, a diferencia del agua que fluye libremente en la atmósfera).
* **Fuentes:** Clase 1 (`extracted_courses/57_FZ92uwT8/course_notes.md`).

---

## La Ley de Ohm y sus Límites Físicos

### Relación fundamental de la electricidad: $V = I \cdot R$
* **Definición:** La corriente que circula por un conductor es directamente proporcional a la tensión aplicada e inversamente proporcional a la resistencia del material.
* **Límites de Aplicación (¿Es una ley universal?):**
  * **Materiales Óhmicos:** Presentan una relación estrictamente lineal entre V e I (conductores metálicos a temperatura constante).
  * **Materiales No Óhmicos:** La resistencia cambia ante estímulos. Ejemplos: diodos, semiconductores, termistores y varistores.
  * **Factores influyentes:** Temperatura, intensidad del campo eléctrico y frecuencia de la señal.

***

**Notas del expositor:**
* **Explicación avanzada:** Señale que comúnmente se enseña la Ley de Ohm como una verdad absoluta en todos los componentes, pero esto es un error conceptual severo.
* **Límites Físicos:**
  * En materiales no óhmicos (como un diodo de silicio), la relación no es una línea recta, sino exponencial.
  * Incluso en resistores de metal "óhmicos", la resistencia cambia al calentarse debido al coeficiente de temperatura.
* **Relevancia Aeroespacial:** Los sensores RTD (como el Pt100) basan su funcionamiento en el cambio de su resistencia con la temperatura. Por lo tanto, se comportan de forma óhmica únicamente dentro de rangos calibrados muy estrechos.
* **Fuentes:** Clase 1 Enrichment (`extracted_courses/57_FZ92uwT8/aerospace_enrichment.md` - Technical improvements).

---

## Convención Pasiva de Signos

### Regla fundamental para el análisis de circuitos
* **Elementos Pasivos (Resistores, Capacitores, Inductores):**
  * La corriente $I$ **entra** por el terminal de **mayor potencial** (positivo, $+$).
  * La potencia calculada $P = V \cdot I$ es **positiva** ($P > 0$).
  * El componente **absorbe o disipa** energía.
* **Elementos Activos (Fuentes de Tensión, Baterías, Celdas Solares):**
  * La corriente $I$ **sale** por el terminal **positivo** ($+$).
  * La potencia absorbida es **negativa** ($P < 0$).
  * El componente **entrega** energía al sistema.

***

**Notas del expositor:**
* **Explicación:** Explique que esta convención es crucial para evitar errores de signo al aplicar las leyes de Kirchhoff (nodos y mallas) en circuitos complejos.
* **Análisis de Balance:** La suma de todas las potencias en un circuito cerrado debe ser exactamente igual a cero ($\sum P = 0$), lo cual es una consecuencia directa del principio de conservación de la energía.
* **Relevancia Aeroespacial:** En el sistema de distribución eléctrica de un satélite (EPS), las baterías cambian de rol: actúan como elemento activo cuando alimentan la computadora de vuelo (descarga, corriente sale de $+$), y como elemento pasivo cuando se cargan usando los paneles solares (carga, corriente entra por $+$). Aplicar mal los signos en las simulaciones de balance de potencia puede causar el sobrediseño de baterías o el fallo catastrófico por descarga total en órbita.
* **Fuentes:** Clase 1 Enrichment (`extracted_courses/57_FZ92uwT8/aerospace_enrichment.md`).

---

## Potencia vs. Energía en Circuitos Eléctricos

### Tasa instantánea de trabajo frente a capacidad acumulada
* **Potencia Eléctrica ($P$):**
  * La rapidez o tasa con la que se transfiere o transforma la energía por unidad de tiempo.
  * Unidad: Vatio (W). $P = V \cdot I = I^2 \cdot R = \frac{V^2}{R}$.
* **Energía Eléctrica ($E$):**
  * La cantidad total de trabajo eléctrico realizado o calor disipado durante un período de tiempo.
  * Unidad: Julio (J) o Kilovatio-hora (kWh). $E = P \cdot t$.
* **Diferencia Crítica:**
  * Potencia = ¿Qué tan rápido se genera calor en un componente?
  * Energía = ¿Cuánto calor total se acumuló o cuánta carga retiene la batería?

***

**Notas del expositor:**
* **Analogía:**
  * Potencia es el velocímetro de un vehículo (km/h); energía es el odómetro que mide la distancia total recorrida (km).
  * Potencia es el caudal de una llave de agua (litros/minuto); energía es el volumen de agua acumulado en una cubeta (litros).
* **Pregunta socrática:** *Si un resistor de potencia de un transmisor satelital opera a 5 W durante 10 milisegundos, ¿generará el mismo calor acumulado que si operara a 5 W durante 10 minutos? ¿Cuál es la potencia instantánea y cuál es la energía térmica total transferida?*
* **Relevancia Aeroespacial:** Dimensionamiento de baterías de emergencia para la Unidad de Potencia Auxiliar (APU) o luces de cabina. Si fallan los generadores principales de una aeronave, se debe calcular la energía total consumida en Wh durante el tiempo mínimo de autonomía (ej. 30 minutos) para seleccionar la capacidad correcta de la batería.
* **Fuentes:** Clase 1 (`extracted_courses/57_FZ92uwT8/course_notes.md`) y Clase 1 Enrichment (`57_FZ92uwT8/aerospace_enrichment.md`).

---

## Bloque 3: Resistores Reales y Limitaciones de Componentes

### El componente real no es un símbolo matemático ideal
* **Valor Nominal:** El valor teórico deseado de resistencia.
* **Tolerancia:** El desvío máximo permitido sobre el valor nominal.
  * Expresado en porcentaje ($\pm\%$).
* **Series E (Valores Normalizados):**
  * Estándar internacional para evitar fabricar infinitos valores.
  * **E12:** $\pm 10\%$ de tolerancia (12 valores por década: 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82).
  * **E24:** $\pm 5\%$ de tolerancia (24 valores por década).
  * **E96:** $\pm 1\%$ de tolerancia (96 valores por década, común en circuitos de precisión).

***

**Notas del expositor:**
* **Explicación:** Explique por qué existen las series normalizadas: los fabricantes producen resistores cuyas campanas de Gauss de tolerancia se traslapan ligeramente. Si fabricaran todos los valores intermedios, muchos componentes serían descartados o comercialmente inviables.
* **Instrucciones para el profesor:** Explique cómo calcular el rango de resistencia real. Por ejemplo, un resistor nominal de $1\text{ k}\Omega$ con tolerancia de $\pm 10\%$ (serie E12) puede medir físicamente en el laboratorio cualquier valor entre $900\ \Omega$ y $1100\ \Omega$.
* **Fuentes:** Clase 2 (`extracted_courses/jli6YBkRt3U/course_notes.md` y `course_outline.json`).

---

## Coeficiente de Temperatura y Código de Colores

### TCR: El efecto del calor en la resistencia
* **Coeficiente de Temperatura de la Resistencia (TCR):**
  * Especifica cuánto varía el valor del resistor por cada grado Celsius de cambio en la temperatura.
  * Unidad: Partes por millón por grado Celsius ($\text{ppm}/^\circ\text{C}$).
  * Fórmula de variación: $\Delta R = R_{nominal} \cdot TCR \cdot \Delta T$.
* **Lectura del Código de Colores:**
  * **4 bandas:** 1er dígito, 2do dígito, multiplicador, tolerancia.
  * **5 bandas (Precisión):** 1er, 2do, 3er dígito, multiplicador, tolerancia.
  * **6 bandas:** Añade la sexta banda para el Coeficiente de Temperatura (TCR).
  * *Corrección técnica crítica:* La banda marrón en la posición de tolerancia indica **$\pm 1\%$**, no $5\%$ (el oro indica $\pm 5\%$).

***

**Notas del expositor:**
* **Ejemplo práctico de TCR:** Si un circuito de acondicionamiento de precisión utiliza un resistor de $10\text{ k}\Omega$ con un TCR estándar de $100\text{ ppm}/^\circ\text{C}$, y la temperatura en el satélite cambia en $\Delta T = 50^\circ\text{C}$:
  $$\Delta R = 10000 \cdot (100 \times 10^{-6}) \cdot 50 = 50\ \Omega$$
  ¡La resistencia real varía en $50\ \Omega$! Esto representa un error del $0.5\%$, el cual es catastrófico en un amplificador de instrumentación de ganancia elevada.
* **Enfoque aeroespacial:** Para puentes de Wheatstone y divisores de referencia de ADC, requerimos resistores de película metálica de ultra-bajo TCR ($25$ a $50\text{ ppm}/^\circ\text{C}$) y tolerancias de $\pm0.1\%$ a $\pm1\%$ para minimizar la deriva térmica.
* **Fuentes:** Clase 2 (`extracted_courses/jli6YBkRt3U/course_notes.md`) y Clase 2 Enrichment (`jli6YBkRt3U/aerospace_enrichment.md`).

---

## Tipos Constructivos de Resistores Fijos

| Tipo | Precisión y TCR | Nivel de Ruido | Robustez Física y Aplicación |
| :--- | :--- | :--- | :--- |
| **Composición de Carbón** | Muy pobre ($\pm10\%$, alto TCR) | Muy Alto (Flicker) | Evitar en aeroespacial. Absorbe humedad. |
| **Película Metálica** | Excelente ($\pm0.1\%$-$\pm1\%$, bajo TCR) | Muy Bajo | Estándar en señales de sensores y control. |
| **Bobinados** | Buena precisión, alta disipación | Bajo (pero muy inductivos) | Fuentes de potencia, motores. No apto para RF. |
| **SMD (Montaje Superficial)** | Excelente | Muy Bajo | Dominante en aviónica. Resiste vibración/choque. |

***

**Notas del expositor:**
* **Explicación constructiva:** Analice los materiales de fabricación. Los resistores bobinados constan de un hilo conductor enrollado sobre un núcleo cerámico; este arrollamiento actúa físicamente como una bobina (inductor parásito), lo que distorsiona las señales de alta frecuencia.
* **Robustez mecánica:** En aplicaciones espaciales y de aviación, los resistores SMD (como los encapsulados 0805 o 0603) son preferidos sobre los resistores con terminales de inserción (Through-Hole). Su baja masa reduce drásticamente las fuerzas mecánicas de fatiga en las soldaduras durante el lanzamiento (vibración severa).
* **Fuentes:** Clase 2 (`extracted_courses/jli6YBkRt3U/course_notes.md` y `course_outline.json`) y Clase 2 Enrichment (`jli6YBkRt3U/aerospace_enrichment.md`).

---

## Resistores Variables y No Lineales

* **Resistores Variables (Potenciómetros y Trimpots):**
  * Usan un cursor móvil para variar la resistencia de forma lineal o logarítmica.
  * *Riesgo aeroespacial:* Sensibles a la vibración y al desgaste por rozamiento. Deben fijarse con epoxi post-ajuste.
* **Termistores (NTC / PTC):**
  * NTC: Resistencia disminuye al aumentar temperatura.
  * PTC: Resistencia aumenta con la temperatura. Alta no linealidad.
* **RTD (Pt100, Pt1000):**
  * Alta precisión y linealidad. Requieren **configuraciones Kelvin de 3 o 4 hilos** para compensar la resistencia parásita de cables largos.
* **Varistores:**
  * Resistencia no lineal que cae drásticamente ante sobretensiones. Protegen contra transitorios.
* **LDR (Resistores Dependientes de Luz):**
  * Lentas y térmicamente inestables. En aviónica se prefieren fotodiodos o fototransistores.

***

**Notas del expositor:**
* **Explicación de la conexión Kelvin de 3 y 4 hilos:** Explique cómo la resistencia de los cables de conexión falsea la lectura en un sensor resistivo de baja resistencia como el RTD Pt100 ($100\ \Omega$ a $0^\circ\text{C}$). Con 2 hilos, la resistencia de un cable largo (ej. de $5\ \Omega$) se suma a la del sensor, induciendo un error de más de $10^\circ\text{C}$. El método de 4 hilos inyecta corriente por un par y mide voltaje de alta impedancia por otro, anulando el efecto del cable.
* **Pregunta socrática:** *¿Por qué creen que el uso de un trimpot (potenciómetro de ajuste manual) puede ser peligroso en un satélite que se lanza en un cohete Falcon 9?* (La vibración del lanzamiento puede mover físicamente el cursor, alterando la calibración del sensor).
* **Fuentes:** Clase 2 (`jli6YBkRt3U/course_notes.md` y `aerospace_enrichment.md`).

---

## Bloque 4: Traducción Aeroespacial y Confiabilidad

### Gestión Térmica en el Vacío Espacial
* **Mecanismos de Transferencia de Calor Terrestres:**
  * Conducción, Radiación y **Convección** (intercambio térmico a través del aire circundante).
* **Mecanismos de Transferencia en el Vacío del Espacio:**
  * Conducción (patas del componente, pistas y planos de cobre de la PCB).
  * Radiación (emisión infrarroja del cuerpo del componente).
  * **Convección = Cero (No hay aire).**
* **Consecuencia de diseño:**
  * Los componentes se calientan mucho más rápido que en la Tierra.
  * Se requiere acoplar térmicamente los resistores de potencia a chasis mediante planos de cobre y vías térmicas.

***

**Notas del expositor:**
* **Explicación del vacío:** Este concepto es vital. En la Tierra, un resistor de 1 W al aire libre disipa calor en gran medida por convección natural. En el vacío, el aire no existe, de modo que el calor se acumula rápidamente en el cuerpo del resistor a menos que proveamos una ruta conductora de metal hacia el chasis metálico del satélite (sumidero térmico).
* **Instrucciones para el profesor:** Explique la física de la disipación térmica y enfatice por qué la potencia máxima nominal de un resistor de catálogo comercial no es real en el vacío espacial.
* **Fuentes:** Clase 2 Enrichment (`extracted_courses/jli6YBkRt3U/aerospace_enrichment.md` - Technical improvements).

---

## Criterios de Derating (Reducción de Parámetros)

### ¿Cómo asegurar que un componente viva más allá de su garantía?
* **Definición de Derating:** Operar los componentes electrónicos por debajo de sus límites máximos declarados por el fabricante para reducir la tasa de falla y compensar variaciones ambientales.
* **Estándares Rectores:**
  * **ECSS-Q-ST-30-11C** (Agencia Espacial Europea).
  * **NASA EEE-INST-002** (Criterio para selección de partes EEE).
* **Reglas Prácticas de Derating:**
  * **Resistores:** Potencia de diseño $\le 50\%$ de la potencia nominal ($P_{disipada} \le 0.5 \cdot P_{nominal}$).
  * **Capacitores:** Tensión de diseño $\le 60\%$ de la tensión nominal ($V_{trabajo} \le 0.6 \cdot V_{nominal}$).
  * **Semiconductores:** Temperatura de unión máxima restringida a $110^\circ\text{C}$ (frente a $150^\circ\text{C}$ comercial).

***

**Notas del expositor:**
* **Explicación de la ecuación de potencia:**
  * Si un resistor comercial tiene una potencia nominal de $0.25\text{ W}$, bajo derating estricto del $50\%$ no podemos disipar en él más de $0.125\text{ W}$ en el peor caso.
  * Si los cálculos de nuestro circuito muestran que disipará $0.15\text{ W}$, debemos elegir un resistor de mayor tamaño comercial, por ejemplo, uno con potencia nominal de $0.5\text{ W}$ (cuyo límite con derating es de $0.25\text{ W}$).
* **Importancia:** El derating compensa el desgaste por envejecimiento (aging), el estrés por radiación y las variaciones térmicas imprevistas en órbita.
* **Fuentes:** Clase 2 Enrichment (`jli6YBkRt3U/aerospace_enrichment.md`), Clase 1 Enrichment (`57_FZ92uwT8/aerospace_enrichment.md`), y Ejercicio B5 de `Material_Didactico_VectorLab.md`.

---

## Análisis de Peor Caso (WCCA) y Seguridad

### Demostrando matemáticamente que el diseño es robusto
* **¿Qué es el WCCA (Worst-Case Circuit Analysis)?**
  * Demostrar que el circuito cumple con todos sus requisitos de diseño cuando todas sus tolerancias individuales, derivas por temperatura y envejecimiento se combinan en la dirección más desfavorable.
* **Tres Métodos Principales:**
  1. **Método de Extremos (Worst-Case Sum):** Se toman los valores mínimos y máximos absolutos de cada componente. Muy conservador, pero seguro.
  2. **Método RSS (Root-Sum-Square):** Enfoque estadístico. Supone que no todas las variables fallarán juntas en el extremo absoluto.
  3. **Método de Monte Carlo:** Simulación de miles de iteraciones usando distribuciones de probabilidad reales de los componentes.

***

**Notas del expositor:**
* **Explicación didáctica:** En un divisor de voltaje compuesto por dos resistores de $\pm1\%$ de tolerancia y un ADC que acepta $3.3\text{ V}$ máximo con un $10\%$ de margen de seguridad (rango útil $2.97\text{ V}$):
  * Debemos verificar el peor caso: resistor de arriba con valor mínimo tolerado y resistor de abajo con valor máximo tolerado.
  * Si en este peor escenario el voltaje supera $2.97\text{ V}$, el diseño no es seguro y el ADC podría saturar o dañarse.
* **Idea Fuerza:** "En ingeniería de vuelo, la deriva y la tolerancia no se ignoran, se calculan y se documentan en el WCCA."
* **Fuentes:** Basado en `Material_Didactico_VectorLab.md` (Parte A5 y Ejercicio B7).

---

## Caso de Estudio: Resistencia de Limitación en Aviónica

### Ejemplo de dimensionamiento seguro para sensor de presión
* **Contexto de Misión:**
  * Sensor de presión alimentado por el bus de aviónica de $28\text{ V DC}$ nominales.
  * En condiciones de peor caso (carga de alternadores/baterías), el bus puede alcanzar **$32\text{ V DC}$**.
  * Se requiere una resistencia de limitación de corriente de **$200\ \Omega$**.
* **Cálculo de Potencia de Peor Caso:**
  $$P_{peor} = \frac{V_{max}^2}{R_{min}} = \frac{(32\text{ V})^2}{198\ \Omega} \approx 5.17\text{ W} \quad (\text{para } R \text{ con } \pm 1\% \text{ tol})$$
* **Selección del Componente con Derating (50%):**
  * Potencia nominal requerida: $P_{nominal} \ge 2 \cdot P_{peor} \ge 10.34\text{ W}$.
  * Decisión: Seleccionar un resistor de potencia de **$15\text{ W}$** o **$20\text{ W}$** bobinado montado sobre chasis.

***

**Notas del expositor:**
* **Explicación del ejercicio:** Muestre el paso a paso matemático en el pizarrón. Resalte la diferencia entre usar el voltaje nominal ($28\text{ V}$) y el voltaje de peor caso ($32\text{ V}$).
  * Usar $28\text{ V}$ da $P = 28^2 / 200 = 3.92\text{ W}$. Un resistor de $10\text{ W}$ cumpliría el derating de $50\%$ ($5\text{ W}$ límite).
  * Sin embargo, al aplicar el peor escenario real de bus de $32\text{ V}$ y tolerancia de resistencia mínima de $198\ \Omega$, la potencia sube a $5.17\text{ W}$. Un resistor de $10\text{ W}$ fallaría el criterio de derating (límite $5.0\text{ W}$). ¡Esto demuestra por qué el análisis de peor caso salva misiones!
* **Fuentes:** Clase 1 Enrichment (`extracted_courses/57_FZ92uwT8/aerospace_enrichment.md` - Sección Aerospace Connections).

---

## Laboratorio 1: Verificación de Ley de Ohm y Límites

### Objetivo de la práctica semanal (2 horas)
* **Diseño de Red Resistiva:**
  * Alimentación: $12\text{ V}$ máximo con protección y límite de corriente.
  * Red segura inicial: $R_1=1\text{ k}\Omega$, $R_2=2.2\text{ k}\Omega$, $R_3=3.3\text{ k}\Omega$.
  * Límite de corriente recomendado: $20\text{ mA}$.
* **Tareas a ejecutar:**
  1. Caracterizar resistores fijos y comprobar si cumplen con su tolerancia nominal.
  2. Caracterizar un potenciómetro y graficar su curva como divisor de voltaje.
  3. Medir tensión ($V$), corriente ($I$) y calcular potencia disipada ($P$).
  4. Completar la secuencia LTspice: Ohm, KVL, KCL, potencia, falla y divisor cargado.
* **Criterio de Aceptación:**
  * Generar una tabla de márgenes de potencia real frente al límite de derating ($50\%$) para cada resistor de la red.
  * Usar la guía: `docs/labs/semana_1_laboratorio.md`.
  * Secuencia de simulación: `docs/labs/semana_1_simulaciones_ltspice.md`.
  * Circuito físico equivalente: `Simulaciones Ltspice/sim/semana1_02_kvl_serie.asc`.

***

**Notas del expositor:**
* **Explicación del laboratorio:** Explique a los estudiantes la importancia de medir físicamente antes de calcular y simular. Las discrepancias entre simulación y realidad se deben a las tolerancias de los componentes reales.
* **Advertencia docente:** No usar redes de pocos ohmios en protoboard para esta primera práctica. Una red de $2\Omega+3\Omega+1\Omega$ a $12\text{ V}$ exigiría $2\text{ A}$ y disiparía $24\text{ W}$; es útil como ejemplo de peligro, no como montaje inicial.
* **Criterio de Cierre de la Práctica:** La práctica no se aprueba simplemente con que "encienda" o "funcione". El estudiante debe presentar y defender la tabla de márgenes de potencia del peor caso físico medido.
* **Recursos:** Antes del laboratorio, los estudiantes pueden practicar en PhET Kit DC (https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html) el armado serie/paralelo y las mediciones.
* **Fuentes:** `Material_Didactico_VectorLab.md` (Parte E) y Clase 2 Laboratory (`extracted_courses/jli6YBkRt3U/aerospace_enrichment.md`).

---

## Recursos Web de Apoyo para la Semana 1

### Simuladores interactivos
* **PhET - Ley de Ohm:** https://phet.colorado.edu/sims/html/ohms-law/latest/ohms-law_en.html
  * Manipula $V$ y $R$ y observa en vivo la ecuación $V = I \cdot R$ y la densidad de portadores.
* **PhET - Kit de Circuitos DC:** https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_en.html
  * Laboratorio virtual: circuito serie/paralelo y medición segura con instrumentos.
* **Falstad Circuit Simulator:** https://www.falstad.com/circuit/
  * Flujo animado de electrones para visualizar KCL y KVL.

### Referencias de diseño aeroespacial (NASA)
* **NASA S3VI - Diseño de circuitos para aplicaciones espaciales (PDF):**
  https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/electronic-circuit-design-and-analysis-for-space-applications.pdf
  * Ejemplos reales de disipación, TCR y WCCA con radiación y envejecimiento.
* **NASA LLIS - EEE Parts Derating (NASA-LLIS-0676):** https://llis.nasa.gov/lesson/676
  * Respaldan la regla de derating de $50\%$ de potencia nominal.

### Video de fundamentos
* **EEVblog #819 - Leyes de Kirchhoff:** https://www.youtube.com/watch?v=WBfAEeEzDlg
  * KCL y KVL con demostraciones de banca; repaso complementario a la teoría.

***

**Notas del expositor:**
* **Cómo usar esta diapositiva:** Ciérrela la sesión dejando los recursos como material de trabajo autónomo. Los simuladores se usan dentro de la clase (Bloques 2 y 3), las guías NASA se recomiendan como lectura del docente para el Bloque 4, y el video de EEVblog se asigna como repaso tras ver Kirchhoff.
* **Tip:** Comparta el documento `docs/resources/recursos_didacticos.md` (índice completo con los enlaces validados y descripciones) a través del aula virtual.
