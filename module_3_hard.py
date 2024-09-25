def calculate_structure_sum(data):
    if isinstance(data, dict):
        return sum(calculate_structure_sum(k) + calculate_structure_sum(v) for k, v in data.items())
    if isinstance(data, (list, tuple, set)):
        return sum(calculate_structure_sum(item) for item in data)
    if isinstance(data, (int, float)):
        return data
    if isinstance(data, str):
        return len(data)
    return 0

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)