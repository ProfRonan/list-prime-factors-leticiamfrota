"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""

    return False


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    primos = []
    for i in range (2,number+1):
        while number % i == 0:
            primos.append(i)
            number = number/i
    return primos
