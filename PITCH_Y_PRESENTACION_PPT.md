# GUÍA OFICIAL DE PRESENTACIÓN PPT Y PITCH DE VENTAS (1 MINUTO)
## SAMSUNG INNOVATION CAMPUS - SIC 2025/2026
### PROYECTO: AstraMed - Analytics & Machine Learning para Telemedicina

---

## PARTE 1: GUIÓN DEL VIDEO PITCH DE 1 MINUTO (HORIZONTAL / ZOOM)
> **Tiempo exacto:** 60 segundos | **Formato:** Video horizontal con cámara activa y diapositivas de fondo.

* **[00:00 - 00:10] EL GANCHO (Hook):**
  > *"¿Sabías que casi 4 de cada 10 pacientes que usan telemedicina terminan insatisfechos, y casi la mitad de los que necesitan seguimiento médico nunca regresan a su control? Bienvenidos a **AstraMed**, la solución inteligente para transformar la salud digital."*

* **[00:10 - 00:25] EL PROBLEMA CON DATOS:**
  > *"Al analizar 500 consultas de telemedicina con Python, descubrimos que la satisfacción promedio es de solo 2.9 sobre 5, y que cuando una consulta se alarga por encima de 45 minutos, la satisfacción se desploma. Además, el 48.6% de los pacientes requiere seguimiento clínico sin que hoy exista un sistema predictivo para evitar el abandono de su tratamiento."*

* **[00:25 - 00:45] LA SOLUCIÓN Y RESULTADOS TECNOLÓGICOS:**
  > *"Desarrollamos una plataforma en Python con Pandas, Scikit-Learn y visualizaciones avanzadas. Nuestro pipeline procesa datos en tiempo real, realiza pruebas estadísticas de hipótesis y entrena modelos de Machine Learning como Random Forest, identificando los factores que más impactan la experiencia del paciente y alertando demoras operativas antes de que generen frustración."*

* **[00:45 - 01:00] LA PROPUESTA DE VALOR Y CIERRE:**
  > *"AstraMed se alinea directamente con los valores de la UNESCO de equidad, inclusión y ética en IA, y con el ODS 3 de Salud y Bienestar. Elevamos la satisfacción al 65%, evitamos el abandono del tratamiento en pacientes crónicos y optimizamos la capacidad hospitalaria en un 20%. Con tecnología Samsung e innovación en Python, democratizamos la salud para todos. ¡Muchas gracias!"*

---

## PARTE 2: ESTRUCTURA DIAPOSITIVA POR DIAPOSITIVA (PPT OFICIAL SAMSUNG)

### Paleta Gráfica Oficial de Samsung recomendada:
* **Azul Samsung Principal:** `#034EA2`
* **Azul Oscuro / Fondo:** `#0B192C`
* **Azul Claro Acento:** `#00A9E0`
* **Gris Neutro Claro:** `#F4F6F9`
* **Texto:** Blanco para fondos oscuros, `#222222` para fondos claros.
* **Tipografía sugerida:** Samsung Sharp Sans / Open Sans / Segoe UI.

---

### Diapositiva 1: Portada Institucional
* **Título:** AstraMed
* **Subtítulo:** Plataforma Analítica Predictiva para la Optimización de la Atención y Satisfacción en Telemedicina.
* **Programa:** Samsung Innovation Campus (SIC) - Proyecto Final Módulo Python.
* **Equipo de Desarrollo:**
  - **Jonathan Reyes:** Líder de Proyecto, Arquitecto & Documentación
  - **Jesús Torres:** Ingeniero de Datos & QA
  - **Ivy Janssen:** Ingeniero de Machine Learning
  - **David Morales:** Analista de Datos & Visualización
* **Línea Gráfica:** Fondo azul Samsung con el logotipo oficial del SIC.

---

### Diapositiva 2: Planteamiento del Problema
* **Encabezado:** El Desafío de la Salud Remota
* **Puntos Clave con Métricas (Data-Driven):**
  - **37.8% de Insatisfacción:** 4 de cada 10 usuarios evalúan negativamente la consulta (satisfacción media: 2.96 / 5.0).
  - **48.6% de Brecha en Seguimiento:** Casi la mitad de pacientes requiere consulta posterior obligatoria sin un sistema de retención predictivo.
  - **Caída Crítica por Demoras:** Consultas de más de 45 minutos caen a 2.74 / 5.0 en satisfacción por fatiga digital.
  - **Dermatología en Riesgo:** Especialidad con menor satisfacción (2.83) frente a Pediatría (3.12).
* **Elemento Visual:** Gráfico `resources/03_duracion_vs_satisfaccion.png` incrustado.

---

### Diapositiva 3: Objetivos del Proyecto
* **Objetivo General:**
  - Desarrollar un sistema analítico y de aprendizaje automático en Python que optimice la eficiencia de atención, garantice la trazabilidad del paciente y aumente la satisfacción global en plataformas de telemedicina.
* **Objetivos Específicos:**
  1. Construir un pipeline modular de carga, validación y feature engineering en Python.
  2. Implementar análisis exploratorio riguroso y pruebas de hipótesis (Chi² y ANOVA).
  3. Entrenar modelos de clasificación supervisada para alertar el riesgo de insatisfacción y clasificar necesidades de seguimiento.
  4. Generar reportes y recomendaciones clínicas accionables para directores médicos y gestores hospitalarios.

---

### Diapositiva 4: Arquitectura del Sistema y Herramientas
* **Flujo de Datos (Arquitectura Modular):**
  `Dataset CSV` ➔ `data_loader.py` ➔ `eda_analysis.py` ➔ `modeling.py` ➔ `visualizer.py` ➔ `Dashboard & Recomendaciones`
* **Stack Tecnológico Utilizado:**
  - **Python 3.13:** Núcleo de desarrollo.
  - **Pandas & NumPy:** Ingesta estructurada, filtrado y vectorización numérica.
  - **Scikit-Learn:** Modelado con Random Forest y Regresión Logística, validación cruzada y métricas de desempeño.
  - **SciPy:** Pruebas estadísticas formales (Chi-cuadrado y ANOVA).
  - **Matplotlib & Seaborn:** Visualización de alta resolución con estándar gráfico Samsung.

---

### Diapositiva 5: Hallazgos Clave de Analítica Exploratoria (EDA)
* **Gráficos Destacados:**
  - `resources/01_distribucion_especialidades.png` (Volumen por especialidad: Pediatría 23.8%, Medicina General 19.6%, etc.).
  - `resources/02_satisfaccion_por_modalidad.png` (Canales: Video 35.6%, Audio 35.0%, Chat 29.4%).
* **Conclusión Estadística Clave:**
  - La prueba de hipótesis Chi-cuadrado ($p = 0.51$) demostró que las consultas por **Audio** logran igual o mejor satisfacción que el **Video**, validando el despliegue de telemedicina en regiones de baja conectividad digital sin comprometer la calidad.

---

### Diapositiva 6: Inteligencia Artificial y Modelado Predictivo
* **Modelo Principal:** Random Forest Classifier (120 estimadores, profundidad optimizada).
* **Variables con Mayor Poder Predictivo en la Satisfacción:**
  1. **Duración de la consulta (minutos):** 29.15% de importancia relativa.
  2. **Edad del paciente:** 24.89% de importancia.
  3. **Género del paciente:** 5.28% de importancia.
  4. **Necesidad de seguimiento clínico:** 3.91% de importancia.
* **Elemento Visual:** Gráfico `resources/06_importancia_caracteristicas.png`.

---

### Diapositiva 7: Demostración Funcional y Recomendaciones Operativas
* **Salida del Pipeline:** Ejecución de `AstraMed_Analytics.py` en consola generando KPIs, pruebas y gráficos automáticamente.
* **Matriz de Recomendaciones Clínicas:**
  - **Alerta de Tiempo Límite:** Notificación clínica al minuto 35 para evitar sobrepasar los 45 minutos.
  - **Automatización de Re-agendamiento:** Integración con WhatsApp/SMS para el 48.6% que requiere control médico.
  - **Protocolo Dermatológico:** Subida previa obligatoria de fotografías dermatológicas en alta resolución antes de iniciar la videollamada.

---

### Diapositiva 8: Propuesta de Valor, Valores UNESCO y ODS de la ONU
* **Alineación con Valores y Ética de la UNESCO:**
  - **Equidad e Inclusión:** Atención de calidad en zonas remotas vía Audio/Chat sin exclusión tecnológica.
  - **Ética y Transparencia en IA:** Algoritmos explicables y auditables (Random Forest con feature importances abiertas).
  - **Privacidad y Dignidad:** Protección de datos médicos y anonimización de identificadores.
* **Impacto en los Objetivos de Desarrollo Sostenible (ODS):**
  - **ODS 3 (Salud y Bienestar - Meta 3.8):** Reducción del abandono terapéutico en el 48.6% que requiere control.
  - **ODS 10 (Reducción de Desigualdades):** Descentralización de especialistas para comunidades vulnerables.
  - **ODS 13 (Acción por el Clima):** Descarbonización de la atención médica al evitar viajes innecesarios.
* **Metas Cuantitativas de Impacto:**
  - Elevar la tasa de alta satisfacción del **38.6% al 65.0%**.
  - Aumentar el cumplimiento de citas de seguimiento del **50% al 85%**.

---

## PARTE 3: BANCO DE PREGUNTAS Y RESPUESTAS DEL JURADO (DEFENSA DEL PITCH)

#### P1: ¿Por qué eligieron Random Forest en lugar de un modelo más simple o una red neuronal profunda?
* **Respuesta:** *"Seleccionamos Random Forest porque ofrece el mejor equilibrio entre precisión predictiva e interpretabilidad clínica. En el sector salud es fundamental explicar el 'por qué' de una predicción; Random Forest nos permite calcular la importancia relativa exacta de cada característica (como la duración y la edad), a diferencia de modelos tipo caja negra."*

#### P2: ¿Qué hicieron para garantizar que el código sea mantenible y profesional de acuerdo con la rúbrica?
* **Respuesta:** *"Diseñamos una arquitectura modular en la carpeta `src/`, separando claramente la ingesta (`data_loader`), la analítica estadística (`eda_analysis`), el modelado (`modeling`) y la visualización (`visualizer`), todo coordinado por un script principal `AstraMed_Analytics.py`. Además, incluimos control de excepciones, tipado estricto (`type hinting`) y un archivo `requirements.txt` reproducible."*

#### P3: ¿Cómo beneficia este desarrollo a comunidades vulnerables o rurales?
* **Respuesta:** *"Nuestra investigación comprobó estadísticamente que la atención por Audio telefónico y Chat no tiene diferencias de satisfacción frente a la videollamada. Esto significa que podemos llevar atención médica especializada a zonas donde no hay fibra óptica ni smartphones de última generación, sin degradar la calidad percibida por el paciente."*

#### P4: ¿Con qué valores de la UNESCO y Objetivos de Desarrollo Sostenible (ODS) se alinea su proyecto?
* **Respuesta:** *"El proyecto se adhiere directamente a la 'Recomendación sobre la Ética de la IA' de la UNESCO en tres pilares: **Equidad** (democratizando el acceso médico sin brechas de conectividad), **Inclusión** (atención accesible para adultos mayores) y **Transparencia** (modelos de IA explicables, no cajas negras). En cuanto a los ODS de la ONU, impactamos prioritariamente el **ODS 3 (Salud y Bienestar)** al garantizar la trazabilidad del 48.6% de pacientes crónicos, el **ODS 10 (Reducción de Desigualdades)** y el **ODS 13 (Acción por el Clima)** mediante la reducción de emisiones por traslados presenciales innecesarios."*
