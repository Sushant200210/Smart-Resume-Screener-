import streamlit as st
from utils.pdf_parser import extract_text_from_pdf  
from model.bert_similarity import get_similarity    


st.title("📄 Resume-Job Description Matcher")
st.markdown("Upload a **Job Description** and **Resumes (PDFs)** to rank candidates.")


jd_file = st.file_uploader("Upload Job Description (TXT or PDF)", type=["txt", "pdf"])  
resume_files = st.file_uploader("Upload Resumes (PDFs)", type=["pdf"], accept_multiple_files=True)


if jd_file and resume_files:
   
    if jd_file.type == "application/pdf":
        jd_text = extract_text_from_pdf(jd_file)  
    else:
        jd_text = jd_file.read().decode("utf-8") 


results = []
for resume_file in resume_files:
        resume_text = extract_text_from_pdf(resume_file)
        score = get_similarity(jd_text, resume_text)
        results.append((resume_file.name, float(score)))

st.subheader("🎯 Matching Results")
results_sorted = sorted(results, key=lambda x: x[1], reverse=True)
for i, (name, score) in enumerate(results_sorted, 1):
        st.write(f"{i}. **{name}** → Score: `{score:.3f}`")