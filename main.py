def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


# Example usage
if __name__ == "__main__":
    raw = input("Enter a number: ")
    try:
        num = int(raw)
    except ValueError:
        print(f"{raw} is not an integer.")
    else:
        even_odd = "even" if is_even(num) else "odd"
        prime_text = "prime" if is_prime(num) else "not prime"
        print(f"{num} is {even_odd} and {prime_text}.")
