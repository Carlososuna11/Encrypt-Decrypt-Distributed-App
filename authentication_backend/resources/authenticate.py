from conf import settings
from typing import Any
from filelock import FileLock


class AuthenticateResource:
    """
    Authenticates a user

    Use Cases:
    1. Authenticate a user
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._database = settings.DATABASE
        self._lock = FileLock("database.txt.lock")

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.authenticate_user(*args, **kwargs)

    def _authenticate(self, user_name: str, password: str) -> bool:
        """
        Authenticates a user

        Parameters
        ----------
        user_name : str, required
            User name
        password : str, required
            Password

        Returns
        -------
        bool
            True if the user is authenticated, False otherwise

        """
        # get the database

        lines = []
        with self._lock:
            with open(self._database, "r") as f:
                lines = f.readlines()

        authenticated = False
        if len(lines) > 0:
            for i in range(len(lines)-1):
                if lines[i+1].strip() == user_name:
                    if lines[i].strip() == password:
                        authenticated = True
                    break

        return {
            "authenticated": authenticated,
        }

    def authenticate_user(
        self,
        user_name: str,
        password: str,
        *args,
        **kwargs
    ) -> bool:
        """
        Authenticates a user

        Parameters
        ----------
        user_name : str, required
            User name
        password : str, required
            Password
        *args
            Arguments
        **kwargs
            Keyword arguments

        Returns
        -------
        bool
            True if the user is authenticated, False otherwise

        """
        return self._authenticate(user_name, password)
