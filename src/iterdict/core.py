import itertools

class iterdict:
    """
    An iterator that yields dictionaries representing the Cartesian product
    of values in the input dictionary.
    """
    def __init__(self, data):
        for key, value in data.items():
            if not isinstance(value, list):
                raise TypeError(f"Value for key '{key}' must be a list, got {type(value).__name__}")
            if len(value) == 0:
                raise ValueError(f"Value for key '{key}' must have at least one entry")
        
        self._data = data
        self._keys = list(data.keys())
        self._values = list(data.values())
        self._exclusions = []

    def __iter__(self):
        # Generate the product of all combinations
        for combo in itertools.product(*self._values):
            d = dict(zip(self._keys, combo))
            # Filter out excluded combinations
            if not any(all(d.get(k) == v for k, v in exclusion.items()) for exclusion in self._exclusions):
                yield d

    def remove(self, exclusion):
        """
        Exclude specific combinations from the iteration.
        Example: it.remove({"voltage": Vmax, "temp": hot})
        """
        self._exclusions.append(exclusion)
        return self
