from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = list()

    def __len__(self):
        """Retorna o tamanho da fila"""
        return len(self._data)

    def enqueue(self, value):
        """Insere um elemento no final da fila"""
        self._data.append(value)

    def dequeue(self):
        """Remove o elemento do início da fila e o retorna"""
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        """Retorna o elemento correspondente ao índice passado como parâmetro"""
        if index < 0 or index >= len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]
