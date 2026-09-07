# Cómo funciona un MOSFET: teoría, analogías y límites

## 1. La idea esencial

Un MOSFET usa una **tensión entre compuerta y fuente**, `VGS`, para crear un
campo eléctrico. La compuerta está separada del semiconductor por un óxido, de
modo que idealmente no circula corriente continua hacia ella. El campo sí
reorganiza las cargas bajo el óxido y puede formar un canal conductor entre
drenaje y fuente.

**Analogía de la válvula:** drenaje y fuente son los extremos de una tubería;
la compuerta es la manija. Mover la manija modifica qué tan fácil pasa la
corriente por el canal.

**Límite de la analogía:** la compuerta no es una pieza mecánica. Es un
capacitor: el driver debe mover carga para cambiar su tensión. Además, el
MOSFET contiene un diodo de cuerpo y sus límites dependen de tensión,
temperatura, tiempo y área segura de operación.

## 2. Cómo nace el canal en un NMOS

1. Con `VGS=0`, no existe un canal de inversión continuo: el dispositivo está
   en corte salvo fugas.
2. Una `VGS` positiva produce un campo a través del óxido y atrae electrones
   hacia la superficie del cuerpo tipo P.
3. Cerca de `VGS(th)` comienza a existir un canal muy débil. En el IRF640N el
   umbral de 2–4 V se ensaya con apenas 250 µA; no representa el encendido de
   potencia.
4. Con una tensión de compuerta mayor, el canal contiene más portadores y su
   resistencia disminuye. Para el IRF640N, `RDS(on)` se especifica a
   `VGS=10 V`, no a 3.3 V.

**Analogía del puente:** el campo eléctrico reúne suficientes “tablones” para
formar un puente. En el umbral apenas existe un paso estrecho; no equivale a
un puente capaz de transportar una carga pesada.

## 3. Tres regiones y dos usos distintos

- **Corte:** `VGS < Vth`; el canal está ausente o es despreciable.
- **Región óhmica o triodo:** `VGS > Vth` y `VDS < VGS−Vth`; el MOSFET se
  aproxima a una resistencia controlada. Es la región buscada para un switch
  cerrado.
- **Saturación:** `VGS > Vth` y `VDS ≥ VGS−Vth`; la corriente depende menos de
  `VDS`. Esta región se usa en amplificación.

Estas condiciones son el modelo ideal de canal largo. Un MOSFET de potencia
real requiere curvas, tolerancias, temperatura y datos dinámicos del
fabricante. En particular, **“MOSFET saturado” no significa lo mismo que “BJT
saturado”**.

## 4. La compuerta: no consume DC, pero sí exige un driver

La compuerta se comporta como una capacidad que debe cargarse y descargarse:

```text
Q = C·V          I = dQ/dt
t_sw ≈ Qg / Idriver
IG,avg ≈ Qg · f
```

**Analogía del depósito:** para elevar `VGS`, el driver llena un depósito de
carga; para apagar, debe vaciarlo. Una tubería ancha representa un driver con
más corriente y produce flancos más rápidos. En la meseta Miller, la carga
adicional se usa principalmente en cambiar `VDS`, por eso `VGS` parece quedar
momentáneamente plana.

**Límite de la analogía:** `Ciss` no es una capacitancia constante que describa
todo el evento. Para estimar conmutación se usa la curva de carga de compuerta
`Qg` bajo condiciones cercanas al circuito real.

## 5. Aplicación al motor de esta práctica

El motor es nominal de 6 V y se alimenta con un bus de 5 V. El IRF640N usa un
driver gate-source separado de 10–12 V. El sistema comparte masa y el drive se
mide siempre respecto del source, que puede elevarse por el shunt; **12 V nunca
se aplican al motor**.

Para no subestimar los 250–400 mA informados, la simulación usa equivalentes
terminales de 20 Ω y 12.5 Ω a 5 V. Si esas corrientes pertenecen a la ficha a
6 V, los equivalentes serían 24 Ω y 15 Ω; la corriente real a 5 V debe medirse.
En ambos casos todavía falta la corriente de arranque/bloqueo, que suele ser
mayor porque al arrancar la fuerza contraelectromotriz es casi cero.

El diodo flyback proporciona un camino a la corriente inductiva cuando el
MOSFET abre. Se conecta con ánodo al drenaje y cátodo a +5 V. Su selección se
hace con la corriente de bloqueo medida, tensión inversa, energía repetitiva y
temperatura, no únicamente con los 400 mA nominales.

## 6. Preguntas para comprobar comprensión

1. ¿Qué parte de la analogía de la válvula representa `VGS` y qué parte no
   puede representar?
2. ¿Por qué superar `VGS(th)` no garantiza baja pérdida?
3. ¿Por qué el switch ON busca la región óhmica y no la saturación?
4. Si el driver entrega el doble de corriente, ¿qué ocurre aproximadamente
   con el tiempo de conmutación?
5. ¿Por qué el motor y la compuerta pueden usar 5 V y 12 V, respectivamente,
   sin violar la tensión nominal del motor?
6. ¿Qué dato del motor falta antes de elegir definitivamente el diodo?
