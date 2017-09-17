text = "X-DSPAM-Confidence:    0.8475";
text = text.strip()

x = text.find("0")
y = text[x:len(text)]

print(float(y))