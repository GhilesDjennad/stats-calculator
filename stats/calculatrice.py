def moyenne(nombres):
    if not nombres:
        raise ValueError("La liste est vide")
    return sum(nombres) / len(nombres)