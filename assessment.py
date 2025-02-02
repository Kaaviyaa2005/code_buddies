import streamlit as st
import random
import requests
import os
import time

def show_results(questions_list):
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
    
    # Generate and display study plan
    st.write("---")
    st.write("### Personalized Study Plan")
    
    # Create a placeholder for the study plan
    study_plan_placeholder = st.empty()
    
    with st.spinner("Generating your personalized study plan... This may take a few moments."):
        study_plan = get_study_plan(st.session_state.previous_answers)
        study_plan_placeholder.write(study_plan)
    
    st.write("---")
    st.write("### Review Your Answers")
    
    for idx, ans in enumerate(st.session_state.previous_answers):
        st.write(f"#### Question {idx + 1}: {ans['question']}")
        st.write(f"**Your Answer:** {ans['selected_answer']}")
        st.write(f"**Correct Answer:** {ans['correct_answer']}")
        st.write(f"**Options:**")
        for option in ans['options']:
            st.write(f"- {option}")
        st.write("---")
    
    # Set assessment_done to True after showing results
    st.session_state.assessment_done = True
    
    # Store assessment data in session state for chatbot
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    st.session_state.chat_history = st.session_state.previous_answers
    
    # Add chatbot button that redirects to the correct page
    if st.button("Chat with AI Tutor", key="chatbot_button"):
        st.switch_page("pages/chatbot")  # Note: no .py extension needed

# Rest of your code remains the same...

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

def parse_questions(questions_text):
    questions_list = []
    current_question = {}
    
    # Split the text into lines
    lines = questions_text.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Detect the start of a new question
        if line.lower().startswith("question:"):
            if current_question:  # Save the previous question if it exists
                questions_list.append(current_question)
            current_question = {'question': line[9:].strip(), 'options': []}
        
        # Detect options (A, B, C, D)
        elif line.startswith(('A)', 'B)', 'C)', 'D)')):
            current_question['options'].append(line)
    
    # Add the last question if it exists
    if current_question:
        questions_list.append(current_question)
    
    return questions_list

GROQ_API_KEY = "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"  # Replace with your actual Groq API key

def get_study_plan(previous_answers):
    """Generate a personalized study plan based on assessment results using Groq API"""
    max_retries = 3
    retry_delay = 2
    
    # Prepare the context from previous answers
    incorrect_questions = [ans for ans in previous_answers if not ans['correct']]
    topics_to_improve = [q['question'] for q in incorrect_questions]
    
    # Construct the prompt
    prompt = f"""Based on the assessment results, the student needs help with the following topics:
    {', '.join(topics_to_improve)}
    
    Please create a detailed study plan that includes:
    1. Key areas to focus on
    2. Recommended learning resources
    3. Practice exercises
    4. Timeline for improvement"""
    
    for attempt in range(max_retries):
        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {GROQ_API_KEY}"
                },
                json={
                    "model": "llama-3.3-70b-versatile",
                    "messages": [{
                        "role": "user",
                        "content": prompt
                    }],
                    "temperature": 0.7,
                    "max_tokens": 500
                },
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            else:
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
                return """Unable to generate study plan at the moment. Here's a general recommendation:
                1. Review the questions you answered incorrectly
                2. Focus on understanding the core concepts
                3. Practice similar problems
                4. Consider seeking additional help from your instructor"""
                
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            return """Unable to connect to the study plan service. Here's a general recommendation:
            1. Review the questions you answered incorrectly
            2. Focus on understanding the core concepts
            3. Practice similar problems
            4. Consider seeking additional help from your instructor"""

def show_results(questions_list):
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
    
    # Generate and display study plan
    st.write("---")
    st.write("### Personalized Study Plan")
    with st.spinner("Generating your personalized study plan..."):
        study_plan = get_study_plan(st.session_state.previous_answers)
        st.write(study_plan)
    
    st.write("---")
    st.write("### Review Your Answers")
    
    for idx, ans in enumerate(st.session_state.previous_answers):
        st.write(f"#### Question {idx + 1}: {ans['question']}")
        st.write(f"**Your Answer:** {ans['selected_answer']}")
        st.write(f"**Correct Answer:** {ans['correct_answer']}")
        st.write(f"**Options:**")
        for option in ans['options']:
            st.write(f"- {option}")
        st.write("---")
    
    # Set assessment_done to True after showing results
    st.session_state.assessment_done = True
    
    # Add chatbot button
    if st.button("Chat with AI Tutor", key="chatbot_button"):
        st.session_state.chat_history = st.session_state.previous_answers  # Store assessment data for chatbot
        st.switch_page("pages/chatbot.py")  

def display_assessment(questions_text):
    st.title("📝 Adaptive Assessment")
    
    if 'previous_answers' not in st.session_state:
        st.session_state.previous_answers = []
    if 'current_question_index' not in st.session_state:
        st.session_state.current_question_index = 0
    
    # Parse the questions
    questions_list = parse_questions(questions_text)[:10]  # Limit to 10 questions
    total_questions = len(questions_list)  
    
    if not questions_list:
        st.error("No valid questions available. Please generate questions first.")
        return
    
    total_questions = len(questions_list)
    current_idx = st.session_state.current_question_index
    
    if current_idx < total_questions:
        question = questions_list[current_idx]
        st.write(f"### Question {current_idx + 1}/{total_questions}")
        st.write(f"**{question['question']}**")
        
        # Display options
        answer = st.radio("Select your answer:", question['options'], key=f"q_{current_idx}")
        
        if st.button("Submit Answer"):
            selected_answer = answer[0]  
            correct_answer = random.choice(['A', 'B', 'C', 'D'])
            
            is_correct = selected_answer == correct_answer
            
            st.session_state.previous_answers.append({
                'question': question['question'],
                'options': question['options'],
                'selected_answer': selected_answer,
                'correct_answer': correct_answer,
                'correct': is_correct
            })
            
            next_difficulty = calculate_difficulty(st.session_state.previous_answers)
            st.session_state.current_difficulty = next_difficulty
            st.session_state.current_question_index += 1
            st.rerun()
    else:
        show_results(questions_list)
