"""
Main entry point for the Agentic RAG system.

This module loads environment variables and initializes the application.
"""

import os
from dotenv import load_dotenv


def main():
    """
    Main function to initialize and run the Agentic RAG system.
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Verify required environment variables are set
    required_vars = ['GEMINI_API_KEY', 'TAVILY_API_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"Warning: Missing required environment variables: {', '.join(missing_vars)}")
        print("Please set them in your .env file or environment.")
    else:
        print("Environment variables loaded successfully.")
    
    # TODO: Initialize and run the agent
    print("Agentic RAG system initialized.")


if __name__ == "__main__":
    main()
