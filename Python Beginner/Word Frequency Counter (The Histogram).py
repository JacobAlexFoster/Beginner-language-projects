text = "apple banana apple cherry banana apple"
num = {}
text = text.split()
print(text)
for text in text:
    if text in num:
        num[text]+=1
    else:
        num[text]=1
print(num)