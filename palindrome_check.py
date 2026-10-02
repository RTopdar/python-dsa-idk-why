def reverse(number: float):

    result = 0
    while number != 0:
        result = (result * 10) + (number % 10)

        number //= 10
    return result


number = 1001
print(f"{number} is {"a" if reverse(number)==number else "not a"} palindrome number")
