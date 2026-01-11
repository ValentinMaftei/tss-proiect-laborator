class BonusCalculator:

    @staticmethod
    def calculate_bonus(salariu: int, experienta: int, performanta: int) -> float | str:

        # Validare input
        if salariu <= 0 or experienta < 0 or not (0 <= performanta <= 100):
            return "INVALID"

        # Bonus initial
        procent_bonus = 5

        # Bonus pe vechime
        if experienta >= 3:
            procent_bonus += 3 * experienta

        # Bonus pe performanta
        if performanta >= 90:
            procent_bonus += 15
        elif 70 <= performanta < 90:
            procent_bonus += 10
        elif performanta < 50:
            procent_bonus = 0

        if procent_bonus > 30:
            procent_bonus = 30

        bonus_total = (salariu * procent_bonus) / 100

        return round(bonus_total, 2)