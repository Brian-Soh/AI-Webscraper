# AI Web Scraper

## Introduction
**"Data is the new gold"** <br>
In a world where technology is improving exponential every day, data has become a commodity that is valued more than every before in history. Much of this is due to advancements in large language models (LLM) and artificial intelligence (AI) - which require large datasets to train.  Web scraping is a technique is often automated at scale to glean valuable information off internet webpages to provide these datasets. In this project, I wanted to explore the use of Python's Selenium Library to scrape websites and pass its Document Object Model (DOM) content through to the Ollama LLM which can summarize information and assists in answering questions. Click [here](https://youtu.be/gVf1yXs3CDk) for a demo!

## Classes
**main.py**
- Created a simply front end using the Streamlit to handle user input and queries
- Links web scraping and parsing functionalities

**scrape.py**
- Leveraged Chrome Driver to interact with web pages
- Utilized the Beautiful Soup library to extract body content

**parse.py**
- Inserts DOM content and user query into a prompt template before passing it into the Ollama LLM
- Parses the prompt in batches to stay within the context length threshold 

## Sources
- https://www.youtube.com/watch?v=Oo8-nEuDBkk&ab_channel=TechWithTim
