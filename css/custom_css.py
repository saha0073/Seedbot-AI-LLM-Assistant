# custom_css.py

import streamlit as st

def inject_custom_css():
    st.markdown(
        """
        <style>
        .radio {
            display: flex;
            align-items: center;
        }
        .radio input {
            width: 1.5em;
            height: 1.5em;
        }
        .radio label {
            font-size: 1.5em;
            display: flex;
            align-items: center;
            gap: 0.5em;
        }
        .radio .icon {
            font-size: 1.5em;
        }
        
        /* Updated styles for agent descriptor with a bright green color */
        .agent-descriptor {
            color: #4CAF50;    /* Bright green for high visibility */
            font-size: 1.2em;    /* Increase the font size */
            font-weight: bold;   /* Bold to make it stand out */
            margin-top: 5px;     /* Space above the text */
            text-align: center;  /* Center the text for better presentation */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )