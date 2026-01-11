from bonus_calculator import BonusCalculator

def main() -> None:
    bonus = BonusCalculator.calculate_bonus(salariu=0, experienta=4, performanta=80)
    print(f"Bonus calculat: {bonus}")


if __name__ == "__main__":
    main()