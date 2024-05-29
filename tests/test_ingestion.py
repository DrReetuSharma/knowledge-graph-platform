  """
    Test if the load_data function loads data successfully.
    """
# tests/test_ingestion.py

import pytest
from src.data_ingestion.ingest import load_data

def test_load_data():
    data = load_data('test_data.csv')
    assert len(data) > 0 
