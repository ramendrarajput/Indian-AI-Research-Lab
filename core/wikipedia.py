#import requests
#import wikipedia
import requests
#import wikipediaapi
import wikipediaapi
from transformers import pipeline
import requests

#@st.cache(allow_output_mutation=True)
def load_qa_pipeline():
    """
    Loads the Question-Answering pipeline using the DistilBERT model.

    Returns:
        Pipeline: The Question-Answering pipeline.
    """
    qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
    return qa_pipeline

def load_wiki(query, language="hi"):
    headers = {
        "User-Agent": "WikiMindAI/1.0"
    }

    wiki_wiki = wikipediaapi.Wikipedia(
        language=language,
        user_agent=headers["User-Agent"]
    )

    try:
        page = wiki_wiki.page(query)

        if not page.exists():
            return "No Wikipedia article found."

        return page.summary

    except Exception as e:
        return f"An Error Occurred: {e}"
    
#def load_wiki(query, language="hi"):
#    """
#    Searches Wikipedia for the given query in the specified language and returns a summary of the first search result.

#    Args:
#        query (str): The search query for Wikipedia.
#        language (str): The language code for the Wikipedia search (default is "hi" for Hindi).

#    Returns:
#        str: The summary of the first Wikipedia search result.
#    """
#    headers = {
#        'User-Agent': 'WikiMindAI/1.0 (https://gideonogunbanjo.netlify.app)'
#    }
#    wiki_wiki = wikipediaapi.Wikipedia(language, headers=headers)
#    try:
#        page = wiki_wiki.page(query)
#        summary = page.summary
#        return summary
#    # Disambiguation Error Exception
#    except wikipediaapi.exceptions.DisambiguationError:
#        return "Multiple articles found. Please provide a more specific topic."
#    except wikipediaapi.exceptions.HTTPTimeoutError:
#        return "No internet connection. Please check your internet connection settings."
#    except Exception as e:
#        return f"An Error Occurred: {e}"

def answer_questions(pipeline, question, paragraph):
    """
    Uses the Question-Answering pipeline to answer a question based on the given context (paragraph).

    Args:
        pipeline (Pipeline): The Question-Answering pipeline.
        question (str): The question to be answered.
        paragraph (str): The context (paragraph) from which the question should be answered.

    Returns:
        dict: A dictionary containing the answer to the question and additional details.
    """
    input_data = {
        "question": question,
        "context": paragraph
    }
    output = pipeline(input_data)
    return output

def get_search_suggestions(query, language):
    """
    Fetches search suggestions from Wikipedia based on the query.

    Args:
        query (str): The search query.
        language (str): The language code for the search.

    Returns:
        list: A list of search suggestions.
    """
    url = f"https://{language}.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "format": "json",
        "search": query,
        "limit": 5,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data[1]

