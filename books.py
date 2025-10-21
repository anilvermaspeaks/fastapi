
from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter()

data_path = Path(__file__).parent / "data" / "books.json"
with open(data_path, "r") as f:
    books_data = json.load(f)



@router.get("/books")
def get_books():
    return {"books": books_data}
