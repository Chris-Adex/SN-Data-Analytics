
# Question 1 : convert string "1000" to an integer

print(int("1000"))

# Question 2 : convert the floating point number 3.764 to an integer

print(int(3.764))

# Question 3

BUSINESS_EXPENSES = 99.45
BUSINESS_EXPENSES = "$" + str(BUSINESS_EXPENSES) + " dollars"

print("business_expenses =", BUSINESS_EXPENSES)


# Question 4
# - The type function returns the class type of argument(object) passed as parameter.

# Question 5
# - Boolean is a special data type used to represent the truth value of an expression.
# - It's two possible values are 'True' and 'False'

# Question 6
# - The technical name for the % operator is Modulo Operator.
# - It returns the remainder of a division after one number is divided by another.


# Question 7

FANCY_NAME = "Oladipo Adediran Christopher"
print(FANCY_NAME)


# Question 8

Hours = int(input("Enter time_in_hours\n"))
Seconds = Hours * 3600

print(Hours, "hours =", Seconds, "seconds")

# Question 9

# easy_money function

def easy_parameter():
    return 100

print(easy_parameter())

# best_food_ever function

def best_food_ever():
    return "Sushi"

print(best_food_ever())

# convert_to_currency function

def convert_to_currency(amount):
    return "$" + str(amount)

print(convert_to_currency(200))
print(convert_to_currency(50))


# Question 1O

def string_adder(a = " ", b = " "):
    return a + " " + b

print(string_adder("Hello", "World"))
print(string_adder("Scholar", "Nurture"))
print(string_adder())
print(string_adder("Football"))

# Question 11

def long_word(word):
    return len(word) > 7

print(long_word("python"))
print(long_word("analysis"))


# Question 12

def same_first_and_last_letter(letter):
    return letter[0] == letter[-1]

print(same_first_and_last_letter("yesterday"))
print(same_first_and_last_letter("Yesterday"))
print(same_first_and_last_letter("A"))
print(same_first_and_last_letter("futures"))


# Question 13

def first_three_characters(letters):
    return letters[0:3]

print(first_three_characters("pythonial"))
print(first_three_characters("function"))
