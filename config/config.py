"""کلید امضای توکن و الگوریتم"""

SECRET_KEY = "Wh0pZrIqEUTWQ2vPBlYORH7_o6ZCcZ-9sRXwqDwoKzA"  # Use a strong, random key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time

import secrets
print(secrets.token_urlsafe(32))