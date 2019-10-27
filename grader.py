score = input("Enter Score: ")


try:
    score = float(score)
except:
    score = 2.0
    
if score > 1.0:
    print('an error')
else:
    if score < 0.6:
        print('F')
    elif score >= 0.6 and score < 0.7:
        print('D')
    elif score >= 0.7 and score < 0.8:
        print('C')
    elif score >= 0.8 and score < 0.9:
        print('B')
    else:
        print('A')