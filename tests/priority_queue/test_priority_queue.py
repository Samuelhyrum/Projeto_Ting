from ting_file_management.priority_queue import PriorityQueue
import pytest

archive_1 = {
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 8,
    "linhas_do_arquivo": [...]
}

archive_2 = {
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 8,
    "linhas_do_arquivo": [...]
}

archive_3 = {
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 2,
    "linhas_do_arquivo": [...]
}


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue(archive_1)
    priority_queue.enqueue(archive_2)

    assert priority_queue.dequeue() == archive_2

    priority_queue.enqueue(archive_3)

    assert priority_queue.search(len(priority_queue) - 1) == archive_2

    with pytest.raises(IndexError):
        priority_queue.search(10)
