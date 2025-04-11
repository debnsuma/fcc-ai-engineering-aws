import re
import unicodedata
import html
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy

# Download NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

class TextCleaner:
    def __init__(self):
        try:
            self.nlp = spacy.load('en_core_web_sm')
        except OSError:
            print("Downloading spaCy model 'en_core_web_sm'...")
            from spacy.cli import download
            download('en_core_web_sm')
            self.nlp = spacy.load('en_core_web_sm')

    def clean_text_bs4(self, text):
        """Clean text using BeautifulSoup for better HTML handling."""
        if not text or not isinstance(text, str):
            return ""
            
        # Decode HTML entities
        text = html.unescape(text)
        
        # Use BeautifulSoup to remove HTML tags
        soup = BeautifulSoup(text, "html.parser")
        text = soup.get_text(separator=" ")
        
        # Remove references in brackets
        text = re.sub(r'\[.*?\]', '', text)
        
        # Remove URLs
        text = re.sub(r'http[s]?://\S+', '', text)
        
        # Normalize unicode characters
        text = unicodedata.normalize('NFKC', text)
        
        # Remove extra spaces, tabs, and newlines
        text = ' '.join(text.split())
        
        return text

    def clean_text_nltk(self, text, remove_stopwords=False):
        """Clean text using NLTK with optional stopword removal."""
        if not text or not isinstance(text, str):
            return ""
            
        # Basic cleaning first
        text = self.clean_text_bs4(text)
        
        # Tokenize text
        tokens = word_tokenize(text)
        
        # Remove stopwords if requested
        if remove_stopwords:
            stop_words = set(stopwords.words('english'))
            tokens = [word for word in tokens if word.lower() not in stop_words]
        
        # Rejoin tokens
        text = ' '.join(tokens)
        
        return text

    def clean_text_spacy(self, text, remove_stopwords=False, lemmatize=False):
        """
        Clean text using spaCy with options for stopword removal and lemmatization.
        
        Args:
            text: Input text to clean
            remove_stopwords: Whether to remove common stopwords
            lemmatize: Whether to perform lemmatization
            
        Returns:
            Cleaned text
        """
        if not text or not isinstance(text, str):
            return ""
        
        # Basic cleaning first
        text = self.clean_text_bs4(text)
        
        # Process with spaCy
        doc = self.nlp(text)
        
        if lemmatize and remove_stopwords:
            # Return lemmatized text without stopwords
            tokens = [token.lemma_ for token in doc if not token.is_stop]
        elif lemmatize:
            # Return lemmatized text with stopwords
            tokens = [token.lemma_ for token in doc]
        elif remove_stopwords:
            # Return original text without stopwords
            tokens = [token.text for token in doc if not token.is_stop]
        else:
            # Return all tokens as they appeared
            tokens = [token.text for token in doc]
        
        # Rejoin tokens
        text = ' '.join(tokens)
        
        return text

    def clean_text_for_rag(self, text, method="bs4"):
        """
        Comprehensive text cleaning function for RAG applications.
        
        Args:
            text: Input text to clean
            method: Cleaning method to use ('basic', 'bs4', 'nltk', or 'spacy')
            
        Returns:
            Cleaned text
        """
        if not text:
            return ""
        
        if method == "basic":
            return self.clean_text_basic(text)
        elif method == "bs4":
            return self.clean_text_bs4(text)
        elif method == "nltk":
            return self.clean_text_nltk(text, remove_stopwords=False)
        elif method == "spacy":
            return self.clean_text_spacy(text, remove_stopwords=False, lemmatize=False)
        else:
            # Default to bs4 method
            return self.clean_text_bs4(text)
