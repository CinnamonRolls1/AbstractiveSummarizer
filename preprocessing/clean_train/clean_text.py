import os
import re
import io
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def clean_only_alpha(text):
    """
    We can remove any characters that are not important. I have removed numbers and characters from the text. Leaving only alphabets.
    """
    return re.sub('[^a-zA-Z\s]',"",text)

def clean_to_lower(text):
    """
    We can reduce every word to lower case for simplicity. This also allows us to prevent duplication of words.
    """
    return str(text).lower()

def clean_tokenize(text):
    """
    Tokenization splits the given text into smaller chunks called tokens
    """
    return word_tokenize(text)

def clean_stopwords(text):
    """
    Stopwords are common words used in a language that do not carry any important meaning. These are also removed from the text.
    """
    return [i for i in text if i not in stop_words]

def clean_length(text):
    """
    This reduces noise by removing short words which often do not give any information.
    """
    return [i for i in text if len(i)>2]

def clean_lemmatization(text):
    """
    Lemmatization involved identifying the common root of a word based which is know as lemma. 
    """
    return [lemma.lemmatize(word=i,pos='v') for i in text]

def preprocess(content):
    content = clean_only_alpha(content)
    content = clean_to_lower(content)
    content = clean_tokenize(content)
    content = clean_stopwords(content)
    #content = clean_lemmatization(content)
    #content = clean_length(content)
    return " ".join(content)