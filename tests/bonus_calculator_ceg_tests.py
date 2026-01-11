from bonus_calculator import BonusCalculator

def test_ceg_1():
    assert BonusCalculator.calculate_bonus(salariu=0, experienta=4, performanta=80) == "INVALID"

def test_ceg_2():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=-1, performanta=80) == "INVALID"

def test_ceg_3():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=-10) == "INVALID"

def test_ceg_4():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=2, performanta=45) == 0

def test_ceg_5():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=2, performanta=65) == 750.0

def test_ceg_6():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=3, performanta=80) == 1200.0

def test_ceg_7():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=95) == 1500.0