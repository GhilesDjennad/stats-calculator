def moyenne(nombres):
    if not nombres:
        raise ValueError("La liste est vide")
    return sum(nombres) / len(nombres)


def maximum(nombres):
    if not nombres:
        raise ValueError("La liste est vide")
    return max(nombres)


def filtrer_positifs(nombres):
    if not nombres:
        return []
    nombres_positifs = []
    for nombre in nombres:
        if nombre > 0:
            nombres_positifs.append(nombre)
    return nombres_positifs
    