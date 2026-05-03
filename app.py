import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Cirrhosis Prediction", layout="centered")

st.title("🧬 Liver Cirrhosis Stage Prediction")
st.write("Bu uygulama hastanın verilerine göre siroz evresini tahmin eder.")

# -------------------------
# MODEL LOAD
# -------------------------
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.success("✅ Model başarıyla yüklendi!")

# -------------------------
# INPUT ALANI (DÜZENLİ)
# -------------------------
st.subheader("📊 Hasta Bilgileri")

col1, col2 = st.columns(2)

with col1:
    Age = st.number_input("Age", min_value=0.0)
    Bilirubin = st.number_input("Bilirubin", min_value=0.0)
    Albumin = st.number_input("Albumin", min_value=0.0)
    Copper = st.number_input("Copper", min_value=0.0)

with col2:
    Cholesterol = st.number_input("Cholesterol", min_value=0.0)
    Alk_Phos = st.number_input("Alk_Phos", min_value=0.0)
    SGOT = st.number_input("SGOT", min_value=0.0)
    Tryglicerides = st.number_input("Tryglicerides", min_value=0.0)

Sex = st.selectbox("Sex", ["M", "F"])
Ascites = st.selectbox("Ascites", ["Y", "N"])
Hepatomegaly = st.selectbox("Hepatomegaly", ["Y", "N"])
Spiders = st.selectbox("Spiders", ["Y", "N"])
Edema = st.selectbox("Edema", ["Y", "N"])
Drug = st.selectbox("Drug", ["D-penicillamine", "Placebo"])

# -------------------------
# TAHMİN
# -------------------------
if st.button("🔍 Tahmin Et"):

    data = pd.DataFrame([{
        "Age": Age,
        "Sex": Sex,
        "Bilirubin": Bilirubin,
        "Cholesterol": Cholesterol,
        "Albumin": Albumin,
        "Copper": Copper,
        "Alk_Phos": Alk_Phos,
        "SGOT": SGOT,
        "Tryglicerides": Tryglicerides,
        "Ascites": Ascites,
        "Hepatomegaly": Hepatomegaly,
        "Spiders": Spiders,
        "Edema": Edema,
        "Drug": Drug
    }])

    try:
        pred = model.predict(data)[0]
        st.success(f"🎯 Tahmin edilen evre: Stage {pred + 1}")

    except Exception as e:
        st.error("❌ Model tahmin yapamadı!")
        st.write(e)
