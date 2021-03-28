from .block import Block


def getHash(vote, prev='6dd24e2f5bbd2c34edc78e6075d3dca41a9a8930679c7adb7fd1f36826956cdf'):
    vote1 = 0
    vote2 = 0
    vote3 = 0
    vote4 = 0
    vote5 = 0
    vote6 = 0
    if vote == 1:
        vote1 += 1
    elif vote == 2:
        vote2 = vote2 + 1
    elif vote == 3:
        vote3 = vote3 + 1
    elif vote == 4:
        vote4 = vote4 + 1
    elif vote == 5:
        vote5 = vote5 + 1
    elif vote == 6:
        vote6 = vote6 + 1
    str1 = str(vote1)
    str2 = str(vote2)
    str3 = str(vote3)
    str4 = str(vote4)
    str5 = str(vote5)
    str6 = str(vote6)

    final_str = str1 + "," + str2 + "," + str3 + "," + str4 + "," + str5 + "," + str6
    x = Block(prev, final_str)
    return [x.block_hash, x.transactions]


def getArr(string):
    string = string[2:-2]
    res = []
    for i in string:
        if not i == ',':
            res.append(int(i))
    return res


def addSum(arr):
    res = [0, 0, 0, 0, 0, 0]
    for i in arr:
        for j in range(6):
            res[j] += i[j]
    return res


def calculate(obj):
    arr = []
    for i in obj:
        arr.append(getArr(i.trans))
    return addSum(arr)
