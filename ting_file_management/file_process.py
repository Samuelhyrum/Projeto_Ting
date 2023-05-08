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


def remove(instance: Queue):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        file_info = instance.dequeue()
        path_file = file_info["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")
        sys.stdout.write(f"Dados do arquivo removido: {file_info}\n")


def file_metadata(instance: Queue, position):
    try:
        archive = instance.search(position)
    except IndexError:
        sys.stderr.write("Posição inválida")
    else:
        sys.stdout.write(str(archive))
