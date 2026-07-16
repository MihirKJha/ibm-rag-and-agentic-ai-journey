"""Main script for running the Icebreaker Bot."""

import sys
import time
import logging
import argparse

from modules.data_extraction import extract_linkedin_profile
from modules.data_processing import split_profile_data, create_vector_database, verify_embeddings
from modules.query_engine import generate_initial_facts, answer_user_query
from typing import Dict, Any, Optional
import config
from modules.llm_interface import change_llm_model

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(stream=sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def process_linkedin(linkedin_url, api_key=None, mock=False):
    """
    Processes a LinkedIn URL, extracts data from the profile, and interacts with the user.

    Args:
        linkedin_url: The LinkedIn profile URL to extract or load mock data from.
        api_key: ProxyCurl API key. Required if mock is False.
        mock: If True, loads mock data from a premade JSON file instead of using the API.
    """ 
    
    try:
        # Extract the profile data
        profile_data = extract_linkedin_profile(linkedin_url, api_key, mock)

        if not profile_data:
            logger.error("Failed to retrieve profile data.")
            return
        
        # Split profile data
        nodes = split_profile_data(profile_data)
        
        # Store in vector database
        vectordb_index = create_vector_database(nodes)
        
        if not vectordb_index:
            logger.error("Failed to create vector database.")
            return

        # Verify embeddings
        if not verify_embeddings(vectordb_index):
            logger.warning("Some embeddings may be missing or invalid.")
            return

        
        #Generate and display intial facts
        initial_facts = generate_initial_facts(vectordb_index)
        logger.info(f"Initial facts about given linked-in profiel: {initial_facts}")
        
        # Start chatbot interface
        chatbot_interface(vectordb_index)

    except Exception as e:
        logger.error(f"Error occured:{str(e)}")


def chatbot_interface(index):
    """
    Provides a simple chatbot interface for user interaction.
    
    Args:
        index: VectorStoreIndex containing the LinkedIn profile data.
    """

    print("\nYou can now ask more in-depth questions about this person. Type 'exit', 'quit', or 'bye' to quit.")

    while True:
        user_query = input("You: ")
        if user_query.lower() in ['exit', 'quit', 'bye']:
            print("Bot: Goodbye!")
            break
        
        print("Bot is typing...", end='')
        sys.stdout.flush()
        time.sleep(1)  # Simulate typing delay
        print('\r', end='')
        
        response = answer_user_query(index, user_query)
        print(f"Bot: {response.response.strip()}\n")


def main():
    """Main function to run the Icebreaker Bot."""
    parser = argparse.ArgumentParser(description='Icebreaker Bot - LinkedIn Profile Analyzer')
    parser.add_argument('--url', type=str, help='LinkedIn profile URL')
    parser.add_argument('--api_key', type=str, help='API key')
    parser.add_argument('--mock', action='store_true', help='Use mock data instead of API')
    parser.add_argument('--model', type=str, help='LLM model to use (e.g., "ibm/granite-3-2-8b-instruct")')    
    
    args = parser.parse_args() 

    # Use command line arguments or prompt user for input
    linkedin_url = args.url or input("Enter LinkedIn profile URL (or press Enter to use mock data): ")
    use_mock = args.mock or not linkedin_url    
    
    if args.model:        
        change_llm_model(args.model)    
         
    api_key = args.api_key or config.PROXYCURL_API_KEY

    if not use_mock and not api_key:
        api_key = input("Enter ProxyCurl API key: ")        
       
    # Use a default URL for mock data if none provided
    if use_mock and not linkedin_url:
        linkedin_url = "https://www.linkedin.com/in/leonkatsnelson/"   
        process_linkedin(linkedin_url, api_key, mock=use_mock)


if __name__ == "__main__":
    main()