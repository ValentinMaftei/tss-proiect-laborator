# Proiect Laborator TSS

### Specificații program

Metoda `calculate_bonus` din clasa `BonusCalculator` calculează bonusul salarial pe baza salariului, experienței și performanței angajatului.
#### `calculate_bonus(salariu: float, experienta: int, performanta: int)`

#### Date de intrare:
- `salariu`: salariul angajatului
- `experienta`: numărul de ani de experiență ai angajatului
- `performanta`: scorul de performanță al angajatului

#### Restricții:
- `salariu` număr întreg pozitiv
- `experienta` număr întreg pozitiv
- `performanta` număr întreg între 0 și 100

#### Reguli de calcul:
- Se verifică datele de intrare, iar dacă oricare dintre ele nu respectă restricțiile, se returnează `INVALID`
- Procentul de bază pentru bonus este 5%.
- Dacă `experienta` este mai mare de 3 ani, se adaugă 3 procente pentru fiecare an.
- Dacă `performanta` este mai mare de 90, se adaugă 15 procente.
- Dacă `performanta` este între 75 și 90, se adaugă 10 procente.
- Bonusul nu poate depăși 30% din salariu.
- Dacă `performanta` este mai mică de 50, bonusul este 0.
- Bonus final = `(salariu * procent_bonus) / 100` 

### 1. Generarea datelor de test
#### a) Equivalence Partitioning

Indentificarea claselor de echivalență pentru fiecare parametru de intrare:

| Variabilă     | Partiție de echivalență | Reprezentant | Tip     | Descriere               |
|---------------|-------------------------|--------------|---------|-------------------------|
| `salariu`     | EP_S1                   | 5000         | Valid   | salariu > 0             |
|               | EP_S2                   | 0            | Invalid | salariu <= 0            |
| `experienta`  | EP_E1                   | 4            | Valid   | experienta > 0          |
|               | EP_E2                   | -1           | Invalid | experienta <= 0         |
| `performanta` | EP_PF1                  | 45           | Valid   | 0 <= performanta < 50   |
|               | EP_PF2                  | 65           | Valid   | 50 <= performanta <= 70 |
|               | EP_PF3                  | 80           | Valid   | 71 <= performanta < 90  |
|               | EP_PF4                  | 95           | Valid   | performanta >= 90       |
|               | EP_PF5                  | -10          | Invalid | performanta < 0         |
|               | EP_PF6                  | 110          | Invalid | performanta > 100       |

Construirea cazurilor de testare pe baza claselor de echivalență:

| Caz de test | `salariu` | `experienta` | `performanta` | Rezultat așteptat | Descriere            |
|-------------|-----------|--------------|---------------|-------------------|----------------------|
| T1          | 5000      | 4            | 95            | 1500.0            | Valid                |
| T2          | 5000      | 5            | 95            | 1500.0            | Valid                |
| T3          | 5000      | 3            | 95            | 1450.0            | Valid                |
| T4          | 5000      | 4            | 80            | 1350.0            | Valid                |
| T5          | 5000      | 4            | 65            | 850.0             | Valid                |
| T6          | 5000      | 4            | 45            | 0.0               | Valid                |
| T7          | 0         | 4            | 95            | INVALID           | Salariu invalid      |
| T8          | 5000      | -1           | 95            | INVALID           | Experiență invalidă  |
| T9          | 5000      | 4            | -10           | INVALID           | Performanță invalidă |
| T10         | 5000      | 4            | 110           | INVALID           | Performanță invalidă |
| T11         | 0         | -1           | -10           | INVALID           | Valori invalide      |
| T12         | 0         | 0            | 110           | INVALID           | Valori invalide      |


Rularea testelor folosind pytest
```commandline
.venv\Scripts\activate
pytest -v tests/bonus_calculator_ep_tests.py
```

#### b) Boundary Value Analysis (BVA)
Identificarea valorilor limită pentru fiecare parametru de intrare

| Parametru       | Prag                   | Sub limită   | Peste limită         |
|-----------------|------------------------|--------------|----------------------|
| `salariu`       | 0 (invalid)            | -1 (invalid) | 1 (valid)            |
| `experienta`    | 0 (valid)              | -1 (invalid) | 1 (valid)            |
| `experienta`    | 3 (prag bonus vechime) | 2 (valid)    | 4 (valid)            |
| `performanta`   | 0 (valid)              | -1 (invalid) | 1 (valid)            |
| `performanta`   | 50 (prag bonus)        | 49 (valid)   | 51 (valid)           |
| `performanta`   | 70 (prag bonus)        | 69 (valid)   | 71 (valid)           |
| `performanta`   | 90 (prag bonus)        | 89 (valid)   | 91 (valid)           |
| `performanta`   | 100 (max valid)        | 99 (valid)   | 101 (invalid)        |
| `procent_bonus` | 30% (plafon)           | 29% (valid)  | 31% (plafon aplicat) |

Construirea cazurilor de testare pe baza valorilor limită:

| Caz de test | `salariu` | `experienta` | `performanta` | Rezultat așteptat |
|-------------|-----------|--------------|---------------|-------------------|
| BVA_T1      | -1        | 4            | 80            | INVALID           |
| BVA_T2      | 0         | 4            | 80            | INVALID           |
| BVA_T3      | 1         | 4            | 80            | 0.27              |
| BVA_T4      | 5000      | -1           | 80            | INVALID           |
| BVA_T5      | 5000      | 0            | 80            | 750.0             |
| BVA_T6      | 5000      | 1            | 80            | 750.0             |
| BVA_T7      | 5000      | 3            | 80            | 1200.0            |
| BVA_T8      | 5000      | 4            | 80            | 1350.0            |
| BVA_T9      | 5000      | 4            | -1            | INVALID           |
| BVA_T10     | 5000      | 4            | 0             | 0.0               |
| BVA_T11     | 5000      | 3            | 50            | 700.0             |
| BVA_T12     | 5000      | 3            | 49            | 0.0               |
| BVA_T13     | 5000      | 3            | 51            | 700.0             |
| BVA_T14     | 5000      | 3            | 70            | 1200.0            |
| BVA_T15     | 5000      | 3            | 69            | 700.0             |
| BVA_T16     | 5000      | 3            | 71            | 1200.0            |
| BVA_T17     | 5000      | 4            | 90            | 1500.0            |
| BVA_T18     | 5000      | 4            | 89            | 1350.0            |
| BVA_T19     | 5000      | 4            | 91            | 1500.0            |
| BVA_T20     | 5000      | 4            | 101           | INVALID           |

```commandline
.venv\Scripts\activate
pytest -v tests/bonus_calculator_bva_tests.py
```