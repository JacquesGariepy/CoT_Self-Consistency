
# Chain of Thought with Self-Consistency
import openai
from dotenv import find_dotenv, load_dotenv
import os
# Initialize OpenAI API with your key
load_dotenv(find_dotenv(), override=True)
api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = api_key
engine = "gpt-3.5-turbo"
def chain_of_thought_prompting(initial_prompt, iterations=5):
    current_prompt = initial_prompt + ", think step-by-step"
    messages = [
        {"role": "system", "content":"you answer like a scientist in a brief and precise manner"},
        {"role": "user", "content": current_prompt}
    ]
    
    response = openai.ChatCompletion.create(
        model=engine,
        messages=messages,
        max_tokens=150,
        n=iterations,
    )
        
    responses = [choice['message']['content'] for choice in response['choices'] if choice['message']['role'] == 'assistant']
    responses_string = "first answer: " + ', next answer:
