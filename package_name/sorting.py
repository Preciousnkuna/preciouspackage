def bubble_sort(items):
    result = items.copy() # in place protection on items
    for i in range(len(result)):
        for j in range(len(result)-1-i):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]     # Swap!

    return result

def merge(a, b):
    list1 = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            list1.append(a[0])
            a.pop(0)
        else:
            list1.append(b[0])
            b.pop(0)

    if len(a) == 0:
        list1 = list1+ b
    if len(b) == 0:
        list1 = list1 + a

    return list1


def merge_sort(items):

    len_item= len(items)
    if len_item== 1:
        return items

    midnumber = int(len_item / 2)
    item1 = merge_sort(items[:midnumber])
    item2 = merge_sort(items[midnumber:])

    return merge(item1, item2)

def quick_sort(items, index=-1):
    len_item = len(items)

    if len_item <= 1:

        return items

    centre = items[index]
    small = []
    big = []
    pul = []
    for i in items:
        if i < centre:
            small.append(i)
        elif i > centre:
            big.append(i)
        elif i == centre:
            pul.append(i)

    small = quick_sort(small)
    big = quick_sort(big)

    return small + pul + big
