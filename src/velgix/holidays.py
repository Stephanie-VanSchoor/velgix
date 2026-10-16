"""
Jours fériés belges.

Les 10 jours fériés légaux en Belgique :
    1. Nouvel An (1er janvier)
    2. Lundi de Pâques
    3. Fête du Travail (1er mai)
    4. Ascension
    5. Lundi de Pentecôte
    6. Fête Nationale (21 juillet)
    7. Assomption (15 août)
    8. Toussaint (1er novembre)
    9. Armistice (11 novembre)
   10. Noël (25 décembre)
"""

from datetime import date, timedelta
from typing import Dict, List


def _paques(annee: int) -> date:
    """
    Calcule la date du dimanche de Pâques pour une année donnée.
    Algorithme grégorien (Meeus/Jones/Butcher).
    """
    a = annee % 19
    b = annee // 100
    c = annee % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mois = (h + l - 7 * m + 114) // 31
    jour = ((h + l - 7 * m + 114) % 31) + 1
    return date(annee, mois, jour)


def feries(annee: int) -> Dict[str, date]:
    """
    Retourne un dictionnaire des jours fériés belges pour une année.

    Args:
        annee: L'année (ex: 2026)

    Returns:
        Dictionnaire {nom: date}

    Exemple:
        >>> feries(2026)["Noël"]
        datetime.date(2026, 12, 25)
    """
    paques = _paques(annee)

    return {
        "Nouvel An": date(annee, 1, 1),
        "Lundi de Pâques": paques + timedelta(days=1),
        "Fête du Travail": date(annee, 5, 1),
        "Ascension": paques + timedelta(days=39),
        "Lundi de Pentecôte": paques + timedelta(days=50),
        "Fête Nationale": date(annee, 7, 21),
        "Assomption": date(annee, 8, 15),
        "Toussaint": date(annee, 11, 1),
        "Armistice": date(annee, 11, 11),
        "Noël": date(annee, 12, 25),
    }


def liste_feries(annee: int) -> List[date]:
    """
    Retourne la liste triée des jours fériés belges pour une année.

    Exemple:
        >>> liste_feries(2026)[0]
        datetime.date(2026, 1, 1)
    """
    return sorted(feries(annee).values())


def est_ferie(jour: date) -> bool:
    """
    Vérifie si une date est un jour férié belge.

    Exemple:
        >>> est_ferie(date(2026, 7, 21))
        True
    """
    return jour in liste_feries(jour.year)