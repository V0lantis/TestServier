import json
from pathlib import Path

import pandas as pd

from .constants import DataSource


PubMed = {"id": int, "title": "str", "date": str, "journal": str}


def _get_pubmed_data_from_csv(*, csv_path="data/raw/pubmed.csv") -> pd.DataFrame:
    """

    :param csv_path: CSV data file path where drugs are stored
    :return: Pandas DataFrame with drugs data
    """
    df = pd.read_csv(csv_path, dtype=PubMed)
    df["date"] = pd.to_datetime(df["date"], format="mixed")
    return df


def _get_pubmed_data_from_json(*, json_path="data/raw/pubmed.json") -> pd.DataFrame:
    """

    :param json_path: Json data file path where drugs are stored
    :return: Pandas DataFrame with drugs data
    """
    data = Path(json_path).read_text()
    parsed_data = json.loads(data)
    df = pd.json_normalize(parsed_data)
    df["date"] = pd.to_datetime(df["date"], format="mixed")
    return df


GET_PUBMED_DATA_FN_MAPPING = {
    DataSource.CSV: _get_pubmed_data_from_csv,
    DataSource.JSON: _get_pubmed_data_from_json,
}


def get_pubmed_data(*, data_source=DataSource.CSV, **kwargs) -> pd.DataFrame:
    df = GET_PUBMED_DATA_FN_MAPPING[data_source](**kwargs)
    df.loc[:, "publication_type"] = "PubMed"
    return df
