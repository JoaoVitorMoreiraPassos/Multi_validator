from datetime import datetime
from collections.abc import Sequence


class Date(Sequence):
    def __init__(self, cpf = None):
        if cpf is None:
            self._datas = {}
            self._index = 0
        else:
            try:
                request = self.validate(cpf)
            except:
                raise ValueError("Formato inválido")
            self._datas = {0: request[1]}
            self._index = 1
        self._next_index = 0
        
        
    @property
    def datas(self):
        return self._datas
    
    @datas.setter
    def datas(self, args):
        try:
            date = self.validate(args)[1]
        except ValueError:
            raise ValueError("Formato inválido")
        else:
            self._datas[self._index] = date
            self._index += 1
    
    def __repr__(self):
        if len(self._datas) > 1:
            return f"Datas: {list(map(lambda x: f'{x}', self.datas.values()))}"
        if len(self.datas) == 1:
            return f"Data: {self._datas[0]}"
        return f"Datas: {self._datas}"
    
    def __len__(self):
        return len(self._datas)
    
    def __getitem__(self, index):
        if index >= len(self._datas):
            raise IndexError
        return self._datas[index]
    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        self._next_index += 1
        return self._datas[self._next_index - 1]
        
    def add(self, date):
        try:
            self.datas = date
        except ValueError:
            raise ValueError("Formato inválido")
        
    def validate(self, date):
        try:
            # Converte a string em um objeto datetime
            datetime.strptime(date, '%d/%m/%Y')
            return True, date
        except Exception as E:
            try:
                datetime.strptime(date, '%d-%m-%Y')
                return True, date
            except Exception as E:
                try:
                    datetime.strptime(date, '%d %m %y')
                    return True, date
                except Exception as E:
                    raise ValueError("Formato inválido")


def read(date : str) -> Date:
    try:
        obj = Date(date)  
        return obj
    except ValueError:
        raise ValueError("Formato inválido")

