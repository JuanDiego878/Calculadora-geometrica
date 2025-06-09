import math
import streamlit as st

st.set_page_config(page_title="Calculadora Geométrica", layout="centered")

# Traducción multilenguaje
lang = st.selectbox("Idioma / Language / Langue / Sprache", ["Español", "English", "Français", "Deutsch"])

def t(es, en, fr, de):
    if lang == "Español": return es
    if lang == "English": return en
    if lang == "Français": return fr
    if lang == "Deutsch": return de

st.title(t("Calculadora de Figuras Geométricas", "Geometric Shapes Calculator", "Calculateur de Formes Géométriques", "Geometrischer Rechner"))

figura = st.selectbox(t("Elige una figura", "Choose a shape", "Choisissez une forme", "Wähle eine Figur"), [
    "Cubo", "Prisma rectangular", "Prisma triangular", "Cilindro", "Cono", "Esfera",
    "Pirámide", "Tetraedro", "Octaedro", "Dodecaedro", "Icosaedro"
])

modo = st.radio(t("¿Qué quieres calcular?", "What do you want to calculate?", "Que voulez-vous calculer ?", "Was willst du berechnen?"), 
                ["Área", "Volumen", "Ambos"])

def resultado(label, valor):
    st.success(f"{label}: {valor:.2f} m²" if "área" in label.lower() else f"{label}: {valor:.2f} m³")

if figura == "Cubo":
    l = st.number_input(t("Lado", "Side", "Côté", "Seite"), min_value=0.0)
    if modo != "Volumen": resultado("Área del cubo", 6 * l**2)
    if modo != "Área": resultado("Volumen del cubo", l**3)

elif figura == "Prisma rectangular":
    l = st.number_input("Largo / Length", min_value=0.0)
    w = st.number_input("Ancho / Width", min_value=0.0)
    h = st.number_input("Altura / Height", min_value=0.0)
    if modo != "Volumen": resultado("Área del prisma", 2 * (l*w + l*h + w*h))
    if modo != "Área": resultado("Volumen del prisma", l * w * h)

elif figura == "Prisma triangular":
    b = st.number_input("Base del triángulo", min_value=0.0)
    h_t = st.number_input("Altura del triángulo", min_value=0.0)
    l = st.number_input("Altura del prisma", min_value=0.0)
    area_base = 0.5 * b * h_t
    if modo != "Volumen": resultado("Área del prisma triangular", b*h_t + 3 * (b * l))  # Aprox.
    if modo != "Área": resultado("Volumen del prisma", area_base * l)

elif figura == "Cilindro":
    r = st.number_input("Radio", min_value=0.0)
    h = st.number_input("Altura", min_value=0.0)
    if modo != "Volumen": resultado("Área del cilindro", 2 * math.pi * r * (r + h))
    if modo != "Área": resultado("Volumen del cilindro", math.pi * r**2 * h)

elif figura == "Cono":
    r = st.number_input("Radio", min_value=0.0)
    g = st.number_input("Generatriz", min_value=0.0)
    h = st.number_input("Altura", min_value=0.0)
    if modo != "Volumen": resultado("Área del cono", math.pi * r * (r + g))
    if modo != "Área": resultado("Volumen del cono", (1/3) * math.pi * r**2 * h)

elif figura == "Esfera":
    r = st.number_input("Radio", min_value=0.0)
    if modo != "Volumen": resultado("Área de la esfera", 4 * math.pi * r**2)
    if modo != "Área": resultado("Volumen de la esfera", (4/3) * math.pi * r**3)

elif figura == "Pirámide":
    b = st.number_input("Área de la base", min_value=0.0)
    h = st.number_input("Altura", min_value=0.0)
    if modo != "Volumen": st.info("El área depende de la forma de la base (triangular, cuadrada, etc.)")
    if modo != "Área": resultado("Volumen de la pirámide", (1/3) * b * h)

elif figura == "Tetraedro":
    a = st.number_input("Arista", min_value=0.0)
    if modo != "Volumen": resultado("Área del tetraedro", math.sqrt(3) * a**2)
    if modo != "Área": resultado("Volumen del tetraedro", (a**3) / (6 * math.sqrt(2)))

elif figura == "Octaedro":
    a = st.number_input("Arista", min_value=0.0)
    if modo != "Volumen": resultado("Área del octaedro", 2 * math.sqrt(3) * a**2)
    if modo != "Área": resultado("Volumen del octaedro", (math.sqrt(2)/3) * a**3)

elif figura == "Dodecaedro":
    a = st.number_input("Arista", min_value=0.0)
    if modo != "Volumen": resultado("Área del dodecaedro", 3 * math.sqrt(25 + 10*math.sqrt(5)) * a**2)
    if modo != "Área": resultado("Volumen del dodecaedro", ((15 + 7*math.sqrt(5))/4) * a**3)

elif figura == "Icosaedro":
    a = st.number_input("Arista", min_value=0.0)
    if modo != "Volumen": resultado("Área del icosaedro", 5 * math.sqrt(3) * a**2)
    if modo != "Área": resultado("Volumen del icosaedro", (5 * (3 + math.sqrt(5))/12) * a**3)
