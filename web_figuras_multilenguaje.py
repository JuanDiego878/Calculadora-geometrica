import streamlit as st
import math

st.set_page_config(page_title="Calculadora Geométrica", page_icon="📐")

# Traducciones
traducciones = {
    "es": {
        "title": "📏 Calculadora de Área y Volumen",
        "figura": "Selecciona una figura geométrica",
        "tipo": "¿Qué quieres calcular?",
        "area": "Área",
        "volumen": "Volumen",
        "dim1": "Dimensión 1 (ej. lado, radio, base)",
        "dim2": "Dimensión 2",
        "dim3": "Dimensión 3",
        "calcular": "Calcular",
        "resultado": "El {tipo} es: {valor:.2f} {unidad}",
        "error": "Error en los cálculos. Revisa las dimensiones.",
    },
    "en": {
        "title": "📏 Area and Volume Calculator",
        "figura": "Select a geometric shape",
        "tipo": "What do you want to calculate?",
        "area": "Area",
        "volumen": "Volume",
        "dim1": "Dimension 1 (e.g., side, radius, base)",
        "dim2": "Dimension 2",
        "dim3": "Dimension 3",
        "calcular": "Calculate",
        "resultado": "The {tipo} is: {valor:.2f} {unidad}",
        "error": "Calculation error. Check the dimensions.",
    },
    "fr": {
        "title": "📏 Calculateur de surface et de volume",
        "figura": "Choisissez une forme géométrique",
        "tipo": "Que voulez-vous calculer ?",
        "area": "Surface",
        "volumen": "Volume",
        "dim1": "Dimension 1 (ex. côté, rayon, base)",
        "dim2": "Dimension 2",
        "dim3": "Dimension 3",
        "calcular": "Calculer",
        "resultado": "Le {tipo} est : {valor:.2f} {unidad}",
        "error": "Erreur de calcul. Vérifiez les dimensions.",
    }
}

# Selección de idioma
idioma = st.selectbox("🌍 Idioma / Language / Langue", ["Español", "English", "Français"])
cod_idioma = {"Español": "es", "English": "en", "Français": "fr"}[idioma]
T = traducciones[cod_idioma]

# Título
st.title(T["title"])

# Figuras disponibles
figura = st.selectbox(T["figura"], [
    "Cubo", "Prisma Rectangular", "Prisma Triangular", "Cilindro",
    "Cono", "Esfera", "Pirámide Cuadrada", "Tetraedro", "Octaedro",
    "Dodecaedro", "Icosaedro"
])

tipo = st.radio(T["tipo"], [T["area"], T["volumen"]])
tipo_base = "Área" if tipo == T["area"] else "Volumen"

# Función de cálculo
def calcular(figura, tipo, a, b=0, c=0):
    try:
        if figura == "Cubo":
            return 6 * a**2 if tipo == "Área" else a**3
        elif figura == "Prisma Rectangular":
            return 2 * (a*b + a*c + b*c) if tipo == "Área" else a*b*c
        elif figura == "Prisma Triangular":
            base_area = 0.5 * a * b
            return (2 * base_area + 3 * a * c) if tipo == "Área" else base_area * c
        elif figura == "Cilindro":
            return 2 * math.pi * a * (a + b) if tipo == "Área" else math.pi * a**2 * b
        elif figura == "Cono":
            g = math.sqrt(a**2 + b**2)
            return math.pi * a * (a + g) if tipo == "Área" else (1/3) * math.pi * a**2 * b
        elif figura == "Esfera":
            return 4 * math.pi * a**2 if tipo == "Área" else (4/3) * math.pi * a**3
        elif figura == "Pirámide Cuadrada":
            return a**2 + 2 * a * math.sqrt((a/2)**2 + b**2) if tipo == "Área" else (1/3) * a**2 * b
        elif figura == "Tetraedro":
            return math.sqrt(3) * a**2 if tipo == "Área" else (a**3) / (6 * math.sqrt(2))
        elif figura == "Octaedro":
            return 2 * math.sqrt(3) * a**2 if tipo == "Área" else (math.sqrt(2)/3) * a**3
        elif figura == "Dodecaedro":
            return 3 * math.sqrt(25 + 10 * math.sqrt(5)) * a**2 if tipo == "Área" else ((15 + 7 * math.sqrt(5))/4) * a**3
        elif figura == "Icosaedro":
            return 5 * math.sqrt(3) * a**2 if tipo == "Área" else (5 * (3 + math.sqrt(5)) / 12) * a**3
    except:
        return None

# Entradas
a = st.number_input(T["dim1"], min_value=0.0, format="%.2f")
b = c = 0

if figura in ["Prisma Rectangular", "Prisma Triangular", "Cilindro", "Cono", "Pirámide Cuadrada"]:
    b = st.number_input(T["dim2"], min_value=0.0, format="%.2f")

if figura in ["Prisma Rectangular", "Prisma Triangular"]:
    c = st.number_input(T["dim3"], min_value=0.0, format="%.2f")

# Botón calcular
if st.button(T["calcular"]):
    resultado = calcular(figura, tipo_base, a, b, c)
    if resultado is not None:
        unidad = "m²" if tipo_base == "Área" else "m³"
        st.success(T["resultado"].format(tipo=tipo, valor=resultado, unidad=unidad))
    else:
        st.error(T["error"])
