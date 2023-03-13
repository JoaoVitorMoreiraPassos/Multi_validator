from collections.abc import Sequence


class TelPhone(Sequence):
    def __init__(self, number = None):
        if number is None:
            self._numbers = {}
            self._index = 0
        else:
            try:
                request = self.validate(number)
            except:
                raise ValueError("Formato inválido")
            self._numbers = {0: request[1]}
            self._index = 1
        self._next_index = 0
        
        
    @property
    def numbers(self):
        return self._numbers
    
    @numbers.setter
    def numbers(self, args):
        try:
            number = self.validate(args)[1]
        except ValueError:
            raise ValueError("Formato inválido")
        else:
            self._numbers[self._index] = number
            self._index += 1
    
    def __repr__(self):
        if len(self.numbers) > 1:
            return f"Numbers: {list(map(lambda x: f'{x}', self.numbers.values()))}"
        if len(self.numbers) == 1:
            return f"Number: {self.numbers[0]}"
        return f"Numbers: {self.numbers}"
    
    def __len__(self):
        return len(self.numbers)
    
    def __getitem__(self, index):
        if index >= len(self.numbers):
            raise IndexError
        return self.numbers[index]
    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        self._next_index += 1
        return self.numbers[self._next_index - 1]
        
    def add(self, number):
        try:
            self.numbers = number
        except ValueError:
            raise ValueError("Formato inválido")
    
    def generate(self):
        ...
        
    def validate(self, number):
        """
        Função que valida um número de telefone e retorna True ou False.
                Parâmetros:
                        numero (str): Número de telefone a ser validado, com ou sem o prefixo do Brasil, mas com o DDD.
                Retorno:
                        tuple: Tupla com dois elementos, o primeiro é um bool que indica se o número é válido ou não, o segundo é o número de telefone formatado.
        """

        # Remove espaços em branco, traços e parênteses, se houver
        number = number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        # Verifica se os primeiros caracteres são +55, caso contrário, assume que o número não tem o prefixo do Brasil
        if not number.startswith("+55"):
            # Adiciona o prefixo do Brasil
            number = "+55" + number

        # Remove o prefixo do Brasil
        number = number[3:]

        # Verifica se o número é composto apenas por dígitos
        if not number.isdigit():
            raise ValueError("Formato inválido!")

        # Verifica se o número tem 10 dígitos (sem contar o prefixo do Brasil)
        if len(number) != 10 and len(number) != 11:
            raise ValueError("Formato inválido!")
        # Extrai os dois primeiros dígitos (DDD)
        ddd = int(number[:2])
        # Verifica se o DDD é válido de acordo com os estados do Brasil
        if ddd not in [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]:
            raise ValueError("Formato inválido!")
        # Retorna True se todas as condições forem satisfeitas
        return True, number


def read(tel_phone : str) -> TelPhone:
    try:
        obj = TelPhone(tel_phone)  
        return obj
    except ValueError:
        raise ValueError("Formato inválido")
