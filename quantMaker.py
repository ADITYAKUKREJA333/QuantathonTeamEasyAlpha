import os
from pdfminer.high_level import extract_text
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import download
download('vader_lexicon')  # Download the VADER lexicon for sentiment analysis

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    
    Args:
    - pdf_path: Path to the PDF file
    
    Returns:
    - The extracted text as a string.
    """
    return extract_text(pdf_path)

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the provided text using NLTK's VADER.
    
    Args:
    - text: The text to analyze.
    
    Returns:
    - A dictionary containing the scores for negative, neutral, positive, and compound sentiments.
    """
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

def analyze_specific_pdf(pdf_filename):
    """
    Analyzes the sentiment of a specific PDF file.
    
    Args:
    - pdf_filename: The filename of the PDF to analyze.
    """
    pdf_path = os.path.join(os.getcwd(), pdf_filename)
    if os.path.exists(pdf_path) and pdf_path.endswith(".pdf"):
        print(f"Processing {pdf_filename}...")
        text = extract_text_from_pdf(pdf_path)
        sentiment = analyze_sentiment(text)
        print(f"Sentiment analysis for {pdf_filename}: {sentiment}\n")
    else:
        print(f"File {pdf_filename} not found or is not a PDF.")

if __name__ == "__main__":
    for i in range(1, 31):  # Looping through reports quarter1.pdf to quarter40.pdf
        pdf_filename = f"quarter{i}.pdf"
        analyze_specific_pdf(pdf_filename)