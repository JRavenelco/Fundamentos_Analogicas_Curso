# Semana 2: divisores, puentes y equivalentes para sensores

Curso: Fundamentos de Sistemas Electronicos Analogicos, Ingenieria Aeroespacial.

Carga: 4 horas de teoria y 2 horas de practica.

## Resultado de aprendizaje

Al terminar la semana, el estudiante podra modelar una red resistiva de sensor,
predecir el error causado por la carga y entregar su equivalente de Thevenin
como interfaz de entrada para una etapa de amplificacion o un ADC.

## Pregunta rectora

Una salida de 2.5 V medida en vacio, ¿seguira siendo de 2.5 V al conectarla a
un instrumento, amplificador o ADC?

## Bloque 1: divisor de tension y efecto de carga

Para dos resistores en serie:

```text
Vout = Vin * R2 / (R1 + R2)
```

Esta expresion solo describe la salida sin carga. Si una resistencia `RL` se
conecta en paralelo con `R2`, debe usarse:

```text
Req = R2 || RL
Vout,cargada = Vin * Req / (R1 + Req)
```

Ideas clave:

- una impedancia de entrada finita forma parte del circuito
- para reducir el error se desea `Rin >> Rth`
- resistores menores reducen el error de carga, pero aumentan consumo
- resistores mayores ahorran energia, pero elevan impedancia, ruido termico y
  sensibilidad a corrientes de fuga

Ejemplo: `Vin = 12 V`, `R1 = 30 kohm`, `R2 = 10 kohm`.

- salida ideal: 3.000 V
- con `RL = 100 kohm`: 2.791 V, error de -6.98%
- con `RL = 47 kohm`: 2.571 V, error de -14.29%
- con `RL = 10 kohm`: 1.714 V, error de -42.86%

## Bloque 2: equivalentes de Thevenin y Norton

Desde los terminales de salida del divisor:

```text
Vth = Vin * R2 / (R1 + R2)
Rth = R1 || R2
In = Vth / Rth
Rn = Rth
```

El equivalente no es un truco algebraico: resume lo que vera la siguiente
etapa. Permite calcular carga, corriente de cortocircuito, disipacion y
compatibilidad de impedancias sin conservar toda la red original.

Para el ejemplo anterior:

- `Vth = 3.000 V`
- `Rth = 7.500 kohm`
- `In = 0.400 mA`

## Bloque 3: puente de Wheatstone como traductor R-V

Un puente se construye con dos divisores. Su salida diferencial es:

```text
Vdiff = Vleft - Vright
Vleft  = Vexc * R2 / (R1 + R2)
Vright = Vexc * R4 / (R3 + R4)
```

Con cuatro resistores iguales, el puente esta balanceado y `Vdiff = 0 V`.
Para un cuarto de puente, si un solo resistor cambia de `R` a `R + dR`, y
`|dR| << R`, la sensibilidad aproximada es:

```text
Vdiff ~= Vexc/4 * dR/R
```

Ejemplo con `Vexc = 5 V`, `R = 350 ohm` y `dR = 0.35 ohm`:

- deformacion resistiva relativa: `dR/R = 0.001`
- salida aproximada: `1.25 mV`
- salida exacta: aproximadamente `1.249 mV`

El signo depende de la rama y de la convencion elegida para `Vdiff`.

## Bloque 4: lectura aeroespacial y preparacion de la interfaz

Antes de amplificar una señal resistiva se documentan:

- rango de `Vdiff`, incluido su signo
- tension de modo comun
- resistencia de salida de cada rama
- tolerancia inicial y deriva termica
- potencia de excitacion y autocalentamiento
- impedancia de entrada requerida
- errores por cableado, fuga, ruido y desbalance

En una galga de 350 ohm excitada con 5 V, cada resistor disipa cerca de
17.9 mW en equilibrio. Aumentar la excitacion mejora la señal, pero la potencia
crece con el cuadrado de la tension y puede producir autocalentamiento.

## Actividades de teoria activa

1. Calcular la salida ideal y cargada de tres divisores.
2. Obtener `Vth`, `Rth` e `In` vistos desde su salida.
3. Predecir el signo de `Vdiff` al incrementar cada brazo del puente.
4. Comparar la expresion exacta del puente con la aproximacion de pequeña señal.
5. Defender una tension de excitacion considerando sensibilidad y potencia.

## Evidencia y evaluacion

Entregable: ficha de interfaz de sensor con esquema, ecuaciones, barrido,
equivalente de Thevenin y presupuesto de error.

| Criterio | Peso |
| --- | ---: |
| Modelo y convenciones de signo | 20% |
| Calculos y equivalente de Thevenin | 25% |
| Comparacion teoria-simulacion-medicion | 25% |
| Analisis de carga, tolerancia y potencia | 20% |
| Conclusion de ingenieria | 10% |

## Fuentes base del repositorio

- Plan rector: `docs/weekly_course_plan_16_weeks_unam_aligned.md`.
- Clase 2, resistores: `extracted_courses/jli6YBkRt3U/course_notes.md`.
- Material VectorLab: `Material_Didactico_VectorLab.md`.
- Practica previa de carga: `Simulaciones Ltspice/sim/semana1_06_divisor_cargado.cir`.
