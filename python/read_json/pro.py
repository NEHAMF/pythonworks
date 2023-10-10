from json import load
path="C:\\Users\\Hamad\\Desktop\\python\\read_json\\data.json"
with open(path) as f:
    records=load(f)
# print(records)    
# print(len(records))
# f_names=[f.get("name")for f in records]
# print(f_names )
# top_fw=max(records,key=lambda d:d.get("rating"))
# print(top_fw)
python_fw=[r.get("name") for r in records if r.get("language")=="python"] 
print(python_fw)
back_fw=[f.get("name")for f in records if f.get("side")=="backend"]
print(back_fw)
top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)

