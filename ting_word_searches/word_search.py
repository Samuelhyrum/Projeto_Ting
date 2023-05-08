from typing import List, Dict, Any
from ting_file_management.queue import Queue


def find_word(word: str, lines: List[str]) -> List[int]:
    return [
        i+1 for i, line in enumerate(lines) if word.lower() in line.lower()]


def process_file(file: Dict) -> List[Dict]:
    return [
        {"linha": i, "conteudo": line.strip()}
        for i, line in enumerate(file["linhas_do_arquivo"], start=1)]


def exists_word(word: str, instance: Queue) -> List[Dict]:
    result = []
    for i in range(len(instance)):
        file = instance.search(i)
        occurrences = find_word(word, file["linhas_do_arquivo"])
        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": [{"linha": j} for j in occurrences]
            })
    return result


def search_by_word(word: str, instance: Queue) -> List[Dict[str, Any]]:
    results = []
    for i in range(len(instance)):
        file = instance.search(i)
        lines_with_word = [
            {"linha": line["linha"], "conteudo": line["conteudo"]}
            for line in process_file(file)
            if word.lower() in line["conteudo"].lower()
        ]
        if lines_with_word:
            results.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines_with_word
            })
    return results
