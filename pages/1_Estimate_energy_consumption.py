import streamlit as st



def check_login():
    try:
        logged = st.session_state["logged_in"] 
    except AttributeError :
        st.session_state['logged_in'] = False
        logged = False
    if not logged:
        st.stop()


st.header("Estimate your dataset energy consumption")

check_login() 
col1,col2 = st.columns(2)

with col1:
    st.subheader("Endpoint")
    
    with st.form("my_form_1"):
       
        dataset_id = st.text_input("Dataset identifier", placeholder="http://dn/db?dataset.uri=ns:///Datasets/SpecificURI.sav")
        storage_systems = st.text_input("Storage systems", placeholder="SSD, NAS, DAS, SAN, etc.")

 

        #Intended operations (array) 

        submitted = st.form_submit_button("Submit")
    

with col2:
    
    if submitted:

        st.subheader("Output data")
        st.json({
                "dataset_identifier":"http://yourserver:8080/peb/view/myDialog.spd?dataset.uri=spsscr:///Datasets/SpecificURI.sav",
    
                 "stored_dataset_energy_consumption(kwh)":30,
                "carbon_emissions(kg/kwh)":20,
                "energy_intensity(w/b)":1.4,


                "profile_timestamp":"2023-01-01 12:00:00"
                 })
        st.subheader("Input data")
        st.json({"storage_systems":storage_systems,
                 "storage_system_model":storage_system_model,
                 "storage_system_size":storage_system_size,
                 "geographic_location":geographic_location,
                 "processor_type":processor_speed,
                 "cores":cores,
                 "processor_speed":processor_speed})