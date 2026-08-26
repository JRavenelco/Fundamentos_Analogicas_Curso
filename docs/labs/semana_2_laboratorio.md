# Laboratorio Semana 2: interfaz resistiva de sensor

Duracion: 2 horas. Tension maxima: 5 V DC. Limite de corriente: 20 mA.

## Proposito

Construir y caracterizar una red resistiva que emule un sensor, cuantificar su
error por carga y entregar el equivalente de Thevenin que usara la siguiente
etapa del sistema.

## Materiales por equipo

- fuente DC de 5 V con limite de corriente
- dos multimetros, si estan disponibles
- protoboard y cables cortos
- cuatro resistores de 1 kohm, preferentemente 1%
- resistores de carga de 100 kohm, 47 kohm y 10 kohm
- un resistor de 1 kohm mas potenciometro de ajuste fino, o una decada resistiva
- LTspice o simulador SPICE compatible

## Seguridad y buenas practicas

- medir resistencias con la fuente apagada
- verificar el limite de corriente antes de energizar
- no cambiar conexiones con el circuito energizado
- registrar unidades y polaridad en cada medicion
- no interpretar una lectura diferencial sin declarar que terminal es positivo

## Pre-lab

1. Para `Vin = 5 V`, `R1 = R2 = 1 kohm`, calcular `Vth` y `Rth`.
2. Calcular `Vout` para cargas de 100 kohm, 47 kohm y 10 kohm.
3. Para un puente de cuatro resistores de 1 kohm, calcular `Vdiff` balanceado.
4. Sustituir un brazo por 1.01 kohm y calcular `Vdiff` exacta.
5. Estimar la potencia de cada resistor en el puente balanceado.

Resultados de referencia:

- `Vth = 2.5 V`, `Rth = 500 ohm`
- con 100 kohm: `Vout = 2.4876 V`
- con 47 kohm: `Vout = 2.4737 V`
- con 10 kohm: `Vout = 2.3810 V`
- puente balanceado: `Vdiff = 0 V`
- cambio de 1 kohm a 1.01 kohm en el brazo superior izquierdo:
  `Vleft = 2.4876 V`, `Vdiff = -12.44 mV` usando `Vleft - Vright`
- potencia por resistor balanceado: `6.25 mW`

## Parte A: divisor real y carga

1. Medir `R1` y `R2` fuera del circuito.
2. Construir el divisor con `R1 = R2 = 1 kohm` y `Vin = 5 V`.
3. Medir la salida sin carga adicional.
4. Conectar sucesivamente `RL = 100 kohm`, `47 kohm` y `10 kohm`.
5. Para cada caso registrar calculo, simulacion y medicion.
6. Calcular el error respecto a la salida sin carga:

```text
error_carga = 100 * (Vout,cargada - Vout,vacio) / Vout,vacio
```

## Parte B: medir el equivalente de Thevenin

1. Usar la tension sin carga como estimacion de `Vth`.
2. Conectar una carga conocida `RL = 1 kohm` y medir `VL`.
3. Estimar:

```text
Rth = RL * (Vth/VL - 1)
```

4. Comparar el resultado con `R1 || R2` calculado usando valores medidos.
5. Explicar el efecto de la impedancia de entrada del multimetro.

## Parte C: puente de Wheatstone

1. Medir cuatro resistores de 1 kohm y asignarlos a R1-R4.
2. Construir los dos divisores y verificar cada nodo respecto a tierra.
3. Medir `Vdiff = Vleft - Vright` directamente.
4. Registrar el desbalance inicial debido a tolerancias reales.
5. Agregar aproximadamente 10 ohm en serie con R1, o ajustar el brazo a
   1.01 kohm.
6. Medir nuevamente `Vleft`, `Vright` y `Vdiff`.
7. Comparar el resultado exacto, la simulacion y la medicion.

## Parte D: decision de interfaz

El equipo debe completar una ficha con:

- rango observado de señal diferencial
- tension de modo comun aproximada
- resistencia de Thevenin de cada mitad del puente
- carga minima que mantiene el error por debajo de 1%
- ganancia tentativa para usar el rango de 0 a 3.3 V de un ADC
- riesgos: saturacion, signo, tolerancia, ruido y autocalentamiento

No se construye aun el amplificador; la ficha define sus requisitos de entrada.

## Tabla de resultados

| Prueba | Prediccion | Simulacion | Medicion | Error | Explicacion |
| --- | ---: | ---: | ---: | ---: | --- |
| Divisor sin carga | | | | | |
| Carga 100 kohm | | | | | |
| Carga 47 kohm | | | | | |
| Carga 10 kohm | | | | | |
| Vth | | | | | |
| Rth | | | | | |
| Puente balanceado | | | | | |
| Puente con R1 = 1.01 kohm | | | | | |

## Criterio de aceptacion

La practica se considera completa cuando el equipo puede explicar, con datos,
por que una salida correcta en vacio puede dejar de ser correcta al conectarse
y puede entregar un modelo de Thevenin verificable para la siguiente etapa.
