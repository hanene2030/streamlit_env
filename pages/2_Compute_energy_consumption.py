import streamlit as st



def check_login():
    try:
        logged = st.session_state["logged_in"] 
    except:
        st.session_state['logged_in'] = False
        logged = False
    if not logged:
        st.stop()


st.header("Compute your dataset energy consumption")
check_login()
    
col1,col2 = st.columns(2)

with col1:
    st.subheader("Endpoint")
    
    with st.form("my_form_2"):
        dataset_id = st.text_input("Dataset identifier", placeholder="http://dn/db?dataset.uri=ns:///Datasets/SpecificURI.sav")
        address_ip = st.text_input("Adress IP", placeholder="127.0.0.0")
        data_sources_path = st.text_input("Data source path", placeholder='/home/')
        storage_systems = st.text_input("Storage systems", placeholder="SSD, NAS, DAS, SAN, etc.")

        storage_system_model = st.text_input("Storage system model", placeholder="File storage, cloud Storage")
        storage_system_size = st.text_input("Storage system size(GB)",placeholder="500")
        geographic_location = st.text_input("Geographic location", placeholder="Irelande,France")
      
        processor_type   = st.text_input("Processor type", placeholder="CPU, GPU")
        cores = st.text_input("Number of cores",placeholder="8")
        processor_speed = st.text_input("Processor speed(Hz)" , placeholder="3.2")
         
        operations_type = st.text_input("Operations" , placeholder="select,update, etc.")

        submitted = st.form_submit_button("Submit")
    

with col2:
    
    if submitted:


        st.subheader("Output data")
        st.json({
                "dataset_identifier":"http://yourserver:8080/peb/view/myDialog.spd?dataset.uri=spsscr:///Datasets/SpecificURI.sav",
                "stored_dataset_energy_consumption(kwh)":30,
                "carbon_emissions(kg/kwh)":20,
                "energy_intensity(w/b)":1.4,
            
                "total_energy_consumption(kwh)":51 ,
                "total_carbon_emission(kg/kwh)":33,
                "profile_timestamp":"2023-01-01 12:00:00"
                 })
    
        st.subheader("Input data")
   
        st.json({
                "address_ip" : address_ip,
                "data_sources_path":data_sources_path,
                "storage_systems":storage_systems,
                 "storage_system_model":storage_system_model,
                 "storage_system_size":storage_system_size,
                 "geographic_location":geographic_location,
                 "processor_type":processor_type,
                 "cores":cores,
                 "processor_speed":processor_speed
                 })
        






