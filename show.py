x = ["1", "2", "3"]
user_input = input()
if len(set(user_input) & set(x)) >= 1:
    print("Такой есть в списке")
