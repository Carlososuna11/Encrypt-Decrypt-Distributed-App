# """
# Client to encrypt a message reading a file
# """
# from utils.files import read_file
# import requests

# BACKEND_BASE_URL = 'http://ray_head:8000'

# INPUT_FILE_NAME = 'input.txt'
# OUTPUT_FILE_NAME = 'output.txt'


# def main():

#     # read the input file
#     file_data = read_file(INPUT_FILE_NAME)

#     # get the type of the file
#     file_type = file_data['type']

#     # call the server
#     if file_type == 'FIRMAR':
#         # call the server to sign the message
#         text_encrypted, password = ray.get(
#             encryption_server.encrypt_md5.remote(
#                 **file_data
#             )
#         )
#         print(f'Text encrypted: {text_encrypted}')
#         print(f'Password: {password}')
#     elif file_type == 'AUTENTICAR':
#         # call the server to authenticate the user
#         authenticated = ray.get(
#             verification_server.authenticate_user.remote(
#                 **file_data
#             )
#         )
#         print(f'Authenticated: {authenticated}')

#     elif file_type == 'INTEGRIDAD':
#         # call the server to verify the integrity of the message
#         integrity = ray.get(
#             verification_server.verify_md5.remote(
#                 **file_data
#             )
#         )
#         print("Integrity: ", integrity)
