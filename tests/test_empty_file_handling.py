import pytest
import csv

@pytest.fixture
def empty_csv_file(tmp_path):
    file_path = tmp_path / "empty_file.csv"
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])
    return file_path

def test_load_empty_file(empty_csv_file):
    """
    Test if the load_data function handles empty files gracefully.
    """
    data = load_data(empty_csv_file)
    assert len(data) == 0
