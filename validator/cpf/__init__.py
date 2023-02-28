import re


class CPF:
    def __init__(self, cpf):
        self._cpf = cpf
        

def validate( cpf):
        # Verifica a formatação do CPF
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            raise ValueError("Formato inválido")

        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            raise ValueError("Formato inválido")

        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            raise ValueError("Formato inválido")

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            raise ValueError("Formato inválido")

        return True

def read_cpf(cpf : str) -> CPF:
    try:
        validate(cpf)
        return CPF(cpf)
    except ValueError:
        raise ValueError("Formato inválido")