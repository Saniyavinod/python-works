mobile={"name":"iphone","brand":"moto","price":60000,"is_available":True,"offers":1000}

# print(mobile.get("name"))

# #1.get(key) return key value

# print(mobile.get("name"))

# #2. keys() return all key 

# print(mobile.keys())

# #3. values() return all values

# print(mobile.values())

# #4. items() return all key and value
# for k,v in mobile.items():
#     print(k,v)

# #5. pop(key) removes the key value pairs 
# mobile.pop("name")
# print(mobile)


#6.add new key value

# mobile["offers"]=1000
# print(mobile)

if "offers" in mobile:
    selling_price=mobile.get("price")-mobile.get("offers")
    print(selling_price)
else:
    selling_price=mobile.get("price")
    print(selling_price)    







