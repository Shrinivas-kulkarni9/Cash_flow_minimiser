#This is a python implementation, which minimises the flow of cash, or number of transactions required to make a group of friends, who owe money to each other, 
#to make everyone even.
#It is a greedy algorithm, and takes O(n2) time, where n is the number of friends. This algorithm is independant of the number of debts within the group.

def min_max_creditor(credit):
    Min = ''
    Max = ''
    maxi,mini = 0,0
    for key in credit:
        if credit[key] >= maxi:
            maxi = credit[key]
            Max = key
        if mini >= credit[key]:
            mini = credit[key]
            Min = key
    return Min,Max

if __name__ == "__main__":
    print('please write the number of transactions and then write each one as - debtor amount creditor')
    n = int(input())
    credit = dict()
    for i in range(n):
        l = input().split()
        amt = int(l[1])
        if l[0] not in credit:
            credit[l[0]] = -1*(amt)
        else:
            credit[l[0]]-=amt
        if l[2] not in credit:
            credit[l[2]] = (amt)
        else:
            credit[l[2]]+=amt
    print('The minimal cash flow is...')
    while len(credit)>1:
        a,b = min_max_creditor(credit)
        credit[b]+=credit[a]
        print(a, end = ' ')
        print(" will have to pay",end=" ")
        print(-credit[a],end=" ")
        print('to',end=" ")
        print(b)
        del credit[a]
