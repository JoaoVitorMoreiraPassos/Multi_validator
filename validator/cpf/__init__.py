import re
import random
from collections.abc import Sequence


class CPF(Sequence):
    def __init__(self, cpf = None):
        if cpf is None:
            self._cpfs = {}
            self._index = 0
        else:
            try:
                request = self.validate(cpf)
            except:
                raise ValueError("Formato inválido")
            self._cpfs = {0: request[1]}
            self._index = 1
        self._next_index = 0
        
        
    @property
    def cpfs(self):
        return self._cpfs
    
    @cpfs.setter
    def cpfs(self, args):
        try:
            cpf = self.validate(args)[1]
        except ValueError:
            raise ValueError("Formato inválido")
        else:
            self._cpfs[self._index] = cpf
            self._index += 1
    
    def __repr__(self):
        
        if len(self._cpfs) > 1:
            return f"CPFs: {list(map(lambda x: f'{x}', self.cpfs.values()))}"
        if len(self.cpfs) == 1:
            return f"CPF: {self._cpfs[0]}"
        return f"CPFs: {self._cpfs}"
    
    def __len__(self):
        return len(self._cpfs)
    
    def __getitem__(self, index):
        if index >= len(self._cpfs):
            raise IndexError
        return self._cpfs[index]
    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        self._next_index += 1
        return self._cpfs[self._next_index - 1]
        
    def add(self, cpf):
        try:
            self.cpfs = cpf
        except ValueError:
            raise ValueError("Formato inválido")
    
    def generate(self):
        cpf = [random.randint(0, 9) for x in range(9)]                              
        for _ in range(2):                                                          
            val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      
            cpf.append(11 - val if val > 1 else 0)                                  
        cpf = '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)
        self.cpfs = cpf
        
    def validate(self, cpf):
        # Verifica a formatação do CPF
        temp = list(map(lambda x: x if x.isdigit() else False, list(cpf)))
        if all(temp):
            temp.insert(3, '.')
            temp.insert(7, '.')
            temp.insert(11, '-')
            cpf = ''.join(list(map(lambda x: str(x), temp)))
        
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
        
        return True, cpf


def read(cpf : str) -> CPF:
    try:
        obj = CPF(cpf)  
        return obj
    except ValueError:
        raise ValueError("Formato inválido")