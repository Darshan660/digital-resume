from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic (3).png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Darshan Kholakiya"
PAGE_ICON = ":wave:"
NAME = "Darshan Kholakiya"
DESCRIPTION = """
Data Science Enthusiast, seeking to gain hands-on experience in data science and leverage my skills to drive value for organizations.
"""
EMAIL = "darshankholakiya12@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/darshankholakiya",
    "GitHub": "https://github.com/Darshan660"
}
PROJECTS = {
    "🏆 Sales Dashboard - Perfect overview of sales in particular state wise": "https://public.tableau.com/app/profile/darshan6443/viz/Task3_16496633540690/Dashboard1?publish=yes",
    "🏆 Whatsapp Chat Analyzer - Detailed analysis of your Whatsapp Chats": "https://youtu.be/3egaMfE9388"

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.image(profile_pic, width=290)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[1].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualifications")

st.write("- ✔️ BSc Data Science | KES Shroff College(Kandivali West)")
st.write("- - "+"2020 - Present")
st.write("- ✔️ HSC | Shri T.P. Bhatia College of Science(Kandivali West)")
st.write("- - "+"2018 - 2020")
st.write("- ✔️ SSC | Rustomjee International School(Dahisar West)")
st.write("- - "+"2007 - 2018")

# --- SKILLS ---
st.write('\n')
st.subheader("Professional proficiencies")
col1,col2 = st.columns(2)
with col1:
    st.write(
        """
    - ➡️ Programming
    - ➡️ Machine Learning
    - ➡️ Data wrangling
    - ➡️ Data Analysis
    """
    )
with col2:
    st.write(
        """
        - ➡️ Data Visualization
        - ➡️ Business acumen
        - ➡️ Problem-solving
        - ➡️ Attention to detail
        """
    )

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "[Data Analyst Intern | Dowell Research India](https://drive.google.com/file/d/1RdlEus2yYHSQduBE3rPmU-MK_cZA0WYW/view?usp=sharing)")
st.write("- "+"Aug 2022 - Feb 2023")
st.write(
    """
- ► Collected, cleaned and standardized data of global indicators for 49 countries using google spreadsheet.
- ► Worked on Google Data Studio to generate visualization charts like bar graphs, pie charts, funnel charts, filled map, and many more charts for making the reports.
- ► Worked with the team of data analyst and conducted analysis on data and provided insights to support business decisions.
- ► Collaborated with cross functional teams to identify data trends, patterns and exchange information to complete the requirments.
- ► Also contributed in developing and implementing data quality control measures to ensure good data and accurate data analysis 
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "[Data Science Intern | LetsGrowMore](https://drive.google.com/file/d/1mmcNWJKBLp8w-fVe4qwO8IfxHbi-nfwW/view?usp=sharing)")
st.write("- "+"Jun 2022 - Jul 2022")
st.write(
    """
- ► Build an Iris flower classification model with algorithms like Logistic Regression and Decision Tree Classifier to predict the species of the flower.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "[Data Science & Business Analytics Intern | The Sparks Foundation](https://drive.google.com/file/d/12eFNXTwrPAT-0TzH426Y8D98mTKWfGiS/view?usp=sharing)")
st.write("- "+"Apr 2022 - May 2022")
st.write(
    """
- ► Build a sales performance dashboard on tableau for US Sample store dataset to compare the sales between the states and region and also displayed the KPI's on the dashboard.
- ► Build a Unsupervised machine learning model that predicts student’s score based upon the number of hours studied.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Certificates ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
st.write("⭐ [Data Analytics Consulting Virtual Internship](https://drive.google.com/file/d/1pgvFCU0yLsfkrpurqWIFeU2fwmlFKQ4W/view?usp=sharing)")
st.write("⭐ [SQL Basic by Hacker Rank](https://www.hackerrank.com/certificates/2210e5fa6e00)")
st.write("⭐ [Python Basic by Hacker Rank](https://www.hackerrank.com/certificates/734db324877c)")
st.write("⭐ [Data Analysis with Python by IBM](https://courses.cognitiveclass.ai/certificates/ed3f311e302e42bb93ca4714102bd94f)")
st.write("⭐ [Data Science 101 by IBM](https://courses.cognitiveclass.ai/certificates/432002b8b4924450ad3a20a06be4c251)")
