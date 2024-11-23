import re

def chatbotContent(chat_export_file): 
    with open(chat_export_file, mode="r", encoding="utf-8") as corpus_file:
        content = corpus_file.read()    
    return tuple(content.split("\n"))
    
    


