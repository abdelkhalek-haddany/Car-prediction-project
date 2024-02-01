import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the pre-trained Logistic Regression model
model = joblib.load('logistic_regression_model.joblib')
df = pd.read_csv("new_catalogue.csv")

# Create a LabelEncoder for each categorical column
label_encoder = LabelEncoder()

# Create a function to get user input and make predictions
def predict_cluster(age, sexe, taux, situationFamiliale, nbEnfantsAcharge, deuxieme_voiture):
    # Create a DataFrame with user input
    input_data = pd.DataFrame({
        'age': [age],
        'sexe': [sexe],
        'taux': [taux],
        'situationFamiliale': [situationFamiliale],
        'nbEnfantsAcharge': [nbEnfantsAcharge],
        '2eme voiture': [deuxieme_voiture]
    })
    
    # Encode categorical columns using the fitted LabelEncoders
    input_data['sexe'] = label_encoder.fit_transform(input_data['sexe'])
    input_data['situationFamiliale'] = label_encoder.fit_transform(input_data['situationFamiliale'])
    input_data['2eme voiture'] = label_encoder.fit_transform(input_data['2eme voiture'])

    prediction = model.predict(input_data)

    cluster_names = {
        0: 'Family Cars',
        1: 'Sport Utility Cars',
        2: 'City Cars',
        3: 'Luxury Cars'
    }
    predicted_class = prediction[0]
    mapped_class = cluster_names.get(predicted_class, 'Unknown Class')
    return mapped_class

def step1():
    st.header("Personal Information")
    age = st.slider('Age', min_value=18, max_value=100, value=20)
    sexe = st.radio('Sexe', ['F', 'M'])
    taux = st.slider('Taux', min_value=100, max_value=10000, value=200)
    situation_familiale = st.selectbox('Situation Familiale', ['Célibataire', 'En Couple', 'Divorcée'])
    nb_enfants_a_charge = st.slider('Nombre d\'enfants à charge', min_value=0, max_value=20, value=0)
    deuxieme_voiture = st.checkbox('Deuxième voiture')
    deuxieme_voiture_str = 'true' if deuxieme_voiture else 'false'
    
    # Store values in session state
    st.session_state.age = age
    st.session_state.sexe = sexe
    st.session_state.taux = taux
    st.session_state.situation_familiale = situation_familiale
    st.session_state.nb_enfants_a_charge = nb_enfants_a_charge
    st.session_state.deuxieme_voiture_str = deuxieme_voiture_str

    return age, sexe, taux, situation_familiale, nb_enfants_a_charge, deuxieme_voiture_str

def step2_3():
    st.header("Car Information")
    selected_occasion = st.selectbox("Select Occasion", ["False", "True"])
    selected_colour = st.selectbox("Select Colour", ["bleu", "noir", "gris", "rouge", "blanc"])
    submit_button = st.form_submit_button("Submit")
    return selected_occasion, selected_colour, submit_button

def show_data():
    # Retrieve values from session state
    age = st.session_state.age
    sexe = st.session_state.sexe
    taux = st.session_state.taux
    situation_familiale = st.session_state.situation_familiale
    nb_enfants_a_charge = st.session_state.nb_enfants_a_charge
    deuxieme_voiture_str = st.session_state.deuxieme_voiture_str
    
    selected_occasion, selected_colour, _ = step2_3()
    prediction_result = predict_cluster(age, sexe, taux, situation_familiale, nb_enfants_a_charge, deuxieme_voiture_str)
    df['occasion'] = df['occasion'].astype(str)
    df['couleur'] = df['couleur'].astype(str)
    filtered_df = df.loc[
        (df['Cluster'] == prediction_result) &
        (df['occasion'] == selected_occasion) &
        (df['couleur'] == selected_colour) 
    ]
    selected_attributes = ['marque', 'nom', 'puissance', 'longueur', 'nbPlaces', 'nbPortes', 'prix']
    filtered_df = filtered_df[selected_attributes]
    
    st.success(f'Predicted Car Type: {prediction_result}')

    # Beautifully display the filtered DataFrame
    st.dataframe(filtered_df.style.highlight_max(axis=0))

def main():
    st.title("Cars Prediction Project")

    # Check if the session state attributes are not initialized
    if "age" not in st.session_state:
        # Initialize variables with default values
        st.session_state.age = 20
        st.session_state.sexe = 'M'
        st.session_state.taux = 200
        st.session_state.situation_familiale = 'Célibataire'
        st.session_state.nb_enfants_a_charge = 0
        st.session_state.deuxieme_voiture_str = 'false'

    with st.form(key="main_form"):
        step = st.session_state.step if "step" in st.session_state else 1

        if step == 1:
            age, sexe, taux, situation_familiale, nb_enfants_a_charge, deuxieme_voiture_str = step1()
        elif step == 2:
            show_data()

        # Navigation buttons
        if step < 2:
            next_button = st.form_submit_button("Next")
            if next_button:
                st.session_state.step = step + 1

        if step > 1:
            prev_button = st.form_submit_button("Previous")
            if prev_button:
                st.session_state.step = step - 1

if __name__ == "__main__":
    main()
