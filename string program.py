input_string = input("enter a Sentence:")
n=int(input("enter the length:"))

words = input_string.split()
long_words = [word for word in words if len (word)>n]

print(f"Words longer than {n} characters : {long_words}")
