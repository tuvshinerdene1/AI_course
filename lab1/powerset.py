def power_set(lst):
    result = []
    first = []
    result.append(first)
    for x in lst:
        new_subsets = []
        for subset in result:
            new_subset = subset + [x]
            new_subsets.append(new_subset)
        result.extend(new_subsets)
    return result
def test(got, expected):
    if hasattr(expected, '__call__'):
        ok = expected(got)
    else:
        ok = (got == expected)
    prefix = ' OK ' if ok else '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))



def main():
    print('power_set')
    test(power_set([]), [[]])
    test(power_set([1]), [[], [1]])
    test(sorted(power_set([1, 2])), sorted([[], [2], [1], [1, 2]]))
    test(sorted(power_set([1, 2, 3])),
         sorted([[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]))
    test(power_set([1, 2, 3, 4]),
         [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], [1, 3], [1, 3, 4],
          [1, 4], [2], [2, 3], [2, 3, 4], [2, 4], [3], [3, 4], [4]])
    test(power_set([2, 2]), [[], [2], [2], [2, 2]])

    toppings = ['onion', 'peppers', 'bacon', 'sausage', 'mushroom']
    test(power_set(toppings),
         [[], ['bacon'], ['bacon', 'mushroom'], ['bacon', 'sausage'],
          ['bacon', 'sausage', 'mushroom'], ['mushroom'], ['onion'],
          ['onion', 'bacon'], ['onion', 'bacon', 'mushroom'],
          ['onion', 'bacon', 'sausage'], ['onion', 'bacon', 'sausage', 'mushroom'],
          ['onion', 'mushroom'], ['onion', 'peppers'],
          ['onion', 'peppers', 'bacon'], ['onion', 'peppers', 'bacon', 'mushroom'],
          ['onion', 'peppers', 'bacon', 'sausage'],
          ['onion', 'peppers', 'bacon', 'sausage', 'mushroom'],
          ['onion', 'peppers', 'mushroom'], ['onion', 'peppers', 'sausage'],
          ['onion', 'peppers', 'sausage', 'mushroom'], ['onion', 'sausage'],
          ['onion', 'sausage', 'mushroom'], ['peppers'], ['peppers', 'bacon'],
          ['peppers', 'bacon', 'mushroom'], ['peppers', 'bacon', 'sausage'],
          ['peppers', 'bacon', 'sausage', 'mushroom'], ['peppers', 'mushroom'],
          ['peppers', 'sausage'], ['peppers', 'sausage', 'mushroom'], ['sausage'],
          ['sausage', 'mushroom']])