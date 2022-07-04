import os

import pytest


@pytest.fixture
def test_root_dir():
    return os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def fixtures_dir(test_root_dir):
    return f'{test_root_dir}/fixtures'


@pytest.fixture
def b3_demo_data(fixtures_dir):
    path = f'{fixtures_dir}/b3-sample-historical-data.txt'
    with open(path, 'r') as f:
        return f.read()
