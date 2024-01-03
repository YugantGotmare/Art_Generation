import streamlit as st
import matplotlib.pyplot as plt
from samila import GenerativeImage
from samila import Projection
from samila import VALID_COLORS

import random
from math import sin, cos
from io import BytesIO


st.title("Generative Art in Python")

fn1 = st.sidebar.selectbox("First EQ", ['sin', 'cos'])
fn2 = st.sidebar.selectbox("Second EQ", ['sin', 'cos'])

def f1(x, y):
    if fn1 == 'sin':
        result = random.uniform(-1, 1) * x**2 - sin(y**2) + abs(y-x)
    elif fn1 == 'cos':
        result = random.uniform(-1, 1) * x**2 - cos(y**2) + abs(y-x)
    return result

def f2(x, y):
    if fn2 == 'cos':
        result = random.uniform(-1, 1) * y**3 - cos(x**2) + 2*x
    elif fn2 == 'sin':
        result = random.uniform(-1, 1) * y**3 - sin(x**2) + 2*x
    return result

projections = st.sidebar.radio("Select the Art Projection here:",
                                options=["RECTILINEAR", "POLAR", "AITOFF", "HAMMER", "LAMBERT", "MOLLWEIDE"])

color = st.sidebar.selectbox("Color:", VALID_COLORS, index=30)
bgcolor = st.sidebar.selectbox("BGColor:", VALID_COLORS, index=15)

with st.spinner("Generating..."):
    g = GenerativeImage(f1, f2)
    g.generate()

    st.set_option('deprecation.showPyplotGlobalUse', False)  # Disable the warning
    generated_plot = g.plot(color=color, bgcolor=bgcolor, projection=eval("Projection." + projections))
    st.pyplot(generated_plot)

