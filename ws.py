import requests
from bs4 import BeautifulSoup
from transformers import T5ForConditionalGeneration, T5Tokenizer


# ABSTRACTIVE CONTEXT ##
def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content_elements = soup.find_all('body')  # Select all <p> tags on the webpage
        if content_elements:
            extracted_content = ' '.join([element.get_text() for element in content_elements])
            return extracted_content
        else:
            print("No content found.")
    else:
        print(f"Error: {response.status_code}")
    return None

def generate_summary(text):
    model_name = "t5-base"
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)

    input_ids = tokenizer.encode(text, return_tensors="pt")
    summary_ids = model.generate(input_ids, num_beams=4, max_length=150, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

website_url = 'https://www.york.ac.uk/teaching/cws/wws/webpage1.html'
website_content = scrape_website(website_url)

if website_content:
    summary = generate_summary(website_content)
    print("\n")
    print("Summary:")
    print(summary)


## SUMMARATIVE CONTEXT ##

# import requests
# import nltk
# nltk.download('vader_lexicon')
# from bs4 import BeautifulSoup
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lex_rank import LexRankSummarizer


# def scrape_website(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         content_elements = soup.find_all('review')  # Select all <p> tags on the webpage
#         if content_elements:
#             extracted_content = ' '.join([element.get_text() for element in content_elements])
#             return extracted_content
#         else:
#             print("No content found.")
#     else:
#         print(f"Error: {response.status_code}")
#     return None

# def summarize_text(text, num_sentences=10):
#     parser = PlaintextParser.from_string(text, Tokenizer("english"))
#     summarizer = LexRankSummarizer()
#     summary_sentences = summarizer(parser.document, num_sentences)
#     summary = ' '.join(str(sentence) for sentence in summary_sentences)
#     return summary

# website_url = 'https://www.amazon.in/Airdopes-141-Playtime-Resistance-Bluetooth/dp/B09N3ZNHTY/ref=sr_1_5?brr=1&qid=1688496900&rd=1&sr=8-5&th=1'
# website_content = scrape_website(website_url)

# if website_content:
#     summary = summarize_text(website_content)
#     print("Summary:")
#     print(summary)

# import requests
# from bs4 import BeautifulSoup
# from transformers import T5ForConditionalGeneration, T5Tokenizer
# from nltk.sentiment import SentimentIntensityAnalyzer

# def scrape_website(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         content_elements = soup.find_all('p')  # Select all <p> tags on the webpage
#         if content_elements:
#             extracted_content = ' '.join([element.get_text() for element in content_elements])
#             return extracted_content
#         else:
#             print("No content found.")
#     else:
#         print(f"Error: {response.status_code}")
#     return None

# def generate_summary(text):
#     model_name = "t5-base"
#     model = T5ForConditionalGeneration.from_pretrained(model_name)
#     tokenizer = T5Tokenizer.from_pretrained(model_name)

#     input_ids = tokenizer.encode(text, return_tensors="pt")
#     summary_ids = model.generate(input_ids, num_beams=4, max_length=150, early_stopping=True)
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return summary

# def analyze_sentiment(text):
#     analyzer = SentimentIntensityAnalyzer()
#     sentiment_scores = analyzer.polarity_scores(text)
#     sentiment_label = ""
#     if sentiment_scores['compound'] >= 0.05:
#         sentiment_label = "Positive"
#     else:
#         sentiment_label = "Negative"
#     return sentiment_label

# website_url = 'https://www.example.com'
# website_content = scrape_website(website_url)

# if website_content:
#     summary = generate_summary(website_content)
#     sentiment = analyze_sentiment(summary)

#     print("Summary:")
#     print(summary)
#     print("Sentiment: " + sentiment)
# from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

# model_name = "deepset/roberta-base-squad2"
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# a) Get predictions
# nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
# QA_input = {
#     'question': 'Which is the best Product?',
#     'context': 'Product A is the not the Best, Product B is not the Best , Product C is not the best , product D is the best ' #summary
# }
# res = nlp(QA_input)
# print("\n")
# print("Generated Answer: ")
# print(res['answer'])
# print(str(res['score']*100)[0:4]+'%')


# import requests
# from bs4 import BeautifulSoup

# def scrape_amazon_reviews(url):
#     # Send a GET request to the URL
#     response = requests.get(url)

#     if response.status_code == 200:
#         # Parse the HTML content using BeautifulSoup
#         soup = BeautifulSoup(response.content, 'html.parser')

#         # Find the container element that holds the overall review information
#         review_summary_container = soup.find('div', {'id': 'reviewsMedley'})

#         if review_summary_container:
#             # Extract overall review information
#             overall_rating = review_summary_container.find('span', {'data-hook': 'rating-out-of-text'}).text.strip()
            
#             # Check if the element containing total review count exists
#             total_reviews_element = review_summary_container.find('span', {'data-hook': 'total-review-count'})
#             if total_reviews_element:
#                 total_reviews = total_reviews_element.text.strip()
#             else:
#                 total_reviews = "N/A"

#             # Print overall review information
#             print("Overall Rating:", overall_rating)
#             print("Total Reviews:", total_reviews)
#             print("-----------------------------")

#             # Find all review elements within the container
#             review_elements = review_summary_container.find_all('div', {'data-hook': 'review'})

#             review_counts = {
#                 '1 star': 0,
#                 '2 stars': 0,
#                 '3 stars': 0,
#                 '4 stars': 0,
#                 '5 stars': 0
#             }

#             for review_element in review_elements:
#                 # Extract relevant information from each review element
#                 review_rating_element = review_element.find('i', {'data-hook': 'review-star-rating'})
#                 review_rating = float(review_rating_element.text.strip().split()[0])  # Extract and convert to float

#                 # Increment the count for the respective star rating
#                 review_counts[f'{int(review_rating)} stars'] += 1  # Convert to integer and use as dictionary key

#             # Print the review counts for each star rating
#             for star_rating, count in review_counts.items():
#                 print(star_rating + ":", count)

#         else:
#             print("Reviews container not found on the page.")
#     else:
#         print("Failed to retrieve the page. Status Code:", response.status_code)

# # Provide the URL of the Amazon product page
# product_url = 'https://www.amazon.in/Airdopes-141-Playtime-Resistance-Bluetooth/dp/B09N3ZNHTY/ref=sr_1_5?brr=1&qid=1688496900&rd=1&sr=8-5&th=1'

# # Scrape the reviews
# scrape_amazon_reviews(product_url)












