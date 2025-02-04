from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "Extract information from the following content: {dom_content}. "
    "{parse_description}"
)

model = OllamaLLM(model = "llama3.2")

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    
    parsed_results = []
    for i, chunk in enumerate(dom_chunks, start = 1):
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)
        
    return "\n".join(parsed_results)