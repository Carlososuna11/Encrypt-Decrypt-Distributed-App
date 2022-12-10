"""
Client to encrypt a message reading a file
"""
import ray
from server.server_encrypt import ServerEncrypt
from server.server_verify import ServerVerify
from utils.files import read_file

INPUT_FILE_NAME = 'files/input_verificar.txt'


def main():
    # connect to the server
    encryption_server = ServerEncrypt.remote()
    verification_server = ServerVerify.remote()

    # read the input file
    file_data = read_file(INPUT_FILE_NAME)

    # get the type of the file
    file_type = file_data['type']

    # call the server
    if file_type == 'FIRMAR':
        # call the server to sign the message
        text_encrypted, password = ray.get(
            encryption_server.encrypt_md5.remote(
                **file_data
            )
        )
        print(f'Text encrypted: {text_encrypted}')
        print(f'Password: {password}')
    elif file_type == 'AUTENTICAR':
        # call the server to authenticate the user
        authenticated = ray.get(
            verification_server.authenticate_user.remote(
                **file_data
            )
        )
        print(f'Authenticated: {authenticated}')

    elif file_type == 'INTEGRIDAD':
        # call the server to verify the integrity of the message
        integrity = ray.get(
            verification_server.verify_md5.remote(
                **file_data
            )
        )
        print("Integrity: ", integrity)
