# Laboratorio Semana 1: Ohm, potencia y margen de diseno

Curso: Fundamentos de Sistemas Electronicos Analogicos, Ingenieria Aeroespacial.

Duracion: 2 horas.

Nivel de riesgo: bajo voltaje. No superar 12 V DC. Usar limite de corriente.

## Proposito

La primera practica no busca que el circuito "encienda". Busca que el alumno
pueda cerrar el ciclo completo:

1. medir componentes reales
2. calcular corriente, caidas de tension y potencia
3. simular el punto de operacion
4. comparar teoria, medicion y simulacion
5. decidir si el circuito tiene margen de potencia suficiente

## Resultado esperado

Al terminar, cada equipo entrega una tabla con:

- valor nominal de cada resistor
- valor medido
- tolerancia calculada
- corriente teorica y medida
- caida de tension teorica y medida
- potencia disipada
- potencia nominal del resistor
- margen de derating
- decision: aceptado, condicionado o rechazado

## Materiales por equipo

- Fuente DC ajustable con limite de corriente.
- Multimetro digital.
- Protoboard.
- Cables cortos.
- Resistores: 1 kohm, 2.2 kohm, 3.3 kohm, 1/4 W o mayor.
- Potenciometro lineal de 10 kohm.
- Opcional: resistores de 1% y 5% para comparar tolerancia.
- LTspice, QSPICE o simulador SPICE compatible.

## Seguridad

- La fuente debe estar apagada mientras se arma el circuito.
- Ajustar el limite de corriente a 20 mA antes de energizar.
- No usar resistores de 1 ohm a 10 ohm en protoboard para esta practica.
- No tocar componentes energizados.
- Si un resistor se calienta, apagar la fuente y revisar potencia.
- No superar 12 V DC.

Nota: una red de 2 ohm + 3 ohm + 1 ohm a 12 V exige 2 A y disipa 24 W en
total. Esa red sirve para discutir potencia y peligro, no para una practica
inicial en protoboard.

## Pre-lab

Antes de entrar al laboratorio, resolver:

1. Para R1 = 1 kohm, R2 = 2.2 kohm, R3 = 3.3 kohm en serie con Vin = 12 V,
   calcular resistencia total.
2. Calcular corriente total.
3. Calcular la caida de tension en cada resistor.
4. Calcular potencia en cada resistor.
5. Si cada resistor es de 1/4 W y se aplica derating de 50%, decidir si cada
   resistor cumple.

Valores esperados aproximados:

- Rtotal = 6.5 kohm
- I = 1.846 mA
- V1 = 1.846 V
- V2 = 4.062 V
- V3 = 6.092 V
- P1 = 3.41 mW
- P2 = 7.50 mW
- P3 = 11.26 mW

Todos cumplen con amplio margen frente a 0.125 W, que es el 50% de 0.25 W.

## Procedimiento A: medicion de resistores

1. Separar R1, R2 y R3.
2. Medir cada resistor fuera del circuito.
3. Registrar valor nominal, valor medido y tolerancia.
4. Calcular:

   ```text
   error_percent = 100 * (Rmedida - Rnominal) / Rnominal
   ```

5. Clasificar cada resistor:

   - cumple si el error queda dentro de la tolerancia indicada
   - revisar si no se conoce tolerancia
   - rechazar si excede tolerancia declarada

## Procedimiento B: red serie

1. Con la fuente apagada, conectar R1, R2 y R3 en serie.
2. Ajustar fuente a 0 V.
3. Ajustar limite de corriente a 20 mA.
4. Subir lentamente a 12 V.
5. Medir corriente total.
6. Medir caida de tension en R1, R2 y R3.
7. Verificar:

   ```text
   Vin ~= VR1 + VR2 + VR3
   ```

8. Calcular potencia:

   ```text
   P = V * I
   P = I^2 * R
   ```

9. Comparar contra potencia nominal con derating:

   ```text
   P_derated_max = 0.5 * P_nominal
   margen = P_derated_max / P_disipada
   ```

## Procedimiento C: potenciometro como divisor

1. Conectar el potenciometro de 10 kohm como divisor: extremo superior a 5 V,
   extremo inferior a GND y cursor como salida.
2. Medir Vout en tres posiciones: minimo, centro aproximado, maximo.
3. Registrar si la curva observada parece lineal.
4. Discutir por que un trimpot mecanico puede moverse por vibracion y por que
   en aeroespacial se fija o se reemplaza por redes de precision.

## Procedimiento D: simulacion

Usar primero la secuencia guiada:

`docs/labs/semana_1_simulaciones_ltspice.md`

Para reproducir directamente la red fisica del laboratorio, abrir:

`Simulaciones Ltspice/sim/semana1_02_kvl_serie.asc`

Ejecutar analisis `.op` y consultar `View > SPICE Error Log`.

Comparar:

- corriente de fuente
- tension en nodos
- potencia por resistor
- balance de potencia

## Plantilla de tabla de datos

| Elemento | R nominal | R medida | Error % | V medida | I medida | P calculada | P nominal | P derated 50% | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| R1 | 1 kohm | | | | | | 0.25 W | 0.125 W | |
| R2 | 2.2 kohm | | | | | | 0.25 W | 0.125 W | |
| R3 | 3.3 kohm | | | | | | 0.25 W | 0.125 W | |

## Preguntas de cierre

1. Por que la suma de caidas de tension debe aproximarse a Vin?
2. Que medicion tiene mas incertidumbre: resistencia, tension o corriente?
3. Que cambia si Vin sube de 12 V a 14 V?
4. Por que potencia nominal no significa potencia segura de diseno?
5. Que parametro de resistor importa mas para sensores de precision: tolerancia,
   TCR o potencia? Justifica.

## Rubrica

| Criterio | Peso |
| --- | ---: |
| Mediciones completas y ordenadas | 20% |
| Calculos correctos de Ohm/Kirchhoff/potencia | 25% |
| Simulacion y comparacion contra medicion | 20% |
| Analisis de derating y decision de seguridad | 25% |
| Claridad del reporte | 10% |
