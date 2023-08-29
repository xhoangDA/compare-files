import time
import sys
from rich.console import Console
from rich.table import Table

def  createTable(resultList):
    table = Table(title="Danh sách các file đáng ngờ")
    rows = []
    for record in resultList:
        record.pop(-2)
        record.pop(3)
        record = map(str, record)
        rows.append(record)
    columns = ["STT", "File path", "Tình trạng", "Dung lượng file (KB)", "Chênh lệch so với file cũ (B)", "Chi tiết"]

    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(table)

def processing_animation(process_time):
    print("Processing...", end="", flush=True)
    puntuation = ["/", "|", "", "\\"]
    while time.time() < process_time:
        for i in puntuation:
            time.sleep(0.05)
            sys.stdout.write("\rProcessing..." + str(i))
            sys.stdout.flush()
