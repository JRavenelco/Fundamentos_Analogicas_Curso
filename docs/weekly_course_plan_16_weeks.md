# Plan semanal base por playlist: Fundamentos Analogicos con enfoque aeroespacial

> Nota curricular: este archivo organiza la playlist como ruta de apoyo. Para
> el plan rector de la asignatura UNAM, usar
> `docs/weekly_course_plan_16_weeks_unam_aligned.md`. La playlist cubre muy bien
> prerrequisitos y electronica basica, pero no cubre por completo el temario
> oficial de Fundamentos de Sistemas Electronicos Analogicos: op-amps, filtros
> activos, osciladores y conversion ADC/DAC requieren fuentes adicionales.

Base teorica: playlist `Curso GRATIS de Electronica Analogica`
`PLb_ph_WdlLDny2cGloFSxyRgO8B733jeo`

Carga: 16 semanas, 6 horas por semana.

- 4 h teoria: conceptos, calculo, ejemplos y discusion aeroespacial.
- 2 h practica: laboratorio seguro, simulacion SPICE/LTspice/QSPICE o revision de diseno.

El objetivo no es reproducir los 100 videos completos en clase, sino usarlos
como base teorica curada. La clase presencial/web debe convertirlos en criterio
de ingenieria aeroespacial: derating, potencia, proteccion, ruido, transitorios,
temperatura, tolerancias, medicion y validacion.

## Calendario actualizado 2026

Inicio de clases: lunes 17 de agosto de 2026. Cada semana se presenta como un
bloque de lunes a domingo; los dias inhabiles y ajustes oficiales se aplicaran
en Classroom a las actividades afectadas.

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

## Semana 1: Magnitudes electricas y criterio de energia

Playlist base:

- 0 `KkoudrHOpGE`: presentacion del curso
- 1 `57_FZ92uwT8`: tension, corriente, resistencia, Ley de Ohm, potencia y energia

Teoria, 4 h:

- Tension, corriente, resistencia, potencia y energia.
- Ley de Ohm como primer modelo de circuito.
- Unidades, signos, medicion y errores comunes.
- Lectura aeroespacial: energia limitada, disipacion, buses de potencia y margen.

Practica, 2 h:

- Red resistiva de bajo voltaje, maximo 12 V.
- Fuente con limite de corriente, multimetro y medicion de caidas de tension.
- Simulacion `.op` en LTspice/QSPICE.

Entregable:

- Hoja de calculo o reporte con V, I, R, P, E y margen de potencia.

Extraccion prioritaria:

- Ya extraido: `57_FZ92uwT8`.
- Pendiente: enriquecer Clase 0 si se desea publicarla como bienvenida.

## Semana 2: Resistores, divisores y sensores resistivos

Playlist base:

- 2 `jli6YBkRt3U`: resistores
- 4 `Sfkp81yplPc`: divisores de corriente y tension
- 4.1 `Sm2KjO_MBzE`: divisor de tension
- 4.3 `QWwoDewT43A`: divisores en la practica
- 5 `4uYnyIRw46g`: potenciometros

Teoria, 4 h:

- Resistores reales: tolerancia, potencia, ruido, temperatura.
- Divisor de tension y divisor de corriente.
- Potenciometro como divisor variable y fuente de error.
- Efecto de carga e impedancia de entrada.

Practica, 2 h:

- Disenar un divisor para entrada de ADC.
- Medir error por carga usando resistencias de carga.
- Simular tolerancia con barrido o Monte Carlo simple.

Enfoque aeroespacial:

- Derating de potencia en resistores.
- Divisores para telemetria, sensado de bus y acondicionamiento inicial.

Entregable:

- Divisor validado con error maximo, potencia y tolerancia.

Extraccion prioritaria:

- `jli6YBkRt3U`, `Sfkp81yplPc`, `Sm2KjO_MBzE`, `QWwoDewT43A`.

## Semana 3: Kirchhoff, conversion de fuentes y puentes

Playlist base:

- 3 `xl-eCmWCAzY`: leyes de Kirchhoff
- 3.1 `JFiDufguZbA`: circuito por KVL y Ohm
- 3.2 `M8EtFN1_5ik`: Kirchhoff y Ohm
- 6 `Dm_fKNuoPP0`: conversion fuente corriente/tension
- 6.1 `EjUwGgPhl_8`: ejercicios conversion de fuentes
- 7 `TQve3J-0510`: puente de Wheatstone

Teoria, 4 h:

- KVL, KCL, signos y planteamiento de ecuaciones.
- Conversion de fuentes.
- Puente de Wheatstone como traductor resistencia-tension.
- Incertidumbre, balance y sensibilidad.

Practica, 2 h:

- Resolver y simular una red con fuente equivalente.
- Armar puente resistivo de bajo voltaje.
- Medir desbalance como senal diferencial.

Enfoque aeroespacial:

- Galgas extensiometricas, termistores y sensores resistivos.
- Instrumentacion en estructuras, vibracion y temperatura.

Entregable:

- Reporte de puente con sensibilidad, rango y error.

Extraccion prioritaria:

- `xl-eCmWCAzY`, `JFiDufguZbA`, `TQve3J-0510`.

## Semana 4: Teoremas de redes y metodos sistematicos

Playlist base:

- 8 `VHNM40ookBw`: delta-estrella
- 9 `cPCXT5OUwgM`: Millman
- 10 `pFbEUhOmges`: superposicion
- 11 `otYl_8qQTAk`: Norton
- 12 `yuHbKjSdEVA`: Thevenin
- 12.1 `jiTbW6sleM4`: Thevenin y Millman
- 12.2 `ZKmfvq3rsks`: Thevenin con fuente dependiente
- 12.3 `0IVNoQC8DyM`: Thevenin con fuente dependiente

Teoria, 4 h:

- Equivalentes de Thevenin/Norton.
- Superposicion y fuentes dependientes.
- Millman y transformaciones para simplificacion.
- Cuando usar cada metodo.

Practica, 2 h:

- Obtener equivalente Thevenin de una red de sensor.
- Validar con simulacion y medicion de carga.

Enfoque aeroespacial:

- Modelado de subsistemas como bloques equivalentes.
- Interconexion de sensores, filtros y ADC.

Entregable:

- Equivalente Thevenin/Norton verificado contra circuito original.

Extraccion prioritaria:

- `pFbEUhOmges`, `otYl_8qQTAk`, `yuHbKjSdEVA`.

## Semana 5: Mallas, nodos y entrada a corriente alterna

Playlist base:

- 13 `z6f951TcIdk`: mallas
- 14 `31idalxvY7w`: lazos
- 15 `f4PXdR_zdnY`: nodos
- 15.1 `yP7oQMhw8Eg`: nodos ejercicio
- 15.2 `FuyJhxB_0Vw`: nodos examen
- 16 `rrr68mtgfCM`: parametros de AC
- 16.1 `BhX8N6yhUSs`: numeros complejos
- 16.2 `cLHHyK1ik7M`: operar complejos

Teoria, 4 h:

- Metodo de mallas y metodo de nodos.
- Seleccion de metodo segun topologia.
- AC como senal sinusoidal: amplitud, RMS, fase, frecuencia.
- Complejos y fasores como lenguaje de AC.

Practica, 2 h:

- Resolver una red por nodos y por simulacion.
- Introducir fasor simple con una fuente AC.

Enfoque aeroespacial:

- Avionica a 400 Hz y senales AC en instrumentacion.
- Fase, RMS y medicion correcta.

Entregable:

- Comparacion nodos/mallas/simulacion.

Extraccion prioritaria:

- `f4PXdR_zdnY`, `rrr68mtgfCM`, `BhX8N6yhUSs`.

## Semana 6: Capacitores y transitorios RC

Playlist base:

- 17 `Jf14yyhVrAk`: capacitores
- 17.1 `8RxiB6t7Rh8`: tipos y aplicaciones
- 17.2 `oZ8J9mgo69w`: lectura de capacitores
- 18 `k9nVIFnkxIE`: capacitor en DC parte I
- 18 parte II `N-RlEoNgIbM`
- 18 parte III `57EwMo4x7D4`
- 18.1 `3DcWhL_ZJRY`: RC con onda cuadrada
- 18.2 `7HnPH5XBiT4`: capacitores serie
- 18.4 `O4cV6k5Y98A`: capacitores paralelo

Teoria, 4 h:

- Capacitancia, energia almacenada y constante de tiempo.
- Carga/descarga, serie/paralelo y lectura de codigo.
- Capacitores reales: ESR, fuga, tolerancia y temperatura.

Practica, 2 h:

- Medir respuesta RC a escalon.
- Comparar tiempo medido contra tau = R x C.

Enfoque aeroespacial:

- Filtros, desacoplo, hold-up, fuga y seleccion por temperatura/radiacion.

Entregable:

- Curva de carga/descarga con tau experimental y simulada.

Extraccion prioritaria:

- `Jf14yyhVrAk`, `3DcWhL_ZJRY`, `8RxiB6t7Rh8`.

## Semana 7: Inductores, RL y comportamiento reactivo

Playlist base:

- 19 `LXwFKTRQzVY`: bobinas/inductores
- 20 `7mYAfZMzdv8`: bobina en DC parte I
- 20 parte II `ZcSSSi6go7c`
- 21 `AYQgpRUtLwU`: bobina en AC
- 22 `17Fk2MN9c_Q`: capacitor en AC
- 23 `sUYxMDPnGWU`: resistencia en AC
- 24 `QoNeZS0Xc7Q`: bobina + resistencia en AC
- 24.1 `cdR5rioDoKo`: medir autoinduccion y resistencia
- 25 `k0Lgoss3Kdw`: capacitor + resistor en AC

Teoria, 4 h:

- Inductancia, energia magnetica y oposicion a cambios de corriente.
- Reactancia inductiva/capacitiva y fase.
- Circuitos RL y RC en AC.

Practica, 2 h:

- Simular respuesta RL/RC en frecuencia.
- Medir o estimar inductancia con senal pequena si hay equipo disponible.

Enfoque aeroespacial:

- Bobinas, relays, solenoides, actuadores y problemas de EMI.

Entregable:

- Grafica de fase/magnitud para RL o RC.

Extraccion prioritaria:

- `LXwFKTRQzVY`, `AYQgpRUtLwU`, `QoNeZS0Xc7Q`.

## Semana 8: Potencia AC y factor de potencia

Playlist base:

- 26 `KwDjl2Y1xW0`: potencias en AC
- 26.1 `bKXM8W-OaE0`: potencia reactiva
- 26.2 `pebkVPmUeVY`: factor de potencia
- 26.3 `Wlw6peR88-w`: reto medicion AC
- solucion `2uoIQwFe_yU`
- 26.4 `PBU9dGh6vZo`: reto intensidad AC

Teoria, 4 h:

- Potencia activa, reactiva y aparente.
- Factor de potencia y correccion.
- RMS, medicion y errores de interpretacion.

Practica, 2 h:

- Simular carga R, L, C y calcular triangulo de potencia.
- Comparar corriente RMS para cargas distintas.

Enfoque aeroespacial:

- Sistemas AC de 400 Hz, peso de magneticos, eficiencia energetica y calentamiento.

Entregable:

- Analisis de potencia AC con factor de potencia y correccion.

Extraccion prioritaria:

- `KwDjl2Y1xW0`, `pebkVPmUeVY`.

## Semana 9: Filtros pasivos, resonancia y transformadores

Playlist base:

- 27 `KQvxdAlBj04`: filtros pasa bajas/pasa altas
- 27.1 `4LhDcDaefzo`: pasa banda/rechaza banda
- 28 `KxDOmMMo6so`: resonancia serie/paralelo parte I
- 28 parte II `vHFVBn3E3l4`
- 29.1 `fHOQ986yyZ0`: transformador monofasico

Teoria, 4 h:

- Filtros RC/RL/RLC y frecuencia de corte.
- Resonancia, Q, ancho de banda y selectividad.
- Transformador como acoplamiento y aislamiento.

Practica, 2 h:

- Disenar filtro RC para senal de sensor.
- Barrido AC en SPICE y medicion de -3 dB.

Enfoque aeroespacial:

- Anti-alias, filtrado EMI, rechazo de ruido y aislamiento.

Entregable:

- Filtro pasivo validado por simulacion y medicion.

Extraccion prioritaria:

- `KQvxdAlBj04`, `4LhDcDaefzo`.

## Semana 10: Diodos y proteccion basica

Playlist base:

- 30 `1QQFe_fQ7Oc`: diodo rectificador
- 30.1 `gB7ImT50VY0`: conduccion de diodo
- 30.2 `3yek_OGj7Bw`: limitador con dos diodos
- 31 `Euj7xa4WoVE`: diodo de proteccion en bobina DC

Teoria, 4 h:

- Curva I-V del diodo, conduccion y polarizacion.
- Limitadores, clamps y proteccion de cargas inductivas.
- Energia en bobina y transitorios.

Practica, 2 h:

- Medir caida de diodo y simular limitador.
- Proteger bobina/relay de bajo voltaje con diodo flyback.

Enfoque aeroespacial:

- Proteccion contra transitorios, cargas inductivas y confiabilidad de actuadores.

Entregable:

- Circuito de proteccion con comparacion antes/despues del diodo.

Extraccion prioritaria:

- `1QQFe_fQ7Oc`, `3yek_OGj7Bw`, `Euj7xa4WoVE`.

## Semana 11: Rectificacion, clamps y polaridad inversa

Playlist base:

- 32 `ptzroHimUGU`: rectificador media onda
- 32.1 `DXmvj0qd0RI`: rectificador onda completa dos diodos
- 32.2 `XIPhBgh3z_Y`: puente rectificador
- 33.1 `k2w1bMIf7mw`: clamp/doblador
- 33.2 `LVrmY0woUEg`: selector mayor/menor voltaje
- 33.4 `TVqnYJURm2o`: errores de potencia
- 33.5 `g4r5cfbkLD8`: proteccion polaridad incorrecta
- 34 `KE3NoFTJeLQ`: calcular resistencias

Teoria, 4 h:

- Rectificacion media onda, onda completa y puente.
- Rizado, conduccion por semiciclo y potencia.
- Clamps, selectores y polaridad inversa.

Practica, 2 h:

- Simular rectificador con carga y capacitor.
- Medir rizado en baja tension aislada o simulada.

Enfoque aeroespacial:

- Entrada de potencia robusta, proteccion contra errores de conexion y transitorios.

Entregable:

- Rectificador/proteccion documentado con tensiones y potencia.

Extraccion prioritaria:

- `ptzroHimUGU`, `XIPhBgh3z_Y`, `g4r5cfbkLD8`.

## Semana 12: Zener, regulacion y fuentes simples

Playlist base:

- 35 `3N2uUs4y4Vo`: diodo zener
- 35.1 `fI9cBsGLV2M`: circuito examen zener/capacitor
- 36 `ssxt0WRjs6M`: proteccion con zener
- 37 `IrYY6pTdo9g`: estabilizador zener
- 38 `eATKEOlqjkw`: fuente estabilizada con zener
- 38.1 `C0q4w_cuz_U`: reto fuente

Teoria, 4 h:

- Zener como referencia, regulador y proteccion.
- Corriente minima/maxima, resistencia serie y disipacion.
- Limitaciones de una fuente zener.

Practica, 2 h:

- Disenar regulador zener de baja potencia.
- Simular variacion de carga y entrada.

Enfoque aeroespacial:

- Referencias, clamps de proteccion, margen termico y degradacion.

Entregable:

- Regulador zener con ventana de operacion segura.

Extraccion prioritaria:

- `3N2uUs4y4Vo`, `IrYY6pTdo9g`, `eATKEOlqjkw`.

## Semana 13: LED, senales promedio y drivers sencillos

Playlist base:

- 39 `13rcRufDGGQ`: LED
- 39.1 `J8lNkVzukSM`: errores conectando LEDs a AC
- 39.2 `JWCLKz6lt7Y`: driver LED en AC
- 40 `sekdEc5wU6k`: valor promedio de senales DC comunes

Teoria, 4 h:

- LED como diodo emisor: curva, corriente y resistencia limitadora.
- Drivers simples, disipacion y errores de conexion.
- Valor promedio y senales pulsantes.

Practica, 2 h:

- Driver LED de baja tension con resistencia calculada.
- Simulacion de senal pulsante y promedio.

Enfoque aeroespacial:

- Indicacion, optoacoplamiento, telemetria visual y confiabilidad por corriente.

Entregable:

- Driver LED con margen de corriente y potencia.

Extraccion prioritaria:

- `13rcRufDGGQ`, `sekdEc5wU6k`.

## Semana 14: Transistores BJT y conmutacion

Playlist base:

- 42 `k8v-ukhCc2g`: NPN
- 42.1 `yCPv7Je-D5E`: circuito NPN basico
- 43 `pfVUD5FVoB0`: polarizacion NPN
- 44 `0Bp0QL9fmA4`: temporizador NPN
- 45 `K-3kEmexz44`: regulador transistor + zener
- 46 `2WhU9fqzEXE`: fuente de corriente transistor + zener
- 47 `5_8AFka51lw`: PNP
- 47.1 `1Cvo0YTPV2g`: polarizacion PNP
- 47.2 `Ic3r9JxoKVg`: terminales NPN/PNP
- 48 `TE_pQ8pyL80`: relay con transistor
- 48.1 `slNPfrQaVlo`: relay con fototransistor

Teoria, 4 h:

- BJT como interruptor y amplificador basico.
- Saturacion, region activa, polarizacion y ganancia.
- Drivers de relay/carga y proteccion.

Practica, 2 h:

- Conmutar carga de bajo voltaje con BJT y diodo de proteccion.
- Simular corriente de base/colector y margen de saturacion.

Enfoque aeroespacial:

- Interfaces discretas, activacion de cargas, aislacion y fallas de actuadores.

Entregable:

- Driver BJT documentado con corriente, potencia y proteccion.

Extraccion prioritaria:

- `k8v-ukhCc2g`, `pfVUD5FVoB0`, `TE_pQ8pyL80`.

## Semana 15: FET, MOSFET, IGBT y gestion termica

Playlist base:

- 51 `GGprFdtFbnU`: JFET
- 52 `h8VcISK7y3w`: MOSFET
- 52.1 `u6UeaLh8nUY`: MOSFET en conmutacion
- 52.2 `Vyyi62GsjZ0`: probar MOSFET
- 52.3 `FCMzV7k8WEM`: PWM con MOSFET
- 53 `PlFjPAwaTNk`: IGBT
- 54 `x8nKy71afas`: evitar quemar transistores, disipador
- 55 `xMqHr51SMmk`: Darlington/Sziklai

Teoria, 4 h:

- JFET, MOSFET e IGBT: control por campo y conmutacion.
- Rds(on), carga de compuerta, disipacion y SOA.
- PWM, perdidas de conduccion/conmutacion y disipador.

Practica, 2 h:

- Driver MOSFET de bajo voltaje para carga resistiva o LED.
- Calculo termico preliminar y simulacion de potencia.

Enfoque aeroespacial:

- Control de cargas, actuadores, redundancia, disipacion y margen termico.

Entregable:

- Seleccion de transistor con margen de corriente, tension y temperatura.

Extraccion prioritaria:

- `h8VcISK7y3w`, `u6UeaLh8nUY`, `x8nKy71afas`.

## Semana 16: Integracion aeroespacial y proyecto final

Playlist base:

- Repaso selectivo de videos clave por necesidad del proyecto.

Teoria, 4 h:

- Integracion de cadena analogica: sensor, puente/divisor, filtro, proteccion,
  acondicionamiento, ADC y actuador.
- Reglas de diseno: derating, tolerancias, proteccion, temperatura, ruido,
  validacion y trazabilidad.
- Revision de ECSS, DO-160, SPICE y documentacion tecnica.

Practica, 2 h:

- Proyecto final: front-end analogico aeroespacial de baja tension.
- Puede ser una de estas rutas:
  - sensor resistivo con puente + filtro + ADC simulado
  - entrada protegida con diodos/zener + filtro
  - driver BJT/MOSFET protegido para carga de baja tension

Entregable:

- Mini dossier de diseno:
  - esquematico
  - calculos
  - simulacion
  - tabla de derating
  - riesgos
  - prueba de aceptacion

Extraccion prioritaria:

- No extraer nuevos videos salvo huecos detectados. Consolidar fuentes,
  NotebookLM y material web.

## Estrategia de extraccion por lotes

Para no saturar el repositorio con 100 clases a la vez, extraer por fases:

1. Semanas 1-4: fundamentos DC y metodos de red.
2. Semanas 5-9: AC, reactivos, filtros y resonancia.
3. Semanas 10-13: diodos, rectificacion, zener y LEDs.
4. Semanas 14-15: transistores y potencia discreta.
5. Semana 16: proyecto integrador y curacion final.

Cada fase debe terminar con:

```powershell
python tools/publish_course.py --urls-file clases_fase_N.txt --provider auto
python tools/build_site_content.py
python tools/export_agent_context.py
python -m unittest discover -s tools\tests -v
```

## Regla editorial

Cada semana debe producir tres capas:

- `teoria`: resumen propio y calculos originales.
- `practica`: guia de laboratorio o simulacion segura.
- `aeroespacial`: conexion con ECSS/DO-160, derating, ruido, temperatura,
  proteccion, confiabilidad o validacion.

No publicar transcripciones completas ni copiar pasajes largos de videos o
fuentes externas.
