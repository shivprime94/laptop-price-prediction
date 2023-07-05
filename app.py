import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the pickled model
file1 = open('pipe.pkl','rb')
rf = pickle.load(file1)
file1.close()
#Company,TypeName,Ram,OpSys,Weight,Price,TouchScreen,IPS,PPI,CpuName,HDD,SSD,Gpu_brand
#Apple,Ultrabook,8,Mac,1.37,71378.6832,0,1,226.98300468106115,Intel Core i5,0,128,Intel

data = pd.read_csv('traintest.csv')
data['IPS'].unique()
st.title