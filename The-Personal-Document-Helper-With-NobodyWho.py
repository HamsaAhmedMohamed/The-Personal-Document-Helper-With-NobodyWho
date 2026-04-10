import fitz  # PyMuPDF
from nobodywho import tool, Chat
def extract_pdf_content(pdf_path):
    doc = fitz.open(pdf_path)
    study_pages = []
    
    for page_num in range(len(doc)):
        text = doc[page_num].get_text("text")
        # Store page number with text for better referencing
        study_pages.append(f"[Source: Page {page_num + 1}]\n{text}")
    
    return study_pages

# Load your book
book_pages = extract_pdf_content("Notes_on_Theory_of_Discounted_MDPs.pdf")



@tool(description="Search the textbook for specific academic concepts or facts.")
def search_textbook(keyword: str) -> str:
    """Finds the most relevant page in the PDF based on a keyword."""
    relevant_chunks = []
    
    for page in book_pages:
        if keyword.lower() in page.lower():
            relevant_chunks.append(page)
            if len(relevant_chunks) >= 2: # Limit to top 2 matches to save memory
                break
                
    return "\n\n".join(relevant_chunks) if relevant_chunks else "Topic not found in book."

# Initialize NobodyWho with your GGUF model
chat = Chat("./Qwen_Qwen3-0.6B-Q4_K_M.gguf", tools=[search_textbook])

system_instruction = (
    "You are a Study Assistant. When asked a question, search the textbook. "
    "Always mention the Page Number provided in the source text."
)

print("PDF Helper: I've indexed your book. What should we review?")

while True:
    query = input("You: ")
    # The AI will call 'search_textbook' if it doesn't know the answer
    response = chat.ask(f"{system_instruction}\nUser: {query}")
    
    for token in response:
        print(token, end="", flush=True)
    print("\n")