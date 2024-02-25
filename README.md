# TensionFlow - Shopping Assistant Project

## Overview
This project aims to create a personalised shopping assistant using uAgents to enhance the shopping experience for users. The shopping assistant will intelligently assist users in finding products, providing recommendations, comparing prices of identical products from multiple sources and making purchases on behalf of the user.
We make use of a locally used agent to take input from the user and communicate it to the processor agent, which collects data based on either the user input from the search bar and chatbot, or filters applied. Two more agents are used to make transactions on behalf of the user by sending a token from the customer account to the merchant account.

## Features
- **Fashion Assistant:** An AI tool created using Prompt Engineering in Open AI Playground that recommends clothing and accessories to the user based on details about the user's personality such as taste in music, location, personal aesthetic, etc. given as input to the program.
- **Product Recommendations:** Offer product recommendations based on product selection.
- **Search and Navigation:** Enable users to efficiently search for products and navigate through various categories from multiple sources using intuitive interfaces.
- **Comparing Prices:** Helps users make the best decision according to their budget by comparing prices of identical items from different sources.

## User Interface
![image](https://github.com/abhaymathur21/HackAI_Round_2/assets/113776577/fe98ad88-01d0-48e0-a6aa-ed95cd876e93)
![image](https://github.com/abhaymathur21/HackAI_Round_2/assets/113776577/652491bd-a7b8-4e46-8259-f64abeb64d59)


## Technologies Used
- **uAgents:** For the purpose of secure peer-to-peer communication, uAgents are used to process data from APIs.
- **Natural Language Processing (NLP):** Leverage cutting-edge ML technologies such as Large Language Models for Natural Language Processing tasks including a Fashion Assistant for personalized fashion recommendations.
- **Frontend:** Used a modern robust frontend framework called Next.js for the user interface.
- **Backend:** Employed a flexible and customizable backend technology called Flask to integrate uAgents with our frontend.

## Setup Instructions
1. **Clone the Repository:** Clone this repository to your local machine using `git clone https://github.com/your-repo-url.git`.
2. **Install Dependencies:** Navigate to the project directory (cd shopping-assistant) and install necessary dependencies using `npm i` for the frontend and `pip install -r requirements.txt` for Python.
3. **Configure Environment:** Set up the OpenAI API key in the Fashion_Assistant.ipynb file by creating your own key after logging into the OpenAI platform.
4. **Run the Application:** Start the application by running the appropriate commands i.e.: `npm run dev` for the frontend and `python app.py`, `python main.py` and `python processor.py` for the uAgents and Python backend, and access it via the specified URL.

### Note: Search example: 'iPhone 9', the search options are limited since dummy data is used

## Demo Video


https://github.com/abhaymathur21/HackAI_Round_2/assets/102252920/a98bc64b-e867-4a63-8793-24f8539699c5



## Assumptions

### Data Cleanliness
- **Assumed Clean Data:** This project assumes that the data retrieved from APIs or utilized within the system is clean, structured, and free from significant inconsistencies or errors.
- **Data Preprocessing:** While working with practical APIs, real-world data often requires preprocessing to handle missing values, outliers, and variations in formats. This aspect is assumed to have been addressed before integrating data into the system.
- **Consistency in API Responses:** It's presumed that the APIs used for fetching product information or user-related data maintain consistency in their responses, adhering to documented formats and structures.

### API Access
- **Dummy API Usage:** For demonstration purposes, this project utilizes 2 dummy APIs with 30 items each and having the same format of data, therefore has limited data. However, in a real-world scenario, multiple authentic APIs from platforms like Amazon, Flipkart, etc., would be integrated to fetch actual product data, prices, availability, and user-related information.
- **API Key Management:** Practical APIs often require API keys or access tokens. The assumption here is that appropriate access keys are obtained and managed securely to interact with real APIs from respective e-commerce platforms.
- **Rate Limiting and Quotas:** Real APIs commonly enforce rate limiting and quotas to control access. This project assumes that such limits are understood and adhered to in the integration process with live APIs.

### Token Exchange for Payment
- **Simulated Token Usage:** The token exchange mechanism between customer and merchant accounts for payment purposes is currently simulated for demonstration purposes. In reality, a secure and authentic token system complying with industry standards and financial regulations would be implemented for secure transactions. This project assumes the simulated tokens are placeholders and does not reflect actual payment tokenization used in production environments.

## Future Scope
- **Query Functionality on AgentVerse:** We failed to implement this project on AgentVerse as it does not currently support the use of query functionality, hence in the future we can make use of AgentVerse to host all the agents used in this project except 1 local agent to take input from the user
- **Further Integration with Frontend:** Integrate the Fashion Assistant with the frontend.
- **User Profiling Refinement:** Implement advanced algorithms to further enhance user profiling based on browsing history, preferences, and purchasing patterns. Utilize machine learning models to offer more accurate and personalized recommendations.
- **Integration with Additional APIs:** Expand the platform's capabilities by integrating with a wider range of e-commerce APIs beyond the current sources. Incorporate APIs from major platforms such as Amazon, Flipkart, eBay, Walmart, etc., to provide a more comprehensive product catalog and diverse options.
- **Interactive Navigation Chatbot:** Implement a chatbot to navigate through the website faster and provide better assistance to the user.
- **User Behavior Analytics:** Implement robust analytics to track user interactions, preferences, and buying behavior. Use this data to derive insights for further improving the shopping assistant's functionalities and user experience.
