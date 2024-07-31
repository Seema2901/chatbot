# Import python packages
import pandas as pd
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.cortex import Complete
import snowflake.snowpark.functions as F
import snowflake.snowpark.types as T

# Set Streamlit page configuration
st.set_page_config(layout="wide", initial_sidebar_state="expanded")
st.title(":truck: Tasty Bytes Support: Customer Q&A Assistant  :truck:")
st.caption(
    f"""Welcome! This application suggests answers to customer questions based 
    on corporate documentation and previous agent responses in support chats.
    """
)
