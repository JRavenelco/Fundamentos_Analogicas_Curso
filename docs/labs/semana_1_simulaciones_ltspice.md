# Semana 1: secuencia de simulaciones LTspice

Duracion sugerida: 90 minutos de teoria activa y 30 minutos de cierre.

## Metodo de trabajo

Para cada circuito el alumno debe completar cuatro acciones:

1. predecir el signo y el orden de magnitud
2. calcular al menos un caso a mano
3. ejecutar LTspice y consultar `View > SPICE Error Log`
4. explicar cualquier diferencia entre calculo y simulacion

Los archivos `.asc` permiten explorar el esquema. Los `.cir` contienen el
mismo experimento en forma reproducible y son adecuados para ejecucion batch.

## S1.1: Ley de Ohm mediante barridos

Archivos:

- `semana1_01_ohm_barrido.asc`
- `semana1_01_ohm_barrido.cir`

Pregunta inicial: si la tension se duplica, que ocurre con corriente y potencia?

Actividad:

- graficar `-I(V1)` contra la tension
- comparar las pendientes de 1 kohm, 2.2 kohm y 4.7 kohm
- explicar por que la pendiente es conductancia

Resultado clave: la corriente es lineal con V, pero la potencia crece con V al
cuadrado para una resistencia fija.

## S1.2: Serie, KVL y balance de potencia

Archivos:

- `semana1_02_kvl_serie.asc`
- `semana1_02_kvl_serie.cir`

Teoria de apoyo: `docs/labs/semana_1_teoria_s12_serie_kvl_balance.md`

Predicciones:

- la corriente es la misma en R1, R2 y R3
- la mayor resistencia presenta la mayor caida de tension
- la potencia entregada por la fuente coincide con la absorbida

Valores aproximados: I = 1.846 mA; VR1 = 1.846 V; VR2 = 4.062 V;
VR3 = 6.092 V; potencia total = 22.15 mW.

## S1.3: Paralelo, KCL y resistencia equivalente

Archivos:

- `semana1_03_kcl_paralelo.asc`
- `semana1_03_kcl_paralelo.cir`

Teoria de apoyo: `docs/labs/semana_1_teoria_s13_paralelo_kcl.md`

Pregunta inicial: que rama conduce mas corriente y por que?

Valores aproximados con 5 V: IR1 = 5.000 mA; IR2 = 2.273 mA;
IR3 = 1.515 mA; Ifuente = 8.788 mA; Req = 568.97 ohm.

Conexion aeroespacial: una fuente de avionica debe dimensionarse para la suma
de corrientes de todas las cargas conectadas, no para la carga promedio.

## S1.4: Potencia nominal y derating

Archivos:

- `semana1_04_potencia_derating.asc`
- `semana1_04_potencia_derating.cir`

El resistor es de 1 kohm y 0.25 W. Para el ejercicio se usa un limite de diseno
del 50%, es decir, 0.125 W.

Pregunta inicial: a que tension se alcanza primero el limite de diseno?

Resultado clave: `sqrt(0.125 W * 1000 ohm) = 11.18 V`. A 12 V el resistor
disipa 144 mW: no supera 0.25 W, pero si supera el limite con derating.

## S1.5: Fuente real y falla de carga

Archivos:

- `semana1_05_fuente_y_falla.asc`
- `semana1_05_fuente_y_falla.cir`

Este circuito es solo para simulacion. No construir los casos de 10 ohm o
1 ohm en protoboard.

Actividad: reducir Rload desde 1 kohm hasta 1 ohm y observar Vbus, corriente y
potencia en la resistencia interna de 10 ohm. Explicar por que una fuente real
reduce su tension de salida y por que necesita limite de corriente.

## S1.6: Potenciometro y efecto de carga

Archivos:

- `semana1_06_divisor_cargado.asc`
- `semana1_06_divisor_cargado.cir`

Actividad: comparar `V(vout_u)` y `V(vout_l)` para tres posiciones del cursor.
La salida cargada usa 10 kohm, igual al valor total del potenciometro.

Pregunta de cierre: cuando se puede tratar un divisor como una fuente ideal de
tension y cuando se necesita un buffer?

## Evidencia minima

Cada equipo entrega una tabla con prediccion, calculo, resultado LTspice, error
porcentual y explicacion para al menos un caso de cada simulacion.

Evaluacion sugerida:

| Criterio | Peso |
| --- | ---: |
| Predicciones justificadas | 20% |
| Calculos manuales | 25% |
| Uso correcto de barridos y `.meas` | 20% |
| Interpretacion fisica | 25% |
| Orden y trazabilidad | 10% |
