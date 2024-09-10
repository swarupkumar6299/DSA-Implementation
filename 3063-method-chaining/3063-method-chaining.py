import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtered_animals=animals[animals['weight']>100].sort_values(by='weight',ascending=False)
    return pd.DataFrame(filtered_animals['name'])