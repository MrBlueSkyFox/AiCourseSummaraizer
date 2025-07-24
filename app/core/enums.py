from enum import Enum

class Environment(str, Enum):
    LOCAL = 'LOCAL'
    DEV = 'DEV'
    TEST = 'TEST'
    PROD = 'PROD'
    PREPROD = 'PREPROD'