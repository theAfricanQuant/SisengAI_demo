def is_divisible_by_3(n):
    """A number is divisible by 3 if the sum of its digits is divisible by 3."""
    return sum(int(digit) for digit in str(n)) % 3 == 0


def is_divisible_by_5(n):
    """A number is divisible by 5 if it ends in 0 or 5."""
    return n % 10 == 0 or n % 10 == 5


def is_divisible_by_7(n):
    """A number is divisible by 7 using a special trick:
    - Double the last digit and subtract it from the remaining number.
    - Repeat the process until you get a small number.
    - If that small number is divisible by 7, the original number is too.
    """
    while n > 9:
        last_digit = n % 10
        remaining_part = n // 10
        n = remaining_part - 2 * last_digit
    return n % 7 == 0


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    print(f"Checking divisibility for {num}...\n")

    if is_divisible_by_3(num):
        print(f"{num} is divisible by 3 ✅")
    else:
        print(f"{num} is NOT divisible by 3 ❌")

    if is_divisible_by_5(num):
        print(f"{num} is divisible by 5 ✅")
    else:
        print(f"{num} is NOT divisible by 5 ❌")

    if is_divisible_by_7(num):
        print(f"{num} is divisible by 7 ✅")
    else:
        print(f"{num} is NOT divisible by 7 ❌")
