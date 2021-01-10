import streamlit as st
import pickle
import numpy as np

# Loading the saved Model
model = pickle.load(open("ccmodel.pkl", "rb"))



def credit_default(features):

    features = np.array(features).astype(np.float64).reshape(1,-1)
    
    predict = model.predict(features)
    probability = model.predict_proba(features)

    return predict, probability


def main():
    st.title("Credit Card Default Prediction")
    html_temp = """
    <div style="background-color:#dd88b3 ;padding:10px">
    <h2 style="color:white;text-align:center;">Credict Card Default Prediction App </h2>
    </div>
    """    
    st.markdown(html_temp, unsafe_allow_html=True)

    LIMIT_BAL = st.text_input("Limit Balance")
    EDUCATION = st.text_input("Enter Education (1 = graduate school; 2 = university; 3 = high school; 4 = others)")
    MARRIAGE = st.text_input("Enter marital status (1 = married; 2 = single; 3 = others)")
    EDUCATION= st.selectbox('Education (1 = graduate school; 2 = university; 3 = high school; 4 = others)',('1','2','3','4'))
    MARRIAGE= st.selectbox('Martial Status(1 = married; 2 = single; 3 = others)',('1','2','3'))

    AGE= st.text_input("Age (in Years)")
    PAY_1=st.text_input("Enter a number as per following:-2=New account,\
                        0 = minimum payment was made,yet to make full payemnt -1 = pay duly,\
                        1 = payment delay for 1 month,2 = payment delay for 2 months,\
                        3 = payment delay for 3 months,4 = payment delay for 4 months\
                        5 = payment delay for 5 months, 6 = payment delay for 6 months,\
                        7 = payment delay for 7 months\
                        8 = payment delay for 8 months; 9 = payment delay for nine months and above")
    
     
    BILL_AMT1 = st.text_input("Enter last month Bill Amount")
    BILL_AMT2 = st.text_input("Enter 2nd last month Bill Amount ")
    BILL_AMT3 = st.text_input("Enter 3rd last month Bill Amount ")
    BILL_AMT4 = st.text_input("Enter 4th last month Bill Amount ")
    BILL_AMT5 = st.text_input("Enter 5th last month Bill Amount ")
    BILL_AMT6 = st.text_input("Enter 6th last month Bill Amount ")

    PAY_AMT1 = st.text_input("Enter Amount Paid in Last Month")
    PAY_AMT2 = st.text_input("Enter Amount Paid in 2nd Last Month")
    PAY_AMT3 = st.text_input("Enter Amount Paid in 3rd Last Month")
    PAY_AMT4 = st.text_input("Enter Amount Paid in 4th Last Month")
    PAY_AMT5 = st.text_input("Enter Amount Paid in 5th Last Month")
    PAY_AMT6 = st.text_input("Enter Amount Paid in 6th Last Month")
    


    if st.button("Predict"):
        
        features = [LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]
        predict, proba = credit_default(features)
        if predict[0] == 1:
            

            st.success('The account will default with sureity of {} %'.format(round(np.max(proba)*100),2))

        else:
            st.success('The account will not default with sureity of {} %'.format(round(np.max(proba)*100),2))




if __name__ == '__main__':
    main()
