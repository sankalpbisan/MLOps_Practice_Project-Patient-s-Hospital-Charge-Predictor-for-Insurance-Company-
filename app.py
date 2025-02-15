import streamlit as st
from src.pipeline.predict_pipeline import LoadData,PredictionPipeline
from src.logger import logging

# Title of the app
st.title("Patient's Hospital Charge Predictor")

#'age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges'
st.text("Enter the details below to predict performance")
# Input fields
age = st.text_input("Age")
sex = st.text_input("Sex")
bmi = st.text_input("BMI")
children = st.text_input("Children")
smoker = st.text_input("Smoker")
region = st.text_input("Region")


logging.info(f"Entered values are:{age, sex, bmi, children, smoker, region}")
print(age, sex, bmi, children, smoker, region)



if age and sex and bmi and children and smoker and region:
    input_data = LoadData(
                     age=int(age.strip()),
                     sex=sex.strip(),
                     bmi=float(bmi),
                     children=int(children.strip()),
                     smoker=smoker.strip(),
                     region=region.strip()
    )

    # input as dataframe
    inp_df = input_data.load_data()

    #Prediction
    prediction_obj = PredictionPipeline()
    result = prediction_obj.predict(inp_df)

    # Button to trigger an action
    if st.button("Predict"):
        st.session_state.submitted = True
        st.success(f"Prediction is : {result[0]}")
        logging.info(f"Your estimated hospital charges :{result[0]}")
    else:
        st.error("Something went wrong !!!!")

else:
    print("One or more inputs are empty. Please fill all fields.")

