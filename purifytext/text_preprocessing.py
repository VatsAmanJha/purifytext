import pandas as pd
import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from bs4 import BeautifulSoup
import contractions
import nltk

# Ensure required NLTK data is downloaded
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize the lemmatizer, stemmer, and stop words
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

def func_text_lower(text):
    return text.lower()

def func_remove_punctuation(text):
    translator = str.maketrans(" ", " ", string.punctuation)
    return text.translate(translator)

def func_remove_number(text):
    return re.sub(r"\d", " ", text)

def func_remove_whitespace(text):
    return " ".join(text.split())

def func_remove_contractions(text):
    return contractions.fix(text)

def func_remove_HTML_tag(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def func_remove_stopwords(text):
    words = text.split()
    words = [word for word in words if word.lower() not in stop_words]
    return " ".join(words)

def func_lemmatize_words(text):
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words]
    return " ".join(words)

def func_stem_words(text):
    words = text.split()
    words = [stemmer.stem(word) for word in words]
    return " ".join(words)

def func_remove_urls(text):
    url_pattern = r"(https?://\S+|www\.\S+)"
    return re.sub(url_pattern, "", text)

def func_remove_emojis(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def func_remove_special_characters(text):
    return re.sub(r"[^a-zA-Z\s]", "", text)


if __name__ == "__main__":
    pass