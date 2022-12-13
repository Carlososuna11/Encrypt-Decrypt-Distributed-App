"""
Servidor ray que contiene todo los métodos para encriptar usando md5 o sha256
"""
import hashlib  # hashing
import cryptocode  # encryption
from filelock import FileLock   # mutual exclusion
from conf import settings
from utils.password import generate_numeric_password
from typing import Any


class SignatureResource:
    """
    Class that contains all the methods to encrypt using md5 or sha256

    Use Cases:
    1. Encrypt a text using md5 or sha256
    2. Encrypt a text using md5 or sha256 and save the password in a database
    """

    def __init__(self) -> None:
        self._database = settings.DATABASE
        self._lock = FileLock("database.txt.lock")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        Calls the encrypt_md5 method
        """
        return self.encrypt_md5(*args, **kwds)

    def _update_database(self, user_name: str, password: str):
        """
        Updates the database with the new user and password

        Parameters
        ----------
        user_name : str, required
            User name
        password : str, required
            Password

        Returns
        -------
        None

        """

        # read the dataset
        lines = []
        # blocks the file while reading
        with self._lock:
            with open(self._database, "r") as f:
                lines = f.readlines()

        # remove the last line if it is 0
        if len(lines) > 0 and lines[-1] in ["0", 0]:
            lines = lines[:-1]

        # add the new user and password
        lines.extend(
            [
                f"{password}\n",
                f"{user_name}\n",
                "0"
            ]
        )

        # normalize \n
        for index, line in enumerate(lines):
            if index == len(lines)-1:
                continue
            lines[index] = line.strip() + "\n"

            # update the dataset
        # blocks the file while writing
        with self._lock:
            # write the dataset
            with open(self._database, "w") as f:
                f.writelines(lines)

    def _encrypt(
        self,
        text_to_encrypt: str,
        user_name: str,
        algorithm_key: str,
        *args,
        **kwargs
    ) -> tuple:
        """
        Encrypts a text, first it hash the text with the algorithm and
        then it encrypts the hash with the password

        Parameters
        ----------
        text_to_encrypt : str, required
            Text to encrypt
        user_name : str, required
            User name
        algorithm_key : str, required
            Algorithm to use
        *args
            Arguments
        **kwargs
            Keyword arguments

        Returns
        -------
        tuple
            Encrypted text and password

        """

        # generate the algorithm method from the algorithm key
        algorithm = hashlib.new(algorithm_key)
        # make the hash
        algorithm.update(text_to_encrypt.encode('utf-8'))
        # get the hash
        text_hash = algorithm.hexdigest()

        # generate the password
        password = generate_numeric_password()

        # encrypt the hash
        text_encrypted = cryptocode.encrypt(
            text_hash,
            password
        )

        # update the database
        self._update_database(user_name, password)

        return {
            "text_encrypted": text_encrypted,
            "password": password,
        }

    def encrypt_md5(
        self,
        text_to_encrypt: str,
        user_name: str,
        *args,
        **kwargs
    ) -> tuple:
        """
        Encrypts a md5 text, first it hash the text with md5 and
        then it encrypts the hash with the password

        Parameters
        ----------
        text_to_encrypt : str, required
            Text to encrypt
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
        str
            Encrypted text

        """

        # call the encrypt method with the md5 algorithm
        return self._encrypt(
            text_to_encrypt,
            user_name,
            'md5',
            *args,
            **kwargs
        )

    def encrypt_sha256(
        self,
        text_to_encrypt: str,
        user_name: str,
        *args,
        **kwargs
    ) -> tuple:
        """
        Encrypts a sha256 text, first it hash the text with sha256 and
        then it encrypts the hash with the password

        Parameters
        ----------
        text_to_encrypt : str, required
            Text to encrypt
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
        str
            Encrypted text

        """

        # call the encrypt method with the sha256 algorithm
        return self._encrypt(
            text_to_encrypt,
            user_name,
            'sha256',
            *args,
            **kwargs
        )
