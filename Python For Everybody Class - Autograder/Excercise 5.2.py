largest = -100
smallest = 100

while True:
  try:
    nume = input("Enter a number: ")
    if nume == "done": 
      	break
    num = int(nume)
    
    if num > largest:
      largest = num
      
    elif smallest > num:
      smallest = num
			 
  except:
	  print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)