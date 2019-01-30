from itertools import combinations
def maxDistance(a,b):
    list1 = list(a.split(","))
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    lenght = len(list1)
    i = 1
    j = 0
    total = 0
    while i<lenght:
        subset = list(combinations(list1,i))
        while j<len(subset):
            if sum(subset[j])<=b and total<sum(subset[j]):
                total = sum(subset[j])
            j=j+1
        i=i+1
    print("Το μεγαλύτερο άθροισμα των ακεραίων της λίστας που είναι μικρότερο ή ισό με το "+ str(b) +" είναι το "+str(total))
c = input("Εισάγεται μια λίστα σε μορφή α,β,γ,...:")
d = int(input("Εισάγεται έναν ακέραιο θετικό αριθμο:"))
maxDistance(c,d)
