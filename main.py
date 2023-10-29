#2
def func(*numbers):
    positive = []
    negative = []

    for number in numbers:
        if number >= 0:
            positive.append(number)
        else:
            negative.append(number)

    resultPositive = sorted(positive)
    resultNegative = list(reversed(sorted(negative)))

    return resultNegative, resultPositive

print(func(9, 10, 11, -2, 3, 4, -90, -12, 23, 0, -10, 2, 3, 4, 0, 0, -12))

#3
c = int(input('c: '))
i = int(input('i: '))
g = int(input('g: '))
ex = int(input('ex: '))
im = int(input('im: '))

inputDict = {'c': c, 'i': i, 'g': g, 'ex': ex, 'im': im}
inputList = [c, i, g, ex, im]

def gdp(c, i, g, ex, im):
    gdp = c + i + g + (ex - im)
    return f'gdp - {gdp}'

print(gdp(**inputDict))
print(gdp(*inputList))

#4
lst = [{1: {1: 'м', 2: None, 3: None, 4: 'ж'}, 
       2: {5: 'м', 6: None, 7: None, 8: 'ж'}, 
       3: {9: 'ж', 10: None, 11: 'ж', 12: None},
       4: {13: 'м', 14: None, 15: None, 16: 'ж'},
       5: {17: None, 18: None, 19: None, 20: None},
       6: {21: 'м', 22: 'м', 23: 'м', 24: None}}]

def train(*args):
    emptyCoupes = []
    emptySeats = []
    emptyLow = []
    emptyHigh = []
    emptyMens = []
    emptyWomens = []

    for train in args:
        for coupes in train:
            for coupe in coupes:
                for seat in coupes[coupe]:
                    if coupes[coupe][seat] == None:
                        if seat % 2 == 0:
                            emptyHigh.append(seat)
                        else:
                            emptyLow.append(seat)

                if len(set(list(coupes[coupe].values()))) == 2:
                    if None in list(coupes[coupe].values()) and 'м' in list(coupes[coupe].values()) and 'ж' not in list(coupes[coupe].values()):
                        emptyMens.append(coupe)
                    elif None in list(coupes[coupe].values()) and 'ж' in list(coupes[coupe].values()) and 'м' not in list(coupes[coupe].values()):
                        emptyWomens.append(coupe)

                if len(set(list(coupes[coupe].values()))) == 1:
                    if None in list(coupes[coupe].values()):
                        emptyCoupes.append(coupe)

                lst1 = [seat for seat in coupes[coupe] if coupes[coupe][seat] == None]
                for seat in lst1:
                    emptySeats.append(seat)

    return f"full empty coupes - {emptyCoupes}\nempty seats - {emptySeats}\nempty low seats - {emptyLow}\nempty high seats - {emptyHigh}\nempty men's coupes - {emptyMens}\nempty women's coupes - {emptyWomens}"

print(train(lst))