
import streamlit as st

# Page config
st.set_page_config(page_title="Simple Discount Calculator", layout="centered")

st.title("🧮 Simple Discount Calculator")

st.markdown("Enter your pricing details below to calculate a **live sale price** after discount.")

# Inputs
current_price = st.number_input("Current Price (Inc VAT)", min_value=0.0, step=0.01, format="%.2f")
cost_price = st.number_input("Cost Price", min_value=0.0, step=0.01, format="%.2f")
discount_percent = st.number_input("Discount %", min_value=0.0, max_value=100.0, step=0.1, format="%.1f")

# Calculation
sale_price = current_price * (1 - discount_percent / 100)
profit = sale_price - cost_price
margin = (profit / sale_price * 100) if sale_price else 0

# Output
st.markdown("### 📉 Calculated Sale Price")
st.metric("Sale Price (£)", f"£{sale_price:.2f}")
st.metric("Profit (£)", f"£{profit:.2f}")
st.metric("Margin %", f"{margin:.2f}%")

st.caption("Live calculator • Built for Battle Nexus")
