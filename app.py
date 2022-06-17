import streamlit as st
import pandas as pd
import pickle
import requests
from PIL import Image


model = pickle.load(open('class.pkl','rb'))

def dataframe(head):
    b=pd.DataFrame(head, columns= ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
       'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave_points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave_points_worst',
       'symmetry_worst', 'fractal_dimension_worst'])
    return b

st.title('Breast Cancer Wisconsin classification ')
 
 
radius_mean = st.text_input(' Enter the radius_mean:',0)
texture_mean = st.text_input('Enter the texture_mean:',0)
perimeter_mean = st.text_input('Enter the perimeter_mean:',0)
area_mean = st.text_input('Enter the area_mean:',0)

smoothness_mean = st.text_input('Enter the smoothness_mean:',0)
compactness_mean = st.text_input('Enter the compactness_mean:',0)
concavity_mean = st.text_input('Enter the concavity_mean:',0)
concave_points_mean = st.text_input('Enter the concave points_mean:',0)

symmetry_mean = st.text_input('Enter the symmetry_mean:',0)
fractal_dimension_mean = st.text_input('Enter the fractal_dimension_mean:',0)
radius_se = st.text_input('Enter the radius_se:',0)

texture_se = st.text_input('Enter the texture_se:',0)
perimeter_se = st.text_input('Enter the perimeter_se:',0)
area_se = st.text_input('Enter the area_se:',0)
smoothness_se= st.text_input('Enter the smoothness_se:',0)

compactness_se = st.text_input('Enter the compactness_se:',0)
concavity_se = st.text_input('Enter the concavity_se:',0)
concave_points_se = st.text_input('Enter the concave points_se:',0)
symmetry_se = st.text_input('Enter the symmetry_se:',0)

fractal_dimension_se = st.text_input('Enter the fractal_dimension_se:',0)
radius_worst = st.text_input('Enter the radius_worst:',0)
texture_worst = st.text_input('Enter the texture_worst',0)
perimeter_worst = st.text_input('Enter the perimeter_worst:',0)

area_worst = st.text_input('Enter the area_worst:',0)
smoothness_worst = st.text_input('smoothness_worst:',0)
compactness_worst = st.text_input('Enter the compactness_worst:',0)
concavity_worst = st.text_input('Enter the concavity_worst:',0)

concave_points_worst = st.text_input('Enter the concave_points_worst:',0)
symmetry_worst = st.text_input('Enter the symmetry_worst:',0)
fractal_dimension_worst = st.text_input('Enter the fractal_dimension_worst:',0)

data = [[radius_mean, texture_mean, perimeter_mean, area_mean,
       smoothness_mean, compactness_mean, concavity_mean,
       concave_points_mean, symmetry_mean, fractal_dimension_mean,
       radius_se, texture_se, perimeter_se, area_se, smoothness_se,
       compactness_se, concavity_se, concave_points_se, symmetry_se,
       fractal_dimension_se, radius_worst, texture_worst,
       perimeter_worst, area_worst, smoothness_worst,
       compactness_worst, concavity_worst, concave_points_worst,
       symmetry_worst, fractal_dimension_worst]]
newdf = dataframe(data)

predict_value = model.predict(newdf)
result = st.button("Predict")

if result :
    if predict_value == "M":
        st.subheader('The Breast cancer is Malignant')
    elif predict_value == "B":
        st.subheader('The Breast Cancer is Benign')
