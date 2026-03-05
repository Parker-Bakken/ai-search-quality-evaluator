# AI Search Quality Evaluator

Lightweight framework for scoring search query/result relevance using:
- human-labeled evaluation guidelines
- TF-IDF + cosine similarity baseline scoring
- reproducible script output

## What this demonstrates
- evaluation thinking (query intent → relevance criteria)
- simple, explainable baseline scoring
- reproducible pipeline (dataset → scoring → report)

## Repo contents
- `search_quality_evaluator.py` — scoring script
- `dataset/` — query/result pairs + guidelines
- `requirements.txt` — dependencies
- `sample_output.txt` — example output
- `system_architecture.md` — pipeline diagram
- `reports/` — summary outputs (added)

## Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

```
## Run tests
```bash
pip install -r requirements-dev.txt
pytest -q
