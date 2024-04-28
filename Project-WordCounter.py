def analyze_code():
    test_str = ''.join(letter for letter in string if letter.isalpha())

    print(f"The number of word in a given input :{len(test_str)}")

    special_chars= ''.join(letter for letter in string if letter.isalnum()==False)
    print(f"The number of special character in a given input :{len(special_chars)}")
    num= ''.join(letter for letter in string if letter.isnumeric())
    print(f"The number of digits in a given input :{len(num)}")

string = input("give word:")
if len(string)==0:
    print("give value")
elif len(string)!=0:
    analyze_code()
