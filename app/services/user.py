from secrets import token_urlsafe

from app.services.base import ServiceBase
from app.services.crypt import crypt_svc
from app.core.exceptions import InvalidCredentials
from app.infraestructure.mail.mail import email_svc
from app.schemas.user import UserUpdate, UserCreate, UserCreateInDB, UserInDB
from app.protocols.db.models.user import User
from app.protocols.db.crud.user import CRUDUserProtocol


class UserService(ServiceBase[User, UserCreateInDB, UserUpdate, CRUDUserProtocol]):
    def create(self, *, obj_in: UserCreate) -> User:
        hashed_password = crypt_svc.get_password_hash(obj_in.password)
        obj = UserCreateInDB(
            **obj_in.dict(
                exclude={
                    "password",
                }
            ),
            hashed_password=hashed_password,
        )
        return super().create(obj_in=obj)

    def authenticate(self, *, email: str, password: str) -> UserInDB:
        user = self.observer.get_by_email(email=email)
        if not user:
            raise InvalidCredentials("User not found")
        crypt_svc.check_password(password, user.hashed_password)
        return user

    def update_password(self, *, id: int, password: str) -> UserInDB:
        hashed_password = crypt_svc.get_password_hash(password)
        return self.observer.change_password(id=id, hashed_password=hashed_password)

    def recover_password(self, *, email: str) -> UserInDB:
        user = self.observer.get_by_email(email=email)
        new_password = token_urlsafe(16)
        obj_db = self.update_password(id=user.id, password=new_password)
        email_svc.send_email(
            subject="Recuperación de contraseña",
            body=f"Su nueva contraseña es: {new_password} ",
            recipients=[email]
        )
        return obj_db


user_svc = UserService()
