import pytest
import tempfile

def test_load_missing_file():
    """
    Test if the load_data function raises FileNotFoundError for missing files.
    """
    nonexistent_file = tempfile.NamedTemporaryFile(delete=True).name
    with pytest.raises(FileNotFoundError):
        load_data(nonexistent_file)
