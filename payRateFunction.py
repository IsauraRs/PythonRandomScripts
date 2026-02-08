def computepay(h, r):
    if h <=40:
        pay = h*r
        
    else:
        extraHour = h-40
        normalPay = 40*r
        pay = normalPay + (extraHour*(1.5*r))
        
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay", p)