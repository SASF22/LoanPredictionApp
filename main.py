import streamlit as st
from visualizations import run_visulizations_app, data_frame_master
from loan_prediction import predictor
from about import info






def main():
	# st.title('Loan Application App')


	menu = ['START','DATA MANIPULATION','LOAN PREDICTION']
	choice = st.sidebar.selectbox('Menu',menu)


	if choice == 'START':
		info()

	elif choice == 'DATA MANIPULATION':
		run_visulizations_app()
		data_frame_master()
	else: 
		predictor()	
	


if __name__ == '__main__':
	main()