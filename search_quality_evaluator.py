import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def tfidf_similarity(text_a: str, text_b: str) -> float:
    """
    Convert both texts into TF-IDF vectors and compute cosine similarity.
    Returns a score from 0.0 to 1.0 (usually).
    """
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text_a, text_b])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return float(score)


CSV_PATH = "dataset/sample_queries.csv"  # change this if your CSV is elsewhere

with open(CSV_PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        query = row["query"]
        result = row["result"]

        score = tfidf_similarity(query, result)

        print("Query:", query)
        print("Result:", result)
        print("NLP relevance score (TF-IDF cosine):", round(score, 3))
        print("-" * 50)
