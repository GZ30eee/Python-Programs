# Text Type: str
str_var = "Hello, World!"
print("String:", str_var)
print("Type:", type(str_var))

# Numeric Types: int, float, complex
int_var = 10
print("Integer:", int_var)
print("Type:", type(int_var))

float_var = 10.5
print("Float:", float_var)
print("Type:", type(float_var))

complex_var = 1j
print("Complex:", complex_var)
print("Type:", type(complex_var))

# Sequence Types: list, tuple, range
list_var = [1, 2, 3, "apple", "banana"]
print("List:", list_var)
print("Type:", type(list_var))

tuple_var = (1, 2, 3, "apple", "banana")
print("Tuple:", tuple_var)
print("Type:", type(tuple_var))

range_var = range(6)
print("Range:", list(range_var))
print("Type:", type(range_var))

# Mapping Type: dict
dict_var = {"name": "John", "age": 30}
print("Dictionary:", dict_var)
print("Type:", type(dict_var))

# Set Types: set, frozenset
set_var = {"apple", "banana", "cherry"}
print("Set:", set_var)
print("Type:", type(set_var))

frozenset_var = frozenset({"apple", "banana", "cherry"})
print("Frozenset:", frozenset_var)
print("Type:", type(frozenset_var))

# Boolean Type: bool
bool_var = True
print("Boolean:", bool_var)
print("Type:", type(bool_var))

# Binary Types: bytes, bytearray, memoryview
bytes_var = b"Hello"
print("Bytes:", bytes_var)
print("Type:", type(bytes_var))

bytearray_var = bytearray(5)
print("Bytearray:", bytearray_var)
print("Type:", type(bytearray_var))

memoryview_var = memoryview(bytes(5))
print("Memoryview:", memoryview_var)
print("Type:", type(memoryview_var))

# None Type: NoneType
none_var = None
print("NoneType:", none_var)
print("Type:", type(none_var))

