import os
from typing import Any


def get_env(name: str, default: Any = None) -> str:
    """
    Get environment variable.
    :param name: Name of the environment variable.
    :param default: Default value if environment variable is not set.
    :return: Value of environment variable.
    """
    if name in os.environ:
        return os.environ[name]
    return default


def password_file(
        file_env_name: str,
        env_name: str,
        default: Any = None
) -> str:
    """
    Get password from file or environment variable.
    :param file_env_name: Name of the environment variable.
    :param env_name: Name of the environment variable.
    :param default: Default value if environment variable is not set.
    :return: Value of environment variable.
    """
    if file_env_name in os.environ:
        file_name = os.environ[file_env_name]
        if os.path.exists(file_name) and os.access(file_name, os.R_OK):
            with open(file_name, 'r') as f:
                return f.read().strip()
    return get_env(env_name, default)


def database_to_uri(dialect: str, database: dict):
    """
    Convert a database dictionary to a URI.
    :param dialect: Database dialect.
    :param database: Database dictionary.
    """
    return "{}://{}:{}@{}:{}/{}".format(
        dialect,
        database.get('USER', ''),
        database.get('PASSWORD', ''),
        database.get('HOST', ''),
        database.get('PORT', ''),
        database.get('NAME', ''),
    )
