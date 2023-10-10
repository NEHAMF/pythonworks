from json import load
path="C:\\Users\\Hamad\\Desktop\\python\\countries\\countries.json"
with open (path,encoding="utf-8") as f:
    countries=load(f)
# print(len(countries))    

# print all country names
country_names=[f.get("name")for f in countries]
# print(country_names)

# capital of china
country_capital=[f.get("capital")for f in countries if f.get("name")=="China"]
# print(country_capital)

# print all regions
regions={f.get("region")for f in countries}
# print(regions)

# bordres  of india
country_borders=[c.get("borders")for c in countries if c.get("name")=="China"][0]
# print(country_borders)
border_name=[c.get("name")for c in countries if c.get("alpha3Code")in country_borders]
# print(border_name)

# print independent country names
# print currencyname of india
# regular exppression

independent_country=[c.get("name")for c in countries if c.get("independent")==True]
# print(independent_country)

# currency_india=[c.get("currencies")for c in countries if c.get("name")=="India"][0]
# print(currency_india)
# currency_name=[c.get("name")for c in currency_india]
# print(currency_name)
