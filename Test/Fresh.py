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
    # Send an HTTP GET request to the product page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the review section
        review_section = soup.find('div', {'id': 'reviewsMedley'})

        # Check if the review section exists
        if review_section:
            # Extract the text of the review section
            review_text = review_section.get_text(separator=' ')

            # Return the review text
            return review_text
        else:
            return "Review section not found on the page."
    else:
        return "Failed to retrieve the page."


# Function to answer questions based on review text
def answer_question(question, review_text):
    # Preprocess the question and review text
    question = question.lower()
    review_text = review_text.lower()

    # Tokenize the question and review text
    question_tokens = word_tokenize(question)
    review_tokens = word_tokenize(review_text)

    # Remove stopwords from question and review text
    stop_words = set(stopwords.words('english'))
    question_tokens = [token for token in question_tokens if token not in stop_words]
    review_tokens = [token for token in review_tokens if token not in stop_words]

    # Perform keyword matching
    keyword_matching_score = sum(1 for token in question_tokens if token in review_tokens)

    # Perform sentiment analysis on the review text
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(review_text)
    sentiment_score = sentiment_scores['compound']

    # Provide answers based on keyword matching and sentiment analysis
    if keyword_matching_score > 0:
        if sentiment_score >= 0.2:
            return "Yes, the reviews generally have a positive sentiment."
        elif sentiment_score <= -0.2:
            return "No, the reviews generally have a negative sentiment."
        else:
            return "The sentiment of the reviews is mixed."
    else:
        return "I'm sorry, I couldn't find any relevant information in the reviews."


# Function to generate a summary of the entire product based on the reviews
def generate_product_summary(review_text):
    def generate_product_summary(review_text):
    # Truncate the review text if it exceeds the maximum sequence length
        max_length = 512
        if len(review_text) > max_length:
            review_text = review_text[:max_length]

    # Generate the summary using the BART model
            summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device="cpu")
            summary = summarizer(review_text, max_length=100, min_length=30, do_sample=False)

    # Check if the 'summary' key is present in the dictionary
            if 'summary' in summary[0]:
                return summary[0]['summary']
            else:
                return "Failed to generate the product summary."





# Chatbot function
def chatbot():
    print("Welcome to the Amazon review chatbot!")
    print("Please enter the product URL from Amazon:")
    product_url = input()

    # Scrape the reviews section
    reviews_text = scrape_amazon_reviews(product_url)

    if reviews_text != "Review section not found on the page." and reviews_text != "Failed to retrieve the page.":
        print("Reviews have been scraped successfully!")
        print("How can I assist you? You can ask questions or request a summary based on the review section.")
        while True:
            user_input = input("User: ")

            # Check if user requests a summary
            if "summary" in user_input.lower():
                # Generate a summary of the entire product based on the reviews
                product_summary = generate_product_summary(reviews_text)    
                print("Chatbot: Here's a summary of the product based on the reviews:")
                print(product_summary)
            else:
                # Answer the user's question based on the review text
                answer = answer_question(user_input, reviews_text)
                print("Chatbot:", answer)

            print("Chatbot: Is there anything else I can help you with?")
    else:
        print(reviews_text)


# Run the chatbot
chatbot()
