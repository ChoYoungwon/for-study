count = 0
count2 = 0
count3 = 0

def knapSack_bnb(obj, W, level, weight, profit, maxProfit, node):
    global count
    if (level == len(obj)):
        return maxProfit

    if weight + obj[level][0] <= W:
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]
        newNode = node + [obj[level][2]]

        if newProfit > maxProfit:
            maxProfit = newProfit

        newBound = bound(obj, W, level, newWeight, newProfit)
        if newBound >= maxProfit:
            count += 1
            # print("count : ", count)
            # print("Node: ", newNode)
            # print("Weight: ", newWeight)
            # print("Profit: ", newProfit)
            # print("MaxProfit: ", maxProfit)
            # print("----")
            maxProfit = knapSack_bnb(obj, W, level+1, newWeight, newProfit, maxProfit, newNode)

    newNode = node[:]
    newWeight = weight
    newProfit = profit
    newBound = bound(obj, W, level, newWeight, newProfit)
    if newBound >= maxProfit:
        count += 1
        # print("count : ", count)
        # print("Node: ", newNode)
        # print("Weight: ", newWeight)
        # print("Profit: ", newProfit)
        # print("MaxProfit: ", maxProfit)
        # print("----")
        maxProfit = knapSack_bnb(obj, W, level+1, newWeight, newProfit, maxProfit, newNode)

    return maxProfit

def bound(obj, W, level, weight, profit):
    if weight > W:
        return 0

    pBound = profit
    for j in range(level+1, len(obj)):
        pBound += obj[j][1]

    return pBound

def knapSack_bnb2(obj, W, level, weight, profit, maxProfit, node):
    global count2
    if (level == len(obj)):
        return maxProfit

    if weight + obj[level][0] <= W:
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]
        newNode = node + [obj[level][2]]

        if newProfit > maxProfit:
            maxProfit = newProfit

        newBound = bound2(obj, W, level, newWeight, newProfit)
        if newBound >= maxProfit:
            count2 += 1
            # print("count2 : ", count2)
            # print("Node: ", newNode)
            # print("Weight: ", newWeight)
            # print("Profit: ", newProfit)
            # print("MaxProfit: ", maxProfit)
            # print("----")
            maxProfit = knapSack_bnb2(obj, W, level+1, newWeight, newProfit, maxProfit, newNode)

    newNode = node[:]
    newWeight = weight
    newProfit = profit
    newBound = bound2(obj, W, level, newWeight, newProfit)
    if newBound >= maxProfit:
        count2 += 1
        # print("count2 : ", count2)
        # print("Node: ", newNode)
        # print("Weight: ", newWeight)
        # print("Profit: ", newProfit)
        # print("MaxProfit: ", maxProfit)
        # print("----")
        maxProfit = knapSack_bnb2(obj, W, level+1, newWeight, newProfit, maxProfit, newNode)

    return maxProfit

def bound2(arr, W, level, weight, profit):

    if weight > W:
        return 0

    pBound = profit
    tWeight = weight

    j = level+1
    n = len(arr)
    while j < n and (tWeight+arr[j][0] <= W):
        tWeight += arr[j][0]
        pBound += arr[j][1]
        j += 1

    if (j < n):
        pBound += (W - tWeight) * (arr[j][1]/arr[j][0])

    return pBound

def knp(W, wt, val, n):
    global count3
    max_value = 0
    # 가능한 모든 항목 조합을 고려
    for i in range(2**n+1):
        value = 0
        weight = 0
        count3 += 1
        # print(count3)
        for j in range(n):

            # i의 j번째 비트가 1인 경우, 해당 항목을 배낭에 넣는다.
            if (i >> j) & 1:
                value += val[j]
                weight += wt[j]
        # 배낭의 용량을 초과하지 않는 경우, 최대 가치를 업데이트
        if weight <= W and value > max_value:
            max_value = value
    return max_value

obj = [(2.7, 60, "A"), (5.2, 100, "B"), (8.1, 190, "C"), (4.7, 120, "D"), (7.1, 200, "E"), (6.5, 150, "F")]
obj.sort(key=lambda e: e[1] / e[0], reverse = True)
wt = []
val = []
for i in range(len(obj)):
    wt.append(obj[i][0])
    val.append(obj[i][1])
n = len(val)
print(obj)
print("배낭채우기(분기 한정 기법) : ", knapSack_bnb(obj, 14, 0, 0, 0, 0, []))
print("분기 한정 기법 탐색 수 : ", count)
print()
print("배낭채우기(개선된 분기 한정 기법): ", knapSack_bnb2(obj, 14, 0, 0, 0, 0, []))
print("개선된 분기 한정 기법 탐색 수 : ", count2)
print()
print("배낭채우기문제(억지기법): ", knp(14, wt, val, n))
print("억지기법 탐색 수 : ", count3)