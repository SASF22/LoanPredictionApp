#Core Pkgs
import streamlit as st

#Additional Pkgs



#Fxns
_name_ = '_main_'

def main():
	"""All your code goes here"""
	st.title("Hello Streamlit Lovers")



if _name_ == '_main_':
	main()


# st.text("Hello World this is a text")
# name = "Jesse"
# st.text("This is cool {}".format(name))


# st.subheader("This is a subheader")

# st.title('This is a title')

# st.markdown('## This is markdown')


# #Displaying Colored Text/Bootstraps Alert
# st.success("Successful")
# st.warning("This is danger")
# st.info("This is information")
# st.exception("This is an exception")

# #Superfunction
# st.write('## This is a text')
# st.write(1+2)

# #Help info
# st.help(range)

#Load EDA Pkgs
import pandas as pd

#Display Data
df = pd.read_csv("Loan.csv")
st.dataframe(df)

# #Method 2: Static Table
# st.table(df)

st.write(df.head())

#Buttons

# name = "Jesse"
# if st.button('Submit'):
# 	st.write('Name: {}'.format(name.upper()))

# if st.button('Submit',key='new01'):
# 	st.write('Name: {}'.format(name.lower()))

# #Working with RadioButtons
# status = st.radio('What is your status',('Active','Inactive'))
# if status == 'Active':	
# 	st.success('You are active')
# elif status == 'Inactive':
# 	st.warning('Inactive')

# #Working with Checkbox
# if st.checkbox('Show/Hide'):
# 	st.text('Showing Something')

# if st.beta_expander('Python'):
# 	st.success('Hello Python')

# with st.beta_expander("Julia"):
# 	st.text('Hello Julia')


# *************************IMPORTANT**********************************
my_lang=['Python','Java','C++','C#']
choice = st.selectbox('Language',my_lang)
st.write('You selected {}'.format(choice))

spoken_lang = ('English', 'French', 'Spanish', 'Twi')
my_spoken_lang = st.multiselect('Spoken Lang', spoken_lang, default='English')


#numbers int/float/dates
age = st.slider('Age',0.0,1000.0,5.0, step=0.1)

#any datatype
#select slider
color = st.select_slider('Choose Color',options=['yellow','red','blue','green','black','white'],value=('yellow','red'))


