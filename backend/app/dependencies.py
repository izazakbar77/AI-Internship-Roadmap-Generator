from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.core.security import verify_token

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    payload = verify_token(credentials.credentials)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid Token")

    username = payload.get("sub")

    user = db.query(User).filter(User.username == username).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found")

    return user