def read_signature_file(file_name: str) -> str:
    """
    Read a signature structure file

    Parameters
    ---------
    file_name : str, required
        File name

    Returns
    -------
    str
        Signature structure
    """
    data = {
        'type': 'FIRMAR'
    }
    with open(file_name, 'r') as f:
        lines = f.readlines()
        try:
            # the first line must be the FIRMAR tag
            if lines[0].strip() != 'FIRMAR':
                raise ValueError('Invalid file')

            # the second line must be the user name
            data['user_name'] = lines[1].strip()

            # the third line must be the text to sign
            data['text_to_encrypt'] = lines[2].strip()
        except IndexError:
            raise ValueError('Invalid file')

    return data


def read_auth_file(file_name: str) -> str:
    """
    Read an authentication structure file

    Parameters
    ---------
    file_name : str, required
        File name

    Returns
    -------
    str
        Authentication structure
    """
    data = {
        'type': 'AUTENTICAR'
    }
    with open(file_name, 'r') as f:
        lines = f.readlines()
        try:
            # the first line must be the AUTENTICAR tag
            if lines[0].strip() != 'AUTENTICAR':
                raise ValueError('Invalid file')

            # the second line must be the password
            data['password'] = lines[1].strip()

            # the third line must be the user name
            data['user_name'] = lines[2].strip()
        except IndexError:
            raise ValueError('Invalid file')

    return data


def read_integrity_file(file_name: str) -> str:
    """
    Read an integrity structure file

    Parameters
    ---------
    file_name : str, required
        File name

    Returns
    -------
    str
        Integrity structure
    """
    data = {
        'type': 'INTEGRIDAD'
    }
    with open(file_name, 'r') as f:
        lines = f.readlines()
        try:
            # the first line must be the INTEGRIDAD tag
            if lines[0].strip() != 'INTEGRIDAD':
                raise ValueError('Invalid file')

            # the second line must be the password
            data['password'] = lines[1].strip()

            # the third line must be the text
            data['text_to_verify'] = lines[2].strip()

            # the fourth line must be the signature
            data['text_to_verify_hash'] = lines[3].strip()
        except IndexError:
            raise ValueError('Invalid file')

    return data


file_methods = {
    'FIRMAR': read_signature_file,
    'AUTENTICAR': read_auth_file,
    'INTEGRIDAD': read_integrity_file
}


def read_file(file_name: str) -> str:
    """
    Read a file

    Parameters
    ---------
    file_name : str, required
        File name

    Returns
    -------
    str
        File content
    """

    method = None
    with open(file_name, 'r') as f:
        method = file_methods.get(f.readline().strip())
    if method is None:
        raise ValueError('Invalid file')
    return method(file_name)
