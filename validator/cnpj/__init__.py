import re
import random


class CNPJ:
    def __init__(self, cnpj = None):
        if cnpj is None:
            self._cnpjs = {}
            self._index = 0
        else:
            try:
                request = self.validate(cnpj)
            except:
                raise ValueError("Formato inválido")
            self._cnpjs = {0: cnpj}
            self._index = 1
        self._next_index = 0
    
    @property
    def cnpjs(self):
        return self._cnpjs
    
    @cnpjs.setter
    def cnpjs(self, cnpj):
        try:
            cnpj = self.validate(cnpj)[1]
        except ValueError:
            raise ValueError("Formato inválido")
        else:
            self._cnpjs[self._index] = cnpj
            self._index += 1
    
    def __repr__(self):
        if len(self._cnpjs) > 1:
            return f"{list(map(lambda x: f'CPF: {x}', self.cnpjs.values()))}"
        if len(self.cnpjs) == 1:
            return f"CPF: {self.cnpjs[0]}"
        return f"CPF: {self.cnpjs}"
    
    def __len__(self):
        return len(self.cnpjs)
    
    def __getitem__(self, index):
        if index >= len(self.cnpjs):
            raise IndexError
        return self.cnpjs[index]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        self._next_index += 1
        return self.cnpjs[self._next_index - 1]
    
    def add(self, cnpj):
        try:
            self.cnpjs = cnpj
        except ValueError:
            raise ValueError("Formato inválido")
    
    def generate(self):
        def calculate_special_digit(l):                                             
            digit = 0                                                               
            for i, v in enumerate(l):                                               
                digit += v * (i % 8 + 2)                                            
            digit = 11 - digit % 11                                                 
            return digit if digit < 10 else 0                                       
        
        cnpj =  [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]             
        for _ in range(2):                                                          
            cnpj = [calculate_special_digit(cnpj)] + cnpj                           
        cnpj = '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1])
        self.cnpjs = cnpj
    
    def validate(self, cnpj):
        # Verifica a formatação do cnpj
        temp = list(map(lambda x: x if x.isdigit() else False, list(cnpj)))
        if all(temp):
            temp.insert(2, '.')
            temp.insert(6, '.')
            temp.insert(10, '/')
            temp.insert(15, '-')
            cnpj = ''.join(list(map(lambda x: str(x), temp)))
            del(temp)
            
        if not re.match(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', cnpj):
            raise ValueError("Formato inválido")
        
        # Obtém apenas os números do cnpj, ignorando pontuações
        numbers = [int(digit) for digit in cnpj if digit.isdigit()]
        
        # Verifica se o cnpj possui 14 números ou se todos são iguais:
        if len(numbers) != 14 or len(set(numbers)) == 1:
            raise ValueError("Formato inválido")
        
        # Validação do primeiro dígito verificador:
        pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        sum_of_products = sum(a*b for a, b in zip(numbers[0:12], pesos))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if expected_digit != numbers[12]:
            raise ValueError("Formato inválido")
        
        # Validação do segundo dígito verificador:
        pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        sum_of_products = sum(a*b for a, b in zip(numbers[0:13], pesos))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if expected_digit != numbers[13]:
            raise ValueError("Formato inválido")
        
        return True, cnpj


def read(cnpj : str) -> CNPJ:
    try:
        obj = CNPJ(cnpj)  
        return obj
    except ValueError:
        raise ValueError("Formato inválido")