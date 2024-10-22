import pickle
import streamlit as st

# Set the title of the app
st.title('System which tells whether the person will be save from sinking')

# Attempt to load the model
try:
    with open('random_forest.pkl', 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Failed to load model: {e}")

# Input fields for user data
sex = st.selectbox('Enter Your Sex', options=['male', 'female'])  # Selectbox for sex
age = st.number_input('Enter Your Age', min_value=0, max_value=100, step=1)  # Number input for age
sibsp = st.number_input('Enter Your SibSp (Siblings/Spouses aboard)', min_value=0, step=1)  # Number input for SibSp
parch = st.number_input('Enter Your Parch (Parents/Children aboard)', min_value=0, step=1)  # Number input for Parch
embarked = st.selectbox('Enter Your Embarked Port', options=['C', 'Q', 'S'])  # Selectbox for Embarked

# Prediction button
if st.button('Predict'):
    try:
        # Transform inputs into the expected 5 features format for the model
        sex_binary = 1 if sex == 'male' else 0  # Convert 'male' to 1 and 'female' to 0
        embarked_mapping = {'C': 0, 'Q': 1, 'S': 2}  # Assuming 'embarked' is encoded as 0, 1, 2
        embarked_encoded = embarked_mapping[embarked]
        
        # Prepare the input as a 2D list with 5 features
        prediction_input = [[age, sex_binary, sibsp, parch, embarked_encoded]]
        
        # Make prediction
        makeprediction = model.predict(prediction_input)
        output = makeprediction[0]
        
        # Display result
        if output == 1:
            st.success('The person is predicted to survive.')
        else:
            st.success('The person is predicted not to survive.')
    except Exception as e:
        st.error(f"Prediction failed: {e}")
