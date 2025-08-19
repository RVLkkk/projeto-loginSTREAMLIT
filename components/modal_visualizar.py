import streamlit as st

@st.dialog("visualizar dados do aluno")
def visualizar_aluno(aluno):
    colunas = st.colunas([2, 3])

    with colunas[0]:
        st.subheader("nome")
        st.subheader("email")
        st.subheader("data de nacimento")
        st.subheader("CPF")
        st.subheader("Telefone")

        with colunas[1]:
            st.subheader(aluno["nome_aluno"])
            st.subheader(aluno["email_aluno"])
            st.subheader(aluno["dataNasc_aluno"])
            st.subheader(aluno["cpf_aluno"])
            st.subheader(aluno["telefone_aluno"])