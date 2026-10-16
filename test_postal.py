from velgix import postal


def test_ville():
    assert postal.ville("1000") == "Bruxelles"
    assert postal.ville("9000") == "Gand"


def test_ville_inconnue():
    assert postal.ville("9999") is None
    assert postal.ville("abc") is None


def test_valide():
    assert postal.valide("1000") is True
    assert postal.valide("99") is False
    assert postal.valide("abcd") is False


def test_province():
    assert postal.province("1000") == "Bruxelles-Capitale"
    assert postal.province("8000") == "Flandre-Occidentale"


def test_codes():
    resultat = postal.codes("Bruxelles")
    assert "1000" in resultat
