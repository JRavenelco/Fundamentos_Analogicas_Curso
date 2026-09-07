# Semana 4: MOSFET de potencia y conmutación verificable

## Resultado de aprendizaje

Al terminar la semana, el estudiante podrá seleccionar y excitar un NMOS de
lado bajo para un motor DC nominal de 6 V alimentado con 5 V, explicar la dinámica de compuerta, proteger
la carga inductiva, escalar una medición de corriente y comparar ese diseño con
un BJT en saturación forzada.

## Correcciones conceptuales obligatorias

1. **Umbral no significa encendido.** En el IRF640N, `VGS(th)=2–4 V` se mide
   con apenas `ID=250 µA`. No garantiza baja resistencia a 3.3 V.
2. **El MOSFET cerrado trabaja en región óhmica**, no en saturación. Su
   saturación corresponde al comportamiento de fuente de corriente usado en
   amplificación.
3. **La compuerta no consume corriente continua idealmente**, pero el driver
   sí debe entregar y retirar carga en cada flanco. Para el IRF640N,
   `Qg ≤ 67 nC` bajo las condiciones de prueba del fabricante.
4. **Un divisor resistivo atenúa; no amplifica ni constituye por sí solo una
   protección completa del ADC.**
5. **La saturación forzada de un BJT es una heurística de diseño.** Reduce
   `VCE`, pero puede aumentar el tiempo de almacenamiento; siempre se debe
   comprobar el punto `IC/IB` en la hoja de datos.

## Datos del IRF640N que se usarán en clase

| Parámetro | Valor | Condición relevante |
| --- | ---: | --- |
| `VDS` absoluto máximo | 200 V | Límite, no punto normal de trabajo |
| `VGS` absoluto máximo | ±20 V | Límite entre compuerta y fuente |
| `ID` continuo publicado | 18 A | `TC=25 °C`, `VGS=10 V`; depende de térmica y SOA |
| `RDS(on)` máximo | 0.15 Ω | `VGS=10 V`, `ID=11 A`, `TJ=25 °C` |
| `VGS(th)` | 2–4 V | `ID=250 µA`, `VDS=VGS` |
| `Qg` máximo | 67 nC | `ID=11 A`, `VDS=160 V`, `VGS=10 V` |
| `Ciss` típico | 1160 pF | `VGS=0`, `VDS=25 V`, `f=1 MHz` |

Fuente primaria: [datasheet IRF640N de Infineon](https://www.infineon.com/assets/row/public/documents/24/49/infineon-irf640n-datasheet-en.pdf).

## Secuencia de aprendizaje sugerida

### Sesión 1 — De la hoja de datos al conmutador

1. **Predicción individual, 5 min:** ¿un GPIO de 3.3 V enciende por completo un
   IRF640N? Cada estudiante debe justificar su respuesta con un parámetro.
2. **Contraste, 10 min:** comparar `VGS(th)` con la condición de `RDS(on)`.
3. **Modelo físico, 20 min:** corte, región óhmica y saturación con sus
   condiciones:
   - corte: `VGS < Vth`;
   - región óhmica: `VGS > Vth` y `0 ≤ VDS < VGS−Vth`;
   - saturación: `VGS > Vth` y `VDS ≥ VGS−Vth`.
4. **Cálculo, 15 min:** motor nominal de 6 V alimentado con 5 V, con 250 mA
   sin carga y hasta 400 mA con carga informados. Para no subestimar, la
   envolvente a 5 V usa 20 Ω y 12.5 Ω; con `RDS(on)≤0.15 Ω`, el peor punto da
   `ID≈395 mA`, `VDS≤59.3 mV` y `Pcond≤23.4 mW` a 25 °C. Si las corrientes son
   de ficha a 6 V, se debe calcular también 24/15 Ω y medir la corriente a 5 V.
5. **Dinámica, 20 min:** `Qg`, corriente pico, meseta Miller y estimación
   `IG,avg≈Qg·f`.
6. **Recuperación, 10 min:** responder sin apuntes tres diferencias entre
   umbral, tensión de drive y límite absoluto de `VGS`.

### Sesión 2 — Energía, medición y comparación BJT

1. **Predicción antes de simular:** dibujar el camino de corriente de una
   bobina inmediatamente después de apagar el MOSFET.
2. **Flyback:** probar los archivos con y sin diodo; explicar por qué el pico
   sin protección no tiene un valor universal.
3. **Shunt y ADC:** calcular `VSENSE`, `VADC` y cuentas de un ADC ideal de
   12 bits/3.3 V; discutir seguridad frente a resolución.
4. **Puente con semana 3:** reconstruir el conmutador BJT corregido. Q1 hunde
   corriente; `RPU` es quien alimenta la base de Q2.
5. **Intercalado:** decidir para tres cargas —resistiva, inductiva y
   capacitiva— qué protección y qué medición se requieren.

## Material asociado

- Teoría: `docs/presentations/clase_4_mosfet.pdf`.
- Diseño BJT corregido: `docs/presentations/clase_4_conmutador_hard_sat.pdf`.
- Laboratorio completo: `docs/labs/semana_4_conmutador_potencia_mosfet.md`.
- Hoja de aprendizaje activo:
  `docs/labs/semana_4_actividades_aprendizaje.md`.
- Teoría con analogías y límites:
  `docs/labs/semana_4_teoria_mosfet_analogias.md`.
- Pizarrones visuales: `docs/presentations/clase_4_pizarrones.pdf` y los PNG
  en `docs/presentations/figs/pizarron_semana4/`.
- Netlists y resultados: `Simulaciones Ltspice/sim/semana4_README.md`.

## Evaluación sugerida

| Evidencia | Peso | Criterio observable |
| --- | ---: | --- |
| Predicciones justificadas | 20 % | Distingue umbral, drive y máximo absoluto |
| Simulaciones LTspice | 30 % | Presenta medidas, unidades y ventanas correctas |
| Explicación causal | 25 % | Sigue la corriente en ON/OFF y explica el flyback |
| Diseño y seguridad | 15 % | Incluye límites, térmica, diodo y masa común |
| Recuperación final | 10 % | Resuelve casos nuevos sin copiar el ejemplo |

## Errores que conviene provocar y discutir

- Elegir el MOSFET únicamente por `VGS(th)`.
- Llamar “saturado” al MOSFET cerrado.
- Dibujar el flyback al revés.
- Medir `VGS` contra GND cuando la fuente está sobre un shunt.
- Afirmar que un divisor aumenta ganancia.
- Usar `ID=18 A` sin revisar temperatura de carcasa, disipación y SOA.
- Confiar en un modelo pedagógico como si fuera validación de hardware.
- Tomar 400 mA como corriente de arranque/bloqueo: ese dato debe medirse o
  consultarse antes de seleccionar MOSFET, diodo, fuente y shunt.
- Confundir el bus del motor (5 V) con el drive gate-source (10–12 V): son
  alimentaciones distintas que comparten referencia, no la misma tensión.

## Nota de ingeniería

El vacío elimina la convección, pero no la conducción ni la radiación. No se
debe trasladar sin análisis un `RθJA` medido en aire quieto: la ruta térmica de
montaje, la temperatura de unión y el derating siguen mandando.
