import pytest
from dundie.core import load
from .constantes import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_2_people(request):
    """Test load function"""

    result = load(PEOPLE_FILE)

    assert len(result) == 2
    assert result[0][0] == 'J'

    assert len(load(PEOPLE_FILE)) == 2


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_j(request):
    """Test load function"""

    assert load(PEOPLE_FILE)[0][0] == 'J'
