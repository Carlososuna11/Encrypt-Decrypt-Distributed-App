import hashlib
import cryptocode
from typing import Any


class VerifyResource:
    """
    Verify class

    """

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.verify_md5(*args, **kwds)

    def _verify(
        self,
        text_to_verify: str,
        text_to_verify_hash: str,
        password: str,
        algorithm_key: str,
        *args,
        **kwargs
    ) -> bool:
        """
        Verifies a text, first it decrypts the text with the password
        then it hash the text with the algorithm and finally it compares
        the hash with the decrypted text

        Parameters
        ----------
        text_to_verify : str, required
            Text to verify
        password : str, required
            Password
        algorithm_key : str, required
            Algorithm to use
        *args
            Arguments
        **kwargs
            Keyword arguments

        Returns
        -------
        bool
            True if the text is verified, False otherwise

        """

        # decrypt the hash
        text_hash_decrypted = cryptocode.decrypt(
            text_to_verify_hash,
            password
        )

        # hash the text
        algorithm = hashlib.new(algorithm_key)
        algorithm.update(text_to_verify.encode('utf-8'))
        text_hash = algorithm.hexdigest()

        # compare the hashes
        if text_hash == text_hash_decrypted:
            return {
                "verified": True,
            }

        return {
            "verified": False,
        }

    def verify_md5(
        self,
        text_to_verify: str,
        text_to_verify_hash: str,
        password: str,
        *args,
        **kwargs
    ) -> bool:
        """
        Verifies a text using md5

        Parameters
        ----------
        text_to_verify : str, required
            Text to verify
        password : str, required
            Password
        *args
            Arguments
        **kwargs
            Keyword arguments

        Returns
        -------
        bool
            True if the text is verified, False otherwise

        """
        return self._verify(
            text_to_verify,
            text_to_verify_hash,
            password,
            'md5',
            *args,
            **kwargs
        )

    def verify_sha256(
        self,
        text_to_verify: str,
        text_to_verify_hash: str,
        password: str,
        *args,
        **kwargs
    ) -> bool:
        """
        Verifies a text using sha256

        Parameters
        ----------
        text_to_verify : str, required
            Text to verify
        password : str, required
            Password
        *args
            Arguments
        **kwargs
            Keyword arguments

        Returns
        -------
        bool
            True if the text is verified, False otherwise

        """
        return self._verify(
            text_to_verify,
            text_to_verify_hash,
            password,
            'sha256',
            *args,
            **kwargs
        )
