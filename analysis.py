import google.generativeai as genai
from pdf import read_pdf
import streamlit as st
import os
genai.configure(api_key = os.getenv("GOOGLE-API-KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# Read the pdf
def profile(resume, job_desc):
               if resume is not None:
                              resume_doc = read_pdf(resume)
                              st.markdown("Resume has been Uploaded")
               else:
                              st.warning("Resume Missing")
                              
               good_fit = model.generate_content(f'''Act as a HR or Ops head in AI domain and compare {resume} with {job_desc}
and suggest - Am I a Good Fit?''')
               probability = model.generate_content(f'''Act as a HR or Ops head in AI domain and compare {resume} with {job_desc}
and suggest the Probability of Selection(in Percent)''')
               
               # Return the Result
               return(st.write(good_fit.text),
                      st.write(probability.text))