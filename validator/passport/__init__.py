import random
import string
from collections.abc import Sequence


class PassPort(Sequence):
    def __init__(self, passport = None):
        if passport is None:
            self._passports = {}
            self._index = 0
        else:
            try:
                request = self.validate(passport)
            except:
                raise ValueError("Formato inválido")
            self._passports = {0: request[1]}
            self._index = 1
        self._next_index = 0
        
        
    @property
    def passports(self):
        return self._passports
    
    @passports.setter
    def passports(self, args):
        try:
            number = self.validate(args)[1]
        except ValueError:
            raise ValueError("Formato inválido")
        else:
            self._passports[self._index] = number
            self._index += 1
    
    def __repr__(self):
        if len(self.passports) > 1:
            return f"Passports: {list(map(lambda x: f'{x}', self.passports.values()))}"
        if len(self.passports) == 1:
            return f"Passport: {self.passports[0]}"
        return f"Passports: {self.passports}"
    
    def __len__(self):
        return len(self.passports)
    
    def __getitem__(self, index):
        if index >= len(self.passports):
            raise IndexError
        return self.passports[index]
    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        self._next_index += 1
        return self.passports[self._next_index - 1]
        
    def add(self, passport):
        try:
            self.passports = passport
        except ValueError:
            raise ValueError("Formato inválido")
    
    def generate(self):
        """
        Função que gera um passaporte aleatório e retorna o mesmo.
        
                    Retorno:
                            str: Passaporte aleatório.
        """

        letras = "".join(random.choices(string.ascii_uppercase, k=2))
        numeros = "".join(random.choices(string.digits, k=7))
        self.add(letras + numeros)
        return True
        
    def validate(self, passport):
        """
        Função que valida um passaporte e retorna True ou False.
                Parâmetros:
                        passaporte (str): Passaporte a ser validado.
                Retorno:
                        tuple: Tupla contendo True ou False e o passaporte.
        """

        if len(passport) != 9:
            raise ValueError("Formato inválido!")
        letras = passport[:2]
        numeros = passport[2:]
        if not letras.isalpha() or not numeros.isdigit():
            raise ValueError("Formato inválido!")
        if numeros[0] == '0':
            raise ValueError("Formato inválido!")
        return True, passport

def read(passport : str) -> PassPort:
    try:
        obj = PassPort(passport)  
        return obj
    except ValueError:
        raise ValueError("Formato inválido")
