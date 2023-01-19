import pytest

from dundie.core import read
from dundie.database import add_person, commit, connect


@pytest.mark.unit
def test_read_with_query():

    pk = "joe@doe.com"
    data = {"role": "Salesman", "dept": "Sales", "name": "Joe Doe"}
    db = connect()
    _, created = add_person(db, pk, data)
    assert created

    pk = "jim@doe.com"
    data = {"role": "Salesman", "dept": "Mangement", "name": "Jim Doe"}
    _, created = add_person(db, pk, data)
    assert created
    commit(db)

    response = read()
    assert len(response) == 2

    response = read(dept="Mangement")
    assert len(response) == 1
    assert response[0]["name"] == "Jim Doe"

    response = read(email="joe@doe.com")
    assert len(response) == 1
    assert response[0]["email"] == "joe@doe.com"
