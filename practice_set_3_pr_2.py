letter='''Dear <|Name|>,
                     you are selected!
                     <|Date|>'''
name=input("enter your name\n")
date=input("enter your date ")
letter= letter.replace("<|Name|>",name)
letter= letter.replace("<|Date|>",date)

print(letter)
# b='''caution"ahead" drive "safely "'''
# print(b)
