import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO

# Set Matplotlib to use the Barlow font by default for all plots
plt.rcParams['font.family'] = 'Barlow'

# Title and description using default font in Streamlit
st.title("Gerador de Gráficos de Incidentes Escolares")
st.write("Insira os dados para gerar o gráfico de incidentes por escola.")

# Collect user inputs
escolas = st.text_input("Digite os nomes das escolas, separados por vírgula (Ex: Escola A, Escola B)", "")
num_chamados = st.text_input("Digite o número de incidentes para cada escola, separados por vírgula (Ex: 4, 3)", "")

# Process the input data
if escolas and num_chamados:
    # Convert the inputs to lists
    lista_escolas = [escola.strip() for escola in escolas.split(',')]
    lista_chamados = [int(chamado) for chamado in num_chamados.split(',')]

    # Create a DataFrame
    data = pd.DataFrame({
        'Escola': lista_escolas,
        'NumChamados': lista_chamados
    })

    # Generate the chart
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x='NumChamados', y='Escola', data=data, color='rebeccapurple')

    # Add numbers on top of the bars
    for p in ax.patches:
        width = int(p.get_width())  # Get the width of the bar
        ax.text(0.1, p.get_y() + p.get_height() / 2,  # Position of the text
                f'{width}', ha='left', va='center', color='white')  # Add the text

    # Customize labels and title using Barlow font
    plt.title('Incidentes no último trimestre', fontsize=14)
    plt.xlabel('Número de Incidentes', fontsize=12)
    plt.ylabel('Escola', fontsize=12)

    # Display the chart in the app
    st.pyplot(plt)

    # Function to save the chart as JPEG
    def save_plot_as_jpeg():
        buffer = BytesIO()
        plt.savefig(buffer, format='jpeg')
        buffer.seek(0)
        return buffer

    # Button to download the chart
    st.write("Baixe o gráfico gerado:")
    buffer = save_plot_as_jpeg()
    st.download_button(
        label="Baixar gráfico como JPEG",
        data=buffer,
        file_name="grafico_incidentes_escolares.jpeg",
        mime="image/jpeg"
    )

else:
    st.write("Por favor, insira os dados para gerar o gráfico.")
