import os
os.environ['TRANSFORMERS_CACHE']='/localscratch/bashyalb/pretrained_models'
from transformers import pipeline
from transformers import AutoTokenizer
import transformers
import torch
import re



model = "meta-llama/Llama-2-7b-chat-hf" 
tokenizer = AutoTokenizer.from_pretrained(model, use_auth_token=True)

llama_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.float16,
    device_map="auto",
)

prompt_path='../Data/prompts.txt'
text_path='../Data/dummy.txt'

def read_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        prompt = file.read()
    return prompt
    
def get_llama_response(prompt: str) -> str:
    full_text = llama_pipeline(prompt, max_length=4096)[0]['generated_text']
    return full_text


def return_relevant_sentences(sentences_path, prompt_path):
    prompt = read_prompt(prompt_path)

    relevant_sentences = []
    with open(sentences_path, 'r', encoding='utf-8') as file:
        sentences = file.read()
        final_sent= f"{prompt}#Original Sentence#:{sentences}\"Output:"
        response = get_llama_response(final_sent)

    return response
relevant_sentence = return_relevant_sentences(text_path, prompt_path)
print(relevant_sentence)