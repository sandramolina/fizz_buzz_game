def fizz_buzz_game(input_number):
    if input_number % 3 == 0:
        return "Fizz"
    elif input_number % 5 == 0:
        return "Buzz"    
    else:
        return input_number