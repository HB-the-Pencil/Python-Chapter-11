import pytest

from barcalow_tiy_11_3_employee import Employee

def test_give_default_raise():
    employee = Employee("John", "Doe", 145000)
    employee.give_raise()

    assert employee.salary == 150000

def test_give_custom_raise():
    employee = Employee("John", "Doe", 120000)
    employee.give_raise(30000)

    assert employee.salary == 150000


# Fixture tests
@pytest.fixture
def default_employee():
    employee = Employee("John", "Doe", 120000)
    return employee


def test_give_default_raise_w_fixture(default_employee):
    default_employee.give_raise()

    assert default_employee.salary == 125000


def test_give_custom_raise_w_fixture(default_employee):
    default_employee.give_raise(30000)

    assert default_employee.salary == 150000