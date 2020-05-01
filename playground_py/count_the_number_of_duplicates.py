def duplicate_count(text):
    result = 0
    for x in set(text):
        result += 1 if text.lower().count(x) > 1 else 0
    return result

print(duplicate_count("abcde"))
print(duplicate_count("abcdea"))
print(duplicate_count("indivisibility"))