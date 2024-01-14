import pandas as pd

Drug = {
    "atccode": str,
    "drug": str,
}


def get_drugs_data(*, csv_path="data/raw/drugs.csv") -> pd.DataFrame:
    """

    :param csv_path: Data file path where drugs are stored
    :return: Pandas DataFrame with drugs data
    """
    return pd.read_csv(csv_path, dtype=Drug)


if __name__ == "__main__":
    print(get_drugs_data())
