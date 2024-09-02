from json import load
f=open("C:\\Users\\ASUS\\Desktop\\PythonJuneWorks\\jsonWorking\\country.json",encoding="UTF-8")

country=load(f)
# print(len(country))

# 1.
# for c in country:
#     if c.get("region")=="Europe":
#         print(c.get("name"))

# 2.

# def get_population(dic):

#     return dic.get("population")
# heighest_population=max(country,key=get_population)
# print(heighest_population.get("name"))


# 3.


# independent=0
# for c in country:
#     if c.get("independent")==True: 
#         independent+=1
# print(independent)
# v=len([c for c in country if c.get("independent")==True])
# print(v)


# 4.subregion western asia

# for c in country:
#     if c.get("subregion")=="Western Asia":
#         print(c.get("name"))

# 5.List all countries that share a border with more than five other countries.

# for c in country:
#     if len(c.get("borders",[])) > 10:
#         print(c.get("name"))

# # 6.Which countries have a Gini index above 40?
# for c in country:
#     if c.get("gini",0)>40:
#         print(c.get("name"))


#?List all countries in the region Africa with a population density greater than 100 people per square kilometer        


#7 area largest


# def get_area(dic):

#     return dic.get("area",0)
# largest_area=max(country,key=get_area)
# print(largest_area.get("name"))


#8.Find all countries with a calling code that starts with '3'
# List comprehension to find countries with a calling code that starts with '3'
# countries_with_code_starting_with_3 = [
#     country for country in country
#     if any(code.startswith('3') for code in country.get('callingCodes', []))
# ]

# Print the names of these countries
# for country in countries_with_code_starting_with_3:
#     print(country.get("name"))


#9
# List comprehension to find countries that are part of the African Union (AU)
# countries_in_au = [c for c in country if any(bloc.get("acronym") == "AU" for bloc in c.get("regionalBlocs", []))]

# # Print the names of these countries
# for c in countries_in_au:
#     print(c.get("name"))


#10 Find countries where the capital city's name is the same as the country's name. 

# for  c in country:
#     c.get("capital")==c.get("name")

# print(c.get("name"))    


#11.Which countries have alternate spellings that include the word 'Republic'?
# def is_altSpelling(c):
#     if c.get("altSpellings") is not None:
#          for w in c.get("alSpellings"):
#              if "Republic" in w:
#                  return True
             
# countries_altSoelling=[c.get("name") for c in country if is_altSpelling(c)]



# def fetch_country_by_name(name):

#     return [c for c in country if c.get("name")==name][0]

# country_filter=fetch_country_by_name("India")

# if "regionalBlocs" in country_filter:

#     block_data=country_filter.get("regionalBlocs")[0]

#     if "otherNames" in block_data:
#         print(block_data.get("otherNames"))  
#     else:
#         print(country_filter.get("name"))    




# region has largest area
all_region={c.get("region")for c in country}

# print(all_region)

region_summary={}

for c in country:

    region_name=c.get("region")

    if region_name in region_summary:
        region_summary[region_name]+=c.get("area",0)
    else:
        region_summary[region_name]=c.get("area",0)

# print(region_summary)        

key_values=[(v,k)for k,v in region_summary.items()]

print(max(key_values))