import streamlit as st
import numpy as np

def calculate_difficulty(previous_answers):
    if not previous_answers:
        return 0.5
    
    correct_count = sum(1 for ans in previous_answers if ans['correct'])
    success_rate = correct_count / len(previous_answers)
    
    if success_rate > 0.7:
        return min(0.9, success_rate + 0.1)
    elif success_rate < 0.3:
        return max(0.1, success_rate)
    else:
        return success_rate

def generate_adaptive_prompt(text, difficulty):
    difficulty_terms = {
        'low': 'basic recall and simple understanding',
        'medium': 'application and analysis',
        'high': 'evaluation and complex analysis'
    }
    
    diff_term = 'low' if difficulty < 0.4 else 'high' if difficulty > 0.7 else 'medium'
    
    return f"""Generate 10 multiple choice questions from this text. 
    Focus on {difficulty_terms[diff_term]} level questions.
    Each question should have 4 options (A, B, C, D).
    Include the correct answer at the end of each question.
    Text: {text}
    
    Format each question as:
    Question: [question text]
    A) [option]
    B) [option]
    C) [option]
    D) [option]
    Correct Answer: [A/B/C/D]
    """

def parse_questions(questions_text):
    questions_list = []
    current_question = {}
    
    for line in questions_text.split('\n'):
        line = line.strip()
        if line.startswith('Question:'):
            if current_question:
                questions_list.append(current_question)
            current_question = {'question': line[9:].strip(), 'options': []}
        elif line.startswith(('A)', 'B)', 'C)', 'D)')):
            current_question['options'].append(line)
        elif line.startswith('Correct Answer:'):
            current_question['correct'] = line[15:].strip()
    
    if current_question:
        questions_list.append(current_question)
    
    return questions_list

def generate_questions(text, difficulty):
    # Simulate generating questions (replace this with an actual API call or model)
    prompt = generate_adaptive_prompt(text, difficulty)
    # For now, return a hardcoded example
    return """
    Question: What is the capital of France?
    A) London
    B) Paris
    C) Berlin
    D) Madrid
    Correct Answer: B
    
    Question: What is 2 + 2?
    A) 3
    B) 4
    C) 5
    D) 6
    Correct Answer: B
    """

def display_assessment(text):
    st.title("📝 Adaptive Assessment")
    
    if 'previous_answers' not in st.session_state:
        st.session_state.previous_answers = []
    if 'current_question_index' not in st.session_state:
        st.session_state.current_question_index = 0
    if 'questions_text' not in st.session_state:
        st.session_state.questions_text = generate_questions(text, 0.5)
    
    questions_list = parse_questions(st.session_state.questions_text)
    
    if not questions_list:
        st.error("No valid questions available. Please generate questions first.")
        return
    
    total_questions = len(questions_list)
    current_idx = st.session_state.current_question_index
    
    if current_idx < total_questions:
        question = questions_list[current_idx]
        st.write(f"### Question {current_idx + 1}/{total_questions}")
        st.write(f"**{question['question']}**")
        
        answer = st.radio("Select your answer:", question['options'], key=f"q_{current_idx}")
        
        if st.button("Submit Answer"):
            selected_answer = answer[0]
            is_correct = selected_answer == question['correct']
            
            st.session_state.previous_answers.append({
                'question': question['question'],
                'answer': selected_answer,
                'correct': is_correct
            })
            
            next_difficulty = calculate_difficulty(st.session_state.previous_answers)
            st.session_state.current_difficulty = next_difficulty
            st.session_state.current_question_index += 1
            st.rerun()
    else:
        show_results()

def show_results():
    st.success("Assessment Complete! 🎉")
    correct_count = sum(1 for ans in st.session_state.previous_answers if ans['correct'])
    total_questions = len(st.session_state.previous_answers)
    score = (correct_count / total_questions) * 100
    
    st.write(f"### Your Score: {score:.1f}%")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Correct Answers", f"{correct_count}/{total_questions}")
    with col2:
        st.metric("Accuracy", f"{score:.1f}%")
    with col3:
        st.metric("Final Difficulty", f"{st.session_state.current_difficulty:.2f}")
    
    if st.button("Start New Assessment"):
        st.session_state.previous_answers = []
        st.session_state.current_question_index = 0
        st.session_state.current_difficulty = 0.5
        st.session_state.questions_text = ""
        st.rerun()



