from bonus_calculator import BonusCalculator

def test_mcdc_1():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=80) == 1350.0

def test_mcdc_2():
    assert BonusCalculator.calculate_bonus(salariu=0, experienta=4, performanta=80) == "INVALID"

def test_mcdc_3():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=-1, performanta=80) == "INVALID"

def test_mcdc_4():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=0) == "INVALID"

def test_mcdc_5():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=110) == "INVALID"

def test_mcdc_6():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=40) == 0.0

def test_mcdc_7():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=5, performanta=95) == 1500.0