import csv
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

with open("dataset/sample_queries.csv", newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        query = row["query"]
        result = row["result"]

        score = similarity(query, result)

        print("Query:", query)
        print("Result:", result)
        print("Relevance score:", round(score,2))
        print("-"*40)
