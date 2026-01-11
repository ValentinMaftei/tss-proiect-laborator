import pytest
from bonus_calculator import BonusCalculator

def test_t1():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=95) == 1500.0

def test_t2():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=5, performanta=95) == 1500.0

def test_t3():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=3, performanta=95) == 1450.0

def test_t4():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=80) == 1350.0

def test_t5():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=65) == 850.0

def test_t6():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=45) == 0.0

def test_t7():
    assert BonusCalculator.calculate_bonus(salariu=0, experienta=4, performanta=95) == "INVALID"

def test_t8():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=-1, performanta=95) == "INVALID"

def test_t9():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=-10) == "INVALID"

def test_t10():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=110) == "INVALID"

def test_t11():
    assert BonusCalculator.calculate_bonus(salariu=0, experienta=-1, performanta=-10) == "INVALID"

def test_t12():
    assert BonusCalculator.calculate_bonus(salariu=0, experienta=0, performanta=110) == "INVALID"