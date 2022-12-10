"""
Servidor ray que contiene todo los métodos para encriptar usando md5 o sha256
"""
import hashlib
import cryptocode
import ray
import fcntl
from utils.password import generate_numeric_password


@ray.remote
class ServerEncrypt:

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
        with open("files/database.txt", "r") as f:
            lines = f.readlines()

        if len(lines) > 0 and lines[-1] in ["0", 0]:
            lines = lines[:-1]

        lines.extend(
            [
                f"{password}\n",
                f"{user_name}\n",
                "0"
            ]
        )

        # normalize \n
        for index, line in enumerate(lines):
            if index==len(lines)-1:
                continue
            lines[index] = line.strip() + "\n"

            # update the dataset
        with open("files/database.txt", "w") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            f.writelines(lines)
            fcntl.flock(f, fcntl.LOCK_UN)

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

        algorithm = hashlib.new(algorithm_key)
        algorithm.update(text_to_encrypt.encode('utf-8'))
        text_hash = algorithm.hexdigest()

        password = generate_numeric_password()

        # encrypt the hash
        text_encrypted = cryptocode.encrypt(
            text_hash,
            password
        )

        # generate the output

        with open(f'files/output_{user_name}.txt', 'w') as f:
            f.write(f"{password}\n")
            f.write(f"{text_encrypted}")

        # update the database
        self._update_database(user_name, password)

        return text_encrypted, password

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

        return self._encrypt(
            text_to_encrypt,
            user_name,
            'sha256',
            *args,
            **kwargs
        )
