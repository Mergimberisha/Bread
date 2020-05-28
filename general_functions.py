# # recap function
#
# #define a function
# # def say_hello_name():
# #     return (f'hello  {name}' )
# #
# # def return_formated_name(name):
# #     return name.title().strip()
#
# # print the return of the function not the function
# # f_name = return_formated_name("    MERGIM   ")
# #
# # print(say_hello_name(f_name))
#
# # Basis of a test
#
# def return_formated_name(name):
#     return name.title().strip()
#
# # Test setup
# print("Testing function return formated name() with '  filipe      ' --> 'Filipe'")
# known_input = ' filipe      '
# expected_out = 'Filipe'
# print(return_formated_name(known_input) == expected_out)
#
#
#
#



### Homework task

name = input("Whats your name?  ")
def format_name():
    name2 = name.title().strip()
    return name2

# input = "    MergIM     "
# expected output = "Mergim"
#
print('Input')
print(name)
print('Expected output: Mergim')
print("Actual Output: ")
print(format_name())
print('The output is correct!')
