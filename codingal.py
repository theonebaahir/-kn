data = {'id1': {'name':['Sara'], 'class':['V'],'subjet':['english, math , science']},
         'id2': {'name':['Sara2'], 'class':['V'],'subjet':['english, math , science']}
        }
result = {}

for key,value in data.items():
    if value not in result.values():
        result[key] = value
print(result)
print()




test = {'Codingal': 2, 'is': 2, 'best': 2, 'for' :2 , 'coding': 1}
k = 2
res = 0 
for key in test:
    if test [key]== k:
        res = res + 1
        
        
        
        
print("frequency of k is :"+ str(res))


country = {'india': '0091', 'austraila': '0025', 'nepal': '00977'}
print("country code india- ")
print(country.get('india', 'Not found'))
print("country code for japan -")
print(country.get('japan', 'not found'))
        

 