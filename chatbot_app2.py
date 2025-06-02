import streamlit as st
import nltk

nltk.download('punkt')

from nltk.tokenize import sent_tokenize

def chatbot(user_input):
    sentences = sent_tokenize(user_input)
    if sentences:
        return "Tu as dit : " + sentences[0]
    else:
        return "Je n'ai pas compris."

def main():
    st.title("Chatbot Descartes")
    st.write("Pose une question sur le texte ou écris ce que tu veux.")
    user_input = st.text_input("Ta question :")
    if user_input:
        response = chatbot(user_input)
        st.write("Réponse :", response)

if __name__ == '__main__':
    main()
