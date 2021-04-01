# kattapa, as you all know was one of the greatest warriors of his time. the kingdom of maahishmati had never lost a battle under him (as army-chief), and the reason for that was their really powerful army, also called as mahasena.
#
# kattapa was known to be a very superstitious person. he believed that a soldier is "lucky" if the soldier is holding an even number of weapons, and "unlucky" otherwise. he considered the army as "ready for battle" if the count of "lucky" soldiers is strictly greater than the count of "unlucky" soldiers, and "not ready" otherwise.
#
# given the number of weapons each soldier is holding, your task is to determine whether the army formed by all these soldiers is "ready for battle" or "not ready".
#
# note: you can find the definition of an even number here.
#
# input
# the first line of input consists of a single integer n denoting the number of soldiers. the second line of input consists of n space separated integers a1, a2, ..., an, where ai denotes the number of weapons that the ith soldier is holding.
#
# output
# generate one line output saying "ready for battle", if the army satisfies the conditions that kattapa requires or "not ready" otherwise (quotes for clarity).
#
# constraints
# 1 ≤ n ≤ 100
# 1 ≤ ai ≤ 100

n = int(input())
arr = map(int,input().split())[:n]
x = 0
y = 0
for i in range(0,n):
    if arr[i]%2==0:
        x += 1
    else:
        y += 1
if x > y:
    print("READY FOR BATTLE")
else:
    print("NOT READY")










