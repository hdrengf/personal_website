import streamlit as st
import os
import base64

def load_css():
    # Get the absolute path to the current directory
    current_dir = os.path.dirname(__file__)
    
    # Construct the path to styles.css relative to the current directory
    css_path = os.path.join(current_dir, 'styles.css')
    
    # Open and read the contents of styles.css
    with open(css_path) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    
    # Load Bootstrap CSS
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

def st_button(url, label, iconsize, custom_icon):
    image_path = os.path.join(os.path.dirname(__file__), 'static', custom_icon)
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    
    button_code = f'''
    <p>
        <a href="{url}" class="btn btn-outline-secondary btn-lg btn-block" type="button" aria-pressed="true">
            <img src="data:image/png;base64,{encoded_image}" width="{iconsize}" height="{iconsize}" style="vertical-align: middle; margin-right: 10px;"/>
            {label}
        </a>
    </p>'''
    return st.markdown(button_code, unsafe_allow_html=True)