import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import requests
from io import BytesIO
from matplotlib import font_manager as fm

# Function to download and use Barlow font
def download_and_use_barlow():
    url = "https://github.com/google/fonts/raw/main/ofl/barlow/Barlow-Regular.ttf"
    response = requests.get(url)
    
    # Load the font into Matplotlib directly from the downloaded content
    font_bytes = BytesIO(response.content)
    font_prop = fm.FontProperties(fname=font_bytes)  # Load font from memory
    fm.fontManager.addfont(font_bytes)  # Add to font manager
    
    # Set this as the default font for Matplotlib
    plt.rcParams['font.family'] = font_prop.get_name()

# Apply the Barlow font to Matplotlib
download_and_use_barlow()

# Apply Barlow font to Streamlit interface
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Barlow:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Barlow', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("Gerador de Gráficos de Incidentes Escolares")
st.write("Insira os dados para gerar o gráfico de incidentes por escola.")

# Collect user inputs
escolas = st.text_input("Digite os nomes das escolas, separados por vírgula (Ex: Escola A, Escola B)", "")
num_chamados = st.text_input("Digite o número de incidentes para cada escola, separados por vírgula (Ex: 4, 3)", "")

# Process input data and create plot
if escolas and num_chamados:
    lista_escolas = [escola.strip() for escola in escolas.split(',')]
    lista_chamados = [int(chamado) for chamado in num_chamados.split(',')]

    # Create DataFrame
    data = pd.DataFrame({'Escola': lista_escolas, 'NumChamados': lista_chamados})

    # Generate the chart
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x='NumChamados', y='Escola', data=data, color='rebeccapurple')

    # Add numbers on top of the bars
    for p in ax.patches:
        width = int(p.get_width())
        ax.text(0.1, p.get_y() + p.get_height() / 2, f'{width}', ha='left', va='center', color='white')

    # Customize labels and title
    plt.title('Incidentes no último trimestre', fontsize=14)
    plt.xlabel('Número de Incidentes', fontsize=12)
    plt.ylabel('Escola', fontsize=12)

    # Display the chart
    st.pyplot(plt)

    # Function to save the chart as JPEG
    def save_plot_as_jpeg():
        buffer = BytesIO()
        plt.savefig(buffer, format='jpeg')
        buffer.seek(0)
        return buffer

    # Download the chart
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
