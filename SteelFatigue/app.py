import streamlit as st
import pandas as pd
import joblib


model_path = os.path.join(os.path.dirname(__file__), "fatigue_model_10.pkl")
model = joblib.load(model_path)


st.title("Steel Fatigue Strength Prediction")

st.write(
    "Predict the rotating-bending fatigue strength of steel "
    "using chemical composition and heat-treatment parameters."
)


st.subheader("Enter Material & Processing Parameters")

CT = st.number_input("Carburization Temperature (CT) [°C]")
DT = st.number_input("Diffusion Temperature (DT) [°C]")
Tt = st.number_input("Tempering Time (Tt) [min]")
Cr = st.number_input("Chromium (Cr) [wt%]")
QmT = st.number_input("Quenching Medium Temperature (QmT) [°C]")
NT = st.number_input("Normalizing Temperature (NT) [°C]")
Ct = st.number_input("Carburization Time (Ct) [min]")
Dt = st.number_input("Diffusion Time (Dt) [min]")
TT = st.number_input("Tempering Temperature (TT) [°C]")
C = st.number_input("Carbon (C) [wt%]")


if st.button("Predict Fatigue Strength"):

    # Create input DataFrame
    input_data = pd.DataFrame([[
        CT,
        DT,
        Tt,
        Cr,
        QmT,
        NT,
        Ct,
        Dt,
        TT,
        C
    ]], columns=[
        'CT',
        'DT',
        'Tt',
        'Cr',
        'QmT',
        'NT',
        'Ct',
        'Dt',
        'TT',
        'C'
    ])

    # Generate prediction
    prediction = model.predict(input_data)[0]


    st.success("Prediction generated successfully!")

    st.metric(
        label="Rotating-Bending Fatigue Strength @ 10⁷ Cycles",
        value=f"{prediction:.2f} MPa"
    )


    st.info(
        "The predicted value represents the rotating-bending fatigue "
        "strength at 10⁷ cycles, as defined by the dataset."
    )

    st.subheader("Material Insight")

    st.write(
        f"The model predicts a rotating-bending fatigue strength of "
        f"**{prediction:.2f} MPa** at 10⁷ cycles."
    )

    st.write(
        "This value represents the predicted resistance of the material "
        "to fatigue under the specified rotating-bending test condition. "
        "The prediction is based on the chemical composition and "
        "heat-treatment parameters provided above."
    )

    st.write(
        f"**Carbon content:** {C:.2f} wt%  \n"
        f"**Chromium content:** {Cr:.2f} wt%  \n"
        f"**Tempering temperature:** {TT:.0f} °C"
    )

    st.caption(
        "Note: This is a machine-learning prediction based on the training "
        "dataset and should not be treated as a universal design limit."
    )

st.divider()

st.caption(
    "Model: Random Forest Regressor | "
    "Features used: 10 | "
    "Output unit: MPa"
)
