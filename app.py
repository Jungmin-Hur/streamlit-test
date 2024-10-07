import streamlit as st
import time

# @st.cache_resource
def get_global_key():
    if 'global_key' not in st.session_state:
        st.session_state['global_key'] = str(time.time())
    return st.session_state['global_key']

st.session_state['key'] = get_global_key()

# Display the key value
st.write('Current key value:')
st.write(st.session_state['key'])
