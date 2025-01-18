import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Hugging Face API Key
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
if not HUGGINGFACE_API_KEY:
    st.error("Hugging Face API key not found. Please set it in your environment variables.")
    st.stop()

# Streamlit settings
st.set_page_config(page_title="Your AI Assistant 🤖", page_icon="🤖")
st.title("Your AI Assistant 🤖")

# Model class definition
model_class = "hf_hub"

#function to load the hugging face model
def model_hf_hub(model="meta-llama/Meta-Llama-3-8B-Instruct", temperature=0.1):
    """Initialize Hugging Face model endpoint."""
    return HuggingFaceEndpoint(
        repo_id=model,
        api_key=HUGGINGFACE_API_KEY,
        temperature=temperature,
        max_new_tokens=512,
        return_full_text=False,
    )

def model_response(user_query, chat_history):
    """Generate response from the model."""
    # Define system prompt
    system_prompt = """
    You are a helpful assistant answering general questions. Please respond in {language}.
    """
    language = "the same language the user is using to chat"

    # Define user prompt
    user_prompt = f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n{user_query}\n<|eot_id|><|start_header_id|>assistant<|end_header_id|>"

    # Combine prompts
    complete_prompt = system_prompt.format(language=language) + user_prompt

    # Load the model and generate response
    llm = model_hf_hub()
    response = llm(complete_prompt)
    return response

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hi, I'm your virtual assistant! How can I help you?")
    ]

# Display chat history
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# User input
user_query = st.chat_input("Enter your message here...")
if user_query:
    # Append user query to chat history
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    # display message
    with st.chat_message("Human"):
        st.markdown(user_query)

    # generate and display AI response
    with st.chat_message("AI"):
        response = model_response(user_query, st.session_state.chat_history)
        st.markdown(response)

    # append AI response to chat history
    st.session_state.chat_history.append(AIMessage(content=response))

