import random

LOGGING = False


def is_prime(number: int) -> bool:
    for i in range(2, int(pow(number, 1 / 2)) + 1):
        if number % i == 0:
            return False
    return True


def random_prime_number(a: int, b: int) -> int:
    prime_number = random.randint(a, b)
    prime_number += prime_number % 2 + 1
    while not is_prime(prime_number):
        prime_number += 2
        if prime_number > b:
            return random_prime_number(a, b)
    return prime_number


def advanced_euclid_algorithm(a, b, x0=1, y0=0, x1=0, y1=1):
    if a % b == 0:
        # return [b, x1, y1]
        return [x1, y1]
    return advanced_euclid_algorithm(b, a % b, x1, y1, x0 - (a // b) * x1, y0 - (a // b) * y1)


def get_random_pair_p_q(bit: int) -> dict:
    return {"p": random_prime_number(int(pow(2, bit - 1)), int(pow(2, bit))), "q": random_prime_number(int(pow(2, bit - 1)), int(pow(2, bit)))}


def get_n(pair: dict[str: int, str: int]) -> int:
    return pair["p"] * pair["q"]


def euler_function(pair: dict[str: int, str: int]) -> int:
    return (pair["p"] - 1) * (pair["q"] - 1)


def get_e(euler_number: int) -> int:
    # e = euler_number - 1
    # while not is_prime(e):
    #     e -= 2
    e = random_prime_number(1, euler_number)
    return e


# def get_d(e: int, euler_number: int, bit: int) -> int:
#     d = pow(2, bit * 2) - 1
#     while not (d * e % euler_number == 1):
#         d -= 2
#     return d


def get_d(e: int, euler_number: int) -> int:
    d = max(advanced_euclid_algorithm(e, euler_number))
    while d == 1:
        d = max(advanced_euclid_algorithm(e, euler_number))
    return d


def generate_rsa_pair(bit: int) -> dict[str: list[int, int], str: list[int, int]]:
    print("Processing...") if LOGGING else ...
    pair = get_random_pair_p_q(bit)
    print(f"Pair               -> [ {pair['p']} | {pair['q']} ]") if LOGGING else ...
    n = get_n(pair)
    print(f"n                  -> {n}") if LOGGING else ...
    euler_number = euler_function(pair)
    print(f"Euler number       -> {euler_number}") if LOGGING else ...
    e = get_e(euler_number)
    d = get_d(e, euler_number)
    print(f"Start testing keys...") if LOGGING else ...
    if "Hello RSA!" != decrypt_data(encrypt_data("Hello RSA!", [e, n]), [d, n]):
        print(f"Tests failed, generating new pair...") if LOGGING else ...
        return generate_rsa_pair(bit)
    print(f"Tests done!") if LOGGING else ...
    print(f"Public key         -> [ {e} | {n} ]") if LOGGING else ...
    # d = get_d(e, euler_number, bit)
    print(f"Private key        -> [ {d} | {n} ]") if LOGGING else ...
    return {"public_key": [e, n], "private_key": [d, n]}


def encrypt_data(data: str, public_kye: list[int, int]) -> list:
    encrypted_data = [ord(i) for i in data]
    print(f"Not encrypted data -> {encrypted_data}") if LOGGING else ...
    for i, e in enumerate(encrypted_data):
        encrypted_data[i] = pow(e, public_kye[0], public_kye[1])
    print(f"Encrypted data     -> {encrypted_data}") if LOGGING else ...
    return encrypted_data


def decrypt_data(data: list, private_kye: list[int, int]) -> str:
    decrypted_data = ""
    for i in data:
        try:
            decrypted_data += chr(pow(i, private_kye[0], private_kye[1]))
        except (ValueError, OverflowError):
            return "-1"
    print(f"Decrypted data     -> {decrypted_data}") if LOGGING else ...
    return decrypted_data
