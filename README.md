# AI Customer Support Assistant

## Project Overview

The AI Customer Support Assistant is a Python-based conversational application that uses LangChain and an LLM API to understand customer queries and provide relevant responses.

The system classifies customer queries into different categories and retrieves relevant information from a predefined knowledge base before generating a clear response using an LLM.

## Features

- Conversational customer support
- Intent classification
- Product inquiry handling
- Order status queries
- Returns and refunds support
- Technical support
- General queries
- Predefined knowledge base
- LLM-generated responses
- Conversation history
- Error handling
- Secure API key management

## Technologies Used

- Python
- LangChain
- OpenAI API
- python-dotenv

## Project Structure

```text
ai-customer-support-assistant/
│
├── chat.py
├── intent_classifier.py
├── knowledge_base.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
└── .env