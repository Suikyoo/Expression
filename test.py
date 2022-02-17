from expressions import Expression


#ways to initialize
obj = Expression()
#no expression

obj = Expression([5,'+', -8])
#with fixed expression

print(obj.answer)
#output = -3

#to get the expression, use:
print(obj.expression)
#returns a string of the expression "5+(-8)"

#to randomize the expression, use:
obj.randomize_expression(3, [-5, 5])
#first argument: terms(binomial, trinomial, or polynomial). If you only want 2 terms(ex.: 3+3), you put 2 in the argument
#second argument: number range. The numbers used in the expression. [-5, 5] would generate an expression with numbers from -5 to 5

print(obj.expression)
#expression has been randomized

personalAnswer = 5

check = obj.check_answer(personalAnswer)
#returns true if personal answer is the same as the answer of expression

#ADDITIONAL METHOD:

#if you only want to randomize specific operations, use:
obj.set_operations(['+', '-'])
#then use randomize_expression() method

#all operations are as follows: +, -, *, /
