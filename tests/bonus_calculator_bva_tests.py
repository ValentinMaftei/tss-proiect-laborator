from bonus_calculator import BonusCalculator

def test_bva_1():
    assert BonusCalculator.calculate_bonus(salariu=-1, experienta=4, performanta=80) == "INVALID"

def test_bva_2():
    assert BonusCalculator.calculate_bonus(salariu=0, experienta=4, performanta=80) == "INVALID"

def test_bva_3():
    assert BonusCalculator.calculate_bonus(salariu=1, experienta=4, performanta=80) == 0.27

def test_bva_4():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=-1, performanta=80) == "INVALID"

def test_bva_5():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=0, performanta=80) == 750.0

def test_bva_6():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=1, performanta=80) == 750.0

def test_bva_7():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=3, performanta=80) == 1200.0

def test_bva_8():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=80) == 1350.0

def test_bva_9():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=-1) == "INVALID"

def test_bva_10():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=0) == "INVALID"

def test_bva_11():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=3, performanta=50) == 1200.0

def test_bva_12():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=3, performanta=49) == 0.0

def test_bva_13():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=3, performanta=51) == 1200.0

def test_bva_14():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=90) == 1500.0

def test_bva_15():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=89) == 1350.0

def test_bva_16():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=91) == 1500.0

def test_bva_17():
    assert BonusCalculator.calculate_bonus(salariu=5000, experienta=4, performanta=101) == "INVALID"