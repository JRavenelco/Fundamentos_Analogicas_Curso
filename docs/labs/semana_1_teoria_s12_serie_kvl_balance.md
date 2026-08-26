# S1.2 — Teoría: Red serie, KVL y balance de potencia

Curso: Fundamentos de Sistemas Electrónicos Analógicos · Ingeniería Aeroespacial.
Prepara la simulación `Simulaciones Ltspice/sim/semana1_02_kvl_serie.asc` y la
red física del laboratorio (R1 = 1 kΩ, R2 = 2.2 kΩ, R3 = 3.3 kΩ con Vin = 12 V).

**Método de trabajo:** predecir el signo y el orden de magnitud → calcular al
menos un caso a mano → ejecutar LTspice y consultar `View > SPICE Error Log` →
explicar cualquier diferencia.

## 1. ¿Qué es una conexión en serie?

Dos o más elementos están **en serie** cuando por ellos circula la **misma
corriente**: el terminal de salida de uno se conecta al terminal de entrada del
siguiente, sin que exista otra rama entre ellos.

Propiedades inmediatas:

- La corriente es **única** en toda la trayectoria: `I = I_R1 = I_R2 = I_R3`.
- La resistencia total es la suma de las resistencias:

```text
Rt = R1 + R2 + R3
```

- La tensión de la fuente se **reparte** entre los elementos en proporción a su
  resistencia.

## 2. Ley de tensiones de Kirchhoff (KVL)

Enunciado: la suma algebraica de las tensiones a lo largo de cualquier **malla
cerrada** es cero.

```text
Σ V (malla cerrada) = 0
```

Aplicado a la red serie con la fuente y las tres caídas:

```text
Vfuente − VR1 − VR2 − VR3 = 0        ⟹        Vfuente = VR1 + VR2 + VR3
```

El signo importa: se recorre la malla en un sentido fijo y se resta toda caída
que se encuentre en el sentido de la corriente. La KVL no es una aproximación:
es una consecuencia de que la tensión es una **diferencia de potencial** — al
regresar al nodo de partida, el potencial debe ser el mismo.

**Divisor de tensión (deducción útil).** Con `I = Vfuente / Rt`, la caída en la
resistencia k es:

```text
VRk = I · Rk = Vfuente · (Rk / Rt)
```

La fracción `Rk / Rt` dice qué parte de la tensión "se queda" en cada elemento.
El elemento de mayor resistencia recibe la mayor caída.

## 3. Convención pasiva de signos y balance de potencia

Para calcular potencias sin errores de signo se usa la **convención pasiva**:

- En un elemento **pasivo** (resistor), la corriente entra por el terminal de
  mayor potencial: `P = V · I > 0` → el elemento **absorbe** (disipa calor).
- En una **fuente**, la corriente sale por el terminal positivo: `P = V · I < 0`
  → la fuente **entrega** energía al circuito.

Conservación de la energía: la suma de todas las potencias del circuito es cero.

```text
Σ P = 0        ⟺        P_fuente (entregada) = P_R1 + P_R2 + P_R3
```

Este "balance de potencia" es la forma más directa de verificar que un cálculo
(o una simulación) es consistente: si la fuente entrega 22.15 mW y los
resistencias no absorben 22.15 mW, algo está mal — un valor, un signo o un
nodo.

> En LTspice, `I(V1)` reporta la corriente que **entra** al terminal positivo de
> la fuente. Para una fuente que entrega energía, `I(V1)` es **negativo**, y
> `V(bus) · I(V1)` también es negativo. Por eso en los `.meas` de la secuencia
> el balance se escribe como `P_absorbida + P_disipada ≈ 0` (residual del orden
> de 1e-9: ruido numérico, no error).

## 4. Ejemplo resuelto (los valores de la simulación)

Red: R1 = 1 kΩ, R2 = 2.2 kΩ, R3 = 3.3 kΩ, Vin = 12 V.

```text
Rt = 1k + 2.2k + 3.3k = 6.5 kΩ
I  = 12 V / 6.5 kΩ = 1.846 mA

VR1 = I · 1k  = 1.846 V     (15.4 % de Vin)
VR2 = I · 2.2k = 4.062 V    (33.8 % de Vin)
VR3 = I · 3.3k = 6.092 V    (50.8 % de Vin)
VR1 + VR2 + VR3 = 12.000 V  (confirma KVL)

P1 = I² · R1 = 3.41 mW
P2 = I² · R2 = 7.50 mW
P3 = I² · R3 = 11.25 mW
ΣP = 22.15 mW = 12 V · 1.846 mA   (balance de potencia)
```

**Margen de derating:** con resistores de 1/4 W y derating al 50 % el límite es
0.125 W = 125 mW. El peor caso (P3 = 11.25 mW) usa menos del 10 % del límite:
margen ≈ 11× → **aceptado con amplio margen**.

## 5. Verificación en LTspice

El archivo `semana1_02_kvl_serie.asc` ya mide corriente total, caídas por
resistencia y el error de KVL. Para cerrar el balance de potencia, agregar al
esquema (o al `.cir`):

```text
.meas op P_R1_mW PARAM I(R1)*I(R1)*1k*1e3
.meas op P_R2_mW PARAM I(R2)*I(R2)*2.2k*1e3
.meas op P_R3_mW PARAM I(R3)*I(R3)*3.3k*1e3
.meas op P_fuente_mW PARAM V(vin)*(-I(V1))*1e3
.meas op Balance_mW PARAM P_fuente_mW - (P_R1_mW + P_R2_mW + P_R3_mW)
```

Criterio de éxito:

- `KVL_error_uV` ≈ 0 (residual numérico).
- `Balance_mW` ≈ 0: la fuente entrega exactamente lo que disipan las tres
  resistencias.

## 6. Errores comunes

| Error | Consecuencia | Corrección |
| --- | --- | --- |
| Sumar caídas con signos arbitrarios | KVL no cierra | Fijar un sentido de recorrido y restar toda caída en ese sentido |
| Usar `P = V²/R` con la tensión total en cada resistor | Potencias 9× mayores | Cada resistor usa **su propia** caída de tensión |
| Confundir entrega y absorción | Balance con signo invertido | Convención pasiva: fuente entrega (P < 0), resistor absorbe (P > 0) |
| Esperar que el resistor de menor valor disipe más | Conclusión de diseño equivocada | En serie, `P ∝ R`: el de mayor valor disipa más (P3 > P2 > P1) |

## 7. Lectura aeroespacial

1. **Presupuesto de potencia del EPS.** La verificación `ΣP = 0` es la misma
   auditoría que se hace a nivel de satélite: la energía que producen los
   paneles solares (o entrega la batería) debe ser exactamente la que consumen
   los subsistemas. Un desbalance de milivatios sostenido es un error de
   dimensionamiento o una fuga térmica.
2. **Caídas en el arnés.** Cada cable, conector y contacto añade una caída en
   serie (KVL): un bus nominal de 28 V puede llegar al equipo con 27 V o menos.
   Por eso el cableado se dimensiona para que su caída quede dentro del rango
   de tensión aceptado por la carga (derating de tensión, ECSS-Q-ST-30-11C).
3. **Batería en carga y descarga.** Con la convención pasiva, la batería
   absorbe (P > 0) al cargarse desde los paneles y entrega (P < 0) al alimentar
   la computadora de vuelo. Aplicar mal los signos en el balance de potencia
   lleva a sobredimensionar o subdimensionar la batería.
4. **KVL en el WCCA.** En el análisis de peor caso se repite la malla con
   valores extremos (R máx/mín, tolerancias) y se verifica que la malla siga
   cerrando dentro de tolerancia antes de dar por válido el diseño.

## 8. Preguntas de verificación

1. Si Vin sube de 12 V a 14 V, ¿en qué porcentaje cambia la corriente y la
   potencia total? (Respuesta: corriente +16.7 %, potencia +36 % porque P ∝ V².)
2. ¿Qué caída de tensión es mayor, la de R1 o la de R3, y por qué?
3. En el log de LTspice, ¿por qué `V(vin)·I(V1)` sale negativo?
4. Un resistor de 1/4 W disipa 0.2 W continuos. ¿Cumple derating de 50 %?
   (No: 0.2 W > 0.125 W → rechazado; subir a 1/2 W.)
5. ¿Por qué el balance de potencia es una verificación y no una "ley" aparte?
   (Es la conservación de la energía aplicada al circuito.)

## Fuentes

- Clase 1 (magnitudes, Ohm, potencia): `extracted_courses/57_FZ92uwT8/course_notes.md` y `aerospace_enrichment.md`
- Clase 2 (resistor real, derating): `extracted_courses/jli6YBkRt3U/course_notes.md` y `aerospace_enrichment.md`
- Convención pasiva y balance: `docs/presentations/semana_1_diapositivas.md`
- Guía docente (bloque KVL/potencia, ejemplo resuelto): `docs/semana_1_guia_docente.md`
- Cadena de instrumentación y WCCA: `Material_Didactico_VectorLab.md`
- Derating: NASA EEE-INST-002, ECSS-Q-ST-30-11C, NASA LLIS-0676 (enlaces en `docs/resources/recursos_didacticos.md`)
- Repaso en video: EEVblog #819 — Leyes de Kirchhoff
