str = 'X-DSPAM-Confidence: 0.8475 '
str_1 = str.find(':')
print(float(str[str_1 + 1 :]))