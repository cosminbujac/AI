import math
import numpy


def ultimulCuvant(sentence):
    '''
    ex 1
    :param sentence - propozitia intiala
    :return: ultimul cuvant dpdv alfabetic
    Complexitate: O(nlogn)
    '''
    toSort = sentence.split(" ")
    toSort.sort()
    return toSort[len(toSort) - 1]


def testUltimCuvant():
    sentence1 = "Ana are mere rosii si galbene"
    assert (ultimulCuvant(sentence1) == "si")
    sentence2 = "abz azb zba baz bza"
    assert (ultimulCuvant(sentence2) == "zba")
    sentence3 = "prin vulturi vantul viu vuia"
    assert (ultimulCuvant(sentence3) == "vulturi")


def distanta(x1, y1, x2, y2):
    # ex 2
    '''
    Input:x1,y1 - Coordonatele primului punct
        x2,y2 - Coordonatele celui de al doilea punct
    Output: distanta euclidiana dintre 2 puncte p1(X1,Y1),p2(X2,Y2)
    Complexitate: Theta(1)
    '''
    return (math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))


def testDistanta():
    assert (distanta(1, 5, 4, 1) == 5.0)
    assert (distanta(-2, 2, 2, -1) == 5.0)
    assert (distanta(7, 4, -3, 5) == 10.04987562112089)


def produsScalar(v1, v2):
    """
    Ex 3
    :param v1 - primul vector
    :param v2 - al doilea vector
    :return: produsul scalar dintre cei doi vectori
    Complexitate : Theta(n)
    """
    return numpy.dot(v1, v2)


def testProdusScalar():
    assert (produsScalar([1, 0, 2, 0, 3], [1, 2, 0, 2, 1]) == 4)
    assert (produsScalar([1, 1, 1, 1], [1, 2, 3, 4]) == 10)
    assert (produsScalar([1, 2, 3, 4], [1, 2, 3, 4]) == 30)


def oneTimeWords(sentence):
    """
    Ex4
    :param sentence - The sentence with multiple words
    :return: List of  words that appear only once
    Complexity: Theta(n), n being the number of words
    """
    array = sentence.split(" ")
    checker = dict()
    for x in array:
        if x in checker.keys():
            checker[x] += 1
        else:
            checker[x] = 1
    res = list()
    for x in checker.keys():
        if checker[x] == 1:
            res.append(x)
    return res

'''
remote change test
add something fancy here
'''
def testOneTimeWords():
    assert (oneTimeWords("ana are ana are mere rosii ana") == ["mere", "rosii"])
    assert (oneTimeWords("a a a b c d a b c") == ["d"])
    assert (oneTimeWords("check check check mic check mic") == [])


def repetitie(array):
    # ex 5
    '''
    Input: o lista cu elemente de la 1 la n-1, de dimensiunea n
    Output: numarul ce se repeta de 2 ori in sirul primit cu numere de la 1 la n-1, n fiind lungimea
    Complexitate: Theta(n)
    '''
    n = len(array) - 1
    return (math.fsum(array) - (n * (n + 1) / 2))


def testRepetitie():
    array1 = [1, 2, 3, 4, 5, 6, 7, 3]
    assert (repetitie(array1) == 3)
    array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2]
    assert (repetitie(array2) == 2)
    array3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6]
    assert (repetitie(array3) == 6)
    array4 = [1, 2, 3, 4, 2]
    assert (repetitie(array4) == 2)


def main():
    testUltimCuvant()
    testDistanta()
    testProdusScalar()
    testOneTimeWords()
    testRepetitie()

main()
