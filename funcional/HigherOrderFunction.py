def multiply_by(multiplyer):
    return lambda number: multiplyer * number

# def concat2(first_arg):
#     def concat(second_arg):
#         return f'{f"{first_arg}:":10s} {second_arg}'
#     return concat
#
# classrooms = concat2('Aluno')
# print()
# print(classrooms('Marluzi Ilustree'))
#
# def multiply_by(multiplyer):
#     def multi(number):
#         return multiplyer * number
#     return multi
#
# score = concat2('Score')
# multiply_by_10 = multiply_by(10)
# print()
# print(score(multiply_by_10(2.5)))
# print(score(multiply_by_10(5)))
# print(score(multiply_by_10(10)))


