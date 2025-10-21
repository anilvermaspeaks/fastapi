
from http.client import HTTPException
from fastapi import APIRouter, Query
import json
from pathlib import Path

router = APIRouter()

data_path = Path(__file__).parent / "data" / "books.json"
with open(data_path, "r") as f:
    books_data = json.load(f)



@router.get("/books")
def get_books():
    return {"books": books_data}


@router.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books_data:
        if book["id"] == book_id:
            return {"book": book}
    return {"error": "Book not found"}   


@router.get("/books/")
def get_book_by_name(title: str = Query(..., description="Name of the book to search")):
    for book in books_data:
        if book["title"].lower() == title.lower():
            return {"book": book}
    return {"error": "Book not found", "status_code":404}  

