import streamlit as st



def check_login():
    try:
        logged = st.session_state["logged_in"] 
    except:
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
       
    
        storage_systems = st.multiselect("Storage systems",['HDDs', 'SSDs', 'SAN', 'NAS'])
        storage_system_model = st.text_input("Storage system model")
        storage_system_size = st.number_input("Storage system size(GB)")
        geographic_location = st.text_input("Geographic location", placeholder="loc.coords.latitude,loc.coords.longitude}")
        processor_speed = st.multiselect("Processor type ",['CPU',"GPU"], default=["CPU"])
        cores = st.number_input("Number of cores",min_value=1, value=8)
        processor_speed = st.number_input("Processor speed(Hz)")
        

        #Intended operations (array) 

        submitted = st.form_submit_button("Submit")
    

with col2:
    
    if submitted:
        st.subheader("Input data")
        st.json({"storage_systems":storage_systems,
                 "storage_system_model":storage_system_model,
                 "storage_system_size":storage_system_size,
                 "geographic_location":geographic_location,
                 "processor_speed":processor_speed,
                 "cores":cores,
                 "processor_speed":processor_speed
                 })
        
        st.subheader("Output data")
        st.json({"energy_consumption":"30",
                 "energy_intensity_profile":"1.4",
                 "carbon_emissions":20,
                 "profile_timestamp":"2023-01-01 12:00:00"
                 })
    





