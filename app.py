import streamlit as st
from datetime import datetime

# Sidebar
st.sidebar.image("logo.png")
st.sidebar.title("Locadora de Veículos")

# Lista de carros
carro = st.sidebar.selectbox(
    "Selecione o seu veículo:",
    [
        "SUPRA MK4",
        "PORSCHE GT3 RS",
        "LAMBORGHINI",
        "FERRARI",
        "GTR R35",
        "SKYLINE GTR-R R34",
        "JESKO"
    ]
)

# Valores das diárias
valores_diarias = {
    "SUPRA MK4": 2000.0,
    "PORSCHE GT3 RS": 3600.0,
    "LAMBORGHINI": 5000.0,
    "FERRARI": 7000.0,
    "GTR R35": 2500.0,
    "SKYLINE GTR-R R34": 1900.0,
    "JESKO": 15000.0
}

# Valor da diária do carro selecionado
valor_diaria = valores_diarias[carro]

# Informações do carro
st.subheader(f"""
CARRO SELECIONADO: {carro}

Preço da diária: R$ {valor_diaria:.2f}
""")

# Imagem do carro
st.image(f"{carro}.png", width=500)

# Datas
data_inicio = st.date_input("Selecione o dia da retirada", datetime.now())
data_final = st.date_input("Selecione o dia da devolução", datetime.now())

# Botão de cálculo
if st.button("Calcular"):
    
    dias = (data_final - data_inicio).days

    if dias <= 0:
        st.error("A data de devolução deve ser maior que a data de retirada.")
    else:
        valor_total = valor_diaria * dias

        st.subheader(
            f"Alugando o {carro} por {dias} dias, "
            f"o valor ficará em R$ {valor_total:.2f}"
        )