import streamlit as st
import pickle


model = pickle.load(open('sentiment_model.pkl', 'rb'))

st.title('Modelo de análise de sentimento')

review = st.text_input('Escreva sua avaliação:')

submit = st.button('Prever')

if submit:
    prediction = model.predict([review])

    if prediction[0] == 'pos':
        st.success('Avaliação Posititvo')
    else:
        st.error('Avaliação Negativa')