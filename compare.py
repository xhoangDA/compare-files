from src.args import arguments
from src import compareAlgorithms
from src import newAlgorithms
import time
from src import terminalActions

def compare():
    argValues = arguments.argsFunc()
    algorithms = compareAlgorithms
    TerminalActions = terminalActions

    filesDir1 = algorithms.getFiles(argValues[0])
    filesDir2 = algorithms.getFiles(argValues[1])

    result = algorithms.compareList(filesDir1, filesDir2)
    algorithms.writeToExcelFile(filesDir1, filesDir2, result, argValues[0], argValues[1], argValues[2], argValues[3], argValues[4])
    TerminalActions.createTable(result)

if __name__ == "__main__":
    start = time.time()
    compare()
    end = time.time()
    # maume.processing_animation(end-start)
    print("Processing time: " + str(end - start))
