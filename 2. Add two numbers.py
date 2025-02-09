
def addTwoNumbers(l1:list, l2:list):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    l2_new = []
    for x in range(0,len(l2),-1):
        l2_new.append(l2[x])
    l1_number = 0
    l2_number = 0

    for i in range(len(l1)):
        l1_number = l1_number + l1[i]*(10**(len(l1)-1-i))

    for j in range(len(l2_new)):
        l2_number = l2_number + l2_new[j]*(10**(len(l2_new)-1-j))

    print(l1_number+l2_number)

addTwoNumbers([2, 4, 3], [5, 6, 4])

