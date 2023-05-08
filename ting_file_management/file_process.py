from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    read_archives = [
        instance.search(i)[
            "nome_do_arquivo"] for i in range(len(instance))]
    if path_file not in read_archives:
        try:
            file = txt_importer(path_file)
            archive = {
                "nome_do_arquivo": path_file,
                "qtd_linhas": len(file),
                "linhas_do_arquivo": file,
            }
            instance.enqueue(archive)
            sys.stdout.write(str(archive))
        except ValueError:
            print(f"Formato inválido do arquivo {path_file}.")
    else:
        print(f"Arquivo {path_file} já processado anteriormente.")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
