import streamlit as st
from book_generator import generate_pdf

st.title("?? JarvisAI Book Generator")
st.write("Type your book's topic and let JarvisAI generate it!")

title = st.text_input("Book Title", "The Rise of JarvisAI")
topic = st.text_area("Book Description / Topic", "Write about AI, future tech, etc.")
num_pages = st.slider("Number of Pages", 1, 100, 10)

if st.button("Generate Book"):
    pdf_path = generate_pdf(title, topic, num_pages)
    with open(pdf_path, "rb") as f:
        st.download_button("?? Download Your Book", f, file_name="JarvisAI_Book.pdf")
