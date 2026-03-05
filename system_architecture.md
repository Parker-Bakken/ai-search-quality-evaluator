# System Architecture

This project simulates a simplified AI search relevance evaluation pipeline.

```mermaid
flowchart TD

A[Search Query Dataset] --> B[Python Evaluation Script]

B --> C[TF-IDF Vectorization]

C --> D[Cosine Similarity Scoring]

D --> E[Relevance Score Output]

E --> F[Evaluation Results]
