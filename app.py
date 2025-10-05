import streamlit as st
from PIL import Image
from st_functions import st_button, load_css

st.set_page_config(initial_sidebar_state="auto",layout="wide")
load_css()
with st.sidebar:
    col1, col2, col3 = st.columns(3)
    col2.image(Image.open('.\static\Haslett_Headshot-modified.png'))

    st.markdown("<h1 class='sidebar'>Reach Out</h1>", unsafe_allow_html=True)
    icon_size = 20
    with st.container():
        st_button('mailto:hdrengf@gmail.com', 'Email me', icon_size, 'email_blue.png')
        st_button('https://www.linkedin.com/in/haslett-fernandes/', 'Follow me on LinkedIn', icon_size, 'linkedin_icon.png')
        st_button('https://github.com/shupersap', 'Follow me on GitHub', icon_size, 'github_blue.png')
        st_button('https://www.kaggle.com/haslettfernandes', 'Follow me on Kaggle', icon_size, 'kaggle_icon.png')
        st_button('https://platform.stratascratch.com/user/shupersap', 'Follow me on StrataScratch', icon_size, 'stratascratch_icon.png')


st.markdown("<h1 class='custom-header'>Haslett Fernandes</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='custom-header'>Data Scientist</h2>", unsafe_allow_html=True)
st.divider()


with st.container(border=True):
    st.markdown("<h3 class='custom-header'>About Me</h3>",unsafe_allow_html=True)
    st.write(" Proficient data scientist/analyst that has mastered concepts involving ETL, EDA, Visualizations, and utilization of cloud based tools. Currently well-versed in machine learning concepts, though still trying to master most aspects, utilizing my skills on datasets and problems in kaggle and self-developed projects. Looking to get more experience in the field and develop my career. ")

with st.expander("See my skills",expanded=True):
    with st.container(border=True):
        st.markdown("<h3 class='custom-header'>Skills</h3>",unsafe_allow_html=True)
        
        col1, col2, col3,col4 = st.columns(4)
        col1.write("Python")
        col2.write("SQL/noSQL")
        col3.write("R")
        col4.write("HTML/CSS/JavaScript")
        
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        col1, col2, col3,col4 = st.columns(4)
        col1.write("Google Cloud")
        col2.write("Azure Cloud")
        col3.write("AWS Cloud")
        col4.write("Atlas")
        
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        col1, col2, col3,col4 = st.columns(4)
        col1.write("Pandas")
        col2.write("Sklearn")
        col3.write("Numpy")
        col4.write("NLTK")

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        col1, col2, col3,col4 = st.columns(4)
        col1.write("Matplotlib")
        col2.write("beatifulsoup")
        col3.write("ggplot/bokeh/seaborn")
        col4.write("plotly")

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        col1, col2, col3,col4 = st.columns(4)
        col1.write("Flask/Streamlit")
        col2.write("Excel")
        col3.write("Tableau")
        col4.write("PowerBi")

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        col1, col2, col3,col4 = st.columns(4)
        col1.write("Web viz/Streamlit")
        col2.write("Database Manipulation")
        col3.write("Deep learning/Neural Networks")
        col4.write("Natural language processing")

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        col1, col2, col3,col4 = st.columns(4)
        col1.write("Time series analysis")
        col2.write("ML tuning/pipepline")
        col3.write("Feature Engineering")
        col4.write("Data presentation")

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("<h3 class='custom-header'>Projects</h3>",unsafe_allow_html=True)
    tab1,tab2,tab3=st.tabs(["NLP Modeling","Time Series Modeling", "EDA"])
    with tab1:
        st.markdown("<h2 class='project-header'>Illness and Condition</h2>", unsafe_allow_html=True)
        st.markdown("<h3 class='project-sub-header'>Project Outline</h3>", unsafe_allow_html=True)
        st.write("""Data was retrieved through webscraping  techniques primarily involving BeatifulSoup on the
                 NHS inform, who's organization is based in Scotland, """)

        st.markdown("<h3 class='project-sub-header'>skills/tools utilized</h3>", unsafe_allow_html=True)

        st.markdown("<h3 class='project-sub-header'>Real world Application</h3>", unsafe_allow_html=True)


    with tab2:
        st.markdown("<h2 class='project-header'>Virtual Skepticism</h2>", unsafe_allow_html=True)
        st.markdown("<h3 class='project-sub-header'>Project Outline</h3>", unsafe_allow_html=True)
        st.markdown("<h3 class='project-sub-header'>skills/tools utilized</h3>", unsafe_allow_html=True)
        st.markdown("<h3 class='project-sub-header'>Real world Application</h3>", unsafe_allow_html=True)

        
    with tab3:
        st.markdown("<h2 class='project-header'>Global Landslide</h2>", unsafe_allow_html=True)
        st.markdown("<h3 class='project-sub-header'>Project Outline</h3>", unsafe_allow_html=True)
        st.markdown("<h3 class='project-sub-header'>skills/tools utilized</h3>", unsafe_allow_html=True)
        st.markdown("<h3 class='project-sub-header'>Real world Application</h3>", unsafe_allow_html=True)

        