# Python et Data Engineering

Vous trouverez l'ensemble de mon travail au chemin `./python-data-eng`.

### Analyse et décisions

Dans le cadre de cet exercice, j'ai tenté de rester le plus simple et claire possible. J'ai donc décidé de n'utiliser
que `Pandas` comme librairie Python. Cependant, d'autres solutions auraient été possibles telle que [DuckDB](https://duckdb.org/).
DuckDb aurait été une solution très élégante et aurait probablement faciliter grandement certains calculs analytiques que j'ai pu
coder en pandas natifs. Néanmoins, bien que DuckDB soit très performant, cela reste une db in-memory, qui ne scale pas horizontalement.
Pandas possède l'avantage d'avoir une API native en Spark, ce qui facilite fortement la migration du code si besoin.

### Exécuter le projet

Vous aurez d'abord besoin de créer un nouveau virtuenv:

```shell
cd python-data-eng
python -m venv venv
source venv/bin/activate
pip install -r src/requirements.txt
```

Une fois les modules installés, vous devrez exporter la variable environment `PYTHONPATH` afin d'avoir accès aux différents
modules présent dans `src`:

```shell
export PYTHONPATH=$(pwd)/src
```

Vous pourrez ensuite exécuter le dag comme cela :

```shell
python src/pipelines/drug_agg.py
```

Pour exécuter la suite de tests, il faut d'abord installer les dépendances (`requirements-dev.txt`), puis lancer la commande
`pytest`:

```shell
pip install -r src/requirements-dev.txt
pytest
```


# 6. Pour aller plus loin

> Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses
volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?

Dans ce type de situation, Spark est la solution la plus optimale pour gérer de gros fichiers ou plusieurs millions de fichiers. De plus, pySpark offre une API native Pandas, ce qui rend la conversion de mon code très facile.

> Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de
telles volumétries ?

En prenant l'hypothèse que Spark est la solution retenue pour s'adapter à la volumétrie décrite dans la question précédente, des changements mineurs seront nécessaires :
- Création d'un cluster spark (Yarn, Kubernetes ou autre).
- Conversation de nos DataFrame en Spark DataFrame. Ce changement est mineur, car Spark a développé une API Pandas qui reproduit toutes les fonctions usuelles de pandas en utilisant le moteur distribué de spark ([Pandas on Spark](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/index.html)). Par exemple, la lecture de fichier CSV deviendrait :

```python
from pyspark import pandas as pd

...
pd.read_csv()
```

