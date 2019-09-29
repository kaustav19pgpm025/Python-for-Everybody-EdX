# hours pay program using function computepay()
def computepay(hours,rate):
	
	if  hours > 40:
		hoursabove40 = hours - 40
		payabove40 = hoursabove40 * (rate * 0.5)
		pay = (hours * rate) + payabove40
		# the worker will get the usual (hours*rate) + additional pay for the extra hours

	else:
		pay = hours * rate
    
	return pay

h = float(raw_input("enter hours: "))
r = float(raw_input("enter rate: "))
p = computepay(h,r)
# payment
print p



