from src.args import arguments
from src import compareAlgorithms
from src import newAlgorithms
import time
from src import terminalActions
import threading

argValues = arguments.argsFunc()
algorithms = compareAlgorithms
TerminalActions = terminalActions

class thread(threading.Thread):
    def __init__(self, thread_name, hasFolder):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.hasFolder = hasFolder

        # helper function to execute the threads
    def run(self):
        TerminalActions.logic(self.thread_name, self.hasFolder)


def getFiles2Folder():
    listFiles = []
    thread1 = thread('get files',argValues[0])
    thread1.start()
    thread1.join()

    if not argValues[0]:
        filesDir1 = [['', '', '', 0, '', '']]
    else:
        filesDir1 = algorithms.getSMBFiles(argValues[0])
    filesDir2 = algorithms.getSMBFiles(argValues[1])
    listFiles.append(filesDir1)
    listFiles.append(filesDir2)

    return listFiles

def compare():
    result = []
    listFiles = getFiles2Folder()
    thread2 = thread('compare',argValues[0])
    thread2.start()
    compareResult = algorithms.compareList(listFiles[0], listFiles[1])
    result.append(listFiles[0])
    result.append(listFiles[1])
    result.append(compareResult)
    thread2.join()
    return result

def output():
    result = compare()
    algorithms.writeToExcelFile(result[0], result[1], result[2], argValues[0], argValues[1], argValues[2], argValues[3], argValues[4])
    thread3 = thread('output', argValues[0])
    thread3.start()
    thread3.join()
    TerminalActions.createTable(result[2])

if __name__ == "__main__":
    terminalActions.load_animation()
    start = time.time()
    output()
    end = time.time()
    print("Processing time: " + str(end - start))
