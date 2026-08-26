# Benchmark curricular: Sistemas Electronicos Analogicos para Aeroespacial

Este documento corrige el encuadre del curso: la playlist de YouTube es una
base teorica de prerrequisitos y refuerzo, pero el curso debe cubrir el programa
oficial de `Fundamentos de sistemas electronicos analogicos` de Ingenieria
Aeroespacial UNAM.

## Fuentes revisadas

### UNAM

- Oferta UNAM, Ingenieria Aeroespacial:
  `https://oferta.unam.mx/ingenieria-aeroespacial.html`
- Plan de estudios Facultad de Ingenieria:
  `https://oferta.unam.mx/planestudios/aeroespacial-fingenieria-planestudios20.pdf`
- Tomo II ENES Juriquilla, programas de asignatura:
  `https://www.enesjuriquilla.unam.mx/wp-content/uploads/2023/02/Tomo-II_Ingenieria-Aeroespacial_Implantacion_ENES-J_23-11-2022-1.pdf`

Datos clave del programa UNAM:

- La carrera busca que el egresado contribuya al diseno, construccion,
  operacion y mantenimiento de sistemas aeroespaciales, y que pueda modelar,
  simular e interpretar sistemas aeroespaciales.
- `Fundamentos de Sistemas Electronicos Analogicos` aparece en 7o semestre.
- Tiene 10 creditos, duracion de 16 semanas, 4 horas teoricas y 2 horas
  practicas por semana: 96 horas totales.
- Seriacion obligatoria antecedente: `Dispositivos y Circuitos Electronicos`.
- Objetivo oficial: analizar la funcionalidad de bloques electronicos analogicos
  elementales como amplificadores, filtros y osciladores realizados con
  componentes discretos y/o circuitos integrados.

Temario oficial UNAM:

| Tema | Horas teoricas | Horas practicas | Cobertura requerida |
| --- | ---: | ---: | --- |
| Polarizacion de transistores TBJ, JFET y MOSFET | 4 | 4 | punto de operacion, estabilidad y diseno de polarizacion |
| Amplificadores elementales discretos | 8 | 4 | una etapa, Darlington, cascada, diferencial, varias etapas, CAD |
| Amplificadores de potencia | 12 | 6 | clases A, AB, B, C, F, disipadores, diseno asistido |
| Osciladores electronicos | 8 | 4 | lazo cerrado, Barkhausen, LC, senoidales y no senoidales |
| Amplificadores operacionales | 8 | 4 | modelo, parametros reales, comparadores, inversor/no inversor, integradores, sumadores |
| Filtros activos | 14 | 7 | Butterworth, Chebyshev, Bessel, orden, polos/ceros, etapas activas, sintonia |
| Conversion A/D y D/A | 10 | 5 | cuantizacion, DAC resistivo/R-2R/corriente, ADC paralelo/SAR/rampa/doble rampa/V-F/V-T |

## Universidades de referencia

### MIT AeroAstro

MIT Course 16 integra senales y sistemas con contexto aeroespacial en Unified
Engineering: sistemas lineales, convolucion, Fourier/Laplace, modulacion,
filtrado, muestreo y una introduccion a control; los laboratorios/proyectos
usan MATLAB/Python y dan contexto aeroespacial.

Leccion para nuestro curso:

- Los filtros, conversion y acondicionamiento deben conectarse a senales,
  muestreo, control y sistemas de vuelo.
- Conviene usar simulacion y analisis computacional desde el inicio.

### Georgia Tech Aerospace Engineering

El flujo de BS Aerospace Engineering incluye `Circuits and Electronics` en la
formacion temprana y laboratorios/metodos experimentales posteriores.

Leccion para nuestro curso:

- La electronica analogica debe funcionar como puente entre circuitos,
  medicion, control, comunicaciones e integracion de sistemas.

### Purdue ECE Linear Circuit Analysis

Purdue ECE 201 declara como resultados analizar circuitos resistivos, de primer
orden y de segundo orden. Su outline incluye elementos, corriente, voltaje,
fuentes, potencia, Ley de Ohm, Kirchhoff, nodos/mallas, op-amps, superposicion,
Thevenin/Norton, inductancia y capacitancia.

Leccion para nuestro curso:

- Esos temas son prerrequisitos, no el destino final. La playlist cubre bien
  esa base, pero la asignatura UNAM exige avanzar hacia bloques analogicos.

## Diagnostico de cobertura de nuestra playlist

Playlist:

- `PLb_ph_WdlLDny2cGloFSxyRgO8B733jeo`
- 100 videos detectados con `yt-dlp`.

Cobertura fuerte:

- Magnitudes electricas, Ohm, Kirchhoff, resistores, divisores.
- Teoremas de red: superposicion, Thevenin, Norton, Millman.
- AC, fasores, capacitores, inductores, potencia AC, filtros pasivos.
- Diodos, rectificacion, zener, LEDs.
- Transistores BJT, JFET, MOSFET, IGBT, conmutacion y termica.

Cobertura parcial o faltante respecto al temario UNAM:

- Amplificadores discretos de pequena senal: parcial.
- Amplificadores de potencia por clases A/AB/B/C/F: faltante o insuficiente.
- Osciladores electronicos y criterio de Barkhausen: faltante.
- Amplificadores operacionales: faltante.
- Filtros activos normalizados Butterworth/Chebyshev/Bessel: faltante.
- ADC/DAC: faltante.

Conclusion:

- Semanas 1-4 deben compactar prerrequisitos usando la playlist.
- Semanas 5-16 deben seguir el temario UNAM y complementar con fuentes de
  NotebookLM, bibliografia UNAM, TI Precision Labs, Analog Devices, MIT OCW,
  ECSS/DO-160 y simulacion SPICE.

## Ajuste estrategico

La web del curso debe manejar dos capas:

1. `Base playlist`: videos de teoria previa y refuerzo.
2. `Nucleo UNAM/aeroespacial`: bloques analogicos exigidos por el programa.

Regla editorial:

- No confundir una playlist de electronica basica con el programa completo.
- Cada semana debe indicar si el video es `core`, `refuerzo` o `prerrequisito`.
- Para temas faltantes, crear modulos propios con NotebookLM + fuentes tecnicas.

