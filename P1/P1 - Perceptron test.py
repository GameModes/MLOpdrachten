input = 2
List = []
for numberamount in range(2):
    TSL = []
    TSL.append(numberamount)
    List.append(TSL)

if input > 1:
    for morelists in range(input-1):
        List = List + List
    print(List)
    for addmorenumbers in range(len(List[0:input])):
        print("first:" + str(List[addmorenumbers]))
        (List[addmorenumbers]).append(0)
    print(List)
    for addmorenumbers in range(len(List[0:input])):
        print("last:" + str(List[addmorenumbers+input]))
        List[addmorenumbers+input][1] = 1

print(List)
