import math


def coco(piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2
        val2 = 0
        for val in piles:
            val2 += math.ceil(val / k)
        print(k)
        if val2 > h:
            l = k + 1
        elif val2 <= h:
            r = k - 1
            res = k
        else:
            return k

    return res


piles = [1,1,1,999999999]
h = 10
print(coco(piles, h))
