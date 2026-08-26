# Respuestas · Normas de los resistores (hoja del docente)

Curso: Fundamentos de Sistemas Electrónicos Analógicos · Ingeniería Aeroespacial.
Documento de referencia para calificar la actividad
`docs/labs/semana_1_actividades_normas_resistores.md`.
**No entregar a los estudiantes.**

---

## Actividad 1 · Código de colores

| # | Bandas | Valor | Control |
| --- | --- | --- | --- |
| 1 | Marrón–Negro–Rojo–Dorado | **1000 Ω = 1 kΩ ±5 %** | 10 × 100 |
| 2 | Rojo–Violeta–Marrón–Dorado | **270 Ω ±5 %** | 27 × 10 |
| 3 | Naranja–Naranja–Naranja–Dorado | **33 kΩ ±5 %** | 33 × 1k |
| 4 | Marrón–Negro–Negro–Marrón–Marrón | **1000 Ω = 1.00 kΩ ±1 %** | 100 × 10 |

> **Qué revisar:** que el alumno lea de izquierda a derecha y separe bien los
> dígitos del multiplicador. El 4º es de 5 bandas (3 dígitos) con tolerancia ±1 %.

---

## Actividad 2 · Series normalizadas

`R_calc = 3.10 kΩ`

- **E24** más cercano: **3.0 kΩ** → `error = 100·|3.0 − 3.1|/3.1 = 3.23 %`.
- **E96:** ¿existe `3.09 kΩ`? **Sí** → `error = 100·|3.09 − 3.10|/3.10 = 0.32 %`.

> **Qué revisar:** que elijan el E24 correcto (3.0, no 3.3) y que calculen el error
> con el valor *calculado* en el denominador. Nota pedagógica: la serie E96
> (3 cifras) permite errores menores; la E24 es de 2 cifras.

---

## Actividad 3 · Tolerancia y peor caso

1. `1 kΩ ± 1 %` → **990 a 1010 Ω**.
2. `4.7 kΩ ± 1 %` → **4653 a 4747 Ω** (4.7×0.99 / 4.7×1.01).
3. Divisor 1:1 (`R1=R2=1kΩ`, `±1 %`, `Vin=5 V`):
   - Máximo: `R1 = 990`, `R2 = 1010` → `Vout = 5·1010/2000 = 2.525 V`.
   - Mínimo: `R1 = 1010`, `R2 = 990` → `Vout = 5·990/2000 = 2.475 V`.
   - Rango: **2.475 a 2.525 V** (desviación ±0.025 V = ±1 % de 2.5 V).
   - **Ambos en el mismo sentido** (R1 y R2 suben o bajan juntos) → la *razón*
     `R2/(R1+R2)` se conserva → `Vout = 2.5 V` (no cambia; solo cambia la corriente/potencia).
   - **Sentidos opuestos** → error máximo: `Vout` se desplaza a ±1 %.

> **Qué revisar** (el punto donde suelen dudar): el **peor caso** se da cuando un
> resistor está en su límite inferior y el otro en el superior. Verifica que
> identifiquen el cruce de variables.

---

## Actividad 4 · TCR y deriva térmica

Con `R = 10 kΩ`, `ΔT = 50 °C`:

- `TCR = 100 ppm/°C` (ejemplo): `ΔR = 10000·100e-6·50 = 50 Ω` → **0.5 %**.
- `TCR = 25 ppm/°C` (película metálica): `ΔR = 10000·25e-6·50 = 12.5 Ω` → **0.125 %**.

> **Qué revisar:** que el alumno convierta ppm a decimal (`/1e6`) y use `ΔR = R·TCR·ΔT`.
> El 25 ppm/°C reduce el error 4× respecto del de carbón. En un divisor de referencia
> de ADC, un 0.5 % de deriva desplaza la salida fuera del rango de precisión.

---

## Actividad 5 · Potencia nominal y derating

Con `2.2 kΩ`, `1/4 W`, `Vin = 12 V`:

- `P = 12²/2200 = 0.0655 W = 65.5 mW`.
- `P_derated = 0.5·0.25 = 125 mW`.
- `65.5 < 125` → **SÍ cumple**. (Un `1/4 W` basta; si no, subir a `1/2 W`.)

> **Qué revisar:** que comparen `P` contra `P_derated` (no contra `P_nominal`).
> En el ejemplo guiado (`1 kΩ` a 12 V) el resultado es `144 mW > 125 mW` → no cumple;
> en éste sí cumple, para que no todos los casos sean iguales.

---

## Actividad 6 · Selección integral (ficha resuelta)

Divisor a `Vout ≈ 2.5 V` desde `Vin = 12 V`.

| Parámetro | Qué pedir | Respuesta (ejemplo) |
| --- | --- | --- |
| Valor (serie E) | `Vout ≈ 2.5 V` | **R1 = 4.7 kΩ, R2 = 1.24 kΩ** (E96; `Vout = 12·1.24/5.94 = 2.505 V`) |
| Tolerancia | `Vout` en ±0.5 % | **±0.5 %** (mínimo); recomendado **±0.1 %** (película metálica) |
| TCR | deriva < 0.1 % en 40 °C | **≤ 25 ppm/°C** (`ΔR/R = TCR·40 < 0.001`) |
| Potencia | `P ≤ 0.5·P_nom` | **1/8 W** (peor caso `P_R1 ≈ 19 mW`; con derating `≥ 38 mW`) |

Cálculos de potencia: `I = 12/(4700+1240) = 2.02 mA`; `P_R1 = I²·4700 ≈ 19.2 mW`,
`P_R2 = I²·1240 ≈ 5.1 mW`. Peor caso R1 = 19.2 mW → `P_nom ≥ 2·19.2 = 38.4 mW`.

> **Ejemplo de justificación** (lo que se espera del alumno):
> *"Elijo resistores E96 (±1 %) y, para garantizar el ±0.5 % de la referencia,
> uso la versión ±0.1 % de película metálica. Con TCR ≤ 25 ppm/°C la deriva a 40 °C
> queda por debajo del 0.1 %. El peor caso de potencia (R1 ≈ 19 mW) con derating del
> 50 % exige ≥ 38 mW, por eso elijo 1/8 W."*

---

## Pares / criterios al calificar

- **Código de colores** (15 %): lectura correcta y unidades.
- **Serie E** (20 %): valor normalizado más cercano + error %.
- **Tolerancia/peor caso** (20 %): rango y deducción del cruce de peor caso.
- **TCR** (15 %): conversión y efecto en la salida.
- **Potencia/derating** (20 %): comparar contra `0.5·P_nom`.
- **Ficha justificada** (10 %): que explique el *porqué* de cada decisión, no solo la tabla.

## Falta / errores frecuentes

- Confundir `±1 %` (banda marrón) con `±5 %` (dorado) en el código de colores.
- Calcular `error %` con el valor *elegido* en el denominador (debe ser el *calculado*).
- No anotar unidades (Ω, kΩ, mW, ppm/°C).
- En el peor caso del divisor, usar ambos resistores en el *mismo* extremo (error incorrecto).
- No distinguir `P_nominal` de `P_derated` (olvidar el 50 %).
