# itertooldict

A missing feature of `itertools`: labeled product of multiple choices from a dictionary.

**PIP:** [itertooldict on PyPI](https://pypi.org/project/itertooldict/)

## Installation

```bash
pip install itertooldict
```

## Usage

`productDict` takes a dictionary where values are iterables and yields dictionaries representing their Cartesian product.

> [!IMPORTANT]
> **`collections.OrderedDict` is the preferred input type.** While standard dictionaries work in modern Python, using `OrderedDict` ensures that the iteration order and dictionary keys remain consistent across all environments.

```python
from itertooldict import productDict
from collections import OrderedDict

# Preferred usage with OrderedDict
data = OrderedDict([
    ("voltage", ["Vmax", "Vmin"]),
    ("temp", ["hot", "cold"]),
    ("humidity", ["low", "high"])
])

for combo in productDict(data):
    voltage = combo["voltage"]
    temp = combo["temp"]
    humidity = combo["humidity"]
    print(f"Testing {voltage} at {temp} with {humidity} humidity")

# Output:
# Testing Vmax at hot with low humidity
# Testing Vmax at hot with high humidity
# Testing Vmax at cold with low humidity
# Testing Vmax at cold with high humidity
# Testing Vmin at hot with low humidity
# Testing Vmin at hot with high humidity
# Testing Vmin at cold with low humidity
# Testing Vmin at cold with high humidity
```

### Specifying Key Order

You can use the `keyorder` argument to specify the order of keys in the resulting dictionaries and the order in which the product is calculated.

```python
data = {"a": [1, 2], "b": ["x", "y"]}
# Iterate with 'b' as the outer loop and 'a' as the inner loop
for combo in productDict(data, keyorder=["b", "a"]):
    print(f"b={combo['b']}, a={combo['a']}")
# b=x, a=1
# b=x, a=2
# b=y, a=1
# b=y, a=2
```

### Compatibility with list() and enumerate()

`productDict` works seamlessly with standard Python functions:

```python
# Convert to list
all_combos = list(productDict(data))

# Use with enumerate
for i, combo in enumerate(productDict(data)):
    print(f"{i}: {combo}")
```
