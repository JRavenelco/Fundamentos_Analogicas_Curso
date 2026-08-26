# Plan 16 semanas alineado a UNAM y reforzado con playlist

Asignatura objetivo:
`Fundamentos de sistemas electronicos analogicos`, Ingenieria Aeroespacial UNAM.

Carga oficial:

- 16 semanas
- 4 h teoria/semana
- 2 h practica/semana
- 64 h teoria + 32 h practica = 96 h

Principio de rediseno:

- La playlist `Curso GRATIS de Electronica Analogica` se usa como base
  diagnostica, refuerzo y prerequisito.
- El temario rector es el programa UNAM: transistores, amplificadores discretos,
  amplificadores de potencia, osciladores, op-amps, filtros activos y ADC/DAC.
- El enfoque aeroespacial se agrega en cada semana mediante derating, ruido,
  temperatura, radiacion, proteccion, validacion, ECSS/DO-160 y diseno para
  avionica/satelites.

## Calendario actualizado 2026

La UNAM recorrio el inicio de clases al lunes 17 de agosto de 2026. Las fechas
siguientes identifican bloques semanales de lunes a domingo; los dias inhabiles
o ajustes oficiales posteriores deben reflejarse en la programacion de cada
actividad, sin cambiar automaticamente el orden tematico.

| Semana | Periodo |
| ---: | --- |
| 1 | 17-23 agosto 2026 |
| 2 | 24-30 agosto 2026 |
| 3 | 31 agosto-6 septiembre 2026 |
| 4 | 7-13 septiembre 2026 |
| 5 | 14-20 septiembre 2026 |
| 6 | 21-27 septiembre 2026 |
| 7 | 28 septiembre-4 octubre 2026 |
| 8 | 5-11 octubre 2026 |
| 9 | 12-18 octubre 2026 |
| 10 | 19-25 octubre 2026 |
| 11 | 26 octubre-1 noviembre 2026 |
| 12 | 2-8 noviembre 2026 |
| 13 | 9-15 noviembre 2026 |
| 14 | 16-22 noviembre 2026 |
| 15 | 23-29 noviembre 2026 |
| 16 | 30 noviembre-6 diciembre 2026 |

## Semana 1: Diagnostico y base electrica minima

UNAM:

- Puente desde `Dispositivos y Circuitos Electronicos` y `Analisis de Circuitos`.

Playlist:

- `KkoudrHOpGE`, `57_FZ92uwT8`, `jli6YBkRt3U`

Teoria, 4 h:

- Diagnostico de Ohm, Kirchhoff, potencia y energia.
- Resistores reales, tolerancia, temperatura y potencia.
- Introduccion a derating y criterio de seguridad.

Practica, 2 h:

- Red resistiva de 12 V maximo con limite de corriente.
- Medicion de V/I/P y simulacion `.op`.

Salida:

- Diagnostico inicial y tabla de margen de potencia.

## Semana 2: Divisores, puentes y equivalentes para sensores

UNAM:

- Base necesaria para amplificadores, ADC/DAC y acondicionamiento.

Playlist:

- `Sfkp81yplPc`, `Sm2KjO_MBzE`, `QWwoDewT43A`, `TQve3J-0510`,
  `yuHbKjSdEVA`, `otYl_8qQTAk`

Teoria, 4 h:

- Divisor de tension/corriente, efecto de carga.
- Puente de Wheatstone y pequenos desbalances.
- Equivalentes Thevenin/Norton.

Practica, 2 h:

- Puente resistivo para sensor simulado.
- Medicion diferencial y error por carga.

Salida:

- Red equivalente de sensor lista para amplificar.

## Semana 3: Polarizacion de TBJ

UNAM:

- Tema 1: Polarizacion de transistores TBJ, JFET y MOSFET.

Playlist:

- `k8v-ukhCc2g`, `yCPv7Je-D5E`, `pfVUD5FVoB0`, `Ic3r9JxoKVg`

Teoria, 4 h:

- Punto Q, regiones de operacion, estabilidad.
- Polarizacion fija, divisor de base y realimentacion por emisor.
- Sensibilidad a beta y temperatura.

Practica, 2 h:

- Simular y medir polarizacion de un NPN de baja potencia.
- Variar beta/temperatura en SPICE.

Salida:

- Circuito TBJ polarizado con punto Q y margen termico.

## Semana 4: Polarizacion JFET/MOSFET y conmutacion segura

UNAM:

- Tema 1: Polarizacion JFET/MOSFET.

Playlist:

- `GGprFdtFbnU`, `h8VcISK7y3w`, `u6UeaLh8nUY`, `Vyyi62GsjZ0`

Teoria, 4 h:

- JFET, MOSFET, Vth, regiones, Rds(on), carga de compuerta.
- Punto de operacion y estabilidad.
- Conmutacion vs operacion lineal.

Practica, 2 h:

- Driver MOSFET de bajo voltaje para carga resistiva/LED.
- Medir caida, corriente y potencia.

Salida:

- Seleccion MOSFET con margen V/I/P y justificacion.

## Semana 5: Amplificadores discretos de una etapa

UNAM:

- Tema 2: Amplificadores elementales basados en transistores discretos.

Playlist:

- Reforzar con videos BJT/MOSFET anteriores.

Fuentes complementarias:

- Sedra/Smith, Gray/Meyer, Analog Devices/TI, NotebookLM.

Teoria, 4 h:

- Modelo de pequena senal.
- Ganancia, impedancia de entrada/salida, acoplamiento capacitivo.
- Emisor comun, colector comun y fuente comun.

Practica, 2 h:

- Simular amplificador de una etapa con barrido AC.
- Medir ganancia y punto Q.

Salida:

- Amplificador de una etapa con respuesta en frecuencia.

## Semana 6: Cascada, Darlington y amplificador diferencial

UNAM:

- Tema 2: Darlington, cascada, diferencial, varias etapas.

Playlist:

- `xMqHr51SMmk` y refuerzo BJT.

Teoria, 4 h:

- Cascada de etapas, carga entre etapas, impedancias.
- Darlington/Sziklai.
- Amplificador diferencial como base de op-amp e instrumentacion.

Practica, 2 h:

- Comparar una etapa vs dos etapas en simulacion.
- Simular par diferencial sencillo.

Salida:

- Reporte de ganancia, impedancia y saturacion.

## Semana 7: Amplificadores de potencia I

UNAM:

- Tema 3: Amplificadores de potencia.

Playlist:

- `x8nKy71afas`, `PlFjPAwaTNk`, `FCMzV7k8WEM`

Teoria, 4 h:

- Potencia, eficiencia, disipacion y SOA.
- Clases A, B y AB.
- Distorsion de cruce y seleccion de disipador.

Practica, 2 h:

- Simular etapa clase A o push-pull de baja potencia.
- Calcular disipacion y temperatura estimada.

Salida:

- Tabla de eficiencia, potencia y margen termico.

## Semana 8: Amplificadores de potencia II y proteccion

UNAM:

- Tema 3: clases C/F y diseno asistido por computadora.

Playlist:

- `Euj7xa4WoVE`, `3yek_OGj7Bw`, `g4r5cfbkLD8`, `TVqnYJURm2o`

Teoria, 4 h:

- Proteccion de cargas inductivas.
- Limitacion de corriente, clamps, polaridad inversa.
- Introduccion a clases C/F desde eficiencia y RF.

Practica, 2 h:

- Driver protegido para carga inductiva de bajo voltaje.
- Ver transitorio con y sin flyback en simulacion.

Salida:

- Etapa de potencia protegida y documentada.

## Semana 9: Osciladores electronicos

UNAM:

- Tema 4: Osciladores electronicos.

Playlist:

- Base con `KxDOmMMo6so`, `vHFVBn3E3l4`.

Fuentes complementarias:

- Op-amp/LC oscillator references, TI/Analog Devices, NotebookLM.

Teoria, 4 h:

- Oscilador como lazo cerrado.
- Criterio de Barkhausen.
- Osciladores LC y RC.
- Estabilidad de frecuencia, ruido y arranque.

Practica, 2 h:

- Simular oscilador RC/LC de baja tension.
- Medir frecuencia, amplitud y condicion de arranque.

Salida:

- Oscilador validado con frecuencia y margen de arranque.

## Semana 10: Amplificadores operacionales I

UNAM:

- Tema 5: Op-amps, modelo elemental, parametros ideales y reales.

Playlist:

- Refuerzo de nodos, Thevenin, AC y filtros pasivos.

Fuentes complementarias:

- Franco, Dailey, TI Precision Labs, Analog Devices.

Teoria, 4 h:

- Op-amp ideal vs real.
- Ganancia abierta, realimentacion, impedancias, offset, slew rate, ancho de banda.
- Comparadores, inversor y no inversor.

Practica, 2 h:

- Simular amplificador inversor/no inversor con op-amp real.
- Medir saturacion, offset y ancho de banda.

Salida:

- Op-amp basico con limites reales documentados.

## Semana 11: Amplificadores operacionales II e instrumentacion

UNAM:

- Tema 5: integradores, sumadores y funciones analogicas.

Fuentes complementarias:

- TI/Analog Devices, NotebookLM, guias de instrumentacion.

Teoria, 4 h:

- Sumador, integrador, diferenciador y comparador con histeresis.
- Amplificador diferencial/instrumentacion.
- CMRR, ruido y saturacion.

Practica, 2 h:

- Acondicionar puente de Wheatstone con etapa diferencial o instrumentacion.
- Simular ruido y rango de salida.

Salida:

- Front-end basico para sensor resistivo.

## Semana 12: Filtros activos I

UNAM:

- Tema 6: filtros activos, especificaciones y aproximaciones.

Playlist:

- `KQvxdAlBj04`, `4LhDcDaefzo` como base de filtros pasivos.

Fuentes complementarias:

- Huelsman/Allen, Wait/Huelsman/Korn, TI/Analog Devices.

Teoria, 4 h:

- Especificaciones: fp, fs, Ap, As, orden, Q.
- Butterworth, Chebyshev y Bessel.
- Polos, ceros y normalizacion.

Practica, 2 h:

- Disenar filtro activo paso bajas de segundo orden.
- Simular Bode y comparar aproximaciones.

Salida:

- Filtro activo con especificacion y respuesta.

## Semana 13: Filtros activos II y anti-alias

UNAM:

- Tema 6: realizacion activa y sintonia.

Teoria, 4 h:

- Sallen-Key, multiple feedback, cascada de etapas.
- Paso altas, paso banda y rechaza banda.
- Anti-alias para ADC y rechazo de EMI.

Practica, 2 h:

- Filtro anti-alias para senal de sensor.
- Analisis de tolerancias y ajuste.

Salida:

- Filtro anti-alias con margen de tolerancia.

## Semana 14: Conversion D/A

UNAM:

- Tema 7: conversion analogica-digital y digital-analogica.

Teoria, 4 h:

- Cuantizacion, resolucion, INL/DNL.
- DAC resistivo, R-2R y DAC por corriente.
- Errores por tolerancia, referencia y carga.

Practica, 2 h:

- Simular escalera R-2R de 4 bits.
- Medir error por tolerancias.

Salida:

- DAC R-2R con tabla codigo-salida y error.

## Semana 15: Conversion A/D

UNAM:

- Tema 7: ADC paralelo, SAR, rampa, doble rampa, V/F y V/T.

Teoria, 4 h:

- Muestreo, cuantizacion, aliasing y referencia.
- ADC flash, SAR, rampa, doble rampa, V/F, V/T.
- Interface analogica previa al ADC.

Practica, 2 h:

- Simular cuantizacion y error.
- Integrar sensor + filtro + ADC conceptual.

Salida:

- Cadena sensor-filtro-ADC con resolucion y rango.

## Semana 16: Proyecto integrador aeroespacial

UNAM:

- Integracion de todos los bloques: amplificador, filtro, oscilador o conversion.

Teoria, 4 h:

- Revision de arquitectura analogica para avionica/satelite.
- Derating, proteccion, temperatura, ruido, tolerancias, pruebas y trazabilidad.
- Conexion con Avionica I, Control Automatico, Comunicaciones y campos de
  profundizacion.

Practica, 2 h:

- Proyecto final de baja tension:
  - sensor resistivo + amplificador + filtro + ADC conceptual
  - o driver protegido + medicion + validacion termica
  - o oscilador/filtro activo con especificacion aeroespacial

Salida:

- Dossier final: esquematico, calculos, simulacion, prueba de aceptacion, tabla
  de derating y riesgos.

## Extraccion y creacion de contenido

Fase 1, playlist/prerrequisitos:

- Semanas 1-4: extraer videos seleccionados de DC, redes, transistores basicos.

Fase 2, nucleos faltantes:

- Crear material propio para semanas 5-16 con NotebookLM, bibliografia UNAM y
  fuentes tecnicas.
- No esperar a que la playlist cubra op-amps, filtros activos o ADC/DAC.

Fase 3, web:

- Cada semana debe publicar:
  - objetivos medibles
  - teoria propia
  - ejemplo numerico
  - practica segura
  - simulacion
  - enfoque aeroespacial
  - evaluacion
  - fuentes
