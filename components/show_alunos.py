import streamlit as st
from controllers.alunos_controllers import load_alunos
from utils.cpf_utils import cpf_utils
from components.modal_visualizar import visualizar_aluno

def show_alunos():
  st.subheader("Lista de Alunos Cadastrados!")

  alunos = load_alunos()

  if not alunos:
    return st.error("Nenhum Aluno Cadastrado. Clique no botão acima para cadatrar aluno.")
  
  tabs = st.tabs(["Alunos", "Pesquisar"])

  with tabs[0]:
    colunas = st.columns([3, 2, 3, 2, 2])

    colunas[0].subheader("Nome")
    colunas[1].subheader("Email")
    colunas[2].subheader("CPF")
    colunas[3].subheader("Visualizar")
    colunas[4].subheader("Deletar")

    for aluno in alunos:
      colunas_alunos = st.columns([3, 2, 3, 2, 2])

      colunas_alunos[0].write(aluno["nome_aluno"])
      colunas_alunos[1].write(aluno["email_aluno"])
      colunas_alunos[2].write(cpf_utils)

    if colunas_alunos[3].button("visualizar", key=f"view_{aluno["id_aluno"]}", use_container_width=True):
      pass

    if colunas_alunos[4].button("deletar", key=f"deletar_{aluno["id_aluno"]}", use_container_width=True):
      pass