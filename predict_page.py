import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('obesity_predictor_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

classifier = data["model"]
le_calories = data["le_calories"]
le_transport = data["le_transport"]

def show_predict_page():
    st.title("Obesity prediction")

    st.write("""### Please enter the following information to predict the result""")

    frequent_consumption_of_calories = (
        "yes",
        "no",
    )

    means_of_transport = (
        'Public_Transportation',
        'Walking',
        'Private',
    )

    age = st.number_input("Age in years?", 10, 65, 10)    
    height = st.number_input("Height in metres?", 0.45, 2.50, 0.45)
    weight = st.number_input("Weight in Kgs?", 10, 173, 10)
    calories = st.selectbox("Do you consume alot of foods containing calories?", frequent_consumption_of_calories)
    water = st.slider("How many litres of water do you take in a day averagely?", 0, 3, 0)
    physical_activities = st.slider("What's the approximate times you do physical activities in a day?", 0, 3, 0)
    transport = st.selectbox("Which means of transport do you use often?", means_of_transport)
    

    predict = st.button("Predict")    
    if predict:        
        X = np.array([[age, height, weight, calories, water, physical_activities, transport]])

        X[:, 3] = le_calories.transform(X[:,3])
        X[:, -1] = le_transport.transform(X[:,-1])
        X = X.astype(float)

        result = classifier.predict(X)

        # st.subheader(result[0])

        if result[0] == 0:
            st.subheader("Normal weight")
        elif result[0] == 1:
            st.subheader("Overweight Level 1")
        elif result[0] == 2:
            st.subheader("Overweight Level 2")
        elif result[0] == 3:
            st.subheader("Obesity type 1")
        elif result[0] == 4:
            st.subheader("Obesity type 2")
        else:
            st.subheader("Obesity type 3")
        
    bmi = st.button("Calculate your BMI")
    if bmi:
        bmiResult = weight/(height*height)
        st.subheader(f"Your BMI result is {bmiResult}Kg m-2")

