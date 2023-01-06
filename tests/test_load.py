from dundie.core import load
from .constantes import PEOPLE_FILE

def test_load():
    """Test load function"""

    result = load(PEOPLE_FILE)

    assert len(result) == 2
    assert result[0][0] == 'J'
