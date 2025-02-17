# Patients Hospital Charges Predictor 🏥💸

A machine learning project designed to predict hospital charges for patients based on various features such as age, BMI, smoking status, and region. This project is part of an MLOps practice initiative to build and deploy machine learning models.

---

The project is live and hosted on Streamlit cloud for making predictions.
The webpage can be accessed by [clicking here](https://sankalp-mlops-practice-project-patient-hospital-charge-estimatr.streamlit.app/)

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [MLOps Pipeline](#mlops-pipeline)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Introduction

This project focuses on predicting hospital charges for patients using machine learning. It is designed as an MLOps practice project to demonstrate end-to-end workflows, including data preprocessing, model training, deployment, and monitoring. The goal is to provide accurate predictions to help hospitals and patients estimate medical costs. Although, the actual aim behind development of this project is to practice only.

---

## Features

- **Data Preprocessing**: Handles missing values, categorical encoding, and feature scaling.
- **Machine Learning Models**: Includes regression models like Linear Regression, Random Forest, XGBoost and many more.
- **MLOps Integration**: Implements modular coding structure for model training and deployment.
- **Deployment**: Deployed the model on Streamlit cloud for real-time predictions.

---

## Usage

This section provides instructions on how to use the Patients Hospital Charges Predictor project.

### 1. Setting up the Environment

Before running the code, ensure you have set up the required environment. This includes cloning the repository, creating a virtual environment, and installing the necessary dependencies using "requirements.txt".

### 2. Executing the repo

* **Running the app on local system:**
    ```bash
    streamlit run app.py 
    ```
    This will start the server. By default, it runs on `http://127.0.0.1:5000/`.

* **Making Predictions:**
   
    You can make predictions by directly entering the respective values to each field. It directly calls and executes the `predict_pipeline.py`
    Here is an example of the values that can be fed to it:

    ```
     {
        "age": 30,
        "sex": "male",
        "bmi": 25.0,
        "children": 0,
        "smoker": "no",
        "region": "northeast"
    }' 
    ```

    * **Input Payload:**  The input data payload should include the following features with appropriate data type:
        * `age` (integer): Age of the patient.
        * `sex` (string): Sex of the patient ("male" or "female").
        * `bmi` (float): Body mass index.
        * `children` (integer): Number of children.
        * `smoker` (string): Smoker status ("yes" or "no").
        * `region` (string): Region of residence (e.g., "northeast", "northwest", "southeast", "southwest").

    * **Response:** The system will return a prediction box just below the input section as response containing the predicted hospital charges in float.  For example:

    ```
    Estimated Hostpital Charges : 12345.67
    ```

### 3. Training the Model (Optional)

The project includes a training script that you can use to retrain the model.

* **Running the Training Script:**
    ```bash
    python src/pipeline/training_pipeline.py
    ```
    This will train and save the  and model pickle file and also it will return a score.
    This script will train the model and save the trained model artifacts along with data transformation pipeline in a `artifacts` directory.  

---

## Model Performance

The performance of the hospital charges prediction model was evaluated using R-squared `r2_square`.  These metrics were chosen because R2 measures the goodness of fit.

The model was trained and evaluated on a dataset, initially data is splitted into train and test before preprocessing. Before training train data is splitted into train and validation set and performed a 10-fold cross-validation to ensure model robustness.


