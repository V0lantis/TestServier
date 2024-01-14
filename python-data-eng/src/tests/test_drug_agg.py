import pytest

from models import get_drugs_data, get_clinical_trials_data
from pipelines.drug_agg import combine_drugs, DRUGS_CSV, CLINICAL_TRIALS_CSV


def test_drug_agg():
    drugs = get_drugs_data(csv_path=DRUGS_CSV)
    clinical_trials = get_clinical_trials_data(csv_path=CLINICAL_TRIALS_CSV)

    res = []
    res += combine_drugs(drugs, clinical_trials, "title")

    assert len(res) > 0
    # Test that all drugs have a drug name
    assert all(drug.get("drug", False) for drug in res)
