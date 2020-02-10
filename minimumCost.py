def findMinCost(N,costOfIndiviual):
    noOfPeople = N
    costOfPerson = costOfIndiviual
    minCost = 0
    if noOfPeople == 1:
        minCost += costOfPerson[0]
        return minCost
    elif noOfPeople == 2:
        minCost += max(costOfPerson)
        return minCost
    elif noOfPeople == 3:
        for i in costOfPerson:
            minCost += i
        return minCost
    else:
        tempStore=[]
        finish1 = 0
        maxm = 0
        for t in range (0,noOfPeople):
            tempStore.append(0)
        for i in range(0, 2):
            tempStore[0] = 1
            finish1 += 1
            count = 1
            for j in range((noOfPeople - 1), 0):
                if count < 2:
                    if tempStore[j] == 0:

                        tempStore[j] = 1
                        finish1 += 1
                        if count == 1:
                            maxm = j
                        count += 1
            minCost += costOfPerson[maxm]
            if finish1 == noOfPeople:
                break
            else:
                tempStore[0] = 0
                finish1 -= 1
                minCost += costOfPerson[0]
            return minCost
people = int(input("Enter no of people:"))#1st User Input
if people == 0:#primary validation
    print("No. of people can't be '0'.Please enter correct user input")
    exit()
cost = list(map(int,input("Enter the respective costs:").split(' ')))#2nd User Input
if len(cost) != people:
    print("Cost value is not matching with no. of people. Please enter correct input")
    exit()
print(findMinCost(people,cost))