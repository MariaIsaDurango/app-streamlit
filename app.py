import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Mi Dashboard Pro", layout="wide")

st.title("📊 Mi Primera App con Streamlit")
st.write("Bienvenido. Esta app carga datos, los filtra y muestra gráficos.")

# 1. Cargar Datos
@st.cache_data # Esto hace que la app sea rápida al no recargar datos siempre
def cargar_datos():
    df = pd.read_csv("dataset.csv")
    return df

df = cargar_datos()

# 2. Sidebar (Barra lateral) para filtros
st.sidebar.header("Filtros")
categoria_seleccionada = st.sidebar.multiselect(
    "Selecciona la Categoría:",
    options=df["Categoria"].unique(),
    default=df["Categoria"].unique()
)

# Filtrar el dataframe
df_filtrado = df[df["Categoria"].isin(categoria_seleccionada)]

# 3. Mostrar Tabla y Estadísticas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Vista de Datos")
    st.dataframe(df_filtrado)

with col2:
    st.subheader("Estadísticas Rápidas")
    st.write(f"Total Ventas: **{df_filtrado['Ventas'].sum()}**")
    st.write(f"Promedio: **{df_filtrado['Ventas'].mean():.2f}**")

# 4. Gráfico Sencillo
st.divider()
st.subheader("Gráfico de Ventas por Producto")
fig, ax = plt.subplots()
ax.bar(df_filtrado["Producto"], df_filtrado["Ventas"], color='skyblue')
ax.set_ylabel("Cantidad Vendida")

st.pyplot(fig)