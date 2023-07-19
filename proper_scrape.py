import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer # tokenize the string
from sumy.summarizers.lex_rank import LexRankSummarizer #text-summ

def scrape_amazon_reviews(url):
   
    response = requests.get(url)  # Send a GET request to the Amazon product page

    
    soup = BeautifulSoup(response.content, 'html.parser') # Parser object representing the Product html

    review_containers = soup.find_all('div', {'data-hook': 'review'}) #where element type is div and the sub class is review

    review_texts = [] #all the text gets stored here, empty list

    # Words or phrases to filter out
    unwanted_words = ['Read more', 'Image not available', 'Unverified Purchase', '"'] #removing double quotes 

    # Iterate over each review container
    for review in review_containers:
        # Extract the review textt
        text = review.find('span', {'data-hook': 'review-body'}).text.strip()

        # Remove unwanted words and double quotes
        text = ' '.join(word for word in text.split() if word not in unwanted_words)

        # Append the review text to the list
        max_length = 390  # Adjust as per your model's maximum sequence length
        text = text[:max_length]

        # Append the review text to the list
        review_texts.append(text)

    # Print the filtered reviews
    print("Current Reviews: ")
    print('\n')
    print('\n')
    for i, review in enumerate(review_containers):
        # Extract the review title
        title = review.find('a', {'data-hook': 'review-title'}).text.strip()

        # Extract the review rating
        rating = float(review.find('i', {'data-hook': 'review-star-rating'}).text.split()[0])

        # Print the review details
        print(f"Title: {title}")
        print(f"Rating: {rating}")
        print(f"Review: {review_texts[i]}")
        print("-" * 40)
        print('\n')

    # Return the compiled review text
    return ' '.join(review_texts)


# Example usage
# product_url = 'https://www.amazon.in/boAt-Airdopes-Atom-81-Wireless/dp/B0BKG5PQ6T/?_encoding=UTF8&pd_rd_w=F8N7i&content-id=amzn1.sym.77f3c872-007d-42e5-b0b4-eed6d696d4a9&pf_rd_p=77f3c872-007d-42e5-b0b4-eed6d696d4a9&pf_rd_r=5QFFS62ZX8612M4TRE77&pd_rd_wg=LIdcb&pd_rd_r=6410f7c8-5600-43d5-8228-cf6e1d6954de&ref_=pd_gw_deals_m1_t1&th=1'  # Replace with the actual product page URL
# all_reviews = scrape_amazon_reviews(product_url)
# print(all_reviews)

from transformers import pipeline
# ##################################SUMMARY SECTION #############################
def summarize_text(text, num_sentences=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary_sentences = summarizer(parser.document, num_sentences)
    summary = ' '.join(str(sentence) for sentence in summary_sentences)
    return summary

# Example usage
# summary = generate_summary(all_reviews)
# print(summary)
###############################################################################


######################### FOR QUESTION ANSWERING ###################################
def answer_question(context, question):
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2") ## for question answering
    result = qa_pipeline(context=context, question=question)
    return result['answer']

############################ CHAT-BOT #################################
def chatbot():
    product_url = input("Enter the URL of the product on Amazon: ")
    print("\n")
    print("Here are the reviews obtained on the product")
    review_text = scrape_amazon_reviews(product_url)

    print("Chatbot: I have summarized the product reviews. \n")
    print("Here is a breif summary on the Product: ")
    print('\n')
    print(summarize_text(review_text))
    print('\n')
    print("If you have questions based on the product feel free to ask!")
    while True:
        user_input = input("User: ")
        if(user_input=="None"):
            break

        # Answer user questions based on the context or summary
        answer = answer_question(review_text, user_input)
        print("Chatbot:", answer)

        print("Chatbot: Is there anything else I can help you with? if you have no more questions, please enter None to relieve me!")

# Run the chatbot
chatbot()

#example url: https://www.amazon.in/boAt-Airdopes-Atom-81-Wireless/dp/B0BKG5PQ6T/?_encoding=UTF8&pd_rd_w=YXhuE&content-id=amzn1.sym.77f3c872-007d-42e5-b0b4-eed6d696d4a9&pf_rd_p=77f3c872-007d-42e5-b0b4-eed6d696d4a9&pf_rd_r=1RRNDG4D3HPW80GJ41XE&pd_rd_wg=XINqK&pd_rd_r=e6be439e-8be1-4d1f-b707-1b334eccaa00&ref_=pd_gw_deals_m1_t1
