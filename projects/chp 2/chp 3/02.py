letter ='''
Dear <|NAME|>,
You are selected !
<|date|>
'''
print(letter.replace("<|NAME|>","Harry").replace("<|date|>", "12-12-2020"))