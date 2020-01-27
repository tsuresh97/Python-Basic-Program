print("Welcome to Election App....!")
nominee=int(input("Please type the number of nominee: "))
nomineeList=[]
voteList=[]
dup=0
def result():
    checkPassword=input("Please enter your password to show result: ")
    if checkPassword==password:
        print("The Result is")
        for j in range(nominee):
            print((nomineeList[j],(voteList[j])))
    else:
        result()

for i in range(0,nominee):
    name=input("Please enter nominee name: ")
    nomineeList.append(name)
    voteList.append(0)

print("Press", (nominee+1), "to show result")
password = input("Please set password: ")
print("The nominees are ",(nomineeList))

maximumNumberOfVoters=int(input("Please enter maximum number of voters: "))
for i in range(0,maximumNumberOfVoters,1):
    if i==maximumNumberOfVoters:
        break
    for j in range(nominee): 
        print(j,(nomineeList[j]))
    voteNumber=int(input("Please pool your vote by number: "))
    if voteNumber== nominee + 1:
        i=i-1
        result()
    if voteNumber>=0 and voteNumber<nominee:
        voteList[voteNumber]=voteList[voteNumber]+1
    else:
        print("Invalid Vote")
        dup=dup+1
result()


