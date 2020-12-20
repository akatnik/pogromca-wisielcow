from utils import *

def assertEquals(value, expectedValue):
    if (value == expectedValue):
        print('OK')
    else:
        print('ERROR')


print('Testujemy funkcję isMatching')
assertEquals(isMatching('....', 'pies'), True)
assertEquals(isMatching('..e.', 'okno'), False)
assertEquals(isMatching('..e.', 'okeo'), True)
assertEquals(isMatching('..x.y', 'okxoy'), True)
assertEquals(isMatching('..x.yz', 'okxoyf'), False)

print('Testujemy funkcję doesntContain')
assertEquals(doesntContain('kot', 'b'), True)
assertEquals(doesntContain('kot', 'bo'), False)
assertEquals(doesntContain('kot', 'ot'), False)
assertEquals(doesntContain('kot', 'ab'), True)


print('Testujemy funkcję isLetterInWord')
assertEquals(isLetterInWord('k', 'kot'), True)
assertEquals(isLetterInWord('o', 'kot'), True)
assertEquals(isLetterInWord('t', 'kot'), True)
assertEquals(isLetterInWord('x', 'kot'), False)

print('Testujemy funkcję showLetterInWord')
assertEquals(showLetterInWord('....', 'pies', 'e'), '..e.')
assertEquals(showLetterInWord('..e.', 'pies', 's'), '..es')
assertEquals(showLetterInWord('..es', 'pies', 'e'), '..es')
assertEquals(showLetterInWord('..es', 'pies', 'p'), 'p.es')
assertEquals(showLetterInWord('p.es', 'pies', 'a'), 'p.es')
assertEquals(showLetterInWord('p.es', 'pies', 'i'), 'pies')
