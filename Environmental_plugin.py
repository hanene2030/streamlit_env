import streamlit as st

import hmac


def check_login():
    try:
        st.session_state['logged_in'] = st.session_state["password_correct"] 
    except:
        st.session_state['logged_in'] = False

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the passward is validated.
    if st.session_state.get("password_correct", False):
        
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if __name__ =="__main__":
    st.set_page_config(
        page_title="Environmental plugin APIs",
        initial_sidebar_state='expanded',
        layout="wide"
    )
    check_login()
    
    if not check_password():
        #pass
        st.stop()  # Do not continue if check_password is not True.

    # Main Streamlit app starts here

    
    
    st.header("Environmental plugin")
    st.write("The environmental plugin comprises 3 services:")
    st.write("""
                1. The energy consumption predictor:
                    * Is available via a REST api
                2. The energy consumption calculator
                    * Is available via a REST api
                3. The energy consumption measuring tool:
                    *   Python scripts
                    *   Can be installed remotely or directly into the dataset provider servers.
                
                """)



    st.divider()
    #st.write("Author: Hanene")
    
    st.warning("""
        - Do we differentiate between the carbon emission when the dataset is stored into the storage 
               system and the carbon emission during the dataset installation into the storage system?
               
            - I think installing the dataset is an operation :thinking_face:
            - Same question for the energy consumption.

               """)
    st.warning("""
        - Do we have to save the result of the env plugin? If yes,
          how can we do it in the case of the measuring tool? 
          In fact, if the provider download, install and execute the plugin himself.
          How will we get back the result from him? (needs to be defined)
    


    """)