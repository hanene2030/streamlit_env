import streamlit as st


def check_login():
    try:
        logged = st.session_state["logged_in"] 
    except:
        st.session_state['logged_in'] = False
        logged = False
    if not logged:
        st.stop()

st.header("Measure the dataset energy consumption")

check_login()

st.write("This sub tool must be installed on the provider servers.")


st.write("""
         2 modes are possible:
         - Remote installation: 
            * In this case, we need credentials to connect to the provider datasets servers.
         - Local installation:
            * In this case, the provider will download and install the env plugin module in his server. 
              He will execute the script. 
      
         """)

st.divider()


st.warning("""
    - The description of this module needs to be completed/refined.
   
""")