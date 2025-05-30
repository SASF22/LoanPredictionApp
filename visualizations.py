import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib 
matplotlib.use('Agg')
import seaborn as sns 
import plotly.express as px












def run_visulizations_app():
	# data_frame_master()
	st.subheader('Loan Data')

def data_frame_master():
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


	# st.dataframe(df)


	submenu = st.sidebar.selectbox('Submenu',['RAW/MANIPULATED DATA','FIRST CORRELATION','SECOND CORRELATION','THIRD CORRELATION','FOURTH CORRELATION','EMPLOYMENT/INCOME/EDUCATION','FINAL'])
	if submenu == 'RAW/MANIPULATED DATA':
		st.write('Data before manipulation.')
		st.dataframe(df)
		st.write('')
		st.write('')
		st.write('')
		st.write('')
		st.write('Data after manipulation.')
		st.dataframe(df_5)

	elif submenu == 'FIRST CORRELATION':
		st.write('The first correlation seen was the correlation between' +
			' the two independent variables Monthly Income and Annual Income.')
		test_f = df[['MonthlyIncome','AnnualIncome']]
		correlation = test_f.corr()
		fig, ax = plt.subplots(figsize=(10,8))
		ax.scatter([1,2],[1,2])
		#plt.figure(figsize=(10,8))
		sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
		plt.title('Correlation Heatmap')
		plt.show()
		st.pyplot(fig)
		st.write("As you can see from the heatmap, the correlation between the "+
			"two independent variables is very high.")
		st.write("I created a column and named it \"Calculated Annual Income\"."+
			'   This column was just the contents of Monthly Income multiplied by twelve.')
		st.write('Click the \'Calculated Annual Income\' drop down just below to see the results.')

		with st.expander('Calculated Annual Income'):
			test_f.loc[:,'Calculated Annual Income'] = test_f.loc[:,'MonthlyIncome'] * 12
			st.write(test_f.head())
			st.write('The Calculated Annual Income column is exactly the same '
				'as the AnnualIncome column.  To remove this correlation from the data, AnnualIncome '
				'will be dropped as an independent variable.')
		


	elif submenu == 'SECOND CORRELATION':
		st.write('We notice that there is a NetWorth column and a TotalAssets column and a TotalLiabilities column.')
		st.write('This would lead us to believe that NetWorth is calculated by subtracting the TotalLiabilities column from the TotalAssets column.') 
		st.write('First let\'s see if there is any correlation between the three columns.')	

		test_f = df_1[['NetWorth', 'TotalAssets', 'TotalLiabilities' ]]
		correlation = test_f.corr()
		fig, ax = plt.subplots(figsize=(10,8))
		ax.scatter([1,2,3],[1,2,3])
		sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
		plt.title('Correlation Heatmap')
		plt.show()
		st.pyplot(fig)

		st.write('So there is a strong correlation between NetWorth and TotalAssets. The correlation between NetWorth and TotalLiabilities is not as strong'
		' as the correlation between NetWorth and TotalAssets')
		st.write('I created a column named \"Calculated Net Worth.\"  This column is the subtraction of TotalLIabilities from TotalAssets')
		st.write('Use the \"Calculated Net Worth\" dropdown below to see the results')

		with st.expander('Calculated Net Worth'):
			test_f.loc[:,'Calculated Net Worth'] = test_f.loc[:,'TotalAssets'] - test_f.loc[:,'TotalLiabilities']
			st.write(test_f.head())
			st.write('With the exception of Row #2, Net Worth seems to be TotalLiabilities subtracted from TotalAssets.')
			st.write('Row 2 may just be a typo.')
			st.write('To remove this correlation from the data, we will remove the TotalAssets independent variable' 
			' and the TotalLiabilities independent variable.')




	elif submenu == 'THIRD CORRELATION':
		st.write('There may also be a correlation between MonthlyIncome, MonthlyDebtPayments, MonthlyLoanPayment and either DebtToIncomeRatio '
		'or TotalDebtToIncomeRatio.') 
		st.write('Let\'s explore any correlation between the five columns')

		
		test_f = df_2[['MonthlyIncome','MonthlyDebtPayments','MonthlyLoanPayment','DebtToIncomeRatio','TotalDebtToIncomeRatio']]
		correlation = test_f.corr()
		fig, ax = plt.subplots(figsize=(12,12))
		ax.scatter([1,2,3,4,5],[1,2,3,4,5])
		sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
		plt.title('Correlation Heatmap')
		plt.show()
		st.pyplot(fig)

		st.write('So there seems to be a correlation between TotalDebtToIncomeRatio, MonthlyIncome, '
		' MonthlyDebtPayments, and MonthlyLoanPayment.' )
		st.write('We will test this out and see if TotalDebtToIncomeRatio is MonthlyDebtPayments added to '
		'MonthlyLoanPayment and then divided by MonthlyIncome.')
		st.write('To do this, there has been a column created named \"Calculated Total Debt To Income Ratio.\"'
		'This column will be created by first calculating the sum of MonthlyDebtPayments and MonthlyLoanPayment. '
		'After the sum is calculated, we will divide it by MonthlyIncome. We will then see if our created column, '
		'\"Calculated Total Debt To Income Ratio\" matches the TotalDebtToIncomeRatio column.')
		st.write('Use the \'Calculated Total Debt To Income Ratio\' dropdown to see the results.')

		with st.expander('Calculated Total Debt To Income Ratio'):
			test_f.loc[:,'CalcTotalDebtToIncomeRatio'] = (test_f.loc[:,'MonthlyDebtPayments'] + test_f.loc[:,'MonthlyLoanPayment'])/test_f.loc[:,'MonthlyIncome']
			st.write(test_f.head())
			st.write('We can now see that the TotalDebtToIncomeRation is the MonthlyDebtPayments plus the MonthlyLoanPayment divided by the MonthlyIncome.')
			st.write('We will remove this correlation by dropping the MonthlyDebtPayments and MonthlyLoanPayment columns.')

	elif submenu == 'FOURTH CORRELATION':
		st.write('Next I wanted to see how much correlation there is between the LoanAmount, LoanDuration, BaseInterestRate, and '
		'InterestRate.') 
		st.write('I hypothesized a strong correlation between some of these independent variables due to the fact that they are '
		'all used together in calculating the loan payment ammount.')
		st.write('The heatmap below shows the correlation between these independent variables.')

		test_b = df_3[['LoanAmount','LoanDuration','BaseInterestRate','InterestRate']]
		
		correlation = test_b.corr()
		fig, ax = plt.subplots(figsize=(10,8))
		sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
		plt.title('Correlation Heatmap')
		plt.show()
		st.pyplot(fig)

		st.write('Next to make the correlation a little more visible to see, I created a pairplot between the earlier stated independent '
		'variables.') 
		st.write('You can see some of the strong correlations, especially between the BaseInterestRate and the InterestRate variable.')
		
		fig2 = sns.pairplot(data=test_b)
		st.pyplot(fig2)

		st.write('The main objective is to have an accurate model with as few independent variables as possible.')
		st.write('BaseInterestRate was removed because of its strong correlation to other independent variables.') 
		st.write('LoanAmount and LoanDuration were not removed because they are key independent variables that a loan applicant ' 
		'is going to factor into their decision in pursuing a loan.')
		st.write('A loan applicant wouldn\'t just simply say they want a loan, but they would say they want a loan for a specific amount '
		'of money over a specific duration of time.')

	elif submenu == 'EMPLOYMENT/INCOME/EDUCATION':
		st.write('Next, I wanted to explore the relationship between EmploymentStatus and MonthlyIncome. '
		'I wanted to see if there was a strong connection between EmploymentStatus and the MonthlyIncome. '
		'I will start by just considering the count of loan seekers with different employment status.')

		fig3 = plt.figure(figsize=(10,5))
		sns.countplot(x='EmploymentStatus',data=df_4)
		st.pyplot(fig3)

		st.write('So from the graph, you can tell that most of the samples that applied for a loan were employed. '
		'There were slightly more self-employed than unemployed.')
		st.write('I next wanted to see if the employed and self-employed samples had a significantly higher income than the unemployed. '
		'So I decided to group the samples by employment status and examine the monthly income information for each employment status side by side.')

		employStat = df_4.groupby("EmploymentStatus")
		st.write(employStat['MonthlyIncome'].describe(include='all'))	

		st.write('So I did not find that employed samples had a significantly higher average monthly income than unemployed. In fact, '
		'unemployed samples had a slightly higher average monthly income than the employed sample.')
		st.write('I wanted to explore and examine this information further, except this time I wanted to break it up by education level.')
		st.write('I wanted to examine the different sample\'s employment status as it relates to monthly income, '
		'but I wanted to further examine it by education level.')

		fig4 = plt.figure(figsize=(10,10))
		sns.boxplot(x='EmploymentStatus', y='MonthlyIncome', hue='EducationLevel',data=df_4, palette='coolwarm')
		plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
		st.pyplot(fig4)

		st.write('We end up with an interesting chart that has many more samples that are employed. The standard deviation of all the '
		'employment status samples overlap somewhat with a lot of outliers in the $12,000 and above income range.')



		
	else:
		st.write('The easily-discovered correlation has been removed. The final independent variables that will be removed are Application date and Risk Score.')
		st.write('Application date shoiuld not be considered when accepting or rejecting a loan.')
		st.write('Risk score is the calculation achieved from all of the other independent variables.  I believe risk score would be used as a dependant variable for a '
		'continuous correlation model.')
		
		st.write('')
		st.write('')
		st.write('')
		st.subheader('Further Data Manipulation')
		st.write('The next step in the data-cleaning process is formatting the data to be used by the ML Model. The non-numerical objects '
		'need to be converted to numerical values.')

		st.write('Below is the data ***before*** converting the non-numerical values.')
		st.write(df_4a.head())


		st.write('Below is the data ***after*** converting the non-numerical values.')
		st.write(df_5.head())

		st.markdown('**EmploymentStatus**, **EducationLevel**, **MaritalStatus**, **HomeOwnershipStatus**, and **LoanPurpose** have all been '
		'converted to numerical values.')




