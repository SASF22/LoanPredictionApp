import streamlit as st 
import pandas as pd 
# from visualizations import run_visulizations_app, data_frame_master
# from data_frame_holder import final_df_retrieval
import matplotlib.pyplot as plt 
import matplotlib 
matplotlib.use('Agg')
import seaborn as sns 
import plotly.express as px
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split






def predictor():		

	df = pd.read_csv('Loan.csv')
	df_1 = df.drop('AnnualIncome',axis=1)
	df_2 = df_1.drop(['TotalAssets','TotalLiabilities'],axis=1)
	df_3 = df_2.drop(['MonthlyDebtPayments','MonthlyLoanPayment'],axis=1)
	df_4 = df_3.drop(['BaseInterestRate'],axis=1)
	df_4a = df_4.copy()
	df_4a.drop(['ApplicationDate','RiskScore'],axis=1,inplace=True)
	employment_values={'Employed':1,'Self-Employed':2,'Unemployed':3}
	educationValues={'High School':1, 'Associate':2, 'Bachelor':3, 'Master':4,'Doctorate':5}
	marital_values={'Married':1, 'Single':2, 'Divorced':3, 'Widowed':4}
	home_ownership_status={'Own':1, 'Mortgage':2, 'Rent':3, 'Other':4}
	loan_purpose_status={'Home':1,'Debt Consolidation':2,'Education':3,'Other':4,'Auto':5}
	df_5 = df_4a.copy()
	df_5['EmploymentStatus']=df_5['EmploymentStatus'].map(employment_values)
	df_5['EducationLevel']=df_5['EducationLevel'].map(educationValues)
	df_5['MaritalStatus']=df_5['MaritalStatus'].map(marital_values)
	df_5['HomeOwnershipStatus']=df_5['HomeOwnershipStatus'].map(home_ownership_status)
	df_5['LoanPurpose']=df_5['LoanPurpose'].map(loan_purpose_status)

	df=df_5.copy()
	

	X=df.drop(['LoanApproved'],axis=1)
	y=df['LoanApproved']	
	X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=22)
	rfc = RandomForestClassifier(n_estimators=20)
	rfc.fit(X_train, y_train)
	preds = rfc.predict(X_test)
	target_names=['class 0', 'class 1']

	submenu = st.sidebar.selectbox('Submenu',['CONFUSION MATRIX', 'LOAN APPROVAL PREDICTION'])
	if submenu == 'CONFUSION MATRIX':
		st.write('confusion matrix portion')
		cm = metrics.confusion_matrix(y_test, preds, labels = rfc.classes_)
		cm_disp = ConfusionMatrixDisplay(confusion_matrix=cm)
		fix, ax = plt.subplots(figsize=(10,10))
		cm_disp.plot(ax=ax)
		st.pyplot(fix)

		st.dataframe(classification_report(y_test,preds, target_names=target_names, output_dict=True))

		st.write('Here is a glimpse of our model\'s confusion matrix.  Based on the data, our model is pretty accurate.')
		

	else:
		st.write('Loan prediction portion')
		col1,col2,col3 = st.columns(3)

		with col1:
			age = st.slider('Age', 18,80,step=1)
			credit_score = st.slider('Credit Score',340,800,step=1 )
			experience = st.slider('Experience in Field',0,65,step=1)
			loan_amount = st.slider('Loan Amount',3000,190000,step=100)
			loan_duration = st.slider('Loan Duration',12,120,step=1)
			cc_utilization_rate = st.slider('Credit Card Utilization Rate',0.001,1.0,step=.001)			
			bankruptcy = st.radio('Have You Ever Filed Bankruptcy',('Yes','No'))
			purpose = st.selectbox('Loan Purpose', loan_purpose_status)
			education = st.selectbox('Education Level',educationValues)	



		with col2:
			savings_account_balance = st.slider('Savings Account Balance',0,205000,step=100)
			checking_account_balance = st.slider('Checking Account Balance',0,52000,step=100)			
			utility_bills_payment_history = st.slider('Utility Bills Payment History',0.2,1.0,step=.01)
			net_worth = st.slider('Net Worth',1000,2700000,step=1000)
			interest_rate = st.slider('Interest Rate',0.10,0.45,step=.01)
			total_debt_to_income_ratio= st.slider('Total Debt To Income Ratio',0.15,5.0,step=.01)				
			number_of_credit_lines = st.slider('Number of Open Credit Lines',0,15,step=1)			
			job_tenure = st.slider('Job Tenure',0,18,step=1)
			home = st.selectbox('Home Ownership Status', home_ownership_status)



			


		with col3:
			monthly_income = st.slider('Monthly Income', 1250,30000,step=100)
			number_of_credit_inquiries = st.slider('Number Of Credit Inquiries',0,8,step=1)
			debt_to_income_ratio = st.slider('Debt To Income Ratio',0.000,1.0,step=.001)
			payment_history = st.slider('Payment History',5,50,step=1)
			length_credit_history = st.slider('Length Of Credit History',1,30,step=1)
			number_of_dependants = st.slider('Number of Dependants',0,6,step=1)
			previous_loan_defaults = st.radio('Previous Loan Default',('Yes','No'))			
			marriage = st.selectbox('Mariage Status', marital_values)
			employment = st.selectbox('Employment Status',employment_values)


		if st.sidebar.button('Check Loan Approval'):
			# st.write(employment_values[employment])
			if bankruptcy == 'Yes':
				bankruptcy_answer = 1
			else:
				bankruptcy_answer = 0
			if previous_loan_defaults == 'Yes':
				previous_default = 1
			else:
				previous_default = 0
			approval = rfc.predict([[age,credit_score,employment_values[employment],educationValues[education],experience,loan_amount,loan_duration,
			marital_values[marriage],number_of_dependants,home_ownership_status[home],cc_utilization_rate, number_of_credit_lines,number_of_credit_inquiries,
			debt_to_income_ratio,bankruptcy_answer,loan_purpose_status[purpose],previous_default,payment_history,length_credit_history,savings_account_balance,
			checking_account_balance,monthly_income,utility_bills_payment_history,job_tenure,net_worth,interest_rate,total_debt_to_income_ratio,]])
			if approval == 1:
				st.success('***YOU ARE APPROVED***')
			else:
				st.warning('Sorry, you are not approved.')
				st.warning('It may help to adjust the interest rate, loan duration, and loan amount.')



