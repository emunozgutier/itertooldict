# itertooldict

A missing feature of `itertools`: labeled product of multiple choices from a dictionary.

## Installation

```bash
pip install itertooldict
```

## Usage

`itertooldict` takes a dictionary where values are iterables and yields dictionaries representing their Cartesian product. It behaves exactly like `itertools.product` but for dictionaries.

```python
from itertooldict import itertooldict

data = {
    "voltage": ["Vmax", "Vmin"],
    "temp": ["hot", "cold"]
}

for combo in itertooldict(data):
    print(combo)

# Output:
# {'voltage': 'Vmax', 'temp': 'hot'}
# {'voltage': 'Vmax', 'temp': 'cold'}
# {'voltage': 'Vmin', 'temp': 'hot'}
# {'voltage': 'Vmin', 'temp': 'cold'}
```

### Repeating the Product

You can use the `repeat` argument to repeat the input iterables, just like `itertools.product`.

```python
data = {"a": [1, 2]}
for combo in itertooldict(data, repeat=2):
    print(combo)
# {'a': 1}
# {'a': 2}
# {'a': 1}
# {'a': 2}
```

### Compatibility with list() and enumerate()

`itertooldict` works seamlessly with standard Python functions:

```python
# Convert to list
all_combos = list(itertooldict(data))

# Use with enumerate
for i, combo in enumerate(itertooldict(data)):
    print(f"{i}: {combo}")
```
