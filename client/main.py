# """
# Client to encrypt a message reading a file
# """
from utils.files import read_file
import requests

BACKEND_BASE_URL = 'http://ray_head:8000'

INPUT_FILE_NAME = '/input.txt'
OUTPUT_FILE_NAME = '/output.txt'


def main():

    print('Starting client...')

    # read the input file
    file_data = read_file(INPUT_FILE_NAME)

    # get the type of the file
    file_type = file_data['type']

    # call the server
    if file_type == 'FIRMAR':
        # call the server to sign the message
        response = requests.post(
            f'{BACKEND_BASE_URL}/signature/',
            json=file_data
        )
        response.raise_for_status()
        response_data = response.json()

        with open(OUTPUT_FILE_NAME, 'w') as f:
            f.write(response_data['text_encrypted'])
            f.write('\n')
            f.write(response_data['password'])
            f.write('\n0')

        print(f'Text encrypted: {response_data["text_encrypted"]}')
        print(f'Password: {response_data["password"]}')
    elif file_type == 'AUTENTICAR':
        # call the server to authenticate the user
        response = requests.post(
            f'{BACKEND_BASE_URL}/authentication/authenticate/',
            json=file_data
        )

        response.raise_for_status()

        response_data = response.json()

        status_text = 'VALIDO' if response_data['authenticated'] \
            else 'NO VALIDO'

        with open(OUTPUT_FILE_NAME, 'w') as f:
            f.write(status_text)
            f.write('\n0')

        print(f'Authenticated: {response_data["authenticated"]}')

    elif file_type == 'INTEGRIDAD':
        # call the server to verify the integrity of the message
        response = requests.post(
            f'{BACKEND_BASE_URL}/authentication/verify/',
            json=file_data
        )

        response.raise_for_status()

        response_data = response.json()

        status_text = 'VALIDO' if response_data['verified'] \
            else 'NO VALIDO'

        with open(OUTPUT_FILE_NAME, 'w') as f:
            f.write(status_text)
            f.write('\n0')

        print("Integrity: ", response_data['verified'])


if __name__ == '__main__':
    main()
