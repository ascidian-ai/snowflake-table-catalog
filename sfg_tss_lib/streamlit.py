import os
import validators
from sfg_tss_lib.common import common
import streamlit as st

class helper_functions:

    def set_css(self, css) -> None:
        if validators.url(css):
            st.markdown(f'<link href="{css}" rel="stylesheet">', unsafe_allow_html=True)
        else:
            if os.path.isfile(css):
                with open(css) as f:
                    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
            else:
                FileNotFoundError(css)
        return

    def page_config(self, css, initial_sidebar_state=common.app_initial_sidebar_state) -> None:
        st.set_page_config( page_title=common.app_name,
                            page_icon=common.page_icon,
                            layout=common.page_layout,
                            initial_sidebar_state=initial_sidebar_state)
        try:
            self.set_css(css=css)
        except FileNotFoundError as e:
            st.error(e)
        return