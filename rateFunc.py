def computepay(h,r):
    if h > 40:
        return (h * r) + ((h - 40.0) * (r * 0.5))
    return h * r

hrs = float(input("Enter Hours:"))
r = float(input("Enter rate: "))
                
p = computepay(hrs, r)
print("Payment", p)