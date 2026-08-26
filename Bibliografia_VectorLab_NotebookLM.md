# Biblioteca de contexto — VectorLab: Fundamentos Analógicos

Bibliografía curada para alimentar NotebookLM con el contexto del laboratorio
**"Acondicionamiento de señales para instrumentación aeroespacial"**
(galga → puente → INA → filtro → ADC → PCB → verificación de vuelo).

**Cómo usarla en NotebookLM:** cada entrada incluye una URL directa. En NotebookLM puedes
(1) pegar este documento completo como fuente de texto, o (2) añadir cada URL como fuente web
("Add source → Website"). Las entradas marcadas con ⭐ ya aparecen en tu sitio; el resto son
añadidos complementarios. La columna *Módulo* indica a qué capa del curso da contexto:
**F** Física · **D** Dispositivo · **C** Circuito · **S** Sistema · **M** Misión aeroespacial.

---

## 1. Libros de texto (teoría base)

**⭐ Chenming Hu — *Modern Semiconductor Devices for Integrated Circuits*** · Módulo F/D
Libro de acceso abierto sobre física de portadores, unión PN, MOS y BJT con modelos físicos.
Punto de partida ideal para la capa "fenómeno físico → dispositivo".
https://www.chu.berkeley.edu/modern-semiconductor-devices-for-integrated-circuits-chenming-calvin-hu-2010/

**Adel S. Sedra & Kenneth C. Smith — *Microelectronic Circuits* (Oxford UP)** · Módulo D/C
Referencia estándar de microelectrónica: diodos, BJT, MOSFET, amplificadores operacionales y
respuesta en frecuencia. Cubre con rigor lo que el sitio resume como "del dispositivo al circuito".
https://global.oup.com/ushe/product/microelectronic-circuits-9780190853532
Copia de consulta (Internet Archive): https://archive.org/details/microelectronicc0000sedr_x6l5

**Behzad Razavi — *Fundamentals of Microelectronics* (Wiley)** · Módulo D/C
Enfoque "análisis por inspección": física de semiconductores, diodos, BJT y amplificadores,
osciladores y respuesta en frecuencia. Muy didáctico para construir intuición de diseño.
https://www.amazon.com/Fundamentals-Microelectronics-Behzad-Razavi/dp/1119833868

**Paul Horowitz & Winfield Hill — *The Art of Electronics*, 3.ª ed. (Cambridge UP)** · Módulo C/S
La referencia práctica por excelencia para diseño de circuitos reales: op-amps, ruido, filtros,
fuentes y criterios de ingeniería. Complementa la teoría con "cómo se hace de verdad".
https://artofelectronics.net/
Índice de contenidos: https://artofelectronics.net/the-book/table-of-contents/

**Walt Kester (ed.), Analog Devices — *Data Conversion Handbook*** · Módulo S
Manual completo sobre conversión A/D: muestreo, arquitecturas de ADC, pruebas, interfaz y
técnicas de diseño de hardware. Cierra la cadena "filtro → ADC → datos confiables".
PDF oficial Analog Devices: https://www.analog.com/media/en/training-seminars/design-handbooks/Data-Conversion-Handbook/Data-Converter-Book-Front-F.pdf

**Henry W. Ott — *Electromagnetic Compatibility Engineering* (Wiley)** · Módulo S/M
Referencia clave para la capa "PCB y entorno": cableado, masas, blindaje, lazos de tierra,
layout mixto analógico/digital y EMC. Esencial para cables largos y entornos con vibración/transitorios.
https://www.wiley.com/en-us/Electromagnetic+Compatibility+Engineering-p-9780470189306

---

## 2. Artículos técnicos y application notes (diseño aplicado)

**⭐ Analog Devices — *Op Amp Applications Handbook* (Walt Jung, ed.)** · Módulo C
Compendio de aplicaciones de amplificadores operacionales: ruido, filtros, estabilidad y
topologías prácticas. Base para la "interfaz analógica" y el diseño de etapas de ganancia.
https://www.analog.com/en/resources/technical-books/op-amp-applications-handbook.html

**⭐ Analog Devices — *Practical Design Techniques for Sensor Signal Conditioning*** · Módulo C/S
Manual dedicado a puentes, galgas, RTD, termopares y sensores de alta impedancia. Es el texto
más alineado con tu misión de "acondicionar una galga".
https://www.analog.com/en/resources/technical-books/practical-design-techniques-sensor-signal-conditioning.html

**⭐ TI Precision Labs — *Instrumentation Amplifiers*** · Módulo C
Serie en video sobre amplificadores de instrumentación: CMRR, offset, ruido y selección de RG.
Conecta directamente con el ejemplo resuelto del INA826 del sitio.
https://www.ti.com/video/series/precision-labs/ti-precision-labs-instrumentation-amplifiers.html

**TI — *Antialiasing filter circuit design for single-ended ADC input* (SBAA282)** · Módulo S
Nota de aplicación con el procedimiento de cálculo de filtro anti-aliasing antes del ADC.
Da soporte cuantitativo a la capa "filtro y ADC".
https://www.ti.com/lit/pdf/sbaa282

**TI — *Three guidelines for designing anti-aliasing filters* (Precision Hub)** · Módulo S
Artículo breve con reglas prácticas para elegir polos del filtro según el sobremuestreo,
útil específicamente para señales de vibración.
https://e2e.ti.com/blogs_/archives/b/precisionhub/posts/three-guidelines-for-designing-anti-aliasing-filters

**Karl Hoffmann (HBM) — *Applying the Wheatstone Bridge Circuit*** · Módulo C
Monografía clásica sobre el puente de Wheatstone para galgas: configuraciones de 1/4, 1/2 y
puente completo, compensación de temperatura y linealidad. Fundamento del front-end del puente.
http://eln.teilam.gr/sites/default/files/Wheatstone%20bridge.pdf
Artículo de referencia HBK: https://www.hbkworld.com/en/knowledge/resource-center/articles/wheatstone-bridge-circuit

**⭐ TI — *TIDA-01471 / IEPE piezoelectric sensor reference design* (TIDUD62)** · Módulo C/S
Diseño de referencia completo para sensores piezoeléctricos IEPE: amplificador de carga,
cadena de medición y consideraciones de ruido.
https://www.ti.com/lit/ug/tidud62/tidud62.pdf

**⭐ Analog Devices — *CN-0540: IEPE vibration measurement chain*** · Módulo C/S
Nota de circuito con la cadena IEPE completa y análisis de ruido para medición de vibración,
muy alineada con el escenario aeroespacial del ensayo de flexión.
https://www.analog.com/media/en/reference-design-documentation/reference-designs/cn0540.pdf

---

## 3. Normas y guías aeroespaciales (justificación de decisiones de vuelo)

**⭐ ECSS-Q-ST-30-11C Rev.2 — *Derating of EEE components*** · Módulo M
Norma europea de derating de componentes EEE para espacio. Da soporte normativo a la capa
"misión: derating".
https://ecss.nl/wp-content/uploads/2022/07/ECSS-Q-ST-30-11C-Rev.2(23June2021).pdf

**⭐ ECSS-E-ST-20C Rev.2 — *Electrical and electronic*** · Módulo M
Marco eléctrico y electrónico para sistemas espaciales: requisitos de diseño, márgenes y
verificación a nivel de sistema.
https://ecss.nl/wp-content/uploads/2022/04/ECSS-E-ST-20C-Rev.2(8April2022).pdf

**⭐ NASA — *Worst-Case Circuit Analysis (WCCA)*** · Módulo M
Guía de análisis de peor caso: métodos de extremos, RSS y Monte Carlo. Fundamenta la capa
"verificación" y la columna de WCCA del glosario.
https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/wcca.pdf

**NASA GSFC — *EEE-INST-002: Instructions for EEE Parts Selection, Screening, Qualification, and Derating*** · Módulo M
Documento NASA de referencia para selección, screening, calificación y derating de partes EEE
por nivel de fiabilidad. Complemento estadounidense a la norma ECSS de derating.
https://nepp.nasa.gov/docuploads/FFB52B88-36AE-4378-A05B2C084B5EE2CC/EEE-INST-002_add1.pdf
Página oficial NEPP: https://nepp.nasa.gov/pages/EEE-INST-002.cfm

---

## 4. Cursos y recursos abiertos (estudio guiado)

**⭐ MIT OpenCourseWare 6.012 — *Microelectronic Devices and Circuits*** · Módulo F/D
Curso completo del MIT: física de semiconductores, unión PN, MOS y BJT con apuntes, exámenes y
problemas resueltos. Base académica de la capa "física → dispositivo".
https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/

**TI Precision Labs — *ADCs* (incluye experimentos de aliasing y filtros anti-aliasing)** · Módulo S
Serie de formación con experimentos prácticos sobre muestreo, aliasing y diseño de filtros
anti-aliasing. Refuerza con video la capa "filtro y ADC".
https://training.ti.com/ti-precision-labs-adcs-hands-experiment-aliasing-and-anti-aliasing-filters

**Engineering LibreTexts — *Strain Gauges and Wheatstone Bridges* (Cap. 6)** · Módulo C
Capítulo abierto, de nivel introductorio, sobre galgas y puentes de Wheatstone. Buen material de
nivelación para estudiantes antes del laboratorio.
https://eng.libretexts.org/Courses/California_State_Polytechnic_University_Humboldt/Measurements_Instrumentation_and_Controls/Chapter_6:_Strain_Gauges_and_Wheastone_Bridges

---

## Mapa de cobertura por módulo del curso

- **Física (portadores, unión PN, ruido):** Chenming Hu · Sedra/Smith · Razavi · MIT OCW 6.012
- **Dispositivo (diodos, BJT, FET, op-amp):** Sedra/Smith · Razavi · Art of Electronics
- **Circuito (ganancia, filtro, protección):** Art of Electronics · Op Amp Handbook · TI Precision Labs INA · Hoffmann/HBM · LibreTexts
- **Sistema (ADC, cableado, alimentación):** Data Conversion Handbook · Henry Ott (EMC) · TI anti-aliasing (SBAA282) · TIDA-01471 · CN-0540
- **Misión (derating, WCCA, pruebas):** ECSS-Q-ST-30-11C · ECSS-E-ST-20C · NASA WCCA · NASA EEE-INST-002

*Nota: ⭐ = ya presente en tu sitio VectorLab; las demás son referencias añadidas como contexto complementario.*
