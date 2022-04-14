from docplex.mp.model_reader import ModelReader
import json
import time

# Getting X, Y, Z values
x = input('X variable: ')  # Source nodes
y = input('Y variable: ')  # Transit nodes where Y >= 2
z = input('Z variable: ')  # Destination nodes
# -------------- LP GENERATION -----------------
def minimize():
    """Sorts out the minimize"""


def contraints():
    """Sorts out constraints"""
    return 1

def bounds():
    """Sorts out the bounds"""
    return 1

# ------------------- RUN CPLEX --------------------

my_prob = ModelReader.read('737.lp')
start_time = time.time()
solution = my_prob.solve()
print("--- %s seconds ---" % (time.time() - start_time))
json_data = json.loads(solution.export_as_json_string())
print(json_data)

count = 0
largest_value = 0
lowest_value = float('Inf')
link_list = list()
for item in json_data['CPLEXSolution']['variables']:
    if (item['name'][0] == "c" or item['name'][0] == "d") and float(item['value']) != 0:
        count += 1
        if float(item['value']) >= largest_value:
            largest_value = float(item['value'])
        if float(item['value']) <= lowest_value:
            lowest_value = float(item['value'])

for item in json_data['CPLEXSolution']['variables']:
    if float(item['value']) == largest_value:
        link_list.append(item['name'])

print(count)
print(largest_value)
print(lowest_value)
print(link_list)