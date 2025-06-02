import nltk
nltk.download('punkt')  # Télécharge le tokenizer nécessaire

from nltk.tokenize import sent_tokenize
import streamlit as st

# Exemple simple de fonction chatbot
def chatbot(user_input):
    sentences = sent_tokenize(user_input)
    # Juste un exemple : retourne la première phrase ou un message par défaut
    if sentences:
        return f"I found this sentence: '{sentences[0]}'"
    else:
        return "I didn't understand your input."

def main():
    st.title("Simple Chatbot")
    
    user_input = st.text_input("Ask me a question about the text:")
    
    if user_input:
        response = chatbot(user_input)
        st.write(response)

if __name__ == '__main__':
    main()
