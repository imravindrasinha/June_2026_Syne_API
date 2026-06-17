import json

filepath="C:\\June2026_Synechron_API\\data_global.json"
with open (filepath, "r") as f:
    data =json.load(f)
 
print(data["cName"])
print(data["empid"])
print(data["empname"])
data["base_url"]="https://grocery.click"
with open(filepath,"w") as f:
    json.dump(data,f,indent =4 )