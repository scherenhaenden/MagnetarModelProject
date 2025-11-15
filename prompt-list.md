# Lista de Prompts para Replicar el Modelo de Proyecto Canónico de Magnetar

Utiliza los siguientes prompts para generar la estructura de archivos y el contenido base para un nuevo proyecto que siga el Modelo de Proyecto Canónico de Magnetar. Cada prompt está diseñado para crear un archivo específico, definiendo su propósito, estructura y contenido requerido.

---

### 1. `README.md`

**Prompt:**

"Crea un archivo `README.md` que sirva como la introducción definitiva a nuestro proyecto, siguiendo el estándar del Modelo de Proyecto Canónico de Magnetar. El `README.md` debe cumplir con los siguientes requisitos:

1.  **Título Principal:** 'Modelo de Proyecto Canónico de [Nombre del Proyecto]'.
2.  **Propósito:** Una sección clara y concisa que explique por qué existe el proyecto, qué problema resuelve y cuál es su valor. Debe establecer que el proyecto sigue el estándar de Magnetar para la documentación, planificación y gobernanza.
3.  **Cómo Utilizar Este Repositorio:** Una guía numerada que instruya a los usuarios y colaboradores sobre cómo empezar, incluyendo los siguientes pasos:
    *   Clonar el modelo canónico.
    *   Copiar y rellenar el archivo `projects/_template.project.yml`.
    *   Replicar el conjunto de documentación requerido.
    *   Seguir las reglas de WIP, branching y blockers.
    *   Consultar el proyecto de ejemplo para resolver dudas.
4.  **Contenido del Proyecto:** Una tabla que enumere los archivos de documentación clave y su propósito. La tabla debe incluir:
    *   `PLAN.md`: Tareas y hitos del proyecto.
    *   `BITACORA.md`: Registro cronológico de eventos.
    *   `REQUIREMENTS.md`: Especificaciones funcionales y no funcionales.
    *   `ARCHITECTURE.md`: Estructura del sistema/módulo.
    *   `RULES.md`: Estándares de nomenclatura y flujo de trabajo.
    *   `STATUS.md`: Resumen de salud y estadísticas de progreso.
    *   `TESTING.md`: Reglas de cobertura de pruebas y informes.
    *   `BLOCKERS.md`: Bloqueos documentados y rutas de escalada.
    *   Mencionar también `BRANCHING_MODEL.md` y `WIP_GUIDELINES.md` como referencias de gobernanza.
5.  **Resumen del Modelo de Progreso:** Una explicación de cómo el proyecto rastrea el progreso a través de hitos, tareas y transiciones de estado (`planned` → `in_progress` → `in_review` → `done`). Debe enfatizar que cada cambio de estado se registra en `BITACORA.md`.
6.  **Esquema del Proyecto YAML:** Una descripción del archivo `projects/_template.project.yml`, explicando que contiene el esquema canónico legible por máquina con metadatos, stakeholders, hitos, tareas y riesgos.
7.  **Guía para Colaboradores de IA:** Un conjunto de directrices para agentes de IA, indicando que deben:
    *   Analizar el archivo YAML del proyecto.
    *   Utilizar `PLAN.md` y `STATUS.md` para determinar el enfoque.
    *   Respetar `RULES.md`, `WIP_GUIDELINES.md` y `BRANCHING_MODEL.md`.
    *   Actualizar `BITACORA.md` después de completar cualquier trabajo.
8.  **Diagrama de Arquitectura (Opcional pero Recomendado):** Un diagrama de flujo simple en texto que muestre cómo los estándares de gobernanza informan la planificación, que a su vez alimenta los artefactos de ejecución y los ejemplos.
9.  **Cómo Aplicar esta Plantilla:** Pasos claros para aplicar la plantilla a un nuevo proyecto, incluyendo:
    *   Copiar la estructura del repositorio.
    *   Reemplazar el contenido de ejemplo con detalles específicos del proyecto.
    *   Instanciar y validar un archivo YAML del proyecto.
    *   Establecer los hitos iniciales y registrar el estado inicial en `PLAN.md`, `STATUS.md` y `BITACORA.md`.
10. **Validación de Cumplimiento Canónico:** Una lista de verificación para confirmar que un proyecto sigue el canon de Magnetar, asegurando que:
    *   Todos los archivos requeridos existen.
    *   El YAML del proyecto coincide con el esquema.
    *   `BITACORA.md` se actualiza cronológicamente.
    *   Las ramas activas siguen las reglas del `BRANCHING_MODEL.md`.
    *   Los compromisos de pruebas y los procesos de bloqueo coinciden con `TESTING.md` y `BLOCKERS.md`."

---

### 2. `RULES.md`

**Prompt:**

"Crea un archivo `RULES.md` que establezca las reglas fundamentales y los estándares de flujo de trabajo para nuestro proyecto, basándose en el Modelo Canónico de Magnetar. El archivo debe ser claro, directivo y cubrir las siguientes áreas:

1.  **Título Principal:** 'Reglamento Canónico de [Nombre del Proyecto]'.
2.  **Introducción:** Una declaración que indique que estas reglas codifican el estándar de Magnetar y que todo el proyecto debe cumplirlas, a menos que se documente una excepción formal en `BITACORA.md`.
3.  **Convenciones de Nomenclatura:** Una lista de reglas de nomenclatura para:
    *   **Repositorios:** `magnetar-<dominio>-<descriptor>`.
    *   **Ramas:** `<tipo>/<descripcion-corta>`, donde `tipo` es `feature`, `fix`, `chore`, `experiment` o `hotfix`.
    *   **Tareas y Bloqueos:** `kebab-case` (por ejemplo, `task-202`, `blocker-db-outage`).
    *   **Claves YAML:** `lower_snake_case`.
    *   **Nombres de Archivo:** Deben reflejar los del repositorio canónico.
4.  **Archivos Requeridos:** Una lista explícita de los archivos que **deben** incluirse en cada proyecto de Magnetar:
    *   `README.md`, `PLAN.md`, `BITACORA.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `RULES.md`, `STATUS.md`, `TESTING.md`, `BLOCKERS.md`.
    *   `BRANCHING_MODEL.md`, `WIP_GUIDELINES.md`, `CONTRIBUTING.md`.
    *   `projects/<proyecto>.project.yml`.
    *   Mencionar que cualquier omisión requiere una exención explícita registrada en `BITACORA.md`.
5.  **Convenciones de Ramas (Branching):** Reglas claras para la gestión de ramas:
    *   `master`: Línea de lanzamiento inmutable; los merges requieren CI exitoso y actualizaciones de documentación.
    *   `develop` (opcional): Agrega características completadas antes de la estabilización.
    *   Ramas de características (`feature`): Se originan desde `master` o `develop` y deben ser actualizadas (rebase) antes de fusionarse.
    *   Ramas de corrección urgente (`hotfix`): Comienzan desde `master` y deben desencadenar una actualización de `STATUS.md` al completarse.
    *   Cada Pull Request debe hacer referencia a las tareas que afecta e incluir entradas en `BITACORA.md`.
6.  **Estados de Tarea Permitidos:** Una lista de los únicos estados de tarea válidos:
    1.  `planned`
    2.  `ready`
    3.  `in_progress`
    4.  `in_review`
    5.  `blocked`
    6.  `done`
    *   Incluir una descripción de las transiciones de estado permitidas (por ejemplo, `ready` → `in_progress` cuando comienza el trabajo).
7.  **Restricciones de Trabajo en Progreso (WIP):**
    *   Límite de WIP: Especificar el número máximo de tareas `in_progress` que un individuo o agente de IA puede tener simultáneamente (por ejemplo, dos).
    *   Excepciones: Indicar que exceder el límite requiere aprobación documentada en `WIP_GUIDELINES.md` y `BITACORA.md`.
8.  **Ciclo de Vida de los Bloqueos (Blockers):** Un proceso numerado para gestionar los bloqueos:
    1.  **Descubrimiento:** Registrar en `BLOCKERS.md` con ID, descripción, severidad, propietario y marca de tiempo.
    2.  **Evaluación:** Actualizar los riesgos en `STATUS.md` y anotar ideas de mitigación en `BITACORA.md`.
    3.  **Escalada:** Definir una política de escalada si no se resuelve en un plazo determinado (por ejemplo, un día hábil).
    4.  **Resolución:** Documentar los pasos de la solución en `BITACORA.md` y actualizar el estado del bloqueo a `resolved`.
    5.  **Retrospectiva:** Capturar las lecciones aprendidas.
9.  **Disciplina de Documentación:**
    *   `BITACORA.md`: Debe registrar cronológicamente cada cambio de estado, decisión o excepción.
    *   `STATUS.md`: Debe actualizarse al menos una vez al día o después de cada merge de PR.
    *   `PLAN.md`: Es la fuente de verdad para los hitos y asignaciones de tareas.
10. **Responsabilidades del Agente de IA:**
    *   Analizar el archivo YAML del proyecto antes de actuar.
    *   No abrir PRs sin confirmar que el estado de la tarea es `in_review`.
    *   Documentar suposiciones en `BITACORA.md` cuando haya incertidumbre.
11. **Cumplimiento y Aplicación:**
    *   Mencionar que la Integración Continua (CI) debe validar la presencia y estructura de los archivos requeridos.
    *   Establecer que se realizarán auditorías periódicas."

---

### 3. `PLAN.md`

**Prompt:**

"Crea un archivo `PLAN.md` que sirva como el documento central de planificación para nuestro proyecto, siguiendo la estructura del Modelo Canónico de Magnetar. El archivo debe ser claro, tabular y fácil de analizar tanto para humanos como para máquinas.

1.  **Título Principal:** 'Plan Canónico de [Nombre del Proyecto]'.
2.  **Introducción:** Una breve frase que indique que este plan captura los hitos, tareas, estimaciones y estado del proyecto, y que su estructura debe mantenerse intacta.
3.  **Tabla de Resumen de Hitos (Milestones):** Una tabla con las siguientes columnas:
    *   `Milestone ID`: Un identificador único (por ejemplo, `ms-01`).
    *   `Name`: Un nombre descriptivo para el hito (por ejemplo, 'Iniciación del Proyecto').
    *   `Target Date`: La fecha objetivo de finalización.
    *   `Description`: Una breve descripción de lo que implica el hito.
    *   `Completion Criteria`: Criterios claros y medibles que definen cuándo se completa el hito.
    *   Rellena la tabla con 1-3 hitos de ejemplo relevantes para el inicio del proyecto.
4.  **Tabla de Backlog de Tareas:** Una tabla detallada que enumere todas las tareas del proyecto, con las siguientes columnas:
    *   `Task ID`: Un identificador único (por ejemplo, `task-101`).
    *   `Milestone`: El `Milestone ID` al que pertenece la tarea.
    *   `Title`: Un título conciso y descriptivo para la tarea.
    *   `Owner`: La persona o equipo responsable de la tarea.
    *   `Effort (pts)`: Una estimación del esfuerzo en puntos de historia.
    *   `Weight (%)`: El peso porcentual de la tarea en relación con el esfuerzo total (opcional pero recomendado).
    *   `State`: El estado actual de la tarea, que debe ser uno de los estados permitidos en `RULES.md` (`planned`, `ready`, `in_progress`, `blocked`, `in_review`, `done`).
    *   `Notes`: Cualquier nota adicional relevante (por ejemplo, enlaces a PRs o documentos).
    *   Rellena la tabla con 3-5 tareas de ejemplo con diferentes estados para ilustrar el formato.
5.  **Resumen de Esfuerzo:** Una sección que resuma el estado del esfuerzo total del proyecto:
    *   **Esfuerzo total:** Suma de todos los puntos de esfuerzo.
    *   **Completado:** Suma de los puntos de las tareas en estado `done`.
    *   **En progreso:** Suma de los puntos de las tareas en estado `in_progress`.
    *   **Restante:** Suma de los puntos de las tareas en otros estados.
6.  **Definiciones de Estado:** Una lista que defina claramente cada uno de los estados de tarea permitidos (`planned`, `ready`, `in_progress`, `blocked`, `in_review`, `done`) para eliminar cualquier ambigüedad.
7.  **Gestión de Cambios:** Una nota final que indique que este documento debe actualizarse siempre que las tareas cambien de estado o alcance, y que los cambios deben reflejarse en el archivo YAML del proyecto y en `BITACORA.md`."

---

### 4. `BITACORA.md`

**Prompt:**

"Crea un archivo `BITACORA.md` que funcione como un registro cronológico inmutable de todos los eventos significativos del proyecto. Este archivo es crucial para la auditoría, la transparencia y el seguimiento del historial del proyecto.

1.  **Título Principal:** 'Bitácora del Proyecto [Nombre del Proyecto]'.
2.  **Introducción:** Una breve descripción que indique que este documento es un 'logbook' o diario de a bordo que registra decisiones, cambios de estado, descubrimientos y eventos clave en orden cronológico inverso (lo más reciente primero).
3.  **Formato de Entrada:** Especifica que cada entrada en la bitácora debe seguir un formato estricto y consistente:
    *   **Timestamp:** Una marca de tiempo en formato `YYYY-MM-DD HH:MM Z` (por ejemplo, `2024-01-15 10:30 UTC`).
    *   **Author:** El nombre de la persona o agente de IA que realiza la entrada.
    *   **Entry:** Una descripción clara y concisa del evento.
4.  **Categorías de Entradas:** Indica que las entradas deben ser auto-descriptivas y pueden incluir, entre otras, las siguientes categorías de eventos:
    *   **State Change:** Cambio de estado de una tarea (por ejemplo, `task-101: state changed from 'in_progress' to 'in_review'`).
    *   **Decision:** Una decisión clave tomada (por ejemplo, `Decision: Adopted PostgreSQL over MySQL for the main database`).
    *   **Blocker:** Creación o resolución de un bloqueo (por ejemplo, `Blocker-001 created: API access denied`).
    *   **Discovery:** Un hallazgo importante o una nueva idea (por ejemplo, `Discovery: Found a critical vulnerability in the authentication library`).
    *   **PR Merge:** Fusión de un Pull Request (por ejemplo, `PR #12 merged: Implemented user authentication feature`).
    *   **Exception:** Una desviación documentada de las reglas canónicas.
5.  **Entradas de Ejemplo:** Proporciona 3-4 entradas de ejemplo que demuestren el formato y la variedad de eventos que se deben registrar. Por ejemplo:

    ---
    **Timestamp:** 2024-01-15 14:00 UTC
    **Author:** Jules
    **Entry:** `task-102`: state changed from `in_progress` to `in_review`. Awaiting approval from governance board.

    ---
    **Timestamp:** 2024-01-15 11:45 UTC
    **Author:** Kai
    **Entry:** `Blocker-001` created: Staging environment deployment is failing due to authentication key mismatch. `task-201` is now `blocked`.

    ---
    **Timestamp:** 2024-01-14 09:00 UTC
    **Author:** Mira
    **Entry:** Decision: The team has decided to use React for the frontend framework based on the prototype's performance. `REQUIREMENTS.md` updated.
    ---

6.  **Inmutabilidad:** Añade una nota final que resalte que la bitácora no debe ser alterada. Las correcciones deben hacerse añadiendo una nueva entrada que aclare o corrija una entrada anterior, en lugar de modificar el historial."

---

### 5. `REQUIREMENTS.md`

**Prompt:**

"Crea un archivo `REQUIREMENTS.md` que defina clara y exhaustivamente los requisitos funcionales y no funcionales del proyecto.

1.  **Título Principal:** 'Requisitos del Proyecto [Nombre del Proyecto]'.
2.  **Secciones para Requisitos Funcionales y No Funcionales:** Divide el documento en secciones claras para cada tipo de requisito.
3.  **Priorización y Etiquetado:** Utiliza etiquetas como 'Must-Have', 'Should-Have', 'Could-Have' y 'Won't-Have' (MoSCoW) para priorizar los requisitos."

---

### 6. `ARCHITECTURE.md`

**Prompt:**

"Crea un archivo `ARCHITECTURE.md` que describa la estructura de alto nivel del sistema, sus componentes y las decisiones de diseño clave.

1.  **Título Principal:** 'Arquitectura del Proyecto [Nombre del Proyecto]'.
2.  **Diagrama de Arquitectura:** Incluye un diagrama de alto nivel (puede ser en formato de texto o un enlace a una imagen) que muestre los componentes principales del sistema y sus interacciones.
3.  **Descripción de Componentes:** Proporciona una breve descripción de cada componente principal, su responsabilidad y las tecnologías utilizadas."

---

### 7. `STATUS.md`

**Prompt:**

"Crea un archivo `STATUS.md` que ofrezca una visión general rápida y actualizada del estado del proyecto.

1.  **Título Principal:** 'Estado del Proyecto [Nombre del Proyecto]'.
2.  **Resumen de Progreso:** Muestra el progreso general del proyecto, idealmente con una barra de progreso o un porcentaje de finalización.
3.  **Hitos Actuales:** Lista los hitos actuales y su estado (por ejemplo, 'En progreso', 'Completado').
4.  **Riesgos y Mitigaciones:** Enumera los riesgos identificados y las estrategias de mitigación."

---

### 8. `TESTING.md`

**Prompt:**

"Crea un archivo `TESTING.md` que describa la estrategia de pruebas del proyecto, los tipos de pruebas a realizar y los criterios de aceptación.

1.  **Título Principal:** 'Estrategia de Pruebas de [Nombre del Proyecto]'.
2.  **Tipos de Pruebas:** Describe los diferentes tipos de pruebas que se llevarán a cabo (por ejemplo, unitarias, de integración, de extremo a extremo).
3.  **Cobertura de Código:** Especifica el objetivo de cobertura de código para las pruebas automatizadas.
4.  **Proceso de Informe de Errores:** Define el proceso para informar y rastrear errores."

---

### 9. `BLOCKERS.md`

**Prompt:**

"Crea un archivo `BLOCKERS.md` para documentar y gestionar todos los impedimentos que obstaculizan el progreso del proyecto.

1.  **Título Principal:** 'Bloqueos del Proyecto [Nombre del Proyecto]'.
2.  **Tabla de Bloqueos:** Utiliza una tabla para rastrear los bloqueos, con columnas para 'ID', 'Descripción', 'Fecha de Creación', 'Propietario' y 'Estado' ('Activo', 'Resuelto').
3.  **Proceso de Escalada:** Describe el proceso a seguir si un bloqueo no se resuelve en un tiempo determinado."

---

### 10. `BRANCHING_MODEL.md`, `CONTRIBUTING.md`, `WIP_GUIDELINES.md`

**Prompt:**

"Crea los siguientes archivos de gobernanza:

*   **`BRANCHING_MODEL.md`:** Describe el modelo de ramificación Git del proyecto (por ejemplo, GitFlow).
*   **`CONTRIBUTING.md`:** Proporciona directrices para los contribuidores, incluyendo cómo configurar el entorno de desarrollo y el proceso de envío de Pull Requests.
*   **`WIP_GUIDELINES.md`:** Define las políticas de Trabajo en Progreso (WIP) y los límites para el equipo."

---

### 11. `projects/_template.project.yml`

**Prompt:**

"Crea un archivo de plantilla YAML llamado `_template.project.yml` en el directorio `projects`. Este archivo servirá como el esquema canónico legible por máquina para la configuración de proyectos.

El archivo debe incluir secciones para:

*   **`metadata`:** Nombre del proyecto, descripción, fecha de inicio.
*   **`stakeholders`:** Lista de partes interesadas clave y sus roles.
*   **`milestones`:** Una lista de hitos con sus ID, nombres y fechas objetivo.
*   **`tasks`:** Una lista de tareas con sus ID, títulos, propietarios y estados iniciales.
*   **`risks`:** Un registro de riesgos potenciales.
*   **`reporting`:** Ganchos o configuraciones para informes automatizados."
