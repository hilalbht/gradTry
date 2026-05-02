import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Cirrhosis Prediction", layout="centered")

st.title("🧬 Liver Cirrhosis Stage Prediction")

st.write("📌 Model dosyanı yükle ve tahmin yap")

# -------------------------
# MODEL UPLOAD (EN GÜVENLİ YÖNTEM)
# -------------------------
uploaded_file = st.file_uploader("model.pkl yükle", type=["pkl"])

if uploaded_file is not None:
    model = joblib.load(uploaded_file)

    st.success("Model yüklendi!")

    # INPUTLAR
    Age = st.number_input("Age")
    Sex = st.selectbox("Sex", ["M", "F"])
    Bilirubin = st.number_input("Bilirubin")
    Cholesterol = st.number_input("Cholesterol")
    Albumin = st.number_input("Albumin")
    Copper = st.number_input("Copper")
    Alk_Phos = st.number_input("Alk_Phos")
    SGOT = st.number_input("SGOT")
    Tryglicerides = st.number_input("Tryglicerides")

    Ascites = st.selectbox("Ascites", ["Y", "N"])
    Hepatomegaly = st.selectbox("Hepatomegaly", ["Y", "N"])
    Spiders = st.selectbox("Spiders", ["Y", "N"])
    Edema = st.selectbox("Edema", ["Y", "N"])
    Drug = st.selectbox("Drug", ["D-penicillamine", "Placebo"])

    # PREDICTION
    if st.button("Tahmin Et"):
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

        pred = model.predict(data)[0]

        st.success(f"🎯 Tahmin edilen evre: Stage {pred + 1}")
