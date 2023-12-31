from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Book, BookUpdate

router = APIRouter()



@router.post("/", response_description="Create a new book", status_code=status.HTTP_201_CREATED, response_model=Book)
def create_book(request: Request, book: Book=Body(...)):
    '''
    "/books"로 시작하는 모든 책 엔드포인트에는 경로가 "/ "으로 설정됩니다. 
    API 문서에서 표시될 내용은 response_description이며, 요청이 성공적일 때 반환되는 HTTP 상태 코드는 status_code입니다. 
    우리는 요청 본문에 전달된 데이터와 보낸 응답을 모두 확인하기 위해 Book 모델을 사용합니다. 
    FastAPI는 이 유효성 검사를 우리 대신 처리합니다. 
    함수 내에서는 PyMongo의 insert_one() 메서드를 사용하여 새로운 책을 "books" 컬렉션에 추가하고, 
    데이터베이스에서 새로 생성된 책을 찾기 위해 find_one() 메서드를 활용합니다.
    '''
    book = jsonable_encoder(book)
    new_book = request.app.database["books"].insert_one(book)
    create_book = request.app.database["books"].find_one(
        {"_id" :new_book.inserted_id}
    )

    return create_book

@router.get("/", response_description="List all books", response_model=List[Book])
def list_books(request: Request):
    '''
    책 목록을 보여주는 메서드
    '''
    books = list(request.app.database["books"].find(limit=100))
    return books


@router.get("/{id}", response_description="Get a single book by id", response_model=Book)
def find_book(id: str, request: Request):
    if (book := request.app.database["books"].find_one({"_id": id})) is not None:
        return book
    

    # 검색 하는 책이 없다면 404 error
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

@router.put("/{id}", response_description="Update a book", response_model=Book)
def update_book(id: str, request: Request, book: BookUpdate = Body(...)):
    book = {k: v for k, v in book.dict().items() if v is not None}
    if len(book) >= 1:
        update_result = request.app.database["books"].update_one(
            {"_id":id}, {"$set": book} # specified fields만 update 되도록 $set 연산자를 사용
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

    
    if (existing_book := request.app.database["books"].find_one({"_id": id})) is not None:
        return existing_book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"book with ID {id} not found")


@router.delete("/{id}", response_description="Delete a book")
def delete_book(id: str, request: Request, response: Response):
    delete_result = request.app.database["books"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")