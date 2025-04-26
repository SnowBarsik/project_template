import os
import tempfile
import pandas as pd
import pytest
from io import StringIO

from app.io.input import file_read, pandas_file_read

def test_file_read_exists():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
        tmp.write("hello world")
        tmp.seek(0)
        tmp_name = tmp.name

    assert file_read(tmp_name) == "hello world"

    os.remove(tmp_name)

def test_file_read_not_exists():
    assert file_read("non_existing_file.txt") is None

@pytest.mark.parametrize("extension,write_func,read_func", [
    ("csv", lambda f: f.write("a,b\n1,2"), pd.read_csv),
    ("json", lambda f: f.write('{"a": [1], "b": [2]}'), pd.read_json),
])
def test_pandas_file_read_supported_formats(extension, write_func, read_func):
    with tempfile.NamedTemporaryFile(mode='w+', suffix=f'.{extension}', delete=False) as tmp:
        write_func(tmp)
        tmp_name = tmp.name

    expected_data = read_func(tmp_name)
    result = pandas_file_read(tmp_name)
    assert expected_data.to_string(index=False) == result

    os.remove(tmp_name)

def test_pandas_file_read_excel():
    df = pd.DataFrame({'a': [1], 'b': [2]})
    with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp:
        tmp_name = tmp.name
    df.to_excel(tmp_name, index=False)
    result = pandas_file_read(tmp_name)
    assert df.to_string(index=False) in result
    os.remove(tmp_name)

def test_pandas_file_read_not_exists():
    assert pandas_file_read("non_existing_file.csv") is None