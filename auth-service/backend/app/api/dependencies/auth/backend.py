from core.authentication.transport import bearer_transport
from fastapi_users.authentication import AuthenticationBackend

from api.dependencies.auth.strategy import get_strategy

authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_strategy,
)
