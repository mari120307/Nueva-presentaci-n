import streamlit as st

# -------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -------------------------------------

st.set_page_config(
    page_title="IA y detección temprana de trastornos del aprendizaje",
    page_icon="🧠",
    layout="wide"
)

# -------------------------------------
# ESTILO CSS
# -------------------------------------

st.markdown("""
<style>

body{
    background-color:#f7f5f2;
}

.card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0 4px 15px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.quote{
    text-align:right;
    font-style:italic;
    color:#555;
    margin-bottom:25px;
}

.ref{
    background:#f3e9dc;
    padding:10px 15px;
    border-radius:15px;
    margin:5px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------
# TITULO
# -------------------------------------

st.title("Impacto de la Inteligencia Artificial en la detección temprana de trastornos del aprendizaje")

st.markdown(
"""
<div class="quote">
"La inteligencia artificial no reemplaza al docente, lo potencia: abre caminos para que cada estudiante alcance su máximo potencial."
</div>
""",
unsafe_allow_html=True
)

# -------------------------------------
# MENÚ DE NAVEGACIÓN
# -------------------------------------

menu = st.sidebar.radio(
    "Navegación",
    [
        "Resumen",
        "Conceptos clave",
        "Beneficios",
        "Desafíos",
        "Perspectivas futuras",
        "Artículos relacionados",
        "Referencias"
    ]
)

# -------------------------------------
# RESUMEN
# -------------------------------------

if menu == "Resumen":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Resumen divulgativo")

    st.write("""
La inteligencia artificial (IA) está transformando la detección temprana de trastornos del aprendizaje.
Mediante el análisis de datos académicos y patrones de comportamiento, los sistemas inteligentes pueden
identificar señales de dificultades como dislexia, problemas de atención o dificultades lectoras.

Esto permite intervenciones educativas más tempranas y personalizadas, favoreciendo una educación inclusiva.

Sin embargo, es importante que la IA se utilice de manera ética y responsable,
como complemento del trabajo docente y respetando la privacidad de los datos educativos.
""")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------
# CONCEPTOS CLAVE
# -------------------------------------

elif menu == "Conceptos clave":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Conceptos clave")

    st.markdown("""
**Inteligencia Artificial (IA)**  
Tecnología que simula procesos de razonamiento humano mediante algoritmos y aprendizaje automático.

**Trastornos del aprendizaje**  
Dificultades específicas en lectura, escritura, atención o procesamiento de información.

**Detección temprana**  
Identificación de señales iniciales que permiten intervenir antes de que las dificultades se agraven.

**Educación inclusiva**  
Modelo educativo que busca atender la diversidad de estudiantes.

**Ética en IA**  
Uso responsable de datos, transparencia algorítmica y protección de la privacidad.
""")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------
# BENEFICIOS
# -------------------------------------

elif menu == "Beneficios":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Beneficios de la IA")

    st.markdown("""
✔ Mayor precisión en la identificación de dificultades de aprendizaje.

✔ Análisis de grandes volúmenes de datos educativos.

✔ Intervenciones educativas más tempranas.

✔ Personalización del aprendizaje.

✔ Apoyo en la toma de decisiones pedagógicas.
""")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------
# DESAFÍOS
# -------------------------------------

elif menu == "Desafíos":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Desafíos y consideraciones éticas")

    st.markdown("""
• Privacidad de datos estudiantiles  
• Sesgos en algoritmos de inteligencia artificial  
• Brecha digital entre instituciones educativas  
• Necesidad de capacitación docente en IA  
• Evitar la deshumanización del proceso educativo
""")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------
# PERSPECTIVAS FUTURAS
# -------------------------------------

elif menu == "Perspectivas futuras":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Perspectivas futuras")

    st.write("""
La inteligencia artificial continuará evolucionando en el ámbito educativo.

En el futuro, los sistemas inteligentes podrán integrarse con plataformas educativas
para ofrecer evaluaciones continuas, personalizadas y adaptativas.

Sin embargo, su implementación debe equilibrar la innovación tecnológica con
los valores humanos, garantizando la participación activa del docente.
""")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------
# ARTÍCULOS RELACIONADOS
# -------------------------------------

elif menu == "Artículos relacionados":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Artículos relacionados")

    articulo = st.selectbox(
        "Selecciona un artículo",
        [
            "NeurekaLAB y detección temprana",
            "IA en educación personalizada",
            "IA en educación infantil"
        ]
    )

    if articulo == "NeurekaLAB y detección temprana":

        st.write("""
La plataforma NeurekaLAB utiliza inteligencia artificial y gamificación para detectar
trastornos del aprendizaje mediante minijuegos que analizan patrones cognitivos
y comportamientos de los estudiantes.
""")

    elif articulo == "IA en educación personalizada":

        st.write("""
Los sistemas de inteligencia artificial permiten analizar el desempeño estudiantil
para adaptar contenidos educativos a las necesidades individuales.
""")

    elif articulo == "IA en educación infantil":

        st.write("""
La inteligencia artificial puede apoyar el desarrollo cognitivo y lingüístico
en la educación infantil mediante herramientas adaptativas y entornos digitales.
""")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------
# REFERENCIAS
# -------------------------------------

elif menu == "Referencias":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Referencias académicas")

    st.markdown("""
**Sphaera E (2024)**  
Impacto de la realidad virtual en la terapia de trastornos de ansiedad.

**Espinosa P (2024)**  
Impacto de la inteligencia artificial en la detección temprana de trastornos del aprendizaje.

**García M (2025)**  
La inteligencia artificial en la educación: hacia un aprendizaje personalizado.

**NeurekaLAB (2023)**  
Gamificación y detección temprana de trastornos del aprendizaje.
""")

    st.markdown('</div>', unsafe_allow_html=True)
