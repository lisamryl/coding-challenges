"""How much rain is trapped in Codelandia?

No buildings mean no rain is captured::

    >>> rain([])
    0

All-same height buildings capture no rain::

    >>> rain([10])
    0

    >>> rain([10, 10])
    0

    >>> rain([10, 10, 10, 10])
    0

If there's nothing between taller buildings, no rain is captured::

    >>> rain([2, 3, 10])
    0

    >>> rain([10, 3, 2])
    0

If two tallest buildings are same height and on ends, it's easy::

    >>> rain([10, 5, 10])
    5

    >>> rain([10, 2, 3, 4, 10])
    21

    >>> rain([10, 4, 3, 2, 10])
    21

    >>> rain([10, 2, 4, 3, 10])
    21

If two tallest buildings are ends, but not the same height,
it will fall off the shorter of thh two::

    >>> rain([10, 2, 3, 4, 9])
    18

Rain falls off the left and right edges::

    >>> rain([2, 3, 10, 5, 5, 10, 3, 2])
    10

Trickier::

    >>> rain([2, 3, 5, 4, 3, 10, 7, 10, 5, 4, 3, 6, 2, 5, 2])
    15

Should also work with floats::

    >>> r = rain([4.5, 2.2, 2.2, 4])
    >>> round(r, 2)
    3.6
"""


def rain(buildings):
    area = 0
    i = 0
    j = 1
    start = 0
    end = None
    numbers = []
    while i < len(buildings) - 1:
        max_remaining = float(max(buildings[i + 1:]))
        while float(buildings[start]) > float(buildings[i]):
            i += 1
        start = i
        end = i + 1
        while float(buildings[end]) < min(float(buildings[start]), max_remaining):
            numbers.append(float(buildings[end]))
            end += 1
        min_height = float(min(float(buildings[end]), float(buildings[start])))
        for num in numbers:
            area += (min_height - num)
        #reset
        numbers = []
        start = end
        i = start
    if int(area) == area:
        return int(area)
    else:
        return area


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
