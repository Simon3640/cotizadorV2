import io
from uuid import uuid1

from fastapi import APIRouter, Depends, UploadFile, HTTPException
from fastapi.responses import StreamingResponse

from app.protocols.db.models.user import User
from app.api.middleware.bearer import get_current_active_empleado
from app.infraestructure.bucket.s3 import s3
from app.core.config import settings


router = APIRouter()


@router.post("/")
def upload_doc(
    file: UploadFile, 
    # current_user: User = Depends(get_current_active_empleado)
):
    contents: list[io.BytesIO] = []

    try:
        content = file.file.read()
        temp_file = io.BytesIO()
        temp_file.write(content)
        temp_file.seek(0)
        contents += [temp_file]
    except Exception:
        raise HTTPException(
            422,
            f"Los documentos no se pudieron subir, {file.filename} está corrupto",
        )

    for content in contents:
        path = f"{uuid1()}" + file.filename
        response = s3.push_file(
            settings.AWS_BUCKET_NAME,
            content,
            file_name=path,
            content_type=file.content_type,
        )
        if response:
            files_path = {"path": path, "name": file.filename}
    return {"file_path": files_path}

@router.get("/")
def get_doc(key: str, 
            # current_user: User = Depends(get_current_active_empleado)
            ):
    try:
        result = s3.get_file(settings.AWS_BUCKET_NAME, key)
    except Exception as e:
        if hasattr(e, "message"):
            raise HTTPException(
                status_code=e.message["response"]["Error"]["Code"],
                detail=e.message["response"]["Error"]["Message"],
            )
        else:
            raise HTTPException(status_code=500, detail=str(e))
    return StreamingResponse(content=result["Body"].iter_chunks(), media_type=result["ContentType"])