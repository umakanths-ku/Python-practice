
searchs= [
    "how to learn python", 
    "best AI tools for coding", 
    "nvidia stock price", 
    "what is generative ai", 
    "apple iphone 18 release date",
    "top AI startups"
]
a = 0
for search in searchs:
    clean_search = search.lower()
    
    if "ai" in clean_search:
     a += 1

print(f"Total searches matching 'ai': {a}")