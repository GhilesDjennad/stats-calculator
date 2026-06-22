from stats.calculatrice import moyenne
import pytest

@pytest.fixture
def nombres_positifs():
    return [10, 20, 30, 40]

@pytest.fixture
def nombres_mixtes():
    return [-10, 0, 10]

def test_moyenne_nombres_positifs(nombres_positifs):
    assert moyenne(nombres_positifs) == 25.0

def test_moyenne_nombres_mixtes(nombres_mixtes):
    assert moyenne(nombres_mixtes) == 0.0

@pytest.mark.parametrize("nombres, attendu", [
    ([2, 4, 6], 4.0),
    ([5], 5.0),
    ([1, 2, 3, 4], 2.5),
    ([-2, 2], 0.0),
])
def test_moyenne(nombres, attendu):
    assert moyenne(nombres) == attendu

def test_moyenne_liste_vide():
    with pytest.raises(ValueError):
        moyenne([])