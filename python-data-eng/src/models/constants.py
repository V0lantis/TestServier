from enum import Enum


class DataSource(Enum):
    """
    Can be any data source, from file to database
    """

    CSV = 1
    JSON = 2
