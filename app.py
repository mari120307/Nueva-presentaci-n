import streamlit as st
import pandas as pd

# ---------------- CONFIGURACIÓN GENERAL ----------------

st.set_page_config(
    page_title="IA y detección temprana de trastornos del aprendizaje",
    layout="wide"
)

# ---------------- ESTILOS ----------------

st.markdown("""
<style>

body {
background-color: #f7f9f7;
}

.block-container{
padding-top:2rem;
}

.card {
background-color:white;
padding:25px;
border-radius:18px;
box-shadow:0 4px 12px rgba(0,0,0,0.08);
margin-bottom:20px;
}

.frase {
text-align:right;
font-style:italic;
color:#3b6f3b;
}

</style>
""", unsafe_allow_html=True)

# ---------------- MENÚ LATERAL ----------------

st.sidebar.title("📚 Navegación")

pagina = st.sidebar.radio(
"Selecciona un apartado:",
[
"Inicio",
"Introducción",
"Trastornos del aprendizaje",
"Detección temprana",
"Educación inclusiva",
"Ética en IA",
"Beneficios de la IA",
"Desafíos",
"Perspectivas futuras",
"Percepción docente",
"Conceptos clave",
"Conclusiones",
"Referencias"
]
)

# ---------------- INICIO ----------------

if pagina == "Inicio":

    st.title("El impacto de la inteligencia artificial en la detección temprana de trastornos del aprendizaje")

    st.markdown("""
<p class="frase">
"La inteligencia artificial no reemplaza al docente, lo potencia: abre caminos para que cada estudiante alcance su máximo potencial."
</p>
""", unsafe_allow_html=True)

    st.write("""
La inteligencia artificial (IA) se ha convertido en una de las tecnologías más influyentes en el ámbito educativo contemporáneo. 
Su capacidad para analizar grandes volúmenes de datos, identificar patrones complejos y generar predicciones ha abierto nuevas posibilidades para mejorar los procesos de enseñanza y aprendizaje.

En el campo de la psicopedagogía, la IA está siendo utilizada para apoyar la detección temprana de trastornos del aprendizaje, permitiendo identificar señales que tradicionalmente podían pasar desapercibidas en los métodos de evaluación convencionales.
""")

# ---------------- INTRODUCCIÓN ----------------

elif pagina == "Introducción":

    st.header("Introducción")

    st.write("""
Los trastornos del aprendizaje constituyen una problemática significativa dentro del sistema educativo. Estas dificultades pueden manifestarse en procesos como la lectura, escritura, razonamiento matemático o atención.

Tradicionalmente, su diagnóstico dependía de evaluaciones psicopedagógicas, observación docente y pruebas estandarizadas. Sin embargo, estos métodos pueden requerir largos periodos de observación.

La inteligencia artificial permite analizar datos educativos como resultados académicos, tiempos de respuesta en tareas digitales, patrones de error y comportamiento en plataformas educativas, lo que facilita identificar tempranamente posibles dificultades.
""")

# ---------------- TRASTORNOS ----------------

elif pagina == "Trastornos del aprendizaje":

    st.header("Trastornos del aprendizaje")

    st.write("""
Los trastornos del aprendizaje son alteraciones en procesos cognitivos que afectan la adquisición y uso de habilidades académicas.

Entre los más comunes se encuentran:

**Dislexia**
- Dificultad en la lectura y decodificación de palabras.
- Problemas en fluidez lectora y comprensión.

**Discalculia**
- Dificultades en el razonamiento matemático.
- Problemas para comprender conceptos numéricos.

**TDAH**
- Dificultades para mantener la atención.
- Conductas impulsivas e hiperactividad.

Estas condiciones pueden generar consecuencias como bajo rendimiento escolar, dificultades emocionales y disminución de la autoestima.
""")

# ---------------- DETECCIÓN TEMPRANA ----------------

elif pagina == "Detección temprana":

    st.header("Detección temprana")

    st.write("""
La detección temprana se refiere a la identificación oportuna de señales que indican posibles dificultades en el aprendizaje.

La inteligencia artificial puede analizar:

- Resultados académicos
- Interacciones en plataformas educativas
- Patrones de error en tareas escolares
- Ritmo de aprendizaje

Esto permite generar alertas tempranas que facilitan intervenciones educativas más rápidas y eficaces.
""")

# ---------------- EDUCACIÓN INCLUSIVA ----------------

elif pagina == "Educación inclusiva":

    st.header("Educación inclusiva")

    st.write("""
La educación inclusiva busca garantizar que todos los estudiantes tengan acceso a oportunidades de aprendizaje independientemente de sus capacidades o contextos sociales.

La IA contribuye a este enfoque mediante:

- Personalización de contenidos educativos
- Adaptación del ritmo de aprendizaje
- Identificación de necesidades educativas específicas
- Generación de estrategias pedagógicas diferenciadas
""")

# ---------------- ÉTICA ----------------

elif pagina == "Ética en IA":

    st.header("Ética en Inteligencia Artificial")

    st.write("""
El uso de inteligencia artificial en educación plantea desafíos éticos importantes.

Entre los principales aspectos a considerar se encuentran:

- Protección de la privacidad de datos estudiantiles
- Transparencia en los algoritmos utilizados
- Prevención de sesgos algorítmicos
- Uso responsable de la tecnología

Es fundamental que la IA sea utilizada como **herramienta complementaria del docente**, evitando reemplazar la interacción humana en el proceso educativo.
""")

# ---------------- BENEFICIOS ----------------

elif pagina == "Beneficios de la IA":

    st.header("Beneficios de la Inteligencia Artificial")

    st.write("""
Entre los beneficios más importantes de la IA en la educación se encuentran:

- Mayor precisión en la identificación de dificultades de aprendizaje mediante el análisis de grandes volúmenes de datos.
- Intervenciones educativas más tempranas que permiten apoyar al estudiante antes de que las dificultades se agraven.
- Personalización del aprendizaje adaptando contenidos, actividades y ritmo de enseñanza.
- Evaluación continua del progreso académico mediante plataformas educativas digitales.
- Apoyo en la toma de decisiones pedagógicas para docentes y especialistas.

Además, estas herramientas pueden facilitar la accesibilidad educativa para estudiantes con necesidades educativas especiales.
""")

# ---------------- DESAFÍOS ----------------

elif pagina == "Desafíos":

    st.header("Desafíos del uso de IA")

    st.write("""
A pesar de sus beneficios, la implementación de la IA en educación enfrenta diversos desafíos:

- Riesgo de sesgos algorítmicos que pueden generar evaluaciones injustas.
- Protección de datos personales y privacidad de los estudiantes.
- Dependencia excesiva de herramientas tecnológicas.
- Brecha digital entre instituciones educativas con diferentes recursos.
- Necesidad de capacitación docente en el uso de tecnologías basadas en inteligencia artificial.

Por ello, es importante desarrollar políticas educativas y marcos éticos que regulen su uso.
""")

# ---------------- PERSPECTIVAS ----------------

elif pagina == "Perspectivas futuras":

    st.header("Perspectivas futuras")

    st.write("""
Las perspectivas futuras del uso de inteligencia artificial en educación apuntan hacia un desarrollo cada vez más integrado con otras disciplinas.

Entre las principales líneas de investigación se encuentran:

- Desarrollo de algoritmos más transparentes y explicables.
- Integración con neurociencia y psicología educativa.
- Uso de analíticas de aprendizaje para identificar estudiantes en riesgo académico.
- Incorporación de realidad virtual y gamificación en procesos de evaluación.
- Creación de plataformas educativas inteligentes que se adapten automáticamente al progreso del estudiante.

Estas innovaciones podrían transformar profundamente los procesos educativos.
""")

# ---------------- PERCEPCIÓN DOCENTE ----------------

elif pagina == "Percepción docente":

    st.header("Percepción y rol de los docentes")

    st.write("""
Los docentes desempeñan un papel fundamental en la integración de la inteligencia artificial en el aula.

Aunque la tecnología ofrece herramientas avanzadas de análisis educativo, el docente continúa siendo el principal mediador del aprendizaje.

Entre sus funciones destacan:

- Interpretar los datos generados por sistemas de IA.
- Diseñar intervenciones pedagógicas personalizadas.
- Acompañar emocional y académicamente a los estudiantes.
- Garantizar un uso ético y responsable de la tecnología.
- Promover el pensamiento crítico y el aprendizaje significativo.

La inteligencia artificial no busca reemplazar al docente, sino fortalecer su capacidad para apoyar a los estudiantes.
""")

# ---------------- CONCEPTOS CLAVE ----------------

elif pagina == "Conceptos clave":

    st.header("Conceptos clave")

    data = {
    "Concepto":[
    "Trastornos del aprendizaje",
    "Detección temprana",
    "Educación inclusiva",
    "Ética en IA"
    ],

    "Definición":[
    "Dificultades en procesos cognitivos relacionados con lectura, escritura, cálculo o atención que afectan el rendimiento académico.",
    "Proceso de identificar señales iniciales de dificultades en el aprendizaje para intervenir oportunamente.",
    "Modelo educativo que busca garantizar oportunidades de aprendizaje para todos los estudiantes.",
    "Principios que regulan el uso responsable de la inteligencia artificial, como privacidad de datos y transparencia."
    ]
    }

    df = pd.DataFrame(data)

    st.table(df)

    st.write("""
Estos conceptos permiten comprender la relación entre tecnología educativa, detección temprana de dificultades y desarrollo de estrategias pedagógicas inclusivas.
""")

# ---------------- CONCLUSIONES ----------------

elif pagina == "Conclusiones":

    st.header("Conclusiones")

    st.write("""
La inteligencia artificial representa una herramienta con gran potencial para mejorar la detección temprana de trastornos del aprendizaje.

Su capacidad para analizar datos educativos permite identificar patrones complejos que facilitan intervenciones pedagógicas oportunas.

Sin embargo, su implementación debe realizarse de manera ética, garantizando siempre el papel central del docente en el proceso educativo.
""")

# ---------------- REFERENCIAS ----------------

elif pagina == "Referencias":

    st.header("Referencias académicas")

    with st.expander("1. Sphaera E. (2024)"):
        st.write("Impacto de la realidad virtual en la terapia de trastornos de ansiedad.")

    with st.expander("2. Alejandra P & Cevallos E. (2024)"):
        st.write("Modelo basado en IA para detección temprana de dificultades lectoras.")

    with st.expander("3. Espinosa P. (2024)"):
        st.write("Impacto de la inteligencia artificial en la detección temprana de trastornos del aprendizaje.")

    with st.expander("4. García M. (2025)"):
        st.write("La inteligencia artificial en la educación: hacia un aprendizaje personalizado.")

    with st.expander("5. NeurekaLAB (2023)"):
        st.write("Gamificación e inteligencia artificial para detección temprana de trastornos del aprendizaje.")

    with st.expander("6. Verzosi P. (2025)"):
        st.write("Uso de IA para potenciar el aprendizaje en educación infantil.")

    with st.expander("7. Vargas G. (2024)"):
        st.write("La inteligencia artificial y las estrategias de enseñanza-aprendizaje.")

    with st.expander("8. Gómez A. (2024)"):
        st.write("Desafíos éticos de la inteligencia artificial en la personalización del aprendizaje.")

    with st.expander("9. Martínez B. (2025)"):
        st.write("IA en procesos de enseñanza-aprendizaje: retos y oportunidades.")

    with st.expander("10. Vaca P. (2025)"):
        st.write("Analíticas del aprendizaje para identificación temprana de estudiantes en riesgo.")
