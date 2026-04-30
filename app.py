import streamlit as st
import numpy as np

from src.math_utils import (
    magnitude,
    dot_product,
    angle_between,
    projection,
    rotate_vector
)

from src.plot_utils import draw_vector, draw_two_vectors

st.title("🚀 Linear Algebra Visual Lab")

menu = st.sidebar.selectbox(
    "Choose Topic",
    ["Vector", "Dot Product", "Projection", "Rotation"]
)

# --------------------------------------
# VECTOR
# --------------------------------------
if menu == "Vector":

    x = st.slider("X", -10,10,3)
    y = st.slider("Y", -10,10,4)

    v = np.array([x,y])

    st.write("Magnitude =", magnitude(v))

    fig = draw_vector(v,"Vector")
    st.pyplot(fig)

# --------------------------------------
# DOT PRODUCT
# --------------------------------------
elif menu == "Dot Product":

    a = np.array([
        st.slider("A_x",-10,10,3),
        st.slider("A_y",-10,10,4)
    ])

    b = np.array([
        st.slider("B_x",-10,10,4),
        st.slider("B_y",-10,10,1)
    ])

    st.write("Dot Product =", dot_product(a,b))
    st.write("Angle =", angle_between(a,b))

    fig = draw_two_vectors(a,b,"Dot Product Geometry")
    st.pyplot(fig)

# --------------------------------------
# PROJECTION
# --------------------------------------
elif menu == "Projection":

    a = np.array([3,4])
    b = np.array([1,2])

    proj = projection(a,b)

    st.write("Projection =", proj)

    fig = draw_two_vectors(a,proj,"Projection")
    st.pyplot(fig)

# --------------------------------------
# ROTATION
# --------------------------------------
elif menu == "Rotation":

    angle = st.slider("Angle",0,360,90)

    v = np.array([2,1])
    new = rotate_vector(v,angle)

    fig = draw_two_vectors(v,new,"Rotation")
    st.pyplot(fig)