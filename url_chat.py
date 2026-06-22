from scraper import get_website_text
from chatbot import ask_ai

website_cache = {}

def answer_from_url(url, question):

    if url not in website_cache:
        website_cache[url] = get_website_text(url)[:3000]

    website_text = website_cache[url]

    prompt = f"""
Website Content:

{website_text}

Question:
{question}

Answer only using website information.
"""

    return ask_ai(prompt)