import pandas as pd
import os
from typing import Iterable, Union

def save_to_file(path: str, index: Union[str, Iterable[str]], data: Union[dict, Iterable[dict]]) -> None:
    """Saves potentially nested dictionary to a csv file.
    
    If the file already exists, it will be appended to, overwriting the index if it already exists.
    
    Data and index can be single values or iterables of values. If they are iterables, they must be of the same length,
    and the data will be saved as a row for each element in the iterable.

    :param path: Path to save the file
    :param index: Name of the row in the file
    :param data: Dict with the data to save
    """
    if isinstance(index, str):
        index = [index]
    
    df = pd.json_normalize(data)
    df.index = index
    
    if os.path.exists(path):
        existing = pd.read_csv(path, index_col=0)
        # combine_first will overwrite the index if it already exists by taking the first value
        # technically, it won't overwrite with a null value, but the same index should have the same number of columns
        df = df.combine_first(existing)
    
    df.to_csv(path)