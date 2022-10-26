# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 19:00:48 2021

@author: Harshu
"""

from flask import Flask, render_template, request,jsonify, redirect

import pickle

import numpy as np
app = Flask(__name__)

# Load the saved model
#loaded_model = pickle.load(open('Final_predictive_model/finalized_model.sav', 'rb'))
model=pickle.load(open('model.pkl','rb'))

@app.route("/", methods=['GET', 'POST'])
def home():
    new=''
    if request.method == 'POST':
        # Fetch form data
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction=model.predict(final_features)

        userDetails = request.form
        Gender = userDetails['Gender']
        Married = userDetails['Married']
        Dependents = userDetails['Dependents']
        Education = userDetails['Education']
        Self_Employed = userDetails['Self_Employed']
        Credit_History= userDetails['Credit_History']
        Property_Area= userDetails['Property_Area']
        ApplicantIncomeLog = userDetails['ApplicantIncomeLog']
        LoanAmountLog = userDetails['LoanAmountLog']
        Loan_Amount_Term_Log = userDetails['Loan_Amount_Term_Log']
        Total_Income_Log = userDetails['Total_Income_Log']
        
        
        #Debt_Ratio = userDetails['debtratio']
        '''Monthly_Income = userDetails['monthlyincome']
        Revolving_Utilization_Of_Unsecured_Lines = userDetails['ruoul']

        NumberOfTime30_59DaysPastDueNotWorse = userDetails['30-59 days']
        NumberOfTime60_89DaysPastDueNotWorse = userDetails['60-89 days']
        NintyDays=userDetails['90days']
        NumberOfOpenCreditLinesAndLoans = userDetails['NumberOfOpenCreditLinesAndLoans']

        NumberRealEstateLoansOrLines = userDetails['NumberRealEstateLoansOrLines']


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO data(Age, Nuumber_Of_Dependents,Debt_Ratio,Montly_Income,RUOUL,30_59Days,60_89Days,90_days,Number_of_open_Credit_lines_and_loans,Number_of_real_estate_loans_lines)VALUES(%s, %s,%s, %s,%s, %s,%s, %s,%s,%s)",(Age,Number_of_dependents,Debt_Ratio,Monthly_Income,Revolving_Utilization_Of_Unsecured_Lines,NumberOfTime30_59DaysPastDueNotWorse,NumberOfTime60_89DaysPastDueNotWorse,NintyDays,NumberOfOpenCreditLinesAndLoans,NumberRealEstateLoansOrLines))
        mysql.connection.commit()
        cur.close()
        # return 'Successfully'
        '''   
        print(prediction)
        if prediction==0:
            new='Your loan application is not selected'

        else:
            new='Your loan application is selected'
        
    return render_template("index.html",prediction_result=new)






if __name__ == "__main__":
    app.run(debug=True)