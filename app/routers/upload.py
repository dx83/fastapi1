import os
from fastapi import APIRouter, Form, File, UploadFile
from pathlib import Path
from uuid import uuid4

router = APIRouter(prefix="/api/upload", tags=["업로드"])

# 현재 파일의 절대 경로. 부모폴더. 부모폴더 / images 폴더 반환
BASE_DIR = Path(__file__).resolve().parent.parent / Path("images")
# print(BASE_DIR)

# http://서버주소:8000/api/upload/save
# code: 상품코드, image: 업로드할 이미지 파일
@router.post("/save")
async def save_image(code:str = Form(...), image: UploadFile = File(...)):
    ext = Path(image.filename).suffix       # 1. 확장자 추출
    new_filename = f"{uuid4().hex}{ext}"    # 2. 새 파일명 생성 (UUID + 확장자)
    file_path = BASE_DIR / new_filename     # 3. 파일 저장 경로

    with open(file_path, "wb") as f:        # 4. 파일 저장
        f.write(await image.read())

    # 5. 응답 반환
    return {"result": 1, "code": code, "filename": new_filename}

