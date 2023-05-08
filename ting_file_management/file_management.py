import sys


def txt_importer(file_path):
    # Verifica a extensão do arquivo
    if not file_path.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
        return []
    
    try:
        with open(file_path, 'r') as file:
            # Lê o conteúdo do arquivo e retorna como lista
            return file.read().splitlines()
    except FileNotFoundError:
        print(f'Arquivo {file_path} não encontrado', file=sys.stderr)
        return []
