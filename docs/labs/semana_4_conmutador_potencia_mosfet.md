# Semana 4: conmutador de potencia con IRF640N

Práctica incremental para controlar un **motor DC nominal de 6 V, alimentado
con 5 V**, con un NMOS de lado bajo. Se han informado 250 mA sin carga y hasta
400 mA con carga nominal. Se
estudian la carga de compuerta, el diodo de libre circulación, un shunt para
ADC y el puente con un BJT en saturación forzada. Cada etapa se calcula
**antes** de ejecutarse.

## 1. Qué se está modelando

El IRF640N no tiene `RDS(on)` garantizada a 3.3 V. En esta práctica se usa un
driver idealizado de 0/12 V con resistencia de salida de 10 Ω y `RG=100 Ω`.
En hardware deben añadirse masa común y una resistencia gate-source de
pull-down, por ejemplo 10 kΩ, para asegurar el apagado si el driver queda
desconectado.

Los netlists usan una envolvente conservadora que reproduce los dos valores de
corriente en el bus real de 5 V:

```text
Req,sin carga = 5 V / 0.25 A = 20 Ω
Req,con carga = 5 V / 0.40 A = 12.5 Ω
```

Si 250/400 mA son valores exclusivos de la ficha a la tensión nominal de 6 V,
los equivalentes serían 24/15 Ω y un cálculo resistivo a 5 V daría cerca de
208/333 mA antes de las pérdidas. Deben medirse las corrientes reales a 5 V;
el material conserva 250/400 mA para no subestimar el diseño.

Esto no convierte al motor en un resistor: su corriente depende de resistencia
de armadura, inductancia, fuerza contraelectromotriz, velocidad y par. Para la
etapa inductiva se conserva `LPLACE=100 mH` únicamente como valor didáctico que
debe sustituirse por la inductancia medida. Los **400 mA son el máximo nominal
informado, no la corriente de arranque o bloqueo**; esa corriente falta y es
obligatoria antes de aprobar hardware.

Datos del fabricante:

| Parámetro | Valor | Condición |
| --- | ---: | --- |
| `VDS,max` | 200 V | límite absoluto |
| `VGS,max` | ±20 V | límite absoluto |
| `RDS(on),max` | 0.15 Ω | `VGS=10 V`, `ID=11 A`, `TJ=25 °C` |
| `VGS(th)` | 2–4 V | `ID=250 µA`, `VDS=VGS` |
| `Qg,max` | 67 nC | `ID=11 A`, `VDS=160 V`, `VGS=10 V` |
| `Ciss,typ` | 1160 pF | `VGS=0`, `VDS=25 V`, 1 MHz |

`VGS(th)` solo marca el inicio de un canal diminuto; no es una especificación
de encendido. El valor de 18 A publicado para `ID` supone `TC=25 °C` y otras
condiciones del datasheet: no autoriza una corriente de banco sin análisis
térmico y de área segura de operación.

Fuente: [IRF640N, Infineon](https://www.infineon.com/assets/row/public/documents/24/49/infineon-irf640n-datasheet-en.pdf).

### Alcance del modelo

`semana4_irf640n_educativo.lib` es un sustituto didáctico. Aproxima la
conducción estática y agrega un límite numérico cerca de 200 V, pero **no** es
el modelo oficial: no valida SOA, temperatura, avalancha, meseta Miller ni
pérdidas reales. La capacitancia equivalente `Qg/Vdrive` sirve para ejercitar
el driver; no sustituye la curva de carga de compuerta del datasheet.

## 2. Herramientas

- **LTspice XVII/24:** abre y ejecuta los netlists incluidos; las directivas
  `.meas` aparecen en `View > SPICE Error Log`.
- **InfineonSpice:** alternativa gratuita para consultar modelos disponibles
  del fabricante.
- **Datasheet oficial:** referencia final para límites y diseño de hardware.

### Lista mínima para el montaje real

- Fuente de motor de 5 V con límite de corriente y fusible adecuados; no
  aplicar los 10–12 V del driver al motor nominal de 6 V.
- Driver gate-source separado de 10–12 V, con masa común; nunca aplicar más de
  ±20 V entre gate y source.
- Resistencia `RG=100 Ω` inicial y pull-down gate-source de 10 kΩ.
- Diodo flyback cuyo `IF` admisible cubra la corriente de bloqueo y cuyo
  `VRRM` tenga margen sobre 5 V y los transitorios del bus.
- Desacoplo cerca de la etapa de potencia y cableado de retorno separado del ADC.
- Shunt con potencia de pulso suficiente. A 400 mA, 1 Ω disipa 160 mW; su
  selección final depende de la corriente de bloqueo aún desconocida.

Un 1N5819 puede servir para ensayos limitados de baja corriente, pero no debe
declararse definitivo hasta conocer la corriente de bloqueo, repetición PWM,
temperatura y margen de tensión. Trabaje primero con la fuente limitada.

## 3. Predicción previa

Sin simular, complete:

1. Si `VGS=3.3 V`, ¿qué dato garantiza `RDS(on)`? ____________________
2. Cuando el gate sube, el drenaje de un lado bajo: sube / baja.
3. Al apagar una bobina, la corriente intenta: detenerse de golpe / mantener
   magnitud y dirección.
4. Un divisor 10 kΩ/10 kΩ tiene ganancia: 2 / 1 / 0.5.
5. En un BJT NPN, un colector sin pull-up puede: entregar / hundir corriente.
6. ¿La corriente de bloqueo del motor es necesariamente 400 mA? __________

## 4. Etapa 1 — PWM y carga de compuerta

Archivo: `semana4_01_pwm_gate_mosfet.cir`.

```text
 +5 V ── motor DC nominal 6 V ── D  IRF640N  S ── GND
             250–400 mA (envolvente conservadora)
                           G
 driver 0/12 V ── RDRV=10 Ω ── RG=100 Ω
```

La salida de drenaje está invertida: gate alto produce drenaje bajo.

Estimación conservadora de conducción a 25 °C, usando el máximo publicado:

```text
Sin carga: ID ≈ 5/(20+0.15) = 248.1 mA
           VDS,on ≤ 37.2 mV; Pcond ≤ 9.2 mW
Con carga: ID ≈ 5/(12.5+0.15) = 395.3 mA
           VDS,on ≤ 59.3 mV; Pcond ≤ 23.4 mW
```

El modelo pedagógico produce un valor algo menor porque está ajustado de forma
aproximada y el drive es 12 V. No debe reemplazarse el cálculo de peor caso por
ese resultado.

La compuerta recibe pulsos aunque `IG≈0` en estado estacionario:

```text
IG,avg ≈ Qg · f ≤ 67 nC · 100 kHz = 6.7 mA
Pdriver ≈ Qg · Vdrive · f ≈ 80 mW
Ceq = Qg/Vdrive ≈ 5.58 nF
t10–90 ≈ 2.2(RDRV+RG)Ceq ≈ 1.35 µs
```

Resultados de referencia obtenidos con LTspice XVII:

| Caso | `ID_ON` | `VDS_ON` | `VGS_ON` |
| --- | ---: | ---: | ---: |
| 20 Ω, sin carga | 248.492 mA | 30.17 mV | 11.980 V |
| 12.5 Ω, con carga | 396.149 mA | 48.13 mV | 11.980 V |

Para ambos casos: `VDS_OFF=5.000 V`, `IG_PEAK=108.97 mA`,
`TG_10_90≈1.350 µs` y `PDRV_AVG≈80.36 mW`.

Preguntas:

- ¿Por qué `IG_PEAK` es grande si la corriente continua de gate es casi cero?
- ¿Qué cambia si la frecuencia aumenta diez veces?
- ¿Por qué se mide `VGS`, no únicamente `VG`?

## 5. Etapa 2 — Carga inductiva

Archivos:

- `semana4_02_carga_inductiva_flyback.cir`: caso protegido.
- `semana4_02b_carga_inductiva_sin_diodo.cir`: demostración numérica, nunca
  para reproducir retirando el diodo en hardware.

El netlist usa el punto cargado conservador `Req=12.5 Ω` y una inductancia
provisional `LPLACE=100 mH` entre +5 V y el drenaje. El diodo externo se coloca
en paralelo con el motor: **ánodo al drenaje y cátodo a +5 V**.

Durante ON:

```text
tau_on ≈ 100 mH/(12.5 Ω + RDS) ≈ 7.9 ms
I(40 ms) ≈ 393 mA
E_L ≈ 0.5 · 100 mH · (0.393 A)² ≈ 7.7 mJ
```

La energía de 7.7 mJ pertenece al `LPLACE` provisional, no al motor real.

Al apagar, la corriente continúa por el lazo drenaje → diodo → +5 V → L → R
→ drenaje. El drenaje queda cerca de `VCC+VF`; `VF` depende de corriente,
temperatura y diodo. La descarga tampoco es una exponencial perfecta porque
la caída del diodo se suma al término resistivo.

Resultados con el diodo genérico incluido:

| Medida | Resultado |
| --- | ---: |
| `VDS_CLAMP_MAX` | 5.901 V |
| `ID_END_ON` | 393.321 mA |
| `IFLY_PEAK` | 393.554 mA |
| `IFLY_3MS` | 248.274 mA |

La variante sin diodo alcanza 200.231 V porque el sustituto pedagógico contiene
un clamp numérico cercano al `VDS,max`. **Ese número no predice la avalancha ni
garantiza supervivencia.** La conclusión válida es causal: sin un camino
externo, el inductor eleva `VDS` hasta que algo conduce o falla.

Para hardware, seleccione el flyback por corriente, tensión inversa, velocidad,
energía repetitiva y temperatura; no copie el diodo genérico del netlist.

## 6. Etapa 3 — Shunt y escalado al ADC

Archivo: `semana4_03_medicion_adc.cir`.

Se inserta `RSENSE=1 Ω` entre la fuente y GND. Por eso la tensión real de
compuerta es `VGS=V(gate,sense)`, no `V(gate)`.

Primero, el mapeo ideal de los valores informados, antes de considerar que el
shunt modifica la corriente, es:

```text
Envolvente informada: ID = 0.25–0.40 A
VSENSE = ID · 1 Ω = 0.25–0.40 V
VADC = 0.5 · VSENSE = 0.125–0.200 V
PSHUNT = ID² · 1 Ω = 62.5–160 mW
```

Para un ADC ideal de 12 bits y 3.3 V, ese mapeo ideal representa
aproximadamente 155–248 cuentas. No son todavía los valores del circuito con
el shunt insertado. La entrada está muy por debajo de 3.3 V, pero usa poco rango.
Reducir la
atenuación puede acercarla a escala completa; obtener ganancia mayor que uno
requiere un amplificador. Ante fallas reales se agregan limitación de corriente
y clamps compatibles con el ADC.

El shunt produce caída y modifica el punto de operación. Con el modelo
resistivo equivalente, LTspice entrega:

| Caso | `ID_ON` | `VSENSE_ON` | `VADC_ON` | `VDS_ON` |
| --- | ---: | ---: | ---: | ---: |
| 20 Ω, sin carga | 236.693 mA | 236.774 mV | 118.387 mV | 29.36 mV |
| 12.5 Ω, con carga | 366.948 mA | 367.021 mV | 183.510 mV | 46.13 mV |

El caso cargado reporta `VGS_ON=11.623 V`; el caso sin carga, 11.753 V.

El netlist también reporta `VADC_TRANSIENT_MAX`; es útil para detectar picos y
efectos del modelo, no para sustituir la medición del nivel estable. El filtro
opcional de 1 nF con `10k || 10k = 5k` tiene `fc≈31.8 kHz`.

## 7. Etapa 4 — BJT corregido y carga RC

Archivo: `semana4_04_conmutador_hard_sat.cir`.

Esta etapa repara la topología anterior. En SPICE los BJT deben llamarse `Q1`
y `Q2`; el prefijo `T` corresponde a una línea de transmisión. Q1 no puede
entregar corriente desde su colector: actúa como pull-down y **RPU=910 Ω**
alimenta la base de Q2.

```text
Entrada alta → Q1 ON  → Q2 OFF → C carga por RC+RSER
Entrada baja → Q1 OFF → Q2 ON  → C descarga por RSER y Q2
```

Se usan `RC=220 Ω`, `RSER=220 Ω` y `C=5 µF` para limitar el peor caso. `RSER`
es el resistor serie del capacitor; no es el motor de las etapas 1–3.

```text
IB2 ≈ (5−0.8)/910 ≈ 4.6 mA
IC2,estable ≈ (5−0.2)/220 ≈ 21.8 mA
IC2,pico ≈ 21.8 mA + (VC−0.2)/220 ≈ 43 mA
beta_forzado,pico ≈ 43/4.6 ≈ 9.4
tau_carga = (RC+RSER)C = 2.2 ms
tau_descarga ≈ RSER·C = 1.1 ms
```

La regla “10:1” es una heurística conservadora, no una garantía universal. Se
debe comprobar `VCE(sat)` para la pareja `IC/IB` del transistor real. Una
saturación más profunda reduce `VCE`, pero puede aumentar el tiempo de
almacenamiento al apagar.

Resultados del modelo genérico:

| Medida | Resultado |
| --- | ---: |
| `VC_CHARGED` | 4.905 V |
| `VC_DISCHARGED` | 52.51 mV |
| `VCE2_ON` | 50.62 mV |
| `IB2_ON` | 4.576 mA |
| `IC2_STEADY` | 22.515 mA |
| `IC2_PEAK` | 44.625 mA |

## 8. Comprobación y entrega

Para cada etapa entregue:

1. predicción escrita antes de simular;
2. captura de las formas de onda con ejes y unidades;
3. tabla `.meas` copiada del Error Log;
4. diferencia porcentual entre cálculo y simulación;
5. una limitación del modelo;
6. una decisión requerida antes de construir hardware.

Lista de comprobación:

- [ ] `VGS` se mide entre gate y source.
- [ ] El MOSFET ON se describe como región óhmica.
- [ ] El flyback está orientado ánodo a D, cátodo a +5 V.
- [ ] El divisor ADC se describe como atenuador.
- [ ] Q1/Q2 tienen prefijos SPICE correctos y Q2 recibe base desde RPU.
- [ ] Ningún límite absoluto se usa como condición normal de trabajo.

Si una etapa no coincide, deténgase allí: revise nodo, polaridad, ventana de
medida, unidad y alcance del modelo antes de agregar otro bloque.

Explicación conceptual complementaria:
`semana_4_teoria_mosfet_analogias.md`.
