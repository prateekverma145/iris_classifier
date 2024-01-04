import streamlit as st
import pandas as pd                     
import pickle

model=pickle.load(open('lr.pkl','rb'))


st.title("Iris Flower Classification")

sl=st.slider("Sepal Length",0.1,10.0)
sw=st.slider("Sepal Width",0.1,10.0)
pl=st.slider("Petal Length",0.1,10.0)
pw=st.slider("Petal Width",0.1,10.0)

data={'sepal_length':sl,'sepal_width':sw,'petal_length':pl,'petal_width':pw}
features=pd.DataFrame(data,index=[0])
st.write (features)

if st.button("Predict"):
    prediction=model.predict(features)
    if(prediction==0):
        ans="Setosa"
    if(prediction==1):
        ans="Versicolor"
    if(prediction==2):
        ans="Virginica"    
    st.subheader(f"The flower's species is {ans}")
    