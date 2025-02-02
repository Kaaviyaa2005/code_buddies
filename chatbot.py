import streamlit as st
import requests
from time import sleep

# Function to interact with the Groq Cloud API
def chat_with_llama(prompt, retries=3, delay=5):
    api_url = "https://api.groq.com/openai/v1/chat/completions"  # Correct Groq Cloud API endpoint
    headers = {
        "Authorization": "Bearer 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",  # Your API key
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.3-70b-versatile",  # Specify the model
        "messages": [{
            "role": "user",
            "content": prompt
        }]
    }
    
    for _ in range(retries):
        try:
            response = requests.post(api_url, headers=headers, json=data, timeout=10)  # Added timeout
            if response.status_code == 200:
                return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response from the bot.")
            else:
                return f"Error: {response.status_code} - {response.text}"
        except requests.exceptions.RequestException as e:
            st.warning(f"Request failed: {e}, retrying...")
            sleep(delay)  # Wait for a short period before retrying
            
    return "Request failed after several attempts. Please check your internet connection or the API URL."

# Initialize session state for conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Main function for the chatbot page
def main():
    st.title("Chat with the Bot")
    st.write("Ask me anything!")

    # Display conversation history
    st.write("### Conversation History")
    for message in st.session_state.conversation:
        st.write(message)

    # Create a form to capture input and submit
    with st.form(key="user_input_form", clear_on_submit=True):
        user_input = st.text_input("You:", value="", placeholder="Type your message and press Enter...", key="input")
        submit_button = st.form_submit_button(label="Send")
        
        # Trigger the callback when the submit button is pressed
        if submit_button and user_input.strip():
            # Add the user's message to the conversation history
            st.session_state.conversation.append(f"You: {user_input}")
            
            # Get response from the Groq Cloud API
            bot_response = chat_with_llama(user_input)
            
            # Add the bot's response to the conversation history
            st.session_state.conversation.append(f"Bot: {bot_response}")
            
            # Rerun the app to immediately display the updated conversation
            st.rerun()

    # Add a button to clear the conversation
    if st.button("Clear Conversation"):
        st.session_state.conversation = []
        st.rerun()

# Run the chatbot page
if __name__ == "__main__":
    main()