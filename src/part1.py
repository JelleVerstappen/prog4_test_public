def volume_kubus(x):
    """Return the volume of a cube

    Raise a RuntimeError exception with message "negatieve lengte" if x < 0.
    """
    vol = x **3
    if x < 0:
        raise RuntimeError("negatieve lengte")
    return vol


class NegativeDuration(RuntimeError):
    pass
def minutes_in_day(x):
    """Return the number of minutes in x days

    Raise a custom NegativeDuration exception if x < 0.
    """
    min = x * 1440
    if x < 0:
        raise NegativeDuration 
    return min


def minutes_in_week(x):
    """Return the number of minutes in x weeks"""
    min = x * 1440 * 7
    return min


def list_of_squares(n):
    """Return a list of the first n squares

    >>> list_of_squares(3)
    [0, 1, 4]
    """
    l = []
    for i in range (0, n):
        sq = i **2
        l.append(sq)
    return l 


def product_of_list(l):
    """Return the product of all numbers in the list

    >>> product_of_list([2,3,4])
    24
    """
    product = 1
    for i in range(0, len(l)):
        product = product * l[0+i]
    return product


def price_search(articles, name):
    """Return the price of the article in list articles

    >>> articles = [
        ["Doom", 25],
        ["Among Us", 5],
    ]
    >>> price_search("Doom")
    25
    """
    for sublist in articles:
        if sublist[0] == name:
            return sublist[1]
    return None
