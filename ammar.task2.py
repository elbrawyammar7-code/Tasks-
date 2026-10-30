

def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Invalid sides")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle")
    if a == b == c:
        return "equilateral"
    if a == b or a == c or b == c:
        return "isosceles"
    return "scalene"

print("Triangle:", classify_triangle(3, 3, 5))


def course_result(coursework, final, attendance):
    if not 0 <= coursework <= 40:
        raise ValueError("Invalid coursework")
    if not 0 <= final <= 60:
        raise ValueError("Invalid final")
    if not 0 <= attendance <= 100:
        raise ValueError("Invalid attendance")
    if attendance < 75:
        return "barred"
    if final < 18:
        return "fail"
    if coursework + final < 60:
        return "fail"
    return "pass"

print("Course result:", course_result(35, 25, 90))


def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print("FizzBuzz:", fizzbuzz(5))


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print("Is prime:", is_prime(7))


def primes_below(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

print("Primes below 10:", primes_below(10))


def first_repeated(values):
    for i in range(len(values)):
        for j in range(i):
            if values[i] == values[j]:
                return values[i]
    return None

print("First repeated:", first_repeated([3, 1, 4, 1, 5]))


def count_pairs(n):
    if n <= 1:
        return 0
    return n * (n - 1) // 2

print("Count pairs:", count_pairs(4))


def calculator(command):
    parts = command.split()
    if not parts:
        raise ValueError("Invalid command")
    try:
        match parts:
            case ["add", a, b]:
                return int(a) + int(b)
            case ["mul", a, b]:
                return int(a) * int(b)
            case ["neg", a]:
                return -int(a)
            case ["sum", first, *rest]:
                total = int(first)
                for number in rest:
                    total += int(number)
                return total
            case _:
                raise ValueError("Invalid command")
    except (TypeError, ValueError) as error:
        raise ValueError("Invalid command or number") from error

print("Calculator add:", calculator("add 2 3"))
print("Calculator sum:", calculator("sum 1 2 3 4"))


def parse_int(text, default=None):
    try:
        return int(text)
    except (TypeError, ValueError):
        return default

print("Parse integer:", parse_int("42"))


def stats(*numbers):
    if len(numbers) == 0:
        raise ValueError("No numbers")
    smallest = numbers[0]
    largest = numbers[0]
    total = 0
    count = 0
    for number in numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
        total += number
        count += 1
    return (smallest, largest, total / count)

print("Statistics:", stats(3, 1, 2))


def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target

print("Append to list:", append_to(3, [0]))


def make_multiplier(k):
    def multiply(number):
        return number * k
    return multiply

triple = make_multiplier(3)
print("Make multiplier:", triple(5))


def apply_n(f, x, n):
    result = x
    for i in range(n):
        result = f(result)
    return result

print("Apply function 3 times:", apply_n(lambda x: x * 2, 1, 3))
