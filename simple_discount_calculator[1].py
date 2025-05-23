
import streamlit as st

# Page config
st.set_page_config(page_title="Simple Discount Calculator (ex VAT)", layout="centered")

st.title("🧮 Simple Discount Calculator")

st.markdown("Enter your product's current price (including VAT), the ex-VAT cost, and a discount %.")
st.markdown("The calculator shows the final **sale price**, **profit**, and **margin** in real time.")

# Inputs
current_price_inc_vat = st.number_input("Current Price (Inc VAT)", min_value=0.0, step=0.01, format="%.2f")
cost_price_ex_vat = st.number_input("Cost Price (Ex VAT)", min_value=0.0, step=0.01, format="%.2f")
discount_percent = st.number_input("Discount %", min_value=0.0, max_value=100.0, step=0.1, format="%.1f")

# Calculation
sale_price = current_price_inc_vat * (1 - discount_percent / 100)
profit = sale_price - cost_price_ex_vat
margin = (profit / sale_price * 100) if sale_price else 0

# Output
st.markdown("### 📉 Calculated Sale Price")
st.metric("Sale Price (£)", f"£{sale_price:.2f}")
st.metric("Profit (£)", f"£{profit:.2f}")
st.metric("Margin %", f"{margin:.2f}%")

st.caption("Cost is treated as ex VAT • Built for Battle Nexus")
