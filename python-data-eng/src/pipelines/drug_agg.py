"""
Pipeline code for aggregating 3 different datasources together:

- drugs: drug database with drugs' id (`atcode`) and name (`drug`)
- pubmed: Paper database with papers' `title`, `journal`, `date` and `id`
- clinical_trials: Clinical trials with their titles (`scientific_title`), `id`, `journal` and `date`

The output will link drug with its respective mention from pubmed and clinical trials data source
"""
from json import dumps
from pathlib import Path
from typing import Dict, List

import pandas as pd

from models import get_drugs_data, get_clinical_trials_data, get_pubmed_data, DataSource

CLINICAL_TRIALS_CSV = "data/raw/clinical_trials.csv"
PUBMED_CSV = "data/raw/pubmed.csv"
PUBMED_JSON = "data/raw/pubmed.json"
DRUGS_CSV = "data/raw/drugs.csv"

COMBINED_DRUGS_INFO_OUTPUT = "data/aggregated/drugs.json"


def combine_drugs(drugs: pd.DataFrame, df: pd.DataFrame, col: str) -> List[Dict]:
    """
    For each drug, check if it is mentioned in the df data in the column `col`. Create a row for each occurence and
    return a python Dict.
    :return: A list of Dict with the name of the drug and a clinical trial which mention it

    EXAMPLE
    -------
    {
    'atccode': 'R01AD',
    'date': '2020-01-01',
    'drug': 'BETAMETHASONE',
    'id': 'NCT04153396',
    'journal': 'Hôpitaux Universitaires de Genève',
    'scientific_title': 'Preemptive Infiltration With Betamethasone and '
                      'Ropivacaine for Postoperative Pain in Laminoplasty or '
                      '\\xc3\\xb1 Laminectomy'
    }
    """

    mentioned_drugs_in_clinical_trials = []
    for index, drug in drugs.iterrows():
        res = df[col].str.lower().str.contains(drug.drug.lower())
        clinical_trials_containing_drug = df[res].copy()
        if not clinical_trials_containing_drug.empty:
            (
                clinical_trials_containing_drug.loc[:, "drug"],
                clinical_trials_containing_drug.loc[:, "atccode"],
            ) = (drug.drug, drug.atccode)
            clinical_trials_containing_drug.date = (
                clinical_trials_containing_drug.date.astype(str)
            )
            mentioned_drugs_in_clinical_trials += (
                clinical_trials_containing_drug.to_dict(orient="records")
            )

    return mentioned_drugs_in_clinical_trials


def dag():
    drugs = get_drugs_data(csv_path=DRUGS_CSV)
    clinical_trials = get_clinical_trials_data(csv_path=CLINICAL_TRIALS_CSV)
    pubmed_csv = get_pubmed_data(csv_path=PUBMED_CSV, data_source=DataSource.CSV)
    pubmed_json = get_pubmed_data(json_path=PUBMED_JSON, data_source=DataSource.JSON)

    res = []
    res += combine_drugs(drugs, clinical_trials, "title")
    res += combine_drugs(drugs, pubmed_csv, "title")
    res += combine_drugs(drugs, pubmed_json, "title")

    Path(COMBINED_DRUGS_INFO_OUTPUT).write_text(dumps(res, indent=4))


if __name__ == "__main__":
    dag()
