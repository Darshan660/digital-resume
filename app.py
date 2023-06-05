from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Darshan's CV(Contact in Detail).pdf"
profile_pic = current_dir / "assets" / "profile-pic(professional).png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Darshan Kholakiya"
PAGE_ICON = "📋"
NAME = "Darshan Kholakiya"
DESCRIPTION = """
Data Science Enthusiast, seeking to gain hands-on experience in data science and leverage my skills to drive value for organizations.
"""

PROJECTS = {
    "🏆 Sales Dashboard - Perfect overview of sales in particular state wise": "https://public.tableau.com/app/profile/darshan6443/viz/Task3_16496633540690/Dashboard1?publish=yes",
    "🏆 Whatsapp Chat Analyzer - Detailed analysis of your Whatsapp Chats": "https://darshan660-whatsapp-chat-analyzer-app-39qdr8.streamlit.app/",
"🏆 Laptop Price Predictor - Predicts your laptop price with respect to specifications": "https://darshans-project-laptop-price-predictor.streamlit.app/",
"🏆 Asian Landmark Detection - Predicts the name and provides the location of your uploaded Asian landmark": "https://darshans-project-landmark-detection.streamlit.app/"

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

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualifications")

st.write("- ✔️ BSc Data Science | KES Shroff College(Kandivali West)")
st.write("- - "+"2020 - 2023")
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

# --Virtual Internships--
st.write('\n')
st.subheader("Virtual Internships")
st.write("---")
st.write("💻 [Data Analytics Consulting Virtual Internship by **KPMG**](https://drive.google.com/file/d/1pgvFCU0yLsfkrpurqWIFeU2fwmlFKQ4W/view?usp=sharing)")
st.write("💻 [Data Analytics and Visualization Virtual Experience by **Accenture**](https://drive.google.com/file/d/1OMGI8JTw2i9-6WeJCElUECS82FVvALaC/view?usp=sharing)")
st.write("💻 [Data Visualisation: Empowering Business with Effective Insights by **Tata**](https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/Tata/MyXvBcppsW2FkNYCX_Tata_cu2bCcpvCZzhhdHT5_1685965885645_completion_certificate.pdf)")

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
st.write("⭐ [SQL Basic by Hacker Rank](https://www.hackerrank.com/certificates/2210e5fa6e00)")
st.write("⭐ [Python Basic by Hacker Rank](https://www.hackerrank.com/certificates/734db324877c)")
st.write("⭐ [Data Analysis with Python by IBM](https://courses.cognitiveclass.ai/certificates/ed3f311e302e42bb93ca4714102bd94f)")
st.write("⭐ [Data Science 101 by IBM](https://courses.cognitiveclass.ai/certificates/432002b8b4924450ad3a20a06be4c251)")
st.write('')

# Create columns for each social media link
col1, col2, col3, col4 = st.columns(4)

# Add LinkedIn link
with col1:
    st.markdown('<a href="https://www.linkedin.com/in/darshankholakiya/" target="_blank" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png?20140125013055" alt="LinkedIn" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">LinkedIn</p>', unsafe_allow_html=True)

# Add GitHub link
with col2:
    st.markdown('<a href="https://github.com/Darshan660" target="_blank" style="text-decoration:none;"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">GitHub</p>', unsafe_allow_html=True)

# Add Twitter link
with col3:
    st.markdown('<a href="https://wa.me/917710020979?text=Hello%20there,%20thanks%20for%20connecting!" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/1200px-WhatsApp.svg.png" alt="Twitter" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">WhatsApp</p>', unsafe_allow_html=True)

# Add Email link
with col4:
    st.markdown('<a href="mailto:darshankholakiya12@gmail.com"  target="_blank" style="text-decoration:none;"><img src="https://workspace.google.com/static/img/products/png/gmail.png?cache=f50ecb6" alt="Email" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">Email</p>', unsafe_allow_html=True)

# Add footer
st.write('---')
st.write('© Darshan Kholakiya  |  Last updated: June 2023')
