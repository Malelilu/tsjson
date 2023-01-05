 
import accounts.json

f = open('tsjsn/accounts.json')
  
data = accounts.json.load(f)
  
for i in data['emp_details']:
    print(i)
  
f.close()
