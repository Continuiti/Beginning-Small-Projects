def computepay(h,r):
	if h > 40:
		return ((h-40) * (r * 1.5)) + (40 * r)
                
	else:
		return h * r
    
hour = float(input("Enter Hours Worked: "))
pay = float(input("Enter Rate Per Hour: "))

print(computepay(hour, pay))
        