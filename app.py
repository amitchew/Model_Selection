"""
Created on Wed Mar 31 09:53:32 2022
@author: __mitchew__
"""
import streamlit as st
import pandas as pd
from lazypredict.Supervised import LazyRegressor
from sklearn.model_selection import train_test_split

st.set_page_config(page_title='Machine Learning Algorithm Comparison',
    layout='wide')

def build_model(df):
    df = df.loc[:100] 
    X = df.iloc[:,:-1] 
    Y = df.iloc[:,-1]  

    st.markdown('**Variable details**:')
    st.write('X variable ')
    st.info(list(X.columns[:20]))
    st.write('Y variable')
    st.info(Y.name)

    # Build lazy model
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size = split_size,random_state = 0)
    reg = LazyRegressor(verbose=0,ignore_warnings=False, custom_metric=None)
    models_train,predictions_train = reg.fit(X_train, X_train, Y_train, Y_train)
    models_test,predictions_test = reg.fit(X_train, X_test, Y_train, Y_test)
    

    st.subheader('2. Table of Model Performance')

    st.write('Training set')
    st.write(predictions_train)

st.write("""
### Sparta X ML Algorithm Comparison
""")


with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

with st.sidebar.header('2. Set Parameters'):
    split_size = st.sidebar.slider('Data split ratio (% for Training Set)', 10, 90, 80, 5)
    #seed_number = st.sidebar.slider('Set the random seed number', 1, 100, 42, 1)

    # Sidebar - Independent Variable
    Independent_var = ['date', 'store', 'item']
    selected_Independent_var = st.sidebar.multiselect('Independent Variable', Independent_var, Independent_var)
    # Sidebar - Dependent Variable
    Dependent_var = ['sales','date', 'store', 'item' ]
    selected_Dependent_var = st.sidebar.selectbox('Dependent Variable', Dependent_var)

st.subheader('1. Dataset')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    build_model(df)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    