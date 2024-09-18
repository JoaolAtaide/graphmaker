import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Título da aplicação
st.title("Gerador de Gráficos de Incidentes Escolares")

# Instruções para o usuário
st.write("Insira os dados para gerar o gráfico de incidentes por escola.")

# Coletar dados dos usuários
escolas = st.text_input("Digite os nomes das escolas, separados por vírgula (Ex: Escola A, Escola B)")
num_chamados = st.text_input("Digite o número de incidentes para cada escola, separados por vírgula (Ex: 4, 3)")

# Processar os dados de entrada
if escolas and num_chamados:
    # Converter os dados em listas
    lista_escolas = [escola.strip() for escola in escolas.split(',')]
    lista_chamados = [int(chamado) for chamado in num_chamados.split(',')]

    # Criar o DataFrame
    data = pd.DataFrame({
        'Escola': lista_escolas,
        'NumChamados': lista_chamados
    })

    # Gerar o gráfico
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x='NumChamados', y='Escola', data=data, color='rebeccapurple')

    # Adicionar números em cima das barras
    for p in ax.patches:
        width = int(p.get_width())  # Obter a largura da barra
        ax.text(0.1, p.get_y() + p.get_height() / 2,  # Posição do texto
                f'{width}', ha='left', va='center', color='white')  # Adicionar o texto

    # Ajustar rótulos e título
    plt.title('Incidentes no último trimestre')
    plt.xlabel('Número de Incidentes')
    plt.ylabel('Escola')

    # Mostrar o gráfico no app
    st.pyplot(plt)
else:
    st.write("Por favor, insira os dados para gerar o gráfico.")