from dotenv import load_dotenv
load_dotenv() # Activate the Local Env Vars
import streamlit as st
import google.generativeai as genai
from pdf import read_pdf
from analysis import profile

# Create the Front End...
st.header(":blue[Resume Analysis] Using AI 📝", 
          divider = "green")
st.subheader("Tips for Using the Application")
# Resume Part
st.sidebar.subheader("Upload the Resume 📍")
resume = st.sidebar.file_uploader(label = "Browse",
                         type = ["pdf"])
notes = f'''
* **Upload the Resume**: Please Upload your Resume. This is a GENAI App to extract Insights
* **Job Description**: Copy Paste the Job Description from Job Boards.
* **Unleash the Power of Gen AI Model**: Click on the Button to generate Insights.'''
st.write(notes)

# Job Desc
st.subheader("Enter the Job Description",
             divider = True)

job_desc = st.text_area(label = "Copy Paste Job Desc",
                        max_chars = 10000)

button = st.button(label = "Get AI Powered Insights")
if button:
               st.markdown(profile(resume=resume, job_desc=job_desc))

