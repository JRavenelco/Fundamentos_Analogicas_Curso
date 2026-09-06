# Semana 4: MOSFET — teoría y práctica

## Objetivo general
Introducir el transistor MOSFET como dispositivo de conmutación de potencia:
estructura, símbolo, regiones de operación, ecuaciones $I_D$–$V_{GS}$ y su
modelo equivalente, y aplicar el análisis a un conmutador de lado bajo con
carga resistiva/inductiva y medición por ADC.

## Contenido

### 1 · El MOSFET como dispositivo
- Estructura NMOS (sustrato P, difusiones $N^+$, óxido de puerta), control por
  **tensión** ($I_G \approx 0$).
- Símbolo NMOS y PMOS; principio de conmutación por $V_{GS}$ frente a $V_{th}$.

### 2 · Regiones y ecuaciones
- **Corte:** $V_{GS}<V_{th}$ $\Rightarrow I_D=0$.
- **Triodo (lineal):** canal resistivo, $I_D \approx k_n(V_{GS}-V_{th})V_{DS}$,
  usado como **interruptor** (ON).
- **Saturación:** $I_D \approx \frac12 k_n (V_{GS}-V_{th})^2$, usada para
  amplificación.
- $k_n = \mu_n C_{ox} W/L$; puerta capacitiva ($Q_G$); $R_{DS(on)}$.

### 3 · Modelos equivalentes
- Puerta = capacitor ($C_{gs}$, $C_{gd}$): no hay corriente DC.
- Interruptor ideal: ON $\Rightarrow V_{DS}=I_D R_{DS(on)}$ (baja tensión);
  OFF $\Rightarrow V_{DS} \approx V_{CC}$.
- Comparación con el BJT (semana 3): control por tensión/corriente, pérdidas
  de ON, uso típico (conmutación vs amplificación).

### 4 · Conmutación de cargas inductivas
- Pico de tensión al apagar y **diodo de libre circulación**.
- Energía de puerta, $Q_G$, $R_G$ y tiempos de conmutación.
- Pérdidas y derating en vacío (sin convección).

### 5 · Aplicación aeroespacial
- Calentadores de traje/mantos, actuadores de superficies (puente H), drivers
  de cargas y multiplexores de señal.
- Selección por $V_{th}$, $R_{DS(on)}$, $Q_G$, $V_{DS,max}$, $I_D$ y temperatura.

## Actividades
- Teoría: presentación `clase_4_mosfet.pdf` + preguntas de verificación.
- Práctica: `docs/labs/semana_4_conmutador_potencia_mosfet.md` (3 etapas LTspice:
  conmutador PWM, carga inductiva con flyback, sensor de corriente + ADC).
- Simulaciones: `semana4_01_pwm_gate_mosfet.cir`,
  `semana4_02_carga_inductiva_flyback.cir`,
  `semana4_03_medicion_adc.cir`.

## Evaluación (ponderación sugerida)
- Teoría: conceptos/regiones/ecuaciones (examen corto).
- Práctica: hoja de comprobación (VDS ON/OFF, pico flyback, VADC) con
  explicación de cada criterio de correcto.
- Entrega: gráficas de LTspice + razones de las decisiones (por qué 680 k en la
  semana 3; por qué $R_G$ y flyback aquí).

## Contexto
- Semana 1-2: divisores, potencias, tolerancia. Semana 3: BJT y polarización.
  Semana 4 les compara y aterriza la conmutación de cargas reales.
