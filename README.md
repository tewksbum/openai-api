# openai-api
pip install "openai[embeddings]"

## to start:
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
uvicorn main:app --reload 

## to kill:
lsof -i :8000 kill

# virtual env:
python3 -m venv openai-api
source openai-api/bin/activate