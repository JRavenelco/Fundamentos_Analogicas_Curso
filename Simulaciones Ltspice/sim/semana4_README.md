# Simulaciones LTspice — Semana 4

## Archivos

- `semana4_01_pwm_gate_mosfet.cir`: motor nominal de 6 V alimentado a 5 V,
  mediante una envolvente terminal conservadora de 20/12.5 Ω, y carga de gate
  a 100 kHz.
- `semana4_02_carga_inductiva_flyback.cir`: modelo terminal inductivo protegido.
- `semana4_02b_carga_inductiva_sin_diodo.cir`: contraste numérico sin diodo;
  nunca reproducir retirando protección en hardware.
- `semana4_03_medicion_adc.cir`: shunt de fuente y divisor hacia ADC.
- `semana4_04_conmutador_hard_sat.cir`: BJT corregido, pull-up de base y carga RC.
- `semana4_05_tl494_pwm.cir`: generador PWM con modelo educativo TL494
  (`tl494_educativo.sub`) a 100 kHz / 50 %, driver de gate 0-12 V y motor 5 V.
- `semana4_irf640n_educativo.lib`: sustituto pedagógico compartido.

## Ejecución

Abra cada `.cir` en LTspice y seleccione **Simulate > Run**. Consulte las
medidas en **View > SPICE Error Log**. Mantenga el `.lib` en esta misma carpeta.

En Windows, LTspice también acepta ejecución por lotes:

```powershell
& 'C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe' -b `
  'C:\ruta\completa\semana4_01_pwm_gate_mosfet.cir'
```

## Resultados verificados con LTspice XVII

| Archivo | Resultados principales |
| --- | --- |
| 01 | 20 Ω: `ID=248.492 mA`, `VDS=30.17 mV`; 12.5 Ω: `ID=396.149 mA`, `VDS=48.13 mV`; `VDS,off=5.000 V`, `t10–90≈1.350 µs` |
| 02A | `VDS,max=5.901 V`, `ID fin ON=393.321 mA`, `IFLY,pico=393.554 mA` |
| 02B | `VDS,max=200.231 V`, fijado por el clamp pedagógico; no es predicción física |
| 03 | 20 Ω: `ID=236.693 mA`, `VADC=118.387 mV`; 12.5 Ω: `ID=366.948 mA`, `VADC=183.510 mV` |
| 04 | `IB2=4.576 mA`, `IC2,pico=44.625 mA`, `VC,cargado=4.905 V` |

## Qué no demuestra el modelo

El archivo `semana4_irf640n_educativo.lib` no es un macromodelo de Infineon.
No debe usarse para validar temperatura, SOA, avalancha, EMI, meseta Miller ni
pérdidas de conmutación. Para diseño final, use un modelo validado del
fabricante cuando esté disponible y trate el datasheet como referencia final.

El motor es nominal de 6 V y se alimenta con 5 V. Los netlists conservan los
250/400 mA como envolvente a 5 V para no subestimar: si esos valores pertenecen
exclusivamente a la ficha a 6 V, use 24/15 Ω y mida la corriente real a 5 V.
Falta medir o consultar la corriente de arranque/bloqueo y la inductancia real
antes de elegir MOSFET, diodo, fuente, pistas y shunt. El modelo EDU produce
una resistencia ON cercana a 0.12 Ω con 12 V de drive; los cálculos de peor
caso siguen usando `RDS(on),max=0.15 Ω` bajo las condiciones del datasheet.
