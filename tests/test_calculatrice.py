from stats.calculatrice import moyenne, filtrer_positifs, maximum
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
    
@pytest.mark.parametrize("nombres, attendu", [
    ([1, 5, 8], 8),
    ([-5, -1, -3], -1),
])
def test_maximum_base(nombres, attendu):
    assert maximum(nombres) == attendu
    
def test_maximum_liste_vide():
    with pytest.raises(ValueError):
        maximum([])
        
def test_filtrer_positifs_liste_vide():
    assert filtrer_positifs([]) == []
    
def test_filtrer_positifs_base():
    assert filtrer_positifs([0, 4, -8, 2]) == [4, 2]
    
