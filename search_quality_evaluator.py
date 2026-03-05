from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

query = "best productivity apps for students"

search_result = "Top productivity apps every college student should use."

score = similarity(query, search_result)

print("Query:", query)
print("Result:", search_result)
print("Relevance score:", round(score, 2))
