num=int(input("Enter number: "))
for num in range(1,21):
    if num==4 or num==13:
        print(f"{num} is unlucky")
    elif num%2==0:
        print(f"{num} is even")
    elif num%2==1:
        print(f"{num} is odd")
    else:
        print("Please give input")
        
#Compact solution
for num in range(1,21):
	if num == 4 or num == 13:
		state = "unlucky"
	elif num % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{num} is {state}")