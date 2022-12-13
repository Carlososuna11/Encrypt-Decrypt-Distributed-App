from pathlib import Path
from utils.enviroment import get_env
from utils.string import bool_from_str

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = bool_from_str(
    get_env('DEBUG', 'f')
)

# Project information
PROJECT_NAME = get_env('PROJECT_NAME', 'Signature Backend')
PROJECT_DESCRIPTION = get_env('PROJECT_DESCRIPTION', '')
PROJECT_VERSION = get_env('PROJECT_VERSION', '1.0.0')


# Database information
DATABASE = get_env('DATABASE', '/database.txt')

RAY_ADDRESS = get_env('RAY_ADDRESS', 'ray://ray_head:10001')
