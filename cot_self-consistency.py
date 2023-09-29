# Import necessary libraries
import openai
from dotenv import find_dotenv, load_dotenv
import os
from litellm import LiteLLM

# Initialize OpenAI API with your key
load_dotenv(find_dotenv(), override=True)
api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = api_key
engine = "gpt-3.5-turbo"

# Initialize LiteLLM
litellm = LiteLLM()

def chain_of_thought_prompting(initial_prompt, iterations=5):
    current_prompt = initial_prompt + ", think step-by-step"
    messages = [
        {"role": "system", "content":"you answer like a scientist in a brief and precise manner"},
        {"role": "user", "content": current_prompt}
    ]
    
    # First, gather responses using OpenAI's API
    response = openai.ChatCompletion.create(
        model=engine,
        messages=messages,
        max_tokens=150,
        n=iterations,
    )
    
    openai_responses = [choice['message']['content'] for choice in response['choices'] if choice['message']['role'] == 'assistant']
    
    # Next, use LiteLLM for additional insights or responses
    litellm_responses = [litellm.generate_response(current_prompt) for _ in range(iterations)]
    
    # Combine or process the responses from both OpenAI and LiteLLM as per your requirement
    combined_responses = openai_responses + litellm_responses  # This is a simplistic combination. You might want to process or filter the responses in a specific manner.
    
    # Create a response string based on the obtained responses
    responses_string = "first answer: " + ', next answer: '.join(combined_responses)
    
    return responses_string

# Usage
initial_prompt = "Explain the process of photosynthesis"
chain_of_thought = chain_of_thought_prompting(initial_prompt)
print(chain_of_thought)
