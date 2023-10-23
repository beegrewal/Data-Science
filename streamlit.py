import streamlit as st  
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


      


df = pd.read_csv('Usedcar.csv')
st.title('Used Cars')
col1,col2,col3 = st.columns(3)
col1.metric('Luxury Sedan','','')
col2.metric('Hatchback','','') 

if st.sidebar.button('Load Dataset'):
    st.write(df)
    df1 =df.head(20)
    fig = plt.figure(figsize=(10,8))
    plt.bar(df['Brand'],df['Price'])
    st.pyplot(fig)

 


