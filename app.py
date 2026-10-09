import streamlit as st

st.title("Situação do aluno")
nome = st.text_input("Nome do aluno")
nota1 = st.number_input("Primeira nota", 0.0, 10.0, 0.0)
nota2 = st.number_input("Segunda nota", 0.0, 10.0, 0.0)

media = (nota1 + nota2) / 2

if st.button("Verificar"):
    st.write(f"Aluno: {nome}")
    st.write(f"Média: {media}")
    if media >= 6:
        st.write("Aprovado")
          else:
        st.write("Reprovado")
