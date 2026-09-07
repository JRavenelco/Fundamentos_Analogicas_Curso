# Semana 4: conmutador de potencia MOSFET lado bajo

Práctica con tres simulaciones independientes. La secuencia permite montar,
medir y corregir un bloque antes de agregar el siguiente. Cada etapa usa un
**IRF640N (Infineon)** como MOSFET de conmutación, excitado con un **driver de
12 V** (el IRF640N **no es de nivel lógico**: `VGS(th)=2–4 V`, típico 3 V, y
necesita `VGS ≥ 10 V` para saturar; un GPIO de 3.3 V no basta, se requieren 12 V
en el gate). La salida de drenaje está **invertida** respecto al PWM (igual que
el TBJ en la semana 3: conmutador de lado bajo).

## Corrección de topología

```text
                  +12 V
                    |
                 RL=100
                    |
      GPIO --driver 12 V-- RG=100 -- G|   D
                            IRF640N (lado bajo)
                                      S |
                                        GND
```

- El PMOS quedaría al revés del lado alto; aquí el **NMOS de lado bajo** es la
  conexión correcta con la fuente (S) a GND.
- Verificar el **marcado real** del MOSFET y su pinout en la hoja de datos antes
  de armar; en las simulaciones se usa un modelo de primer orden del IRF640N
  (`VTO=3`, `KP=1.0` → `RDS(on) ≈ 0.15 Ω`).
- **Datos clave del IRF640N (Infineon):** `VDS=200 V`, `ID=18 A`,
  `RDS(on) ≤ 0.22 Ω` (tip. 0.15 Ω @ VGS=10 V), `Qg=67 nC`, `Ciss=1300 pF`,
  `VGS(th)=2–4 V`.

## Etapa 1 — PWM (12 V), compuerta y conmutador resistivo

Archivo: `semana4_01_pwm_gate_mosfet.cir`.

Montar driver de 12 V, `RG=100`, el IRF640N y `RL=100` de +12 V al drenaje.
Graficar `V(gate)` y `V(drain)`.

Datos del generador:

```text
PULSE(0 12 0 1n 1n 5u 10u)  ->  f = 100 kHz, D = 50 %
```

Predicción con el modelo (`Vth=3 V`, `KP=1.0`, `VGS=12 V`):

```text
ID(sat) = 0.5*KP*(VGS - Vth)^2 = 0.5*1.0*(12 - 3)^2 = 40 A  (>> 120 mA)
ID(carga) = (12 - VDS) / 100 ≈ 120 mA
```

Como `ID(sat) >> ID(carga)`, el MOSFET entra en **triodo** (canal resistivo):

```text
VDS_ON ≈ ID * RDS(on) ≈ 0.12 A * 0.15 Ω ≈ 18 mV  (~0.02 V)
VDS_OFF ≈ 12 V (corte, sin corriente)
```

Resultados esperados en el log (`View > SPICE Error Log`):

| Medida | Valor esperado |
| --- | ---: |
| `VGS_ON` | ~12 V |
| `VDS_ON_MIN` | ~0.02 V |
| `VDS_OFF_MAX` | ~12 V |
| `ID_ON` | ~120 mA |

Comprobación práctica: medir primero `+12 V`, luego el PWM del driver y por
último el drenaje. La señal está invertida.

## Etapa 2 — Carga inductiva y diodo de libre circulación

Archivo: `semana4_02_carga_inductiva_flyback.cir`.

Agregar `L1=100 mH` en serie con `RL1=100` entre +12 V y el drenaje, y el diodo
`D1` **en paralelo con la carga** (ánodo al drenaje, cátodo a +12 V).

```text
PULSE(0 3.3 0 1n 1n 5m 10m)  ->  f = 100 Hz, D = 50 %
tau = L/RL1 = 100 mH / 100 = 1 ms  (menor que el intervalo ON de 5 ms)
```

Esperado con `D1` presente:

```text
VDS_MAX ≈ VCC + VD ≈ 12.7 V  (fijado por el diodo)
ID_ON ≈ 120 mA  (en estado estable)
ID_OFF_TAIL = corriente de descarga por D1 (decaen con tau = L/RL1)
```

Para ver el **pico destructivo sin protección**: comentar `D1` y descomentar la
línea `;D1 drain vcc D4148` (el `VDS_MAX` crece varios voltios por encima de
+12 V). Es la justificación de usar siempre un diodo de libre circulación con
cargas inductivas (motores, relés, bobinas de actuador).

## Etapa 3 — Sensor de corriente con shunt y ADC protegido

Archivo: `semana4_03_medicion_adc.cir`.

Poner `RSENSE=1` en serie con la **fuente** del MOSFET, y un divisor
`RF=10k / R2=10k` hacia el ADC:

```text
VSENSE = ID * RSENSE ≈ 120 mA * 1 = 120 mV
VADC = 0.5 * VSENSE ≈ 60 mV   (siempre < 3.3 V)
```

Esperado en el log: `VSENSE_ON ≈ 120 mV`, `VADC_ON ≈ 60 mV`, `VADC_MAX ≈ 60 mV`.

Notas de diseño:
- El shunt colocado en la **fuente** (no en el drenaje) tiene masa común con el ADC.
- Con `VADC_MAX` muy por debajo de 3.3 V, se puede aumentar la ganancia (p. ej.
  `RF/R2` mayor o un amplificador) sin riesgo de exceder el rango del ADC.
- El `C1` comentado (1 nF) es un filtro anti-ruido opcional.

## Directivas de LTspice incluidas

- `.param`: valores de la etapa (alimentación, carga, gate, filtro).
- `.tran`: formas de onda en el tiempo con `.meas` en el Error Log.
- Comentadas: variantes para el pico sin protección (semana 4.2) y filtro `C1`
  (semana 4.3). LTspice ejecuta solo un análisis por corrida.

## Hoja de comprobación práctica

Medir con GND común y registrar: `+12 V`, PWM, `V(drain)` ON/OFF, y (etapa 3)
`V(sense)` y `V(adc)`.

| Medida | VCC | VGS | VDS ON | VDS OFF | ID | V_sense | V_adc | Simulación |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Etapa 1 | 12 V | 3.3 V | ~0.1 V | ~12 V | 120 mA |  |  | 0.1 V / 12 V / 120 mA |
| Etapa 2 | 12 V | 3.3 V | ~0.1 V | 12.7 V | 120 mA |  |  | 12.7 V / 120 mA |
| Etapa 3 | 12 V | 3.3 V | ~0.1 V | ~12 V | 120 mA | 120 mV | 60 mV | 120 mV / 60 mV |

## Criterios para considerar correcta cada etapa

1. La etapa 1 conmuta e invierte sin calentar el MOSFET (ON ≈ 0.1 V).
2. La etapa 2 mantiene el pico en ~12.7 V (diodo de libre circulación).
3. La etapa 3 entrega `V_adc ≈ 60 mV` estable, siempre menor que 3.3 V.

Si cualquiera falla, detenerse en esa etapa; no avanzar agregando bloques.

## Resultados de referencia

Las simulaciones se ejecutan con LTspice XVII. Los valores esperados se
obtienen del modelo de primer orden (ver arriba) y se confirman con `.meas`;
si no coinciden, revisar: marcado/pinout del MOSFET, orientación de `D1`
(ánodo al drenaje), `+12 V` real y masa común.

## Diseño de clase: conmutador de saturación dura con carga RC

Archivo: `semana4_04_conmutador_hard_sat.cir`. Es el diseño alrededor del cual
gira la clase (`clase_4_conmutador_hard_sat.pdf`): driver PULSE 5 V → 2k → T1
(BC548, pre-driver) → 2k → T2 (BC548, **saturación dura**), con Rc=100 Ω a 5 V
y una carga RC (100 Ω + 5 µF) desde el colector (N1) a GND.

```text
Regla 10:1:  IC,max = 5 V/100 Ω = 50 mA;  IB2,sat = 50 mA/10 = 5 mA
tau = 100 Ω*5 µF = 0.5 ms;  pico i_carga ≈ (5-0.2)/102.5 ≈ 47 mA
```

Esperado en el log: `IC2_MAX ≈ 50 mA`, `IB2_AVG ≈ 5 mA`, `VC_FINAL ≈ 5 V`,
`IC2_PEAK_MAX ≈ 47 mA`. Con el modelo de BC548 real (BF=300) la saturación es
profunda y los valores coinciden con la regla 10:1.

## Conexión con la clase de MOSFET

El diseño usa BJT en saturación dura; en la práctica se puede sustituir T2 por
un **NMOS de nivel lógico** (misma función, sin consumir corriente de base),
que es el tema de la clase teórica `clase_4_mosfet.pdf` y de las etapas 1-3 de
esta práctica.
