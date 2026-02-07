from fastapi import FastAPI

app = FastAPI(
    title="Agri Python DevOps",
    description="FastAPI backend for DevOps assignment",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Agri Python DevOps project is running"}

@app.get("/health")
def health():
    return {"status": "UP"}
