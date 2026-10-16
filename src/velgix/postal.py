"""
Codes postaux belges.
"""

from typing import List, Optional


# Quelques villes principales (on completera plus tard)
CODES_POSTAUX = {
    "1000": "Bruxelles",
    "1020": "Laeken",
    "1030": "Schaerbeek",
    "1040": "Etterbeek",
    "1050": "Ixelles",
    "1060": "Saint-Gilles",
    "1070": "Anderlecht",
    "1080": "Molenbeek-Saint-Jean",
    "1090": "Jette",
    "2000": "Anvers",
    "3000": "Louvain",
    "4000": "Liege",
    "5000": "Namur",
    "6000": "Charleroi",
    "7000": "Mons",
    "8000": "Bruges",
    "9000": "Gand",
}


def valide(code: str) -> bool:
    """
    Verifie si un code postal belge est valide (4 chiffres).

    Exemple:
        >>> valide("1000")
        True
        >>> valide("99")
        False
    """
    return code.isdigit() and len(code) == 4


def ville(code: str) -> Optional[str]:
    """
    Retourne le nom de la ville pour un code postal.

    Exemple:
        >>> ville("1000")
        'Bruxelles'
    """
    if not valide(code):
        return None
    return CODES_POSTAUX.get(code)


def codes(nom_ville: str) -> List[str]:
    """
    Retourne la liste des codes postaux d'une ville.

    Exemple:
        >>> codes("Bruxelles")
        ['1000']
    """
    nom = nom_ville.strip().lower()
    return [code for code, v in CODES_POSTAUX.items() if v.lower() == nom]


def province(code: str) -> Optional[str]:
    """
    Retourne la province belge a partir du code postal.

    Exemple:
        >>> province("1000")
        'Bruxelles-Capitale'
    """
    if not valide(code):
        return None

    prefixe = int(code[:2])

    if 10 <= prefixe <= 12:
        return "Bruxelles-Capitale"
    elif 13 <= prefixe <= 14:
        return "Brabant wallon"
    elif 15 <= prefixe <= 19:
        return "Brabant flamand"
    elif 20 <= prefixe <= 29:
        return "Anvers"
    elif 30 <= prefixe <= 39:
        return "Brabant flamand / Limbourg"
    elif 40 <= prefixe <= 49:
        return "Liege"
    elif 50 <= prefixe <= 59:
        return "Namur"
    elif 60 <= prefixe <= 79:
        return "Hainaut"
    elif 80 <= prefixe <= 89:
        return "Flandre-Occidentale"
    elif 90 <= prefixe <= 99:
        return "Flandre-Orientale"
    return None
