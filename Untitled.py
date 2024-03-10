
def addition(numb1,numb2):
    return numb1 + numb2
def subtraction( numb1,numb2):
    return numb1 -  numb2
def diviion(numb1, numb2):
    return numb1/numb2
def multiplication(numb1,numb2):
    return numb1*numb2
    
numb1 = int(input("Enter the first number"))
numb2 = int(input("Enter the second number"))
#print(addition(numb1,numb2))
operator = print("Enter the operation you want to perform")
print("1: ADDITION")
print("2: SUBTRACTION")
print("3: MULTIPLICATION")
print("4: DIVISION")
operator= int(input(" "))
if operator == 1:
    print("result =",addition(numb1,numb2))
if operator == 2:
    print("result =", subtraction(numb1,numb2))
if operator == 3:
    print("result =", multiplication(numb1, numb2))
if operator == 4:
    print("result =", diviion(numb1,numb2))

