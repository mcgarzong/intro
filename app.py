import streamlit as st
from PIL import Image

st.title(" Laboratorio de emociones ")

st.header(" Exploro cómo se comunican las emociones con el cuerpo, la voz y el entorno ")
st.write(" Descubre más... ")
image = Image.open('dibujo.jpg')

st.image(image, caption='Interfaces multimodales')


texto= st.text_input('¿Como te sientes hoy?', 'Cuentame aquí')
st.write('Hoy te sientes...', texto)

st.subheader("Ahora usaremos  columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Mira aquiiii")
    st.write("Los gestos pueden cambiar cómo nos sentimos.")
    resp = st.checkbox('¿Has notado cómo cambia tu ánimo al sonreír?')
    if resp:
       st.write('Correcto!')
  
with col2:
    st.subheader("Tambien...")
    modo = st.radio("¿Qué tipo de expresión usas más para mostrar tus emociones?", ('Facial', 'Voz', 'Movimiento'))
    if modo == 'Facial':
       st.write('Cada emoción tiene su propio lenguaje')
    if modo == 'Voz':
       st.write('Cada emoción tiene su propio lenguaje')
    if modo == 'Movimiento':
       st.write('Cada emoción tiene su propio lenguaje')
        
st.subheader("Cambialo")
if st.button('Presiona para transformar tu emoción'):
    st.write('Gracias por presionar')
else:
    st.write('No has presionado aún')

st.subheader("Selecciona")
in_mod = st.selectbox(
    "Selecciona una emoción",
    ("Alegria", "Tristeza", "Calma"),
)
if in_mod == "Alegria":
    set_mod = ":)"
elif in_mod == "Tristeza":
    set_mod = ":("
elif in_mod == "Calma":
    set_mod = ":))"
st.write(" La acción es:" , set_mod)


with st.sidebar:
    st.subheader("Configura tus emociones")
    mod_radio = st.radio(
        "Escoge como te quieres sentir hoy",
        ("Feliz", "Emocionado","Concentrado")
    )
