import pandas as pd 

# JSON string
# json_str = '''
# {
#     "name": ["Alice", "Bob", "Charlie"],
#     "age": [25, 30, 35],
#     "city": ["New York", "Los Angeles", "Chicago"]
# }
# '''

# df = pd.read_json(json_str)
# print(df)

# with open('metric.json', 'r') as file:
#   lines = file.readlines()
#   print(lines)
#   d2 = pd.read_json(lines)
#   print(d2)

d2 = pd.read_json('metric.json', lines=True)

d2 = pd.json_normalize(d2['log'])
print(d2['cloud'])