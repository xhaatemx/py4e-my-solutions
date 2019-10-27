text = "X-DSPAM-Confidence:    0.8475"
num = None

inedx = text.find('    ')
num = float(text[index+1:])

print(num)