# WebScraing-and-Product-Review-System-Using-Machine-Learning

This project is an intelligent AI-based review system designed specifically for e-commerce products. Its purpose is to assist users in obtaining comprehensive insights and evaluations of products by leveraging advanced technologies. The system operates by accepting a user-provided input in the form of a product URL. Using the Beautiful-Soup Library, it scrapes and retrieves the contents of the review section from the targeted product page, which corresponds to the URL provided.
To enhance user experience and facilitate easier understanding of the collected reviews, the system employs the Sumy summarization model. This powerful automatic summarizer analyses the text reviews and generates concise summaries that capture the key points and sentiments expressed by customers. This way, users can quickly grasp the overall consensus and main highlights of the product's reviews without having to read through lengthy texts.
Furthermore, the project incorporates a simple yet effective Question-Answering model known as deepset/roberta-base-squad2. This model is designed to understand and respond to user queries related to the product reviews. By inputting specific questions, users can seek clarification or gather additional information about certain aspects of the product. The system utilizes the deepset/roberta-base-squad2 model to provide accurate and relevant answers based on the user's input.

Combining the review summarization capability with the question-answering functionality, this project transforms into a fully-functional chatbot. Users can engage in interactive conversations with the system, posing questions and receiving prompt responses about the product's reviews. This comprehensive chatbot serves as a valuable tool for appraising and evaluating products, empowering users to make informed decisions based on the aggregated feedback and insights obtained.

In summary, this AI-based e-commerce review system streamlines the process of product evaluation by extracting and summarizing reviews from a given URL. By incorporating an intuitive question-answering model, it offers users a user-friendly and interactive experience to explore and comprehend the opinions of others. Whether users seek a concise overview or have specific inquiries about a product's reviews, this project aims to provide them with valuable information and guidance.

### THIS PROJECT WORKS ONLY FOR AMAZON BASED PRODUCT URL's as of Now ###

Instructions to Use:
1)Currently There is no specific UI designed for this project , so you will have to use it through the console itself 
2)Ensure Python base 3.11 or better is installed , also install pytorch 
3)Press the RUN button in the IDE , the console will ask for the AMAZON URl of the Product
4)After entering the URL, the summary and the reviews will be dispalyed on the console in a properly formatted way
5)After which the Chatbot will take queries in english
