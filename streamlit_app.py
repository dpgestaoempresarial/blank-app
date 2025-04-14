import streamlit as st

# Título
st.title("Calculadora de Tributos - IBS e CBS")

# Entradas do usuário
vProduto = st.number_input("Valor Bruto do Produto (R$)", min_value=0.0, format="%.2f")
vIBSUF = st.number_input("Alíquota IBS Estadual (%)", value=10.0, format="%.2f")
vIBSMun = st.number_input("Alíquota IBS Municipal (%)", value=0.0, format="%.2f")
vCBS = st.number_input("Alíquota CBS (%)", value=0.0, format="%.2f")

# Botão para calcular IBS
if st.button("Calcular IBS"):
    vCalculoIBS = vProduto * (1 + ((vIBSUF + vIBSMun) / 100))
    st.success(f"Valor com IBS: R$ {vCalculoIBS:,.2f}")

# Botão para calcular CBS
if st.button("Calcular CBS"):
    vCalculoCBS = vProduto * (1 + (vCBS / 100))
    st.success(f"Valor com CBS: R$ {vCalculoCBS:,.2f}")
