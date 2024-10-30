import streamlit as st

st.title('st.form')

st.header('1. Ejemplo de uso de la notación `with`')
st.subheader('Maquina de Café')

with st.form('my_form'):
    st.write('**Ordena tu café**')

    coffee_bean_val = st.selectbox('Tipo de café', ['Colombiano', 'Americano', 'Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Termino del café', ['Claro', 'Medio', 'Negro'])
    brewing_val = st.selectbox('Metodo de elboración', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Como lo deseas', ['Caliente', 'Frio', 'Frappe'])
    milk_val = st.select_slider('Intesidad de la leche', ['Nada', 'Baja', 'Media', 'Alta'])
    owncup_val = st.checkbox('Traer taza propia')

    submitted = st.form_submit_button('Enviar')

if submitted:
    st.markdown(f'''
            ☕ Has ordenado:
            - Tipo de café: `{coffee_bean_val}`
            - Termino del café: `{coffee_roast_val}`
            - Elaboración: `{brewing_val}`
            - Lo deseas: `{serving_type_val}`
            - Leche: `{milk_val}`
            - Traer taza propia: `{owncup_val}`
            ''')
else:
    st.write('☝️ Crea tu orden!')

st.header('2. Ejemplo de notación de objetos')

form = st.form('my_form_2')
selected_val = form.slider('Selecciona un valor')
form.form_submit_button('Enviar')

st.write('Valor seleccionado: ', selected_val)