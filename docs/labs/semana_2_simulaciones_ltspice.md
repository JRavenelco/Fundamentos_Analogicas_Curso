# Semana 2: secuencia de simulaciones LTspice

Los netlists estan en `Simulaciones Ltspice/sim`. Cada actividad exige una
prediccion, un calculo manual, el resultado de `.meas` y una conclusion.

## S2.1: divisor cargado

Archivo: `semana2_01_divisor_cargado.cir`.

Se barre la carga de 10 kohm a 1 Mohm. Identificar la resistencia minima que
mantiene el error por carga por debajo de 1%. Relacionar el resultado con
`Rth = R1 || R2`.

## S2.2: tolerancia del divisor

Archivo: `semana2_02_divisor_tolerancia.cir`.

Se evaluan las cuatro combinaciones extremas de dos resistores de 1%. Comparar
el rango de salida con el valor nominal. Distinguir error de razon de error de
valor absoluto.

## S2.3: puente de Wheatstone

Archivo: `semana2_03_wheatstone_desbalance.cir`.

Se barre el cambio fraccional de un brazo entre -1% y +1%. Graficar la salida
diferencial y comparar su pendiente cerca de cero con `Vexc/4`.

## S2.4: equivalente de Thevenin del sensor

Archivo: `semana2_04_thevenin_sensor.cir`.

La red original y su equivalente alimentan cargas iguales. Las salidas deben
coincidir. Verificar casos de 1 kohm, 10 kohm y 100 kohm.

## Evidencia minima

- captura o tabla de los cuatro experimentos
- ecuaciones usadas
- diferencia porcentual teoria-simulacion
- ficha de interfaz con `Vth`, `Rth`, rango diferencial y carga admisible
