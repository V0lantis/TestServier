import pandas as pd


def get_most_cited_drugs_journal():
    df = pd.read_json("data/aggregated/drugs.json")
    df = df.loc[:, ["journal", "drug"]].drop_duplicates()
    return df.groupby(["journal"]).count().sort_values(["drug"], ascending=False)


def get_drugs_cited_in_same_journal():
    df = pd.read_json("data/aggregated/drugs.json")
    df = df[(df.publication_type == "PubMed")]

    drugs = df.loc[:, ["journal", "drug"]].drop_duplicates()

    res = pd.merge(drugs, df, how="left", left_on=["journal"], right_on=["journal"])
    res = res[["drug_x", "journal", "drug_y"]].drop_duplicates()
    return res[res.drug_x != res.drug_y]


if __name__ == "__main__":
    print("Here are the journal with the most different cited drugs")
    print(get_most_cited_drugs_journal())

    """
                                                            drug
    journal                                                 
    Psychopharmacology                                     2
    The journal of maternal-fetal & neonatal medicine      2
    American journal of veterinary research                1
    Hôpitaux Universitaires de Genève                      1
    Journal of back and musculoskeletal rehabilitation     1
    Journal of emergency nursing                           1
    Journal of emergency nursing\xc3\x28                   1
    Journal of food protection                             1
    Journal of photochemistry and photobiology. B, ...     1
    The Journal of pediatrics                              1
    The journal of allergy and clinical immunology....     1
    """

    print("Here are the drugs cited in the same journal, but not from clinical trials")
    print(get_drugs_cited_in_same_journal())

    """
               drug_x  ...         drug_y
    6    TETRACYCLINE  ...        ETHANOL
    7         ETHANOL  ...   TETRACYCLINE
    12       ATROPINE  ...  BETAMETHASONE
    15  BETAMETHASONE  ...       ATROPINE
    [4 rows x 3 columns]
    """
