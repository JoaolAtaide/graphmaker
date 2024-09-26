import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO

# Título da aplicação
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Barlow:wght@400&display=swap');
    .font {
        font-family: 'Barlow', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Gerador de Gráficos de Incidentes Escolares", anchor=None)
st.markdown('<p class="font">Insira os dados para gerar o gráfico de incidentes por escola.</p>', unsafe_allow_html=True)

# Coletar dados dos usuários
escolas = st.text_input("Digite os nomes das escolas, separados por vírgula (Ex: Escola A, Escola B)", "")
num_chamados = st.text_input("Digite o número de incidentes para cada escola, separados por vírgula (Ex: 4, 3)", "")

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
    plt.title('Incidentes no último trimestre', fontsize=14, fontfamily='Barlow')
    plt.xlabel('Número de Incidentes', fontsize=12, fontfamily='Barlow')
    plt.ylabel('Escola', fontsize=12, fontfamily='Barlow')

    # Mostrar o gráfico no app
    st.pyplot(plt)

    # Função para salvar o gráfico como JPEG
    def save_plot_as_jpeg():
        buffer = BytesIO()
        plt.savefig(buffer, format='jpeg')
        buffer.seek(0)
        return buffer

    # Botão para baixar o gráfico
    st.markdown('<p class="font">Baixe o gráfico gerado:</p>', unsafe_allow_html=True)
    buffer = save_plot_as_jpeg()
    st.download_button(
        label="Baixar gráfico como JPEG",
        data=buffer,
        file_name="grafico_incidentes_escolares.jpeg",
        mime="image/jpeg"
    )

else:
    st.markdown('<p class="font">Por favor, insira os dados para gerar o gráfico.</p>', unsafe_allow_html=True)
