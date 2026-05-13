text = "  Hello World  "

print("Original text:", repr(text))

# -----------------------
# CASE METHODS
# -----------------------
print("\n--- Case Methods ---")
print("upper():", text.upper())
print("lower():", text.lower())
print("title():", text.title())
print("capitalize():", text.capitalize())

# -----------------------
# TRIM SPACES
# -----------------------
print("\n--- Strip Methods ---")
print("strip():", repr(text.strip()))
print("lstrip():", repr(text.lstrip()))
print("rstrip():", repr(text.rstrip()))

# -----------------------
# SEARCH METHODS
# -----------------------
print("\n--- Search Methods ---")
print("find('World'):", text.find("World"))
print("count('l'):", text.count("l"))

# -----------------------
# REPLACE
# -----------------------
print("\n--- Replace ---")
print("replace:", text.replace("World", "Python"))

# -----------------------
# SPLIT & JOIN
# -----------------------
print("\n--- Split & Join ---")
sentence = "apple,banana,grape"
fruits = sentence.split(",")
print("split:", fruits)

joined = "-".join(fruits)
print("join:", joined)

# -----------------------
# CHECK METHODS (BOOLEAN)
# -----------------------
print("\n--- Check Methods ---")
print("isalpha:", "hello".isalpha())
print("isdigit:", "123".isdigit())
print("isalnum:", "abc123".isalnum())
print("startswith('He'):", text.strip().startswith("He"))
print("endswith('ld'):", text.strip().endswith("ld"))

# -----------------------
# LENGTH
# -----------------------
print("\n--- Length ---")
print("len:", len(text))