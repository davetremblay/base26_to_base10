def base_26_to_10(text):
    """
    Input: text (a to z, lower or uppercase, no space or punctuation)
    Returns the value of the base 26 input as a base 10 integer
    """
    new_list = [ ord(letter)-97 for letter in text.lower() ]
    new_list = [ x for x in new_list if x < 26 and x >= 0 ]
    txet = new_list[::-1]
    def multiply_by_index(data):
        new_data = []
        output = 0
        for index, item in enumerate(data):
            new_data.append(item * 26 ** index)
            output += (item * 26 ** index)
        return output
    final = multiply_by_index(txet)
    print ("in base_26_to_10(text):",text,"gives",final)
    return final
text1 = input("Enter text: ")

val1 = base_26_to_10(text1)

out = val1
print (out)