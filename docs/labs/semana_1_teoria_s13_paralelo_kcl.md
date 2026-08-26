# S1.3 — Teoría: Paralelo, KCL y resistencia equivalente

Curso: Fundamentos de Sistemas Electrónicos Analógicos · Ingeniería Aeroespacial.
Prepara la simulación `Simulaciones Ltspice/sim/semana1_03_kcl_paralelo.asc`
(R1 = 1 kΩ, R2 = 2.2 kΩ, R3 = 3.3 kΩ sobre un bus de 5 V).

**Método de trabajo:** predecir el signo y el orden de magnitud → calcular al
menos un caso a mano → ejecutar LTspice y consultar `View > SPICE Error Log` →
explicar cualquier diferencia.

**Pregunta inicial:** ¿qué rama conduce más corriente y por qué?

## 1. ¿Qué es una conexión en paralelo?

Dos o más elementos están **en paralelo** cuando comparten el **mismo par de
nodos**: todos ven la **misma tensión** `Vbus`, y la corriente de la fuente se
**reparte** entre las ramas.

Propiedades inmediatas:

- La tensión es **común**: `V_R1 = V_R2 = V_R3 = Vbus`.
- Cada rama conduce su propia corriente, dada por su propia resistencia:
  `Ik = Vbus / Rk`.
- La corriente total es la **suma** de las corrientes de rama (KCL).
- La resistencia equivalente es **menor que la rama de menor valor**.

## 2. Conductancia y resistencia equivalente

Conviene pensar en paralelo con **conductancia**, `G = 1/R` (siemens, S): la
conductancia mide cuánta corriente deja pasar un elemento por cada voltio
aplicado. En paralelo las conductancias **se suman**:

```text
Gt = G1 + G2 + G3 = 1/R1 + 1/R2 + 1/R3
Req = 1 / Gt
```

Formas equivalentes para dos resistencias:

```text
Req = (R1 · R2) / (R1 + R2)      (solo para dos)
```

Reglas de verificación rápida:

- `Req < R_minima` (la rama de menor valor manda).
- Si todas las ramas son iguales a R, `Req = R / n`.
- `G` es la pendiente de la curva I vs V de cada rama: a mayor G, mayor
  corriente (esto conecta con la pendiente-conductancia vista en S1.1).

## 3. Ley de corrientes de Kirchhoff (KCL)

Enunciado: en cualquier **nodo**, la suma de las corrientes que **entran** es
igual a la suma de las que **salen**.

```text
Σ I_entran = Σ I_salen        ⟺        Σ I (nodo) = 0
```

En el nodo superior (bus):

```text
Ifuente = I_R1 + I_R2 + I_R3
```

La KCL se cumple también en el **nodo de retorno** (tierra): la corriente que
regresa por el retorno es exactamente la suma de las corrientes de rama. Si
"falta" corriente en un nodo, hay una fuga, una rama no contada o un error de
medición.

**Divisor de corriente (deducción útil).** La corriente de cada rama es
proporcional a su conductancia:

```text
Ik = Ifuente · (Gk / Gt) = Ifuente · (Req / Rk)
```

La rama de **menor resistencia** (mayor conductancia) conduce la mayor
corriente — respuesta a la pregunta inicial.

## 4. Balance de potencia en paralelo

La misma conservación de la energía de S1.2 aplica: la fuente entrega
exactamente lo que disipan las ramas.

```text
P_fuente (entregada) = Vbus · Ifuente = P1 + P2 + P3 = Vbus² · (G1 + G2 + G3)
```

Nota: cada rama disipa `Pk = Vbus² / Rk`. La rama de menor resistencia disipa
**más** potencia (al revés que en serie).

## 5. Ejemplo resuelto (los valores de la simulación)

Bus: V = 5 V; ramas: R1 = 1 kΩ, R2 = 2.2 kΩ, R3 = 3.3 kΩ.

```text
G1 = 1.000 mS     G2 = 0.4545 mS     G3 = 0.3030 mS
Gt = 1.7576 mS    ⟹    Req = 1 / 1.7576 mS = 568.97 Ω  (< 1 kΩ ✓)

I1 = 5 V / 1 kΩ   = 5.000 mA     P1 = 25 / 1k  = 25.00 mW
I2 = 5 V / 2.2 kΩ = 2.273 mA     P2 = 25 / 2.2k = 11.36 mW
I3 = 5 V / 3.3 kΩ = 1.515 mA     P3 = 25 / 3.3k = 7.58 mW
Ifuente = I1 + I2 + I3 = 8.788 mA                  (confirma KCL)

ΣP = 43.94 mW = 5 V · 8.788 mA                     (balance de potencia)
```

**Margen de derating:** el peor caso es la rama de 1 kΩ con 25 mW, muy por
debajo del límite de 125 mW (50 % de 0.25 W): margen ≈ 5× → **aceptado**.

## 6. Verificación en LTspice

El archivo `semana1_03_kcl_paralelo.asc` ya mide las tres corrientes de rama,
la corriente de fuente y el error de KCL (`KCL_error_uA`). Para cerrar el
balance de potencia, agregar:

```text
.meas op P_R1_mW PARAM V(bus)*V(bus)/1k*1e3
.meas op P_R2_mW PARAM V(bus)*V(bus)/2.2k*1e3
.meas op P_R3_mW PARAM V(bus)*V(bus)/3.3k*1e3
.meas op P_fuente_mW PARAM V(bus)*(-I(V1))*1e3
.meas op Balance_mW PARAM P_fuente_mW - (P_R1_mW + P_R2_mW + P_R3_mW)
```

Criterio de éxito:

- `KCL_error_uA` ≈ 0: la corriente de fuente es exactamente la suma de ramas.
- `Balance_mW` ≈ 0: fuente entrega lo que disipan las ramas.

## 7. Errores comunes

| Error | Consecuencia | Corrección |
| --- | --- | --- |
| Sumar resistencias en paralelo como si fueran serie | Req demasiado grande | Sumar conductancias: `1/Req = Σ 1/R` |
| Usar `(R1·R2)/(R1+R2)` con tres resistencias | Req incorrecta | Esa fórmula vale solo para dos ramas |
| Creer que la rama de mayor R lleva más corriente | Orden de magnitud invertido | `Ik ∝ 1/Rk`: la menor R lleva más corriente |
| Olvidar que Req < R mínima | No detectar el error de cálculo | Verificación rápida siempre |
| Calcular Pk con la corriente total | Potencias 3× mayores | Cada rama usa **su propia** corriente |

## 8. Lectura aeroespacial

1. **Dimensionar la fuente por la suma, no por el promedio.** Un bus de
   aviónica alimenta varias cargas en paralelo (computadoras, actuadores,
   calefactores, sensores). La fuente y su protección deben dimensionarse para
   `Σ Ik` en el peor caso, no para la carga "típica". Este es el mismo criterio
   con que se dimensiona el EPS de un satélite: `P_bus = Vbus · Σ Ik`.
2. **Protección por rama.** Cada rama lleva su propio fusible o limitador: si
   una carga falla en corto, su corriente crece y su protección debe abrir
   **antes** de que el bus entero caiga. La KCL del nodo explica por qué una
   sola rama en corto puede disparar la protección general si no hay
   aislamiento por rama.
3. **Redundancia en paralelo.** Los calefactores o sensores redundantes se
   conectan en paralelo: si una rama se abre, las demás mantienen su tensión y
   su corriente (la fuente entrega menos). Es la topología natural para
   tolerancia a fallas.
4. **Retorno de tierra.** La KCL del nodo de retorno es la razón del
   **single-point ground** en aviónica: si las corrientes de retorno toman
   caminos distintos, aparecen diferencias de potencial entre "tierras" que
   corrompen la medición de sensores (ruido de masa).
5. **Celdas solares en paralelo.** Sumar celdas en paralelo suma corriente a
   tensión constante; en serie suma tensión. El panel de un satélite combina
   ambas para alcanzar el punto de operación del regulador.

## 9. Preguntas de verificación

1. ¿Por qué la rama de 1 kΩ conduce más corriente que la de 3.3 kΩ?
2. Si se abre la rama de 1 kΩ, ¿qué pasa con la corriente de las otras dos
   ramas y con la de la fuente? (No cambian las ramas; la fuente entrega menos.)
3. ¿Cómo cambiaría `Req` si se agrega una cuarta rama de 10 kΩ? (Bajaría: más
   conductancia en paralelo.)
4. Con Vbus = 5 V, ¿cuánto disipa la rama de 2.2 kΩ? (11.36 mW.)
5. ¿Por qué un fusible por rama protege mejor el bus que un solo fusible
   general?

## Fuentes

- Clase 1 (magnitudes, Ohm, potencia): `extracted_courses/57_FZ92uwT8/course_notes.md` y `aerospace_enrichment.md`
- Clase 2 (resistor real, topologías): `extracted_courses/jli6YBkRt3U/course_notes.md` y `aerospace_enrichment.md`
- Conexión aeroespacial de la suma de corrientes: `docs/labs/semana_1_simulaciones_ltspice.md` (S1.3)
- Guía docente (bloque KCL): `docs/semana_1_guia_docente.md`
- Cadena de instrumentación y ruido de masa: `Material_Didactico_VectorLab.md`
- Retorno de tierra y protección: NASA EEE-INST-002; enlaces en `docs/resources/recursos_didacticos.md`
- Repaso en video: EEVblog #819 — Leyes de Kirchhoff
