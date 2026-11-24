# PROGRAMA SAMSUNG INNOVATION CAMPUS (SIC - 2025/2026)
## PROYECTO FINAL DEL MÓDULO PYTHON: FORMULARIO DE DESARROLLO Y PRESENTACIÓN DE IDEAS

---

### 1. Nombre y función de los miembros del equipo

| Nombre de los Integrantes | Papel o rol a desempeñar en el equipo | Responsabilidades Clave |
| :--- | :--- | :--- |
| **Jonathan Reyes** | **Líder de Proyecto, Arquitecto & Documentación** | Coordinación general, diseño de arquitectura modular, integración en GitHub, estructuración técnica y pitch. |
| **Jesús Torres** | **Ingeniero de Datos & QA** | Pipeline de ingesta, limpieza, preprocesamiento y validación de tipos (`src/data_loader.py`) y aseguramiento de calidad. |
| **Ivy Janssen** | **Ingeniero de Machine Learning** | Modelos predictivos supervisados, ingeniería de variables y evaluación de métricas (`src/modeling.py`). |
| **David Morales** | **Analista de Datos & Visualización** | Análisis exploratorio (EDA), pruebas de hipótesis estadísticas y gráficos de alta resolución (`src/visualizer.py`). |

---

### 2. Nombre de la prueba (Prototipo a construir)

> **AstraMed: Plataforma Analítica Predictiva para la Optimización de la Atención, Eficiencia Clínica y Satisfacción del Paciente en Servicios de Telemedicina**

---

### 3. Descripción de la prueba

#### Planteamiento del problema (Respaldado con datos reales del dataset):
La rápida adopción de la telemedicina ha permitido democratizar el acceso a la salud; sin embargo, las instituciones de salud enfrentan graves cuellos de botella en la calidad percibida del servicio, la adherencia a tratamientos y la asignación de canales de comunicación (Video, Audio, Chat).

A partir del análisis cuantitativo de **500 consultas médicas** registradas durante 2025 en 5 especialidades clínicas (Pediatría, Medicina General, Dermatología, Cardiología y Psiquiatría), se evidenciaron los siguientes puntos críticos:
1. **Alta insatisfacción en el servicio:** Un **37.8% de los pacientes reportan insatisfacción** (puntajes de 1 o 2 sobre 5), mientras que la satisfacción media global es de solo **2.96 / 5.00**, lo que indica que casi 4 de cada 10 pacientes tienen una experiencia deficiente.
2. **Impacto negativo de consultas prolongadas por demoras técnicas o clínicas:** Las consultas que superan los 45 minutos registran una satisfacción media de solo **2.74 / 5.00**, en contraste con las consultas estándar (15 a 45 minutos) que promedian **3.02 / 5.00**. La fatiga digital y los tiempos muertos deterioran la percepción del usuario.
3. **Brecha crítica en el seguimiento de pacientes:** El **48.6% de los pacientes requieren seguimiento clínico obligatorio**, pero la mayoría de plataformas no cuentan con un mecanismo predictivo o automatizado para garantizar su re-agendamiento, arriesgando la adherencia terapéutica y aumentando la probabilidad de reingresos a urgencias.
4. **Disparidad por especialidad:** Especialidades de alta dependencia visual como Dermatología registran la satisfacción más baja (**2.83 / 5.00**), demostrando la necesidad de protocolos estandarizados de captura previa de imágenes.

#### Concepto general de la solución:
**AstraMed** es un ecosistema analítico y predictivo desarrollado en **Python** que integra:
- **Pipeline de Ingesta y Limpieza Automatizada:** Procesamiento robusto con validación de tipos y tratamiento de fechas.
- **Motor de Analítica Descriptiva y Pruebas Estadísticas:** Cálculo de KPIs operacionales y pruebas de hipótesis (Chi-cuadrado y ANOVA) para determinar la correlación entre canal, especialidad y satisfacción.
- **Modelo Predictivo de Clasificación (Machine Learning):** Implementación de algoritmos supervisados (*Random Forest Classifier*) para predecir con anticipación el riesgo de baja satisfacción del paciente y anticipar la necesidad de seguimiento clínico.
- **Módulo de Recomendación Clínica y Alertas Operacionales:** Generación automatizada de alertas tempranas (por ejemplo, consultas que exceden 35 minutos) y recomendaciones ejecutivas para directores médicos y gestores hospitalarios.

---

### Preguntas del Formulario de Desarrollo

#### (1) ¿Qué valor está generando su idea (ambiental, social, financiero, etc.)?
* **Valor Social y de Salud Pública:** Permite cerrar la brecha de acceso a atención médica de calidad, identificando de forma temprana a pacientes vulnerables que requieren citas de control (48.6% del total). Además, valida que las consultas vía Audio y Chat son clínicamente viables y valoradas equitativamente en zonas donde el ancho de banda no permite videollamadas fluidas.
* **Valor Financiero y Operacional:** Reduce el absentismo y el costo de abandono de tratamientos en centros de salud. Al optimizar los tiempos de consulta y alertar sobre consultas prolongadas (>45 min), los centros médicos pueden aumentar su capacidad de atención en un **15% a 20%** sin contratar médicos adicionales.
* **Valor Ambiental:** Al fortalecer la telemedicina efectiva frente a las visitas presenciales innecesarias, contribuye a la reducción de la huella de carbono asociada al desplazamiento en transporte vehicular de pacientes y cuidadores.

---

### 4. Alineación con los Valores y Principios Éticos de la UNESCO y la Agenda 2030 (ODS)

El proyecto **AstraMed** se encuentra estrechamente alineado con el marco axiológico de la **UNESCO** y la **Recomendación sobre la Ética de la Inteligencia Artificial de la UNESCO**:

| Valor / Principio UNESCO | Aplicación Concreta en el Proyecto AstraMed |
| :--- | :--- |
| **1. Equidad y No Discriminación** | Garantiza que la atención en salud no dependa del poder adquisitivo o la infraestructura de internet del paciente. La validación estadística de los canales telefónicos (Audio) democratiza el acceso en zonas rurales sin degradar la calidad percibida. |
| **2. Inclusión y Respeto a la Diversidad** | Proporciona soluciones accesibles para los adultos mayores (40% de los pacientes analizados), quienes presentan mayores barreras de alfabetización digital, habilitando canales auditivos asistidos. |
| **3. Bienestar Humano y Derecho a la Salud** | Pone a la persona en el centro: el motor predictivo asegura que el **48.6%** de pacientes con necesidad de seguimiento no queden en el olvido, protegiendo su derecho a la continuidad terapéutica. |
| **4. Transparencia y Explicabilidad en la IA (Recomendación UNESCO 2021)** | En lugar de algoritmos tipo "caja negra" inescrutables, el modelo predictivo de Random Forest provee explicabilidad matemática completa (cálculo de importancia relativa de duración 29.15% y edad 24.89%), garantizando decisiones auditables y éticas. |
| **5. Privacidad y Protección de Datos** | Manejo estricto de identificadores anonimizados (`consultation_id`), salvaguardando la confidencialidad médica conforme a los principios bioéticos de la UNESCO. |

#### Objetivos de Desarrollo Sostenible (ODS de la ONU / UNESCO) Impactados:
* **ODS 3: Salud y Bienestar (Meta 3.8):** Cobertura sanitaria universal y reducción de complicaciones por enfermedades crónicas (hipertensión, infecciones) mediante seguimiento proactivo.
* **ODS 10: Reducción de las Desigualdades:** Cierre de brechas asistenciales entre grandes ciudades y zonas periféricas desatendidas.
* **ODS 9: Industria, Innovación e Infraestructura:** Innovación tecnológica abierta y reproducible desarrollada en software libre (Python).
* **ODS 13: Acción por el Clima:** Disminución directa de emisiones de $CO_2$ al evitar traslados motorizados innecesarios hacia hospitales de tercer nivel.

---

#### (2) ¿Existen consideraciones que deban tenerse en cuenta para la comunidad (¿la gente amará esta idea, tendrá que acostumbrarse a ella, afecta negativamente a algunas personas)?
* **Aceptación comunitaria:** Los pacientes valorarán enormemente recibir un seguimiento proactivo y una atención más ágil sin tiempos de espera frustrantes.
* **Curva de adaptación:** Adultos mayores (que representan el 40% de las consultas analizadas) pueden requerir interfaces simplificadas o acompañamiento para el uso de canales digitales. Por ello, el proyecto respalda el uso del canal **Audio telefónico**, el cual demostró una satisfacción sólida (3.01/5) sin requerir alfabetización digital avanzada.
* **Mitigación de efectos adversos:** El sistema no reemplaza el criterio médico ni niega la atención presencial; funciona como un asistente analítico para optimizar recursos y alertar sobre casos que requieren cita de control urgente.

#### (3) ¿Cómo impactará esto a la comunidad (positiva o negativamente)?
* **Impacto Positivo:**
  - Descongestión de las salas de urgencias hospitalarias al resolver patologías de baja y mediana complejidad a distancia.
  - Mayor continuidad del cuidado médico para pacientes crónicos (hipertensión, dermatitis, estrés).
  - Mayor transparencia y control de calidad asistencial medido objetivamente a través de KPIs.
* **Mitigación de riesgos:** La privacidad de los datos de salud se protege bajo estándares éticos y anonimización de identificadores de pacientes (`consultation_id`), evitando cualquier filtración de información médica confidencial.

#### (4) ¿Existen preguntas pendientes y/o supuestos que puedan responder sobre su idea?
* **Supuesto validado:** *¿Es indispensable el video de alta definición para lograr una buena satisfacción del paciente?*
  - **Respuesta cuantitativa:** No. Las pruebas de hipótesis demostraron que la satisfacción en Audio (3.01) y Chat (2.95) es estadísticamente comparable al Video (2.92). Esto valida que la telemedicina por canales ligeros es perfectamente viable en regiones rurales con conectividad limitada.
* **Supuesto validado:** *¿El tiempo de consulta siempre incrementa la satisfacción?*
  - **Respuesta cuantitativa:** Falso. Las consultas superiores a 45 minutos sufren un descenso a 2.74/5 en satisfacción, refutando la idea de que mayor duración equivale a mayor calidad.

#### (5) ¿Cuáles son las preguntas más importantes sin responder o las dudas pendientes que deberían resolverse antes de desarrollar más esta idea?
1. **Integración con Historias Clínicas Electrónicas (HCE / EHR):** ¿Cuál es la compatibilidad con los sistemas hospitalarios existentes bajo estándares internacionales como HL7 / FHIR?
2. **Latencia y Conectividad en Tiempo Real:** ¿Cómo influyen las micro-desconexiones en la frustración del usuario en zonas periféricas durante videollamadas?
3. **Escalabilidad del Modelo:** ¿Cómo se comporta el modelo predictivo cuando el volumen escala a más de 100,000 consultas mensuales y con diagnósticos de mayor severidad?

#### (6) ¿Cuál es el objetivo principal o métrica que intenta impactar con esta prueba?
* **Objetivo Primario:** Incrementar la **Tasa de Alta Satisfacción del Paciente** del actual **38.6% al 65.0%**, reduciendo la insatisfacción (puntajes 1-2) del **37.8% a menos del 18.0%**.
* **Métricas Operativas Secundarias:**
  - Reducción de consultas prolongadas (>45 min) no justificadas en un **30%** mediante alertas en tiempo real.
  - Aumento de la tasa de adherencia al seguimiento clínico programado del **50% al 85%** mediante el motor de re-agendamiento predictivo.
  - Reducción del tiempo de triage y asignación de modalidad adecuada en un **40%**.
