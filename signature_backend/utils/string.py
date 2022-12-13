import secrets
from typing import Union


def bool_from_str(value: str) -> Union[bool, None]:
    """
    Convert string to boolean.
    :param value: String to convert.
    :return: Boolean value.
    """
    if value is None:
        return None
    if value.lower() in ['true', '1', 'yes', 'y', 't', 'True']:
        return True
    elif value.lower() in ['false', '0', 'no', 'n', 'f', 'False']:
        return False
    return None


RANDOM_STRING_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # noqa: E501


def get_random_string(length, allowed_chars=RANDOM_STRING_CHARS):
    """
    Return a securely generated random string.
    The bit length of the returned value can be calculated with the formula:
        log_2(len(allowed_chars)^length)
    For example, with default `allowed_chars` (26+26+10), this gives:
      * length: 12, bit length =~ 71 bits
      * length: 22, bit length =~ 131 bits
    """
    return ''.join(secrets.choice(allowed_chars) for i in range(length))


def set_next_prev_url(
    count: int,
    url: str,
    page: int = 0,
    page_size: int = 10,
):
    """
    Set the next and previous urls for a paginated response.
    :param count: Total number of items.
    :param url: Base url.
    :param page: Current page.
    :param page_size: Page size.
    """

    url = str(url).split('?')[0]

    if page > 0:
        prev_page = page - 1
        prev_url = f'{url}?page={prev_page}&page_size={page_size}'
    else:
        prev_url = None
    if page * page_size < count:
        next_page = page + 1
        next_url = f'{url}?page={next_page}&page_size={page_size}'
    else:
        next_url = None
    return prev_url, next_url
