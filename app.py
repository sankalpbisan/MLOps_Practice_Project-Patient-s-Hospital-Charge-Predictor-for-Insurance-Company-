import streamlit as st
from src.pipeline.predict_pipeline import CustomData,PredictionPipeline
from src.logger import logging

# Title of the app
st.title("Students' Performance Prediction")

#'age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges'
st.text("Enter the details below to predict performance")
# Input fields
age = st.text_input("Age")
sex = st.text_input("Sex")
bmi = st.text_input("BMI")
children = st.text_input("Children")
smoker = st.text_input("Smoker")
region = st.text_input("Region")


logging.info(f"The values are:{age, sex, bmi, children, smoker, region}")
print(age, sex, bmi, children, smoker, region)

if age and sex and bmi and children and smoker and region:

    input_data = CustomData(
                     age=age.strip(),
                     sex=sex.strip(),
                     bmi=bmi.strip(),
                     children=children.strip(),
                     smoker=smoker.strip(),
                     region=int(region),
                     writing_score=int(writing_score)
    )

    # input as dataframe
    inp_df = input_data.get_data_as_dataframe()

    #Prediction
    prediction = PredictionPipeline()
    result = prediction.predict(features=inp_df)

    # Button to trigger an action
    if st.button("Predict"):
        st.session_state.submitted = True
        st.success(f"Prediction is : {result[0]}")
    else:
        st.error("Something is Fishy !!!!")

else:
    print("One or more inputs are empty. Please fill all fields.")