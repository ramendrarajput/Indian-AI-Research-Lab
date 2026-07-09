import streamlit as st
from streamlit_chat import message
from core.ai import chat
from core.prompts import AI_CHATBOT_SYSTEM_PROMPT
from streamlit_chat import message  # Install using: pip install streamlit-chat

def AI_Chatbot():
    st.sidebar.title("AI Chatbot")
    st.sidebar.markdown("""
    ### Features:
    - Chat with AI
    - Memory of past conversations
    - Sleek UI like ChatGPT
    """)

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "memory" not in st.session_state:
        st.session_state["memory"] = {}

    st.subheader("My AI Chatbot💬")
    st.markdown("""
    Welcome to the AI Chatbot! Type your message below and start chatting.
    """)
    #st.caption("Developer: Ramendra Singh Rajput")

    for chat in st.session_state.messages:  
        message(chat["content"], is_user=chat["is_user"])

    user_input = st.chat_input("Type your message:", key="user_input")
    st.caption("Powered by Ramendra Singh Rajput")
    input_prompt = """
                       You are an expert in chatting like human. You are trained by Ramendra Singh Rajput, working for Mp govt as a patwari.He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System etc.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between phylosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ ,github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput
                       you will have to answer questions based on the user input but last line of first questions answer should contain only profile links of Ramendra singh rajput as water mark. 
                       """
    
    #from core.prompts import AI_CHATBOT_SYSTEM_PROMPT

    if user_input:  
        st.session_state.messages.append({"content": user_input, "is_user": True})
        # Updating memory with relevant information
        if "my name is" in user_input.lower():
             name = user_input.lower().split("my name is")[-1].strip()
             st.session_state.memory["name"] = name
             response=f"Ok {name}, i'll remember your name"
             st.session_state.messages.append({"content": response, "is_user": False})
             st.rerun()
        elif "what is my name" in user_input.lower() and "name" in st.session_state.memory:
             response = f"Your name is {st.session_state.memory['name']}!"
             st.session_state.messages.append({"content": response, "is_user": False})
             #st.write(response)
             st.rerun()
        elif "what is my name" in user_input.lower() and "name" not in st.session_state.memory:
         response="Sorry! Please tell me your name"
         st.session_state.messages.append({"content": response, "is_user": False})
         st.rerun()
        else:
          with st.spinner(text='Thinking'):
           from core.ai import chat
           response = chat(prompt=user_input,system_prompt=AI_CHATBOT_SYSTEM_PROMPT,)
           st.session_state.messages.append({"content": response, "is_user": False})
           if response:
            st.success('Done')
            #st.write(response)
           st.rerun()
