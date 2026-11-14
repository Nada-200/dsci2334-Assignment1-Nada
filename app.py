import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Revenue Explorer", page_icon="$")
st.title("$ Qahwa Corner Revenue")
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

view = df[df["total_sar"] > 0]
if research != "All":
    view = view[view["Branch"] == (1 if branch == "Yes" else 0)]

# Key numbers
c1, c2, c3= st.columns(3)
c1.metric("Product", len(view))
if len(view) > 0:
    c2.metric("Average revenue", f"{view['total_sar'].mean():.2f}")
    c3.metric("Total revenue", f"{view['total_sar'].sum():.2f}")
else:
    st.warning("No branch match these filters.")

# Chart
fig, ax = plt.subplots()
product_revenue = filtered_df.groupby('product')['total_sar'].sum()
ax.bar(product_revenue.index, product_revenue.values, color='pink')
ax.set_xlabel("Product")
ax.set_ylabel("Total Revenue (SAR)")
ax.set_title("Revenue by Product")
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Data table
st.subheader("First 20 matching students")
st.dataframe(view.head(20))
