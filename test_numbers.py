from velgix import numbers


def test_tva_valide():
    assert numbers.tva_valide("BE0411905847") is True
    assert numbers.tva_valide("BE0428759497") is True
    assert numbers.tva_valide("BE 0411.905.847") is True


def test_tva_invalide():
    assert numbers.tva_valide("BE1234567890") is False
    assert numbers.tva_valide("BE0403038617") is False
    assert numbers.tva_valide("") is False


def test_niss_format():
    # Juste verifier que ca tourne sans erreur
    result = numbers.niss_valide("85031512345")
    assert isinstance(result, bool)
