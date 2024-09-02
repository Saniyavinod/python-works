from json import load

f=open("C:\\Users\\ASUS\\Desktop\\PythonJuneWorks\\jsonWorking\\products.json",encoding="UTF-8")

products=load(f)

#print(len(products))

#for i in products
# print(i.get("title"))


# t=[i.get("title") for i in products]

# print(t)




# for i in products:

#     if i.get("category")== "jewelery":
#         print(i.get("title"))

# p=[i.get("title")for i in products if i.get("category")=="jewelery"]
# print(p)

# p=[i.get("title")for i in products if i.get("price")>100]
# print(p)

# products vailable in range 100 to 150




# p=[i.get("title")for i in products if i.get("price") in range(100,151)]    floating points
# print(p)    

# p = [i.get("title") for i in products if  i.get("price")>=100 and i.get("price")<= 150]
# print(p)


def get_rating_product(dic):

    return dic.get("rating").get("count")
top_selling_product=max(products,key=get_rating_product)
print(top_selling_product.get("title"))


