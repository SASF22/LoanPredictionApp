import streamlit as st 








def info():
	st.title("Loan Prediction Application")
	st.write("Welcome to the  Loan Prediction Application.")

	st.write("This application was created to perform loan approvals for **Munder Difflin Finance Company**.")
	st.write("Use the Menu to the left of the screen to navigate through the available categories.")
	st.write("")
	st.write("")

	st.subheader("DATA MANIPULATION")
	st.write("To view the technical details of the data used to create the ML Model, both before and after "
	"the data was manipulated, select **\"DATA MANIPULATION\"** from the dropdown menu.")
	st.write("  You can then use the submenu dropdown view the steps in the data-cleaning process used to arrive "
	"at the data in its final form.")
	st.write("")
	st.write("")

	st.subheader("LOAN APPROVAL")
	st.write("To use the loan approval portion of the application, select **\"LOAN PREDICTION\"** from the menu dropdown. "
	"Next select **\"LOAN APPROVAL PREDICTION\"** from the submenu.  You can then enter the information needed by use of "
	"the easy-to-understand widgets.  Use the **\"Check Loan Approval\"** button to the left to see if a loan will be "
	"approved or not approved.")
	st.write("To view the metrics of the Loan-Predicting ML Model, select **\"CONFUSTION MATRIX\"** from the submenu.")
