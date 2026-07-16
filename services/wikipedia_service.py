import wikipediaapi

def load_wiki(query, language="hi"):
    """
    Searches Wikipedia for the given query in the specified language and returns a summary of the first search result.

    Args:
        query (str): The search query for Wikipedia.
        language (str): The language code for the Wikipedia search (default is "hi" for Hindi).

    Returns:
        str: The summary of the first Wikipedia search result.
    """
    headers = {
        'User-Agent': 'WikiMindAI/1.0 (https://gideonogunbanjo.netlify.app)'
    }
    wiki_wiki = wikipediaapi.Wikipedia(language, headers=headers)
    try:
        page = wiki_wiki.page(query)
        summary = page.summary
        return summary
    # Disambiguation Error Exception
    except wikipediaapi.exceptions.DisambiguationError:
        return "Multiple articles found. Please provide a more specific topic."
    except wikipediaapi.exceptions.HTTPTimeoutError:
        return "No internet connection. Please check your internet connection settings."
    except Exception as e:
        return f"An Error Occurred: {e}"