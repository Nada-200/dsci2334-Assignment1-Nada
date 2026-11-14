import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Revenue Explorer", page_icon="☕")
st.title("☕ Qahwa Corner Revenue")
st.write("Explore how revenue differs from one prouduct to the another.")


@st.cache_data
def load_data():
    df = pd.read_csv("cafe_sales.csv")
    df.columns = df.columns.str.strip()  # some column names end with a space
    return df


df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
branch = st.sidebar.selectbox("Branch", ["All","Al Malqa", "Al Nakheel", "Diriyah", "Olaya"])

view = df.copy()
if branch != "All":
    view = view[view["branch"] == branch]

# Key numbers
c1, c2, c3= st.columns(3)
c1.metric("product", len(view))
if len(view) > 0:
    c2.metric("Total revenue (SAR)", f"{view['total_sar'].sum():.2f}")
else:
    st.warning("No data match these filter.")

# Chart
x= df['product']
y = df['total_sar']
plt.bar(x,y, color = 'pink')
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.show()

