# Bibliografía complementaria — Fundamentos de Sistemas Electrónicos Analógicos (Aeroespacial)

Fuentes **nuevas** que no están en `Bibliografia_VectorLab_NotebookLM.md`, elegidas para
cubrir los huecos del plan de 16 semanas: libros base en español para los alumnos,
amplificadores de potencia y osciladores (semanas UNAM que la bibliografía actual cubre débil),
radiación/RHA, y referencias rápidas gratuitas para impartir clase.

Leyenda de módulo: **F** Física · **D** Dispositivo · **C** Circuito · **S** Sistema · **M** Misión.
🆓 = descarga gratuita y legal verificada.

---

## 1. Libros de texto en español (nivelación de alumnos)

**Robert Boylestad & Louis Nashelsky — *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos* (Pearson)** · D/C
El texto estándar en facultades de ingeniería mexicanas (incluida FI-UNAM). Cubre exactamente el
temario rector: polarización TBJ/JFET/MOSFET, amplificadores discretos, respuesta en frecuencia,
op-amps y osciladores. Ideal como libro base del alumno; disponible en bibliotecas UNAM.

**Albert Malvino & David Bates — *Principios de Electrónica* (McGraw-Hill)** · D/C
Muy didáctico, con enfoque de "aproximaciones" (ideal → segunda → exacta) que funciona bien
para diagnóstico y nivelación en las semanas 1–4. Buenos problemas de análisis de fallas.

**Thomas Floyd — *Dispositivos Electrónicos* (Pearson)** · D/C
Alternativa visual con muchas figuras y ejemplos con Multisim. Útil para los alumnos que llegan
más débiles del puente con `Dispositivos y Circuitos Electrónicos`.

**Robert Coughlin & Frederick Driscoll — *Amplificadores Operacionales y Circuitos Integrados Lineales* (Prentice Hall)** · C
Clásico en español dedicado por completo a op-amps: comparadores, filtros activos,
osciladores, y convertidores. Refuerza las semanas de op-amps y filtros activos.

---

## 2. Referencias gratuitas de fabricante (para impartir y para el laboratorio)

**🆓 Ron Mancini (ed.), TI — *Op Amps for Everyone* (2.ª ed., PDF completo)** · C
Tutorial y referencia de diseño con op-amps reales de TI: realimentación, single-supply,
ruido, estabilidad, filtros activos y osciladores. Complemento directo del Op Amp Handbook de Jung.
https://pearl-hifi.com/06_Lit_Archive/15_Mfrs_Publications/Texas_Instruments/Op_Amps_for_Everyone_TI.pdf
(versión Rev. A alojada por U. Mass Lowell: https://faculty.uml.edu/george_cheney/Teaching/Courses/Fall2017/eece-565/TIOpAmpBook.pdf)

**🆓 Art Kay & Tim Green (eds.), TI — *Analog Engineer's Pocket Reference* (5.ª ed.)** · C/S
Formulario de bolsillo: ecuaciones AC/DC, configuraciones de op-amp, ancho de banda y
estabilidad, sensores, trazas de PCB, ADC/DAC. Perfecto como material de examen abierto
y hoja de fórmulas oficial del curso.
https://www.ti.com/seclit/eb/slyw038d/slyw038d.pdf

**🆓 Hank Zumbahlen (ed.), Analog Devices — *Linear Circuit Design Handbook* (2008)** · C/S
Puente entre teoría de componentes y diseño práctico: op-amps, sensores, sistemas muestreados,
convertidores, filtros analógicos, gestión de potencia, sobretensiones y PCB. Un solo volumen
que cubre las capas C y S completas.
https://www.analog.com/en/resources/technical-books/linear-circuit-design-handbook.html
(copia en Internet Archive: https://archive.org/details/JL10244)

---

## 3. Textos abiertos (licencia libre, para repartir a los alumnos)

**🆓 Tony R. Kuphaldt — *Lessons in Electric Circuits, Vol. III: Semiconductors* (Creative Commons)** · F/D/C
Texto abierto (CC BY) con capítulos sólidos de teoría de estado sólido, diodos, TBJ,
tiristores y op-amps. Se puede copiar y distribuir legalmente completo — útil como lectura
previa obligatoria. *Ojo: los capítulos de JFET, MOSFET y filtros activos están incompletos;
para esos temas usar Boylestad o el Linear Circuit Design Handbook.*
HTML: https://www.ibiblio.org/kuphaldt/electricCircuits/Semi/index.html
PDF: https://www.ibiblio.org/kuphaldt/electricCircuits/Semi/SEMI.pdf
Serie completa (6 volúmenes, incluye Vol. I DC y Vol. II AC para nivelación):
https://www.ibiblio.org/kuphaldt/electricCircuits/

---

## 4. Misión aeroespacial: radiación y RHA (hueco de la bibliografía actual)

**🆓 NASA — *Avionics Radiation Hardness Assurance (RHA) Guidelines* (NTRS 20210018053)** · M
Guía NASA de aseguramiento de dureza a radiación para aviónica: TID, SEE, definición de
requisitos y flujo RHA. Complementa los posters NSREC que ya están en `contexto_NLM` con un
documento guía formal.
https://ntrs.nasa.gov/api/citations/20210018053/downloads/20210018053.pdf

**NASA SSRI Knowledge Base — *Radiation Analysis* y *Radiation Testing* (TID/SEE)** · M
Índices curados de normas, guías y mejores prácticas de análisis y prueba de radiación para
small-sats. Buen punto de partida para asignar lecturas por equipo.
https://s3vi.ndc.nasa.gov/ssri-kb/topics/21/ · https://s3vi.ndc.nasa.gov/ssri-kb/topics/41/

**🆓 NASA — *Mission Radiation Environment Modeling and Analysis* (TM-20220011775)** · M
Modelado del entorno de radiación de misión (cinturones, rayos cósmicos, partículas solares).
Da el contexto físico previo a derating y selección de componentes.
https://ntrs.nasa.gov/api/citations/20220011775/downloads/Mission_Radiation_Modeling_STI.pdf

---

## 5. Huecos que cubre cada fuente (mapa contra el plan de 16 semanas)

| Semanas / tema del plan | Fuente nueva que lo respalda |
|---|---|
| 1–4 nivelación y diagnóstico | Malvino · Kuphaldt Vol. I–III |
| Polarización TBJ/JFET/MOSFET | Boylestad · Floyd |
| Amplificadores discretos y de potencia | Boylestad · Malvino |
| Osciladores | Boylestad · Coughlin/Driscoll · Op Amps for Everyone |
| Op-amps y filtros activos | Coughlin/Driscoll · Op Amps for Everyone · Linear Circuit Design Handbook |
| ADC/DAC y sistema | Linear Circuit Design Handbook · Pocket Reference |
| Misión: radiación (TID/SEE, RHA) | NASA RHA Guidelines · SSRI KB · TM-20220011775 |
| Hoja de fórmulas / examen abierto | Analog Engineer's Pocket Reference |

*Los libros en español (sección 1) no tienen descarga legal gratuita; verificar disponibilidad
en la Biblioteca Central UNAM o BIDI-UNAM (https://www.bidi.unam.mx) con cuenta institucional.*
