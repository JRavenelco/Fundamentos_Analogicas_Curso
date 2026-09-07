# Semana 4: hoja de aprendizaje activo

Use esta hoja sin consultar la guía durante el primer intento. Después compare,
corrija con otro color y explique qué cambió en su modelo mental.

## A. Recuperación rápida

1. Complete: `VGS(th)` indica ____________________, mientras que `RDS(on)` a
   una tensión especificada indica ____________________.
2. Dibuje las tres regiones del NMOS y marque cuál se busca para un switch ON.
3. Explique por qué `IG≈0` en DC y `IG` puede ser grande durante un flanco.
4. Escriba el camino completo de la corriente de una bobina un instante después
   de apagar el NMOS.
5. ¿Por qué un divisor 10 kΩ/10 kΩ no protege por sí solo un ADC ante cualquier
   falla?

## B. Prediga antes de calcular

Marque primero la tendencia y después justifique con una ecuación.

| Cambio | `VDS,on` | pérdida de conducción | esfuerzo del driver |
| --- | --- | --- | --- |
| Duplicar `ID` | sube / baja | sube / baja | igual / cambia |
| Duplicar frecuencia | igual / cambia | igual / cambia | sube / baja |
| Aumentar `RG` | igual en DC / cambia | igual en DC / cambia | flancos más rápidos / lentos |
| Retirar flyback | igual / pico mayor | igual / cambia | seguro / peligroso |

## C. Casos intercalados

Para cada caso elija tensión de gate, protección y medida principal.

1. **Motor DC nominal de 6 V, alimentado con 5 V, 250 mA sin carga y 400 mA
   con carga informados:** estime dos puntos de pérdida ON, distinga corriente
   nominal de corriente medida a 5 V e indique qué corriente aún falta para
   seleccionar hardware.
2. **Motor durante el apagado PWM:** dibuje el diodo y especifique su orientación.
3. **Entrada capacitiva de 5 µF:** identifique corriente pico y dos constantes
   de tiempo si existen resistencias distintas para carga y descarga.
4. **ADC 12 bits/3.3 V:** compare 118–184 mV del circuito con shunt contra
   escala completa. Proponga una mejora y un riesgo nuevo.

## D. Detecte el error

Corrija cada frase.

- “El IRF640N está totalmente encendido porque 3.3 V supera su umbral.”
- “El MOSFET se satura cuando funciona como interruptor cerrado.”
- “Como la puerta no consume corriente, no importa `Qg`.”
- “El divisor 10 kΩ/10 kΩ duplica la señal del shunt.”
- “Un NPN con el colector flotante puede suministrar corriente a otra base.”
- “Saturar más profundo siempre hace más rápida la conmutación del BJT.”

## E. Problema de transferencia

Un sistema nuevo usa `VCC=24 V`, una carga resistiva de 220 Ω y un MOSFET cuya
`RDS(on),max=0.20 Ω` está garantizada a la tensión real del driver.

1. Estime `ID`, `VDS,on` y `Pcond`.
2. Si `Qg=40 nC` y `f=50 kHz`, estime corriente media y potencia ideal del
   driver para una excursión de 10 V.
3. Si la carga se vuelve inductiva, dibuje la protección.
4. Liste tres datos aún necesarios antes de aprobar el hardware.

## F. Ticket de salida

Sin fórmulas, explique en cuatro frases:

1. qué dato descarta el uso directo de un GPIO de 3.3 V con el IRF640N;
2. dónde está la energía al apagar una bobina;
3. qué mide el shunt;
4. qué diferencia esencial existe entre la corriente de base y la carga de gate.
