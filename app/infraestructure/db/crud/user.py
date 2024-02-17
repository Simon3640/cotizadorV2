from sqlalchemy.exc import NoResultFound

from app.infraestructure.db.utils.session import SessionLocal
from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models import User
from app.schemas.user import UserCreateInDB, UserUpdate
from app.core.exceptions import ORMError


class UserCrud(CRUDBase[User, UserCreateInDB, UserUpdate]):
    def get_by_email(self, *, email: str) -> User:
        with SessionLocal() as db:
            try:
                return db.query(User).filter(User.email == email).first()
            except NoResultFound as e:
                raise ORMError(str(e))
            
    def change_password(self, *, id: int, hashed_password: str) -> User:
        with SessionLocal() as db:
            try:
                user = self.get(id=id)
                user.hashed_password = hashed_password
                db.add(user)
                db.commit()
                db.refresh(user)
                return user
            except NoResultFound as e:
                raise ORMError(str(e))


user_crud = UserCrud(User)
