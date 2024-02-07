from sqlalchemy import Integer, Column

from app.infraestructure.db.utils.model import BaseModel
from app.infraestructure.db.utils.session import SessionLocal


class Consecutive(BaseModel):
    consecutive = Column(Integer)


class ConsecutiveRepository:
    def get_consecutivo(self) -> int:
        with SessionLocal() as db:
            consecutivo_info = db.query(Consecutive).first()
            if consecutivo_info:
                return consecutivo_info.consecutive
            else:
                return None

    def update_consecutivo(self, new_consecutivo):
        with SessionLocal() as db:
            consecutivo_info = db.query(Consecutive).first()
            if consecutivo_info:
                consecutivo_info.consecutive = new_consecutivo
            else:
                new_consecutivo_info = Consecutive(consecutive=new_consecutivo)
                db.add(new_consecutivo_info)

            db.commit()


consecutive_repo = ConsecutiveRepository()
