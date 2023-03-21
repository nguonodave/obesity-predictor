import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def clean_means_of_transport(x):
    if 'Public_Transportation' in x:
        return 'Public_Transportation'    
    if 'Walking' in x or 'Bike' in x:
        return 'Walking'
    return 'Private'


@st.cache
def loadData():
    dataframe = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")

    # dataframe = dataframe.rename({"Gender": "Total_individuals"}, axis=1)
    dataframe = dataframe.rename({"FAVC": "Consumes_high_caloric_food_frequently"}, axis=1)
    dataframe = dataframe.rename({"CH2O": "Litres_of_water_per_day"}, axis=1)
    dataframe = dataframe.rename({"FAF": "Physical_activities_in_a_day"}, axis=1)
    dataframe = dataframe.rename({"MTRANS": "Means_of_transport"}, axis=1)
    dataframe = dataframe.rename({"NCP": "Number_of_main_meals"}, axis=1)
    dataframe = dataframe.rename({"CAEC": "Consumption_of_food_between_meals"}, axis=1)
    dataframe = dataframe.rename({"CALC": "Consumption_of_alcohol"}, axis=1)
    dataframe = dataframe.rename({"TUE": "Time_using_technology_devices"}, axis=1)
    dataframe = dataframe.rename({"NObeyesdad": "Obesity_level"}, axis=1)

    dataframe = dataframe[dataframe["Obesity_level"] != "Insufficient_Weight"]

    dataframe['Means_of_transport'] = dataframe['Means_of_transport'].apply(clean_means_of_transport)

    return dataframe


dataframe = loadData()


def show_explore_page():
    st.title("Explore obesity levels with various factors")
    
    data = dataframe.groupby(["Gender"])["Obesity_level"].count()
    st.bar_chart(data)

    st.write(
        """
        ### Percentage of male and female that participated in the survay.
        """
    )

    data = dataframe["Gender"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)


    st.write(
        """
        ### Number of people with different levels of weight and obesity
        """
    )
    data = dataframe.groupby(["Obesity_level"])["Gender"].count()
    st.bar_chart(data)



    st.write(
        """
        ### Number of people with different levels of weight and obesity
        """
    )
    fig2 = plt.figure()
    sns.barplot(x = "Obesity_level", y = "Weight", data = dataframe, hue = "Gender")
    st.pyplot(fig2)

