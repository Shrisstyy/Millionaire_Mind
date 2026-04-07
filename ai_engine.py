import requests
import re

def generate_question():

    prompt = """
    Generate 1 easy multiple choice question.

    Format:
    Question: ...
    A) ...
    B) ...
    C) ...
    D) ...
    Correct Answer: A/B/C/D
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    text = response.json()["response"]

    question = re.search(r"Question:\s*(.*)", text).group(1)
    options = re.findall(r"[A-D]\)\s*(.*)", text)
    correct_letter = re.search(r"Correct Answer:\s*([A-D])", text).group(1)

    correct_index = ord(correct_letter) - ord("A")

    return {
        "question": question,
        "options": options,
        "correct": options[correct_index]
    }