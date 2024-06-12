import pandas as pd # type: ignore
import os


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded dataset as a pandas DataFrame.

    Raises:
        AssertionError: If the file doesn't exist or if the file format is not .csv.

    """
    try:
        if not os.path.exists(path):
            raise AssertionError("The file doesn't exist")
        if not path.lower().endswith('.csv'):
            raise AssertionError("The file format is not .csv")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return None