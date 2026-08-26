# Actividades guiadas · Normas de los resistores

Curso: Fundamentos de Sistemas Electrónicos Analógicos · Ingeniería Aeroespacial.
Diseñado para que lo hagas **sin conocimientos previos**: cada actividad te dice
qué saber, qué hacer paso a paso, te muestra un ejemplo resuelto y te indica qué
buscar. Duración sugerida: 90 minutos.

## Cómo usar esta guía

1. **Lee** primero el recuadro "¿Qué necesitas saber?" de cada actividad.
2. **Sigue** el "Paso a paso".
3. **Revisa** el ejemplo resuelto para ver el método.
4. **Haz** tu tarea ("Tu turno").
5. Si te atoras, ve a **"Investiga"**: ahí está dónde buscar la respuesta.

Toda cantidad lleva su unidad (Ω, kΩ, mA, V, mW, ppm/°C).

## ¿Qué es un resistor y qué "normas" lo rigen?

Un resistor se opone al paso de la corriente. Se elige/verifica según 4 normas:

| Norma | Qué mide | Unidad |
| --- | --- | --- |
| **Valor** (series E) | su resistencia | Ω (ohm) |
| **Tolerancia** | el error máximo del valor | % |
| **TCR** | cómo cambia con la temperatura | ppm/°C |
| **Potencia / derating** | cuánto calor puede disipar con seguridad | W |

> En ingeniería aeroespacial un resistor debe cumplir las 4: el valor *y* el
> margen térmico *y* la deriva térmica *y* la potencia. Por eso "funciona en el
> papel" no basta (ver NASA EEE-INST-002 y ECSS-Q-ST-30-11C).

---

## Actividad 1 · Código de colores

**¿Qué necesitas saber?** El valor se lee con 4, 5 o 6 **bandas de color**
(código IEC 60062). De izquierda a derecha:

- 4 bandas: dígito, dígito, multiplicador, tolerancia.
- 5 bandas: dígito, dígito, dígito, multiplicador, tolerancia.
- 6 bandas: igual que 5 + una banda final de **TCR**.

| Color | Dígito | Multiplicador | Tolerancia |
| --- | --- | --- | --- |
| Negro | 0 | ×1 | — |
| Marrón | 1 | ×10 | ±1 % |
| Rojo | 2 | ×100 | ±2 % |
| Naranja | 3 | ×1k | — |
| Amarillo | 4 | ×10k | — |
| Verde | 5 | ×100k | ±0.5 % |
| Azul | 6 | ×1M | ±0.25 % |
| Violeta | 7 | — | ±0.1 % |
| Gris | 8 | — | ±0.05 % |
| Blanco | 9 | — | — |
| Dorado | — | ×0.1 | **±5 %** |
| Plata | — | ×0.01 | ±10 % |

**Paso a paso:**
1. Cuenta las bandas.
2. Anota el color de cada banda de izquierda a derecha.
3. Escribe los dígitos y el multiplicador de la tabla.
4. Combina: `dígitos × multiplicador`.
5. Lee la tolerancia (última banda).

**Ejemplo resuelto:** `Marrón – Negro – Rojo – Dorado`
- Dígitos: 1 y 0 → "10". Multiplicador rojo = ×100. Tolerancia dorado = ±5 %.
- Valor = 10 × 100 = **1000 Ω = 1 kΩ ±5 %**.

**Tu turno** (4 bandas, salvo el 4º que tiene 5):

1. Marrón – Negro – Rojo – Dorado → ______ Ω ±5 %
2. Rojo – Violeta – Marrón – Dorado → ______ Ω ±5 %
3. Naranja – Naranja – Naranja – Dorado → ______ kΩ ±5 %
4. Marrón – Negro – Negro – Marrón – Marrón → ______ kΩ ±1 %

**Investiga:**
- Busca "código de colores de resistencias" o usa una calculadora online
  ("resistor color code calculator").
- Si tienes resistores, mide el valor real con el multímetro y compáralo con el
  rango de la tolerancia (ver `docs/labs/semana_1_laboratorio.md`, Procedimiento A).

---

## Actividad 2 · Series normalizadas (IEC 60063)

**¿Qué necesitas saber?** No existe "cualquier valor". Los fabricantes producen
**series** de valores: **E12** (±10 %), **E24** (±5 %), **E96** (±1 %). Se elige
el valor de la serie **más cercano** al que calculaste.

**Paso a paso:**
1. Escribe el valor que necesitas (`R_calc`).
2. Mira la tabla **E24** y toma el más cercano → `R_elegido`.
3. (Si necesitas menos de 1 % de error, usa la tabla **E96**.)
4. Calcula el error: `error % = 100 · |R_elegido − R_calc| / R_calc`.

**Ejemplo resuelto:** necesitas `R = 2.37 kΩ`.
- E24 (valores con 2 cifras significativas): 2.2 kΩ o 2.4 kΩ. El más cercano es
  **2.4 kΩ** → `error = 100·|2.4 − 2.37|/2.37 = 1.27 %`.
- E96 (3 cifras): **2.37 kΩ** existe → `error = 0 %`.

**Tu turno:** necesitas `R = 3.10 kΩ`.
- Valor E24 más cercano → ______ kΩ → error ______ %
- ¿Existe en E96 (3.09 kΩ)? → ______ → error ______ %

**Investiga:**
- Busca "tabla de valores normalizados E24 E96" / "preferred resistor values".
- ¿Por qué no hay un valor *exacto*? (Pista: fabricar todos los valores
  intermedios no es viable; las tolerancias se traslapan.) Responde con una frase.

---

## Actividad 3 · Tolerancia y peor caso

**¿Qué necesitas saber?** Un resistor de `R` con tolerancia `t %` puede valer
entre `R·(1 − t/100)` y `R·(1 + t/100)`. Por eso medimos el **rango**.

**Paso a paso:**
1. `R_min = R · (1 − t/100)`.
2. `R_max = R · (1 + t/100)`.
3. Escribe el rango `R_min a R_max`.
4. Para el divisor, repite con ambos resistores y busca el **peor caso**.

**Ejemplo resuelto:** `1 kΩ ± 5 %`
- `R_min = 1000·0.95 = 950 Ω`; `R_max = 1000·1.05 = 1050 Ω`. → rango **950 a 1050 Ω**.

**Tu turno:**
1. `1 kΩ ± 1 %` → ______ a ______ Ω
2. `4.7 kΩ ± 1 %` → ______ a ______ Ω
3. Divisor 1:1 (`R1=R2=1kΩ`, `±1 %`, `Vin=5 V`): calcula el **valor mínimo y máximo**
   de `Vout` y su desviación respecto de 2.5 V. ¿Cambia si ambos resistores se
   desvían *en el mismo sentido*? ¿Y en sentidos opuestos?

**Investiga:**
- Busca "peor caso de tolerancia en divisor de voltaje" (o repasa la S2.2).
- Conclusión de una línea: ¿qué ventaja tiene que el divisor dependa de la
  *razón* y no del valor absoluto?

---

## Actividad 4 · TCR y deriva térmica

**¿Qué necesitas saber?** El valor cambia con la temperatura. El **TCR** se da en
**ppm/°C** (partes por millón por grado). La variación es:

```
ΔR = R_nominal · TCR · ΔT        error % = 100 · ΔR / R_nominal
```

(1 ppm = 1×10⁻⁶).

**Paso a paso:**
1. Pasa el TCR a decimal: `TCR/1e6`.
2. Multiplica: `ΔR = R · TCR/1e6 · ΔT`.
3. Divide entre R para el error %.

**Ejemplo resuelto:** `R = 10 kΩ`, `TCR = 100 ppm/°C`, `ΔT = 50 °C`.
- `ΔR = 10000 · 100e-6 · 50 = 50 Ω`.
- `error % = 50/10000 = 0.5 %`.

**Tu turno** (usa los mismos datos del ejemplo: `R = 10 kΩ`, `ΔT = 50 °C`):
1. Con `TCR = 25 ppm/°C` (película metálica) → `ΔR = ______ Ω`,
   `error = ______ %`.
2. ¿Por qué en un divisor de referencia de ADC se exige TCR bajo? Responde con
   una frase (piensa en cuánto se desplaza `Vout` si R cambia 0.5 %).

**Investiga:**
- Busca "coeficiente de temperatura de temperatura TCR ppm/°C resistencias".
- Busca el TCR típico de un resistor de **carbón** (~100–200 ppm/°C) vs
  **película metálica** (≤50 ppm/°C) en
  `docs/presentations/semana_1_diapositivas.md`.

---

## Actividad 5 · Potencia nominal y derating

**¿Qué necesitas saber?** El resistor disipa calor: `P = V²/R` (o `P = I²·R`).
Su potencia nominal (1/8, 1/4, 1/2 W) es la máxima a temperatura ambiente. En el
**vacío** no hay convección, por eso las normas aplican **derating** (~50 %):

```
P_derated = 0.5 · P_nominal       →  un 1/4 W permite 0.125 W seguros
```

**Paso a paso:**
1. Calcula `P = V²/R` (en vatios; conviértelo a mW).
2. `P_derated = 0.5 · P_nominal`.
3. Si `P > P_derated` → **no cumple**: sube la potencia nominal.

**Ejemplo resuelto:** `1 kΩ` de `1/4 W` a **12 V**.
- `P = 12²/1000 = 0.144 W = 144 mW`.
- `P_derated = 0.5·0.25 = 0.125 W = 125 mW`.
- `144 > 125` → **no cumple**. Elegir `1/2 W` (límite 250 mW).

**Tu turno:** `2.2 kΩ` de `1/4 W` a **12 V**.
- `P = ______ mW`; `P_derated = ______ mW`; ¿cumple? → ______
- Si no cumple, ¿qué potencia nominal elegirías?

**Investiga:**
- Lee la lección **NASA LLIS-0676** (enlace en `docs/resources/recursos_didacticos.md`)
  y busca la **tabla de derating de resistores** (sección de componentes pasivos).
- En **EEE-INST-002** y **ECSS-Q-ST-30-11C**, consulta la **tabla/anexo de derating
  por familia de componentes** y la fila de **resistores** (50 % de potencia). No
  necesitas leer el documento completo.
- ¿Por qué el vacío empeora la disipación? (Pista: no hay aire para convección.)

---

## Actividad 6 · Selección integral de un resistor

**¿Qué necesitas saber?** Es como un "examen final": elige un resistor que cumpla
las **4 normas** a la vez. Diseñaremos un divisor que entregue `Vout ≈ 2.5 V`
desde `Vin = 12 V` para una referencia de un ADC (la carga es despreciable).

**Paso a paso (llena la ficha):**
1. **Valor:** `Vout = Vin·R2/(R1+R2)`. Propor `R2/(R1+R2) = 2.5/12 = 0.208`.
   Prueba `R1 = 4.7 kΩ` → `R2 ≈ 0.263·R1 ≈ 1.24 kΩ` (E96). Anota `R1` y `R2`.
2. **Tolerancia:** para que `Vout` se mantenga en ±0.5 %, ¿qué tolerancia usas?
   (Compara con la Actividad 3.)
3. **TCR:** con `ΔT = 40 °C`, ¿qué TCR mantiene `ΔR` bajo 0.1 %?
4. **Potencia:** calcula `P = V²/R` sobre la **mayor** resistencia y verifica
   que `P ≤ 0.5·P_nom`.

**Ficha:**

| Parámetro | Qué pedir | Tu decisión |
| --- | --- | --- |
| Valor (serie E) | `Vout ≈ 2.5 V` | R1 = ____, R2 = ____ |
| Tolerancia | `Vout` en ±0.5 % | ______ % |
| TCR | deriva < 0.1 % en 40 °C | ______ ppm/°C |
| Potencia | `P ≤ 0.5·P_nom` | ______ W |

**Justificación (por escrito) — vale el 10 %:** junto a la ficha, redacta **1–2
líneas por parámetro** explicando *por qué* elegiste ese valor, tolerancia, TCR y
potencia (p. ej. "elijo ±0.5 % porque..."). La tabla sin razonamiento **no** suma
los puntos de la justificación.

**Investiga / explica:** ¿Qué pasa si subes la potencia nominal (más robusto pero
más caro y más grande)? Responde con una frase.

---

## Cómo y cuándo entregar

- **Formato:** un solo **reporte PDF** con: (1) tus respuestas y cálculos (puedes
  escanear tu cuaderno), (2) capturas de las **simulaciones** que uses
  (PhET / Falstad / LTspice), y (3) la **ficha + justificación** de la Actividad 6.
- **Nombre del archivo:** `Apellido_Nombre_actividad_resistores.pdf`.
- **Plataforma y fecha límite:** subir a **aula virtual (dónde indique el
  docente)** antes del **`fecha límite`** a las **`hora`**.

---

## Plantilla de tabla (entregable)

| Elemento | Valor nom. | Tolerancia | Rango | T. medido | Error % | Ficha (tol/TCR/Pot) | Apto |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| R (act. 1) | | | | | | | |
| R_divisor | | | | | | | |

## Rúbrica

| Criterio | Peso |
| --- | ---: |
| Código de colores | 15 % |
| Serie E y valor normalizado | 20 % |
| Tolerancia y peor caso | 20 % |
| TCR y deriva | 15 % |
| Potencia y derating | 20 % |
| Ficha de selección justificada | 10 % |

## Recursos y referencias

- Código de colores y series E: **IEC 60062** y **IEC 60063** (tablas arriba).
- Derating: **NASA LLIS-0676**, **ECSS-Q-ST-30-11C**; selección de partes por
  **NASA EEE-INST-002** (enlaces en `docs/resources/recursos_didacticos.md`).
- Valores, tolerancia y TCR (definiciones y tablas) en
  `docs/presentations/semana_1_diapositivas.md` (Clase 2).
- Simulaciones de apoyo: `Simulaciones Ltspice/sim/semana2_02_divisor_tolerancia.cir`
  (tolerancia) y `semana1_04_potencia_derating.cir` (derating).
- Laboratorio de medición: `docs/labs/semana_1_laboratorio.md` (Procedimiento A).
