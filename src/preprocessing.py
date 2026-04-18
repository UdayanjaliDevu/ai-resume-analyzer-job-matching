import re

def clean_text(text):
    """
    Cleans resume text for further processing
    """

    # 1. Lowercase everything
    text = text.lower()

    # 2. Remove emails (optional but useful later)
    text = re.sub(r'\S+@\S+', ' ', text)

    # 3. Remove URLs
    text = re.sub(r'http\S+|www\S+', ' ', text)

    # 4. Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # 5. Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text