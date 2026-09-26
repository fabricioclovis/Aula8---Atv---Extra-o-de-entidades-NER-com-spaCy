import streamlit as st
import spacy

# carrega o modelo de português do spaCy
# instalar antes com: python -m spacy download pt_core_news_sm
nlp = spacy.load("pt_core_news_sm")

st.title("Atividade - Extração de entidades (NER) com spaCy")

texto = st.text_area(
    "Digite o texto:",
    
)

if st.button("Extrair entidades"):
    doc = nlp(texto)

    if doc.ents:
        for entidade in doc.ents:
            st.write(f"**{entidade.text}** → {entidade.label_}")
    else:
        st.write("Nenhuma entidade encontrada")