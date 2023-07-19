import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from transformers import pipeline

# Download required NLTK resources
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')

# Function to scrape the text of the reviews section
def scrape_amazon_reviews(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        review_section = soup.find('div', {'id': 'reviewsMedley'})
        if review_section:
            return review_section.get_text(separator='\n')
    return ""

# Function to generate a summary of the review text
def generate_summary(review_text, max_length=512):
    if len(review_text) > max_length:
        review_text = review_text[:max_length]

    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device="cpu") ## FOr summarization 
    summary = summarizer(review_text, max_length=500, min_length=300, do_sample=False)

    return summary[0]['summary_text']




# Function to answer user questions based on the context
def answer_question(context, question):
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2") ## for question answering
    result = qa_pipeline(context="My name is Debosmita , i live in lalpur", question=question)
    return result['answer']

def chatbot():
    product_url = input("Enter the URL of the product on Amazon: ")
    review_text = scrape_amazon_reviews(product_url)
    summary = generate_summary(review_text)
    # print(summary)


    print("Chatbot: I have summarized the product reviews. How can I assist you?")
    while True:
        user_input = input("User: ")

        # Answer user questions based on the context or summary
        answer = answer_question(summary, user_input)
        print("Chatbot:", answer)

        print("Chatbot: Is there anything else I can help you with?")

# Run the chatbot
chatbot()
