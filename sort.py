def sort_dictionary(dict):
    listOfItems = list(dict.items())
    def sortAge(e):
        return e[1][1]
    listOfItems.sort(key=sortAge)
    result = []
    for i in listOfItems:
        tup = (i[0], i[1][0])
        result.append(tup)
    return result

