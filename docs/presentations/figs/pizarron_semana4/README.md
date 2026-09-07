# Pizarrones de la Semana 4

Doce láminas 16:9 para explicación y recuperación activa. Se generaron como
infografías de pizarra y se revisaron eléctricamente antes de integrarlas en
`docs/presentations/clase_4_pizarrones.pdf`.

## Secuencia

| Archivo | Idea central | Pregunta de recuperación |
| --- | --- | --- |
| `01_umbral_no_es_encendido.png` | `VGS(th)` no garantiza baja pérdida | ¿Qué dato decide si 3.3 V basta? |
| `02_nmos_lado_bajo.png` | motor DC, región óhmica e inversión | ¿Por qué el drenaje baja al subir el gate? |
| `03_compuerta_capacitiva.png` | `Qg`, corriente de flanco y Miller | ¿Qué cambia al multiplicar la frecuencia por diez? |
| `04_flyback.png` | camino de corriente al apagar el motor | ¿Por qué conduce el diodo únicamente al apagar? |
| `05_shunt_adc.png` | 250–400 mA a tensión y cuentas ADC | ¿Qué sacrifica el divisor 1:2? |
| `06_sintesis.png` | cinco decisiones antes de conectar | ¿Qué debes predecir antes de simular? |
| `07_bjt_corriente_base.png` | `RPU` entrega; Q1 y Q2 hunden | ¿Qué nodo quedaba flotante en el circuito erróneo? |
| `08_bjt_dos_constantes.png` | carga, descarga y corriente pico | ¿Por qué existen dos constantes de tiempo? |
| `09_valvula_controlada_por_campo.png` | analogía de válvula y sus límites | ¿Qué representa `VGS` en la analogía? |
| `10_formacion_del_canal.png` | campo eléctrico y canal de inversión | ¿Por qué el umbral apenas inicia el canal? |
| `11_regiones_y_usos.png` | corte, región óhmica y saturación | ¿Qué región busca un switch ON? |
| `12_gate_deposito_miller.png` | analogía del depósito, `Qg` y Miller | ¿Por qué el driver entrega pulsos? |

## Conjunto de prompts

Todos los prompts pidieron una infografía científica 16:9, fondo verde oscuro,
tiza marfil y acentos cian/amarillo/rojo, sin personas ni logotipos. Las
restricciones técnicas fueron:

1. Tres estados del canal: corte, umbral a 250 µA y `RDS(on)` a 10 V.
2. Motor nominal de 6 V alimentado con +5 V, 250/400 mA informados usados como
   envolvente conservadora; driver 0/12 V separado, `VDS≤60 mV` y
   `Pcond≤24 mW`.
3. Driver 0/12 V, `RG=100 Ω`, pulsos de `IG`, meseta Miller,
   `Qg≤67 nC`, `Qgd≤33 nC` e `IG,avg≈Qg·f`.
4. Motor con diodo en paralelo, ánodo a D y cátodo a +5 V; corriente de
   recirculación y advertencia sin asignar un pico universal.
5. `RSENSE=1 Ω`, divisor 10 kΩ/10 kΩ, 118.2/183.2 mV, 147/227 cuentas y
   filtro opcional realmente conectado al nodo ADC.
6. Ruta de decisión `datasheet → cálculo → simulación → medición`.
7. BJT con `RPU=910 Ω` hacia la base de Q2, Q1 como pull-down, colector de Q2
   separado y `RSER=220 Ω` hacia el capacitor.
8. `tau_carga=(RC+RSER)C=2.2 ms`, `tau_descarga≈RSER·C=1.1 ms` y pico
   simulado de 44.6 mA.
9. Válvula como analogía de tensión, canal y corriente, con el límite explícito
   de que el gate es capacitivo y no mecánico.
10. Sección transversal de un NMOS: cuerpo P, source/drain N+, óxido, campo,
    canal débil en el umbral y canal ancho con 10 V.
11. Tres regiones del modelo ideal, separación entre MOSFET ON en región
    óhmica y BJT ON en saturación, y advertencia sobre curvas y SOA.
12. Depósito de carga como analogía de `Qg`, corriente del driver y meseta
    Miller, con bus de motor de 5 V separado del drive de 12 V.

## Datos y límites

- El motor es nominal de 6 V y se alimenta con un bus de 5 V.
- 250/400 mA son corrientes informadas por el usuario y se usan como envolvente
  conservadora a 5 V; si pertenecen a la ficha a 6 V, deben medirse a 5 V.
- El drive gate-source de 10–12 V es una alimentación separada y nunca se
  conecta al devanado del motor.
- La corriente de arranque/bloqueo y la inductancia real no se inventaron:
  deben medirse antes de seleccionar hardware.
- Los parámetros del IRF640N proceden del
  [datasheet oficial de Infineon](https://www.infineon.com/assets/row/public/documents/24/49/infineon-irf640n-datasheet-en.pdf).
