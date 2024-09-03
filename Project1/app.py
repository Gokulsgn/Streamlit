import streamlit as st
import numpy as np
import pickle

def load_model():
    try:
        with open(r'C:\Users\gokul\Documents\GitHub\Streamlit\Project1\diabetes.pkl', 'rb') as file:
            model_data = pickle.load(file)
        st.write(f"Model Loaded: {model_data.keys()}")
        return model_data
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def main():
    data = load_model()
    if data is None:
        return

    model = data.get("model")
    scaler = data.get("scaler")

    if model is None or scaler is None:
        st.error("Model or Scaler is missing.")
        return

    st.write(f"Model Type: {type(model)}")
    st.write(f"Scaler Type: {type(scaler)}")

    st.title("Diabetes Prediction")

    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, step=1)
    glucose = st.number_input('Glucose', min_value=0, max_value=200)
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=140)
    skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100)
    insulin = st.number_input('Insulin', min_value=0, max_value=900)
    bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, format="%.1f")
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, format="%.3f")
    age = st.number_input('Age', min_value=0, max_value=120)

    if st.button('Predict'):
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, 
                                bmi, diabetes_pedigree_function, age]])
        st.write(f"Input Data: {input_data}")
        st.write(f"Input Data Shape: {input_data.shape}")

        try:
            input_transform = scaler.transform(input_data)
            st.write(f"Transformed Input Data: {input_transform}")
            prediction = model.predict(input_transform)
            st.write(f"Predicted Outcome: {'Diabetic' if prediction[0] == 1 else 'Not Diabetic'}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

if __name__ == '__main__':
    main()
