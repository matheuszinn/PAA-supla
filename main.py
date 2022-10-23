import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

from pathlib import Path
from sorting_algos import (
    Quicksort,
    Mergesort,
    CombSort,
    BubbleSort,
    Shellsort,
    InsertionSort,
)
from rich.progress import (
    BarColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
)

from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress

import pandas as pd

INPUT_DIR = Path(__file__).parent.resolve() / "inputs"
ALGORITMOS = [
    {
        "name": "Bubblesort",
        "fn": BubbleSort().bubble_sort
    },
    {
        "name": "Insertionsort",
        "fn": InsertionSort().insertion_sort
    },
    {
        "name": "Shellsort",
        "fn": Shellsort().shellsort
    },
    {
        "name": "Combsort",
        "fn": CombSort().combsort
    },
    {
        "name": "Quicksort",
        "fn": Quicksort().quicksort
    },
    {
        "name": "Mergesort",
        "fn": Mergesort().merge_sort
    },
]


def extract_file_name(fp):
    return str(fp).split("/")[-1]


def create_data_dict(tam_lista, algoritmo, tipo_lista, tempo, comparacoes,
                     trocas):
    return {
        "tam_lista": tam_lista,
        "algoritmo": algoritmo,
        "tipo_lista": tipo_lista,
        "tempo": tempo,
        "comparacoes": comparacoes,
        "trocas": trocas,
    }


def read_input_file(f):
    with open(f) as file:
        return list(map(lambda x: int(x), file.read()[1:-1].split(" ")))


progress = Progress(TimeElapsedColumn(), BarColumn(),
                    TextColumn("{task.description}"))

table = Table.grid()
table.add_row(
    Panel.fit(
        progress,
        title="Progresso Total",
        border_style="green",
        padding=(2, 2),
        width=200,
    ))

if __name__ == "__main__":
    # A pasta inputs não vai estar no diretório do programa, use os arquivos do repositório "PAA-generator"
    files_paths = sorted(INPUT_DIR.glob("*"))

    execution_data = pd.DataFrame(
        {},
        columns=[
            "tam_lista",
            "algoritmo",
            "tipo_lista",
            "tempo",
            "comparacoes",
            "trocas",
        ],
    )
    with Live(table, refresh_per_second=10):
        t1 = progress.add_task("", total=len(files_paths))
        console = progress.console

        while not progress.finished:

            for idx, file in enumerate(files_paths):
                file_name = extract_file_name(file)
                tipo_lista, tam_lista = (
                    lambda x: (x.split("_")[0], x.split("_")[1]))(file_name)
                for algo in ALGORITMOS:
                    algo_name = algo["name"]

                    progress.update(
                        t1,
                        description=f"{file_name}-{idx}/{len(files_paths)}",
                    )

                    exec_info = algo["fn"](read_input_file(file))[1]
                    full_exec_data = create_data_dict(
                        tam_lista,
                        algo_name,
                        tipo_lista,
                        exec_info["time"],
                        exec_info["comparacoes"],
                        exec_info["troca"],
                    )
                    execution_data = execution_data.append(full_exec_data,
                                                           ignore_index=True)
                    console.log(
                        f"Finalizando arquivo {file_name} com algoritmo {algo_name}"
                    )
                progress.update(t1, advance=1)

    execution_data.to_csv("execution_data.csv")
    print("Terminado!")
