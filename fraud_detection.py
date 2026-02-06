import streamlit as st
import pandas as pd
import joblib

model = joblib.load('fraud_detection_pipeline.pkl')

st.title('Fraud Detection Prediction App')
st.markdown("Please enter the prediction details and click on the button.")
st.divider()

transaction_type = st.selectbox('Transaction Type', ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEPOSIT'])

amount = st.number_input('Transaction Amount', min_value=0.0, value = 1000.0)

oldbalanceOrg = st.number_input('Old Balance of Origin Account', min_value=0.0, value = 10000.0)

newbalanceOrig = st.number_input('New Balance of Origin Account', min_value=0.0, value = 9000.0)

oldbalancedest = st.number_input('Old Balance of Destination Account', min_value=0.0, value = 0.0)

newbalancedest = st.number_input('New Balance of Destination Account', min_value=0.0, value = 0.0)

if st.button("Predict"):


    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalancedest],
        'newbalanceDest': [newbalancedest]

    })
    prediction = model.predict(input_data)[0]


    
    st.subheader(f" Prediction : ' {int(prediction)}'")

    if prediction == 1:
        st.error('The transaction is predicted to be Fraudulent.')
    else:
        st.success('The transaction is predicted to be Not Fraudulent.')

