#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Covid-19_Dataset")

#import dataset
df = pd.read_csv('Covid-19_India.csv')
#First twenty rows
tips = df.head(20)
#Display the table
st.table(tips)
st.header("Visualisation Using Seaborn")
#bar plot
st.subheader("Bar Plot")
tips.plot(kind='bar')
st.pyplot()
#Displot
st.subheader("Displot")
sns.displot(tips['Total Cases'])
st.pyplot()
#joinplot
st.subheader("JointPlot")
sns.jointplot(x='Total Cases',y='Deaths',data=tips,kind='scatter')
st.pyplot()
#pairplot
st.subheader("Pairplot")
sns.pairplot(tips,hue='Discharged',palette='rainbow')
st.pyplot()
#Rugplot
#st.subheader("Rugplot")
#sns.rugplot(tips['Deaths'])
#st.pyplot()
#Correation
#st.subheader("Heatmap")
#sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
#st.pyplot()
