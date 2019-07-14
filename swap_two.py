# Swap commas and dots in a String
text = "hello. how are you, I am good,"
s1 = text.replace(',', '#')
s1 = s1.replace('.', ',')
s1 = s1.replace('#', '.')
print(s1)
