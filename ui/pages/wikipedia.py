import streamlit as st
from core.wikipedia import load_wiki
from core.wikipedia import get_search_suggestions
#from huggingface_hub import InferenceClient

def Mypedia():
    topic = st.text_input("Search Topic:", "")
    if not topic:
        st.info("Enter a specific topic to search.", icon="ℹ️")

    # Search Suggestions
    if topic:
        with st.spinner("Fetching search suggestions..."):
            suggestions = get_search_suggestions(topic, "en")  # Default language code, "en"
        st.write("Search Suggestions:")
        if suggestions:
            selected_suggestion = st.selectbox("Select a suggestion", suggestions)
            st.write("Click on a suggestion to learn more.")
        else:
            st.write("No suggestions found. Try refining your search.")

    # Article Paragraph
    article_paragraph = st.empty()

    if topic:
        # Loads Wikipedia summary of the topic
        with st.spinner("Fetching Wikipedia summary..."):
            summary = load_wiki(topic, language="en")  # Default language code, "en"

        # Displays article summary in paragraph
        article_paragraph.markdown(summary)
        #st.write("Scroll down for more details or ask a specific question about the topic.")

    #    # -- Questions--
    #    if question:
    #        # Loads the question answering pipeline
    #        with st.spinner("Answering your question..."):
    #            qa_pipeline = load_qa_pipeline()

    #        # Answers query question using article summary
    #        result = answer_questions(qa_pipeline, question, summary)
    #        answer = result["answer"]

    #        # Displaying answer in real-time
    #        st.write(answer)

# Footer with link
    #link = 'Created by [Gideon Ogunbanjo](https://gideonogunbanjo.netlify.app)'
    #st.markdown(link, unsafe_allow_html=True)    
    #         