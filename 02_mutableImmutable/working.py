x = 4
y = x
print(x)
print(y)
x = 5
print(x)
print(y)

# Mutable vs Immutable in Python
# 🔸 Mutable:
# Mutable objects can be changed after creation. This means their content in memory can be updated without changing their identity (address/id).

# 🔹 Immutable:
# Immutable objects cannot be changed. Any operation that tries to modify them creates a new object in memory. The variable may point to a new object, but the original stays unchanged.

# 🧠 Common Misunderstanding:

# It's not that we "change" immutable objects — we just point the variable name to a new object.

# Meanwhile, mutable objects can be truly modified in-place.

# ✅ Examples:
# Type	Mutable / Immutable
# list	✅ Mutable
# dict	✅ Mutable
# set	✅ Mutable
# bytearray	✅ Mutable
# int	❌ Immutable
# float	❌ Immutable
# str	❌ Immutable
# tuple	❌ Immutable
# bool	❌ Immutable
# frozenset	❌ Immutable
# bytes	❌ Immutable
