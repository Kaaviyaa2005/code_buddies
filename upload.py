import streamlit as st
import pdfplumber
from fpdf import FPDF
import groq
from groq import Groq
import time
from assessment import display_assessment

# Function to extract text from PDF (only first 5 lines for speed)
def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        first_page = pdf.pages[0]
        extracted_text = first_page.extract_text()
        if extracted_text:
            return "\n".join(extracted_text.split("\n")[:5])  # Extract first 5 lines
    return ""

# Function to generate questions efficiently
def generate_questions(text):
    shortened_text = text[:50]  # Reduce API input size for speed
    prompt = f"""Generate 5 multiple-choice questions from this text. 
    Each question should have 4 options (A, B, C, D).
    Do NOT include the correct answer.
    Format:
    
    Question: [question text]
    A) [option]
    B) [option]
    C) [option]
    D) [option]
    
    Text: {shortened_text}
    """

    try:
        client = Groq(api_key="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")  # Replace with your API key
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,  # Reduce randomness for faster response
            max_tokens=150,  # Reduce max tokens to speed up processing
            stream=False
        )
        return completion.choices[0].message.content

    except groq.GroqError as e:
        if "rate_limit_exceeded" in str(e):
            time.sleep(10)  # Wait 10 seconds before retrying
            return generate_questions(shortened_text)  # Retry with same text
        return f"Error: {str(e)}"

# Function to create a PDF with the generated questions
def create_pdf(questions):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(190, 8, questions)  # Optimized layout
    pdf_path = "generated_questions.pdf"
    pdf.output(pdf_path, "F")  # Faster saving
    return pdf_path

# Initialize session state
st.session_state.setdefault('questions', None)
st.session_state.setdefault('is_assessment_started', False)
st.session_state.setdefault('questions_text', "")
st.session_state.setdefault('text_content', "")

# Main App
if not st.session_state.is_assessment_started:
    st.title("📚 Quiz Generator")

    uploaded_file = st.file_uploader("Upload PDF (First Page Only)", type=["pdf"])

    if uploaded_file:
        with st.spinner("Processing..."):
            if not st.session_state.text_content:
                st.session_state.text_content = extract_text_from_pdf(uploaded_file)

            if st.session_state.text_content:
                # Generate questions if not already generated
                if not st.session_state.questions:
                    st.session_state.questions = generate_questions(st.session_state.text_content)
                    st.session_state.questions_text = st.session_state.questions
                
                questions = st.session_state.questions

                if questions and "Error" not in questions:
                    st.text_area("Generated Questions", questions, height=300)

                    # Two columns for buttons
                    col1, col2 = st.columns(2)

                    with col1:
                        pdf_path = create_pdf(questions)
                        with open(pdf_path, "rb") as file:
                            st.download_button(
                                label="📥 Download Questions",
                                data=file,
                                file_name="quiz_questions.pdf",
                                mime="application/pdf",
                                use_container_width=True
                            )

                    with col2:
                        if st.button("🚀 Start Assessment", use_container_width=True):
                            st.session_state.is_assessment_started = True
                            st.rerun()
                else:
                    st.error(questions)
    else:
        st.write("Please upload a PDF file to get started.")
else:
    display_assessment(st.session_state.questions_text)
