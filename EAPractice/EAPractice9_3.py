# %%
import json
import pandas as pd

# %%
# Create and populate the dictionary
dict = {}
dict["name"] = "Chaya"
dict["age"] = 12
dict["city"] = "Boulder"
dict["type"] = "Canine"

dict
# %%
# Notice that JSON strings are enclosed in quotes, ''.
json_example = json.dumps(dict, ensure_ascii=False)

json_example
# %%
# Check object type of json_example
type(json_example)

# %%
# Turn JSON string into dictionary

# Create JSON string variable
json_sample = '{"name": "Chaya", "age": 12, "city": "Boulder", \
               "type": "Canine"}'

# Load JSON into dictionary using json.loads() function
data_sample = json.loads(json_sample)
data_sample

# %%
# Check object type of data_sample
type(data_sample)

# %%
# Call dictionary keys
data_sample["name"]
data_sample["city"]

# %%
# Read dictionary into Pandas DataFrame using from_dict() function
df = pd.DataFrame.from_dict(data_sample, orient='index')
df

# %%
# Convert Pandas DataFrame to JSON using .to_json() method
sample_json = df.to_json(orient='split')

type(sample_json)
# %%
