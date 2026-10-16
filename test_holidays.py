from datetime import date
from velgix import holidays


def test_paques_2026():
    assert holidays._paques(2026) == date(2026, 4, 5)


def test_paques_2024():
    assert holidays._paques(2024) == date(2024, 3, 31)


def test_nombre_feries():
    assert len(holidays.feries(2026)) == 10


def test_noel():
    assert holidays.feries(2026)["Noel".replace("Noel", "No\u00ebl")] == date(2026, 12, 25)


def test_est_ferie():
    assert holidays.est_ferie(date(2026, 7, 21)) is True
    assert holidays.est_ferie(date(2026, 7, 22)) is False
