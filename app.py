import streamlit as st
import pandas as pd

# Configuración general
st.set_page_config(page_title="IA en la detección temprana", layout="wide")

# Sidebar de navegación
st.sidebar.title("Navegación")
pagina = st.sidebar.radio(
    "Selecciona una sección:",
    ["Resumen", "Conceptos clave", "Beneficios", "Desafíos", "Conclusiones", "Artículos relacionados", "Referencias"]
)

# Título principal
st.title("El impacto de la inteligencia artificial en la detección temprana de trastornos del aprendizaje")
st.markdown("<p style='text-align:right; font-style:italic;'>La inteligencia artificial no reemplaza al docente, lo potencia: abre caminos para que cada estudiante alcance su máximo potencial.</p>", unsafe_allow_html=True)

# Contenido según la página seleccionada
if pagina == "Resumen":
    st.header("Resumen")
    st.markdown("La IA permite identificar señales de dislexia, problemas de atención y dificultades lectoras mediante el análisis de datos académicos y patrones de comportamiento. Esto facilita intervenciones más rápidas y personalizadas, promoviendo una educación inclusiva.")

elif pagina == "Conceptos clave":
    st.header("Conceptos clave")
    conceptos = {
        "Trastornos del aprendizaje": "Dificultades específicas en lectura, escritura, atención o procesamiento de información.",
        "Detección temprana": "Identificación de señales iniciales para intervenir antes de que se agraven.",
        "Educación inclusiva": "Modelo que atiende la diversidad de estudiantes.",
        "Ética en IA": "Privacidad, transparencia y
