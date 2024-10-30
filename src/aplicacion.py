import streamlit as st

st.set_page_config(layout="wide")

st.title('Aplicación de prueba')

with st.expander('About this app'):
    st.write('Hola, ando experimentando cositas para mi primera aplicacion de streamlit')
    st.write('Andamos subiendo de nivel, sabe')
    st.image('https://i.blogs.es/b1a267/original/500_333.jpeg', width=400)

st.sidebar.header('Opciones pa interactuar')
user_name = st.sidebar.text_input('Cual es tu nombre?')
user_emoji = st.sidebar.selectbox('Elige un emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱', '🤏'])
user_food = st.sidebar.selectbox('Cual es tu comida favorita?', ['', 'Sandwich', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza', 'Comida asiatica', 'Ninguna de las anteriores'])

st.header('Que he aprendido sobre ti?')

col1, col2, col3 = st.columns(3)

with col1:
    if user_name != '':
        st.write(f'Tu nombre es {user_name}, 👋  Hola {user_name}!')
    else:
        st.write('👈 Por favor pon tu **nombre**!')

with col2:
    if user_emoji != '' and user_emoji == '🤏':
        st.write(f'Así {user_emoji} de chiquita la tienes')
    elif user_emoji != '':
        st.write(f'{user_emoji} es tu emoji favorito (de los que había para elegir)')
    else:
        st.write('👈 Por favor elige un **emoji**!')

with col3:
    if user_food != '' and user_food == 'Ninguna de las anteriores':
        st.write('A usted no le gusta es nada mlp 😡')
    elif user_food != '':
        st.write(f'🍴 **{user_food}** es tu comida **favorita**!')
    else:
        st.write('👈 Por favor elige tu comida **favorita**!')