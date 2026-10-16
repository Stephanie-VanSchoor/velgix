"""
Verification de numeros belges : TVA et NISS.
"""

import re


def _nettoyer(numero: str) -> str:
    numero = re.sub(r"[\s\.\-/]", "", numero).upper()
    if numero.startswith("BE"):
        numero = numero[2:]
    if numero.startswith("(0)"):
        numero = "0" + numero[3:]
    if len(numero) == 9:
        numero = "0" + numero
    return numero


def tva_valide(numero: str) -> bool:
    numero = _nettoyer(numero)
    if not numero.isdigit() or len(numero) != 10:
        return False
    if int(numero) <= 0:
        return False
    if numero[0] not in "01":
        return False
    return (int(numero[:-2]) + int(numero[-2:])) % 97 == 0


def niss_valide(numero: str) -> bool:
    numero = _nettoyer(numero)
    if not numero.isdigit() or len(numero) != 11:
        return False
    base = int(numero[:9])
    checksum = int(numero[9:11])
    return (97 - (base % 97)) == checksum or (base % 97) == checksum
