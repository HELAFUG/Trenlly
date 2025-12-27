from api.dependencies.auth.backend import authentication_backend
from api.dependencies.auth.user_manager import get_user_manager
from fastapi_users import FastAPIUsers

from core.models import User

fastapi_users_app = FastAPIUsers[User, int](get_user_manager, [authentication_backend])
