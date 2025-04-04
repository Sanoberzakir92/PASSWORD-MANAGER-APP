import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    criteria = {
        "Length (8+ characters)": len(password) >= 8,
        "Uppercase Letter": bool(re.search(r"[A-Z]", password)),
        "Lowercase Letter": bool(re.search(r"[a-z]", password)),
        "Digit": bool(re.search(r"\d", password)),
        "Special Character": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    strength = sum(criteria.values())
    
    if strength == 5:
        return "Strong", "green"
    elif strength >= 3:
        return "Moderate", "orange"
    else:
        return "Weak", "red"

# Streamlit UI
st.title("Password Strength Meter🔐")
password = st.text_input("Enter Password", type="password")

if password:
    strength, color = check_password_strength(password)
    st.markdown(f"**Strength:** <span style='color:{color}; font-weight:bold'>{strength}</span>", unsafe_allow_html=True)
    
    st.subheader("Password Criteria")
    st.write("- At least 8 characters")
    st.write("- At least one uppercase letter")
    st.write("- At least one lowercase letter")
    st.write("- At least one digit")
    st.write("- At least one special character (!@#$%^&* etc.)")
