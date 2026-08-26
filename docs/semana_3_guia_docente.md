# Semana 3: polarización de TBJ y punto Q

Curso: Fundamentos de Sistemas Electrónicos Analógicos, Ingeniería Aeroespacial.

Carga: 4 horas de teoría y 2 horas de práctica.

## Resultado de aprendizaje

Al terminar la semana, el estudiante podrá polarizar un transistor NPN de baja
potencia, calcular su punto Q (IC, VCE) y decidir qué topología de polarización
ofrece la estabilidad térmica y frente a β que exige una aplicación embebida.

## Pregunta rectora

Un transistor con β = 100 da un punto Q correcto. ¿Qué pasa si el lote siguiente
trae β = 200 o si la temperatura sube 40 °C?

## Punto Q y regiones de operación

El punto Q es el par (IC, VCE) de reposo (sin señal). Debe quedar en la **región
activa** para amplificar:

- **Corte:** IC ≈ 0, VCE ≈ VCC.
- **Activa:** BE en directa, BC en inversa; IC = β·IB (zona de amplificación).
- **Saturación:** IC máximo, VCE ≈ VCE(sat) ≈ 0.2 V; el transistor "conduce".

Convención de signos (S1.2): en un NPN, IB y IC entran, IE sale.
`IE = IC + IB ≈ IC` si `β >> 1`.

## Bloque 1: polarización fija

```text
IB = (VCC - VBE) / RB
IC = β · IB
VCE = VCC - IC · RC
```

Instabilidad: `IC = β·IB` depende linealmente de β. Si β sube, IC sube y el
punto Q se desplaza (puede saturar).

## Bloque 2: realimentación por emisor

Se agrega `RE` en el emisor:

```text
IE ≈ (VCC - VBE) / ( RB/(β+1) + RE )
```

`RE` introduce realimentación negativa: si IC sube, VE sube, VBE baja, IB baja.
La dependencia de β se reduce.

## Bloque 3: polarización por divisor de base

Se fija la base con un divisor R1–R2 y se agrega RE:

```text
Vth = VCC · R2 / (R1 + R2)      Rth = R1 || R2
IE  ≈ (Vth - VBE) / ( RE + Rth/β )
```

Con `Rth/β` pequeño, `IE ≈ (Vth - VBE)/RE`: el punto Q casi no depende de β
ni de la temperatura. Es la topología más estable.

## Regiones y margen térmico

Para que el punto Q sea estable ante β y temperatura:

- `IE` debe depender poco de β y de VBE (usar RE y divisor rígido).
- El diseño debe tener margen: `VCE` en activa, lejos de corte y saturación.
- En vacío (sin convección) el transistor disipa `P = VCE · IC`; se respeta el
  derating y se acopla térmicamente al chasis.

## Actividades de teoría activa

1. Calcular IB, IC y VCE de la polarización fija para β = 100.
2. Repetir para β = 200 y observar el desplazamiento del punto Q.
3. Calcular el punto Q del divisor de base con RE.
4. Comparar IC ante una variación de β y de temperatura en las tres topologías.
5. Elegir la topología para una etapa que debe operar de −30 °C a +60 °C.

## Evidencia y evaluación

Entregable: punto Q, recta de carga, simulación del barrido de β y justificación
de la topología.

| Criterio | Peso |
| --- | ---: |
| Cálculo del punto Q | 25% |
| Regiones y margen | 20% |
| Estabilidad frente a β y T | 25% |
| Simulación vs cálculo | 20% |
| Justificación de diseño | 10% |

## Fuentes base

- Clase 3 (TBJ): playlist `k8v-ukhCc2g`, `yCPv7Je-D5E`, `pfVUD5FVoB0`, `Ic3r9JxoKVg`.
- Plan rector: `docs/weekly_course_plan_16_weeks_unam_aligned.md`.
- Material VectorLab: `Material_Didactico_VectorLab.md`.
- Simulaciones: `Simulaciones Ltspice/sim/semana3_01..03`.
