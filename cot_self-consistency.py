import litellm

# Initialize LiteLLM
litellm = litellm.LiteLLM()

def chain_of_thought_prompting(initial_prompt, iterations=5):
    current_prompt = initial_prompt + ", think step-by-step"
    messages = [
        {"role": "system", "content": "you answer like a scientist in a brief and precise manner"},
        {"role": "user", "content": current_prompt}
    ]
    
    # Use LiteLLM for chat completion
    response = litellm.completion(
        model="gpt-3.5-turbo",  # specify model, adjust as needed
        messages=messages,
        max_tokens=150,
        n=iterations,
    )
    
    responses = [choice['message']['content'] for choice in response['choices'] if choice['message']['role'] == 'assistant']
    responses_string = "first answer: " + ', next answer: '.join(responses)
    
    return responses_string

# Usage example:
initial_prompt = "Explain the process of photosynthesis"
chain_of_thought = chain_of_thought_prompting(initial_prompt)
print(chain_of_thought)
