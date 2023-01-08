import os
import uuid
import pytest

from dundie.core import load
from .constantes import PEOPLE_FILE


def setup_module():
    print("\nroda antes dos teste\n")


def teardown_module():
    print("\nroda apos os teste desse modulo\n")


@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    file_ =tmpdir.join("new_file.txt")
    file_.write("isso é sujeira....")
    yield
    file_.remove()


@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test load function"""
    filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filepath))

    result = load(PEOPLE_FILE)

    with open(filepath, "w") as file_:
        file_.write("dados uteis somente para o teste")

    assert len(result) == 2
    assert result[0][0] == 'J'


@pytest.mark.unit
@pytest.mark.high
def test_load2():
    """Test load function"""

    result = load(PEOPLE_FILE)

    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("dados uteis somente para o teste")

    assert len(result) == 2
    assert result[0][0] == 'J'
