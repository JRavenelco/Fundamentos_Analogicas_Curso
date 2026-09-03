# Semana 3: sensor capacitivo con conmutador TBJ y entrada ADC

Esta práctica divide el circuito real en cuatro simulaciones independientes. La
secuencia permite montar, medir y corregir un bloque antes de agregar el
siguiente. Cada etapa tiene un `.asc` autónomo para abrir con LTspice y un `.cir`
equivalente como netlist legible. El archivo original `Practica_transistor.asc`
se conserva sin cambios como referencia del prototipo.

## Corrección de topología

La etapa se analiza como un **conmutador NPN de lado bajo**:

```text
                    +5 V
                      |
                    R2=10k
                      |
            colector--+---- sensor ---- GND
                      |
                    Q1 NPN
GP16 PWM -- R3=2.2k --B
                    E |
                      |
                     GND
```

Esto es coherente con un emisor conectado a GND. Un BC557B es PNP y no
corresponde a esta conexión. Antes de armar, leer el marcado real del transistor
y comprobar su pinout en su hoja de datos; para estas simulaciones se usa un NPN
genérico equivalente a un BC547B/2N3904 como interruptor.

El sensor no es solamente una resistencia en serie con un capacitor. Un modelo
inicial más útil es:

```text
terminal A --- Cs --- RESR --- terminal B
           |               |
           +---- RLEAK ----+
```

- `Cs`: capacitancia entre las placas; cambia con el dieléctrico y la humedad.
- `RESR`: pérdida serie de placas, terminales y cables.
- `RLEAK`: fuga en paralelo; suele disminuir cuando aparece conductividad por
  agua o contaminación.

Los valores de `Cs` y `RLEAK` incluidos son hipótesis para iniciar el ajuste, no
una caracterización del sensor. Deben sustituirse por valores obtenidos de tus
mediciones.

## Etapa 1 — PWM y transistor

Archivos: `semana3_04_sensor_etapa1_conmutador.asc` y su netlist `.cir`.

Montar solamente el GPIO, la resistencia de base, el NPN y el resistor de
colector. Graficar `V(gpio)`, `V(base)` y `V(colector)`.

Datos del generador:

```text
PULSE(0 3.3 0 1n 1n 1u 2u)
f = 1 / 2 us = 500 kHz
D = 1 us / 2 us = 50 %
```

Predicción de corriente de base durante el nivel alto:

```text
IB ~= (3.3 - 0.7) / 2.2k = 1.18 mA
```

Con `R2=10k` y `VCC=5 V`, la corriente de colector queda limitada cerca de:

```text
IC(sat) ~= (5 - 0.2) / 10k = 0.48 mA
```

Por eso la excitación de base es suficiente para saturar al transistor. Cuando
el GPIO está alto, el colector debe quedar cerca de 0.1–0.2 V; cuando el GPIO
está bajo, debe subir cerca de 5 V. La señal está invertida.

Comprobación práctica: medir primero `VCC`, luego el PWM en GP16 y por último el
colector. No conectar todavía ni el sensor ni el Pico ADC.

## Etapa 2 — Sensor equivalente

Archivos: `semana3_05_sensor_etapa2_capacitivo.asc` y su netlist `.cir`.

Agregar el sensor desde colector a GND. La directiva

```text
.step param HUM list 0 1 2 3
```

genera cuatro estados. `HUM=0` representa seco y `HUM=3`, mojado. Graficar
`V(colector)` y leer `VC_PK` en **View > SPICE Error Log**.

La reactancia ideal a 500 kHz es:

| Estado | Cs inicial | Xc = 1/(2 pi f C) |
| --- | ---: | ---: |
| seco | 15 pF | 21.22 kohm |
| ligeramente húmedo | 68 pF | 4.68 kohm |
| húmedo | 120 pF | 2.65 kohm |
| mojado | 180 pF | 1.77 kohm |

Al aumentar `Cs`, el nodo de colector tarda más en cargarse durante el intervalo
de 1 us en que Q1 está apagado. Su pico disminuye, que es el comportamiento
observado en el prototipo.

Para estimar la capacitancia real, medir el pico del colector y ajustar `Cs` en
la tabla `CS=table(...)` hasta que simulación y práctica coincidan. Después
ajustar `RLEAK` usando el decaimiento o el valor en estado estable.

## Etapa 3 — Diodo y detector de envolvente

Archivos: `semana3_06_sensor_etapa3_rectificador.asc` y su netlist `.cir`.

Agregar D1, R1 y C1. R1 y C1 están **en paralelo** desde `ADC_RAW` a GND:

```text
colector --|>|-- ADC_RAW
                   |--- R1=1Meg --- GND
                   +--- C1=1uF ---- GND
```

D1 carga C1 hacia los picos positivos. R1 proporciona un camino de descarga y
evita que el nodo quede flotante. La constante de descarga ideal es:

```text
tau_descarga = R1*C1 = 1Meg*1uF = 1 s
```

La carga inicial puede ser más rápida porque ocurre a través de D1 y R2. En el
prototipo se midieron `5.000 V` de alimentación y `4.493 V` en `ADC_RAW` seco;
la caída efectiva observada es:

```text
VD1 ~= 5.000 - 4.493 = 0.507 V
```

**No conectar este nodo directamente a GP26:** puede llegar a unos 4.5 V. En
esta etapa sólo se mide con multímetro u osciloscopio.

Para que la simulación con cuatro estados no tenga que resolver decenas de miles
de ciclos de 500 kHz durante varios segundos, el archivo usa `CFILT_SIM=10 nF`.
Así, las constantes de tiempo del filtro aparecen 100 veces más rápidas. La
forma y el valor final se conservan como referencia, pero el rizado visible será
mayor. En el circuito físico se mantiene `C1=1 uF`; para una corrida exacta se
puede cambiar `CFILT_SIM` a `1u` y ampliar el tiempo de `.tran`.

## Etapa 4 — Divisor, filtro y ADC protegido

Archivos: `semana3_07_sensor_etapa4_adc_protegido.asc` y su netlist `.cir`.

Agregar R5 de 680 kohm entre la salida del diodo y GP26. R1 y C1 permanecen en
paralelo, pero ahora cuelgan del nodo protegido:

```text
ADC_RAW -- R5=680k --+-- GP26 / ADC0
                     |--- R1=1Meg --- GND
                     +--- C1=1uF ---- GND
```

En corriente continua, C1 queda abierto y R5 con R1 forman el divisor:

```text
VADC = VRAW * 1Meg/(680k + 1Meg)
VADC = 0.595238 * VRAW
```

Resultados teóricos:

| Caso | VRAW | VADC ideal |
| --- | ---: | ---: |
| seco medido | 4.493 V | 2.674 V |
| máximo supuesto | 5.000 V | 2.976 V |
| mojado anterior | 1.600 V | 0.952 V |

Se midieron `2.581 V` en GP26 después de instalar 680 kohm. La razón real es
`2.581/4.493 = 0.57445`, un `-3.49 %` respecto al divisor ideal. Es razonable
como primer resultado por tolerancia, carga del instrumento, caída dinámica del
diodo o porque ambas tensiones no se midieron exactamente en el mismo instante.
Para una comparación válida, medir `ADC_RAW` y `GP26` sin cambiar el estado del
sensor.

El equivalente de Thévenin visto por C1 es:

```text
Rth = 680k || 1Meg = 404.76 kohm
tau = Rth*C1 = 0.405 s
t95 ~= 3*tau = 1.21 s
```

Ese filtro reduce picos pero también retrasa la curva. Si se quiere más rapidez,
primero reducir C1 (por ejemplo a 100 nF), comprobar el ruido y recalibrar.

## Directivas de LTspice incluidas

- `.param`: define componentes y estados del sensor.
- `.step param HUM`: repite la simulación para cuatro niveles de humedad.
- `.op`: alternativa comentada que verifica el punto de operación DC del divisor
  final.
- `.dc VRAW 0 5 0.05`: alternativa comentada que barre la entrada y comprueba
  que la salida sea lineal.
- `.tran`: muestra las formas de onda en el tiempo.
- `.meas`: deja valores numéricos en **View > SPICE Error Log**.

LTspice ejecuta un solo tipo de análisis por corrida en estos archivos. La etapa
4 deja `.tran` activo. Para usar `.op` o `.dc`, comentar temporalmente `.tran` y
sus medidas, y descomentar sólo la alternativa elegida con sus `.meas`.

Para la etapa 4 existe una línea comentada que compara R5=470 kohm y 680 kohm.
Con 470 kohm el factor sería `1Meg/(470k+1Meg)=0.68027` y una entrada de 5 V
produciría 3.401 V, por lo que **no garantiza** quedar debajo de 3.3 V. Se deja
680 kohm como valor de montaje.

## Hoja de comprobación práctica

Medir con GND común y registrar ambos lados de R5 en el mismo estado.

| Estado | VCC | VGPIO alto | Vcolector pico | ADC_RAW | GP26 | Simulación GP26 | Error % |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| seco | 5.000 V |  |  | 4.493 V | 2.581 V | 2.674 V | -3.49 % |
| ligeramente húmedo |  |  |  |  |  |  |  |
| húmedo |  |  |  |  |  |  |  |
| mojado |  |  |  | 1.600 V* | por medir | 0.952 V* |  |

`*` El valor de 1.600 V fue observado antes de confirmar la nueva ubicación de
R5. Debe repetirse la medición mojada en los dos nodos.

## Criterios para considerar correcta cada etapa

1. La etapa 1 conmuta e invierte sin calentar Q1.
2. La etapa 2 reproduce la reducción del pico al aumentar la humedad.
3. La etapa 3 entrega una envolvente estable y confirma el máximo de `ADC_RAW`.
4. La etapa 4 nunca supera 3.3 V en GP26 y reproduce los estados seco/mojado.

Si cualquiera falla, detenerse en esa etapa; no avanzar agregando bloques.

## Resultados de referencia verificados en LTspice XVII

Las cuatro simulaciones `.asc` se ejecutaron sin error el 2026-09-03. Las
medidas automáticas dieron:

| Etapa | Medida | Resultado LTspice | Referencia teórica/práctica |
| --- | --- | ---: | ---: |
| 1 | corriente de base ON | 1.179 mA | 1.182 mA teórico |
| 1 | colector con Q1 ON | 0.023 V | cercano a saturación |
| 1 | colector con Q1 OFF | 5.000 V | 5.000 V teórico |
| 2 | pico colector HUM 0/1/2/3 | 5.048/3.816/2.835/2.176 V | debe disminuir al mojar |
| 3 | ADC_RAW medio HUM 0/1/2/3 | 4.185/3.014/2.151/1.561 V | seco medido 4.493 V; mojado ~1.600 V |
| 4 | GP26 seco, al final del transitorio | 2.659 V | 2.674 V DC ideal |
| 4 | GP26 mojado, al final del transitorio | 0.962 V | 0.952 V DC ideal |

El estado mojado del modelo ya coincide aproximadamente con la práctica. En
seco, `ADC_RAW` simulado queda 0.308 V por debajo de 4.493 V. Esa diferencia es
información útil: antes de cambiar `Cs`, conviene confirmar el resistor real de
colector, la orientación de D1, el tipo de Q1 y medir simultáneamente el pico de
colector y `ADC_RAW`. Con esos datos se ajustan `RCVAL`, el modelo del diodo y la
tabla `CS`, en ese orden.
