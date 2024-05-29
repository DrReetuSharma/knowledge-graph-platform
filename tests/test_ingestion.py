# testing if ingestion is working as desired
# tests/test_data_ingestion.py

import pytest
from src.data_ingestion import load_data

def test_load_data():
    data = load_data('test_data.csv')
    assert len(data) > 0 
