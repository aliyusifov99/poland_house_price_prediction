# streamlit_app/main.py
import streamlit as st
from apartment_page import apartment_price_page
from rent_page import rent_price_page

# Sidebar title with Polish flag
st.sidebar.title("Housing Price Prediction in Poland")
st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <img src="https://upload.wikimedia.org/wikipedia/en/1/12/Flag_of_Poland.svg" alt="Polish Flag" width="100">
    </div>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio("Go to", ["Apartment Price", "Rent Price"])

if page == "Apartment Price":
    apartment_price_page()
elif page == "Rent Price":
    rent_price_page()

st.sidebar.markdown("---")
st.sidebar.write("Made by Ali Yusifov 2024")

# Custom CSS for icons
st.sidebar.markdown(
    """
    <style>
    .social-icons a {
        margin-right: 10px;
        color: inherit;
        text-decoration: none;
    }
    .social-icons i {
        font-size: 20px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Contact Details
st.sidebar.markdown("### Contact")
st.sidebar.markdown(
    """
    <div class="social-icons">
        <a href="https://github.com/aliyusifov99" target="_blank">
            <i class="fab fa-github"></i> GitHub
        </a><br>
        <a href="https://www.linkedin.com/in/ali-yusifov/" target="_blank">
            <i class="fab fa-linkedin"></i> LinkedIn
        </a><br>
        <a href="https://medium.com/@ali.yusifli0011" target="_blank">
            <i class="fab fa-medium"></i> Medium
        </a><br>
        <a href="mailto:ali.yusifli0011@gmail.com" target="_blank">
            <i class="fas fa-envelope"></i> Email
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)

# Load the FontAwesome icons
st.sidebar.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    """,
    unsafe_allow_html=True
)
