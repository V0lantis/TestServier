import pandas as pd

PubMed = {"id": str, "scientific_title": "str", "date": str, "journal": str}


def get_clinical_trials_data(
    *, csv_path="data/raw/clinical_trials.csv"
) -> pd.DataFrame:
    """

    :param csv_path: Data file path where drugs are stored
    :return: Pandas DataFrame with drugs data
    """
    df = pd.read_csv(csv_path, dtype=PubMed)
    df["date"] = pd.to_datetime(df["date"], format="mixed")
    df["title"] = df["scientific_title"]
    df.loc[:, "publication_type"] = "ClinicalTrial"
    df.drop(columns=["scientific_title"], inplace=True)
    return df
