import os
from pathlib import Path
import streamlit as st
from sfg_tss_lib.common import common
from sfg_tss_lib.streamlit import helper_functions

#########################################################################################
os.chdir(Path(__file__).parent.parent)
cwd = os.getcwd()
#########################################################################################
# PAGE CONFIGURATION | No Streamlit commands before this line!
sfg_st = helper_functions()
sfg_st.page_config(css='css/style.css')

# ----------------------------------------------------------------------------
# SET PAGE TITLE AND LOGO
st.image(image=common.logo_image, width=common.logo_size)
st.title('About')
st.divider()
#########################################################################################
# PAGE CONTENT
st.subheader(f'Version {common.app_version}')
st.subheader('COPYRIGHT & ATTRIBUTIONS')
st.markdown(common.app_copyright)
st.subheader('CREDITS')
st.markdown('Author | Steven Tuften')

st.snow()



