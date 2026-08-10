'''
Question 3
'''
def snake_to_camel(text: str) -> str:
    camel = []
    for i in range(len(text)):
        if text[i] == '_':
            continue
        if i > 0 and text[i - 1] == '_':
            camel.append(text[i].upper())
        else:
            camel.append(text[i].lower())
    camel = "".join(camel)
    return camel

print(snake_to_camel("hello_python"))
print(snake_to_camel("my_variable_name"))
print(snake_to_camel("python"))
print(snake_to_camel("a_b_c_d"))
print(snake_to_camel("_hello_world"))