import os
import openpyxl 
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils import get_column_letter
import smbclient
import magic

# from smb.SMBHandler import SMBHandler
# from src import banner

def getSMBFiles(dir_path):
    listFiles = []
    smbclient.ClientConfig(username='sod', password='12345678@Abc')
    try:
        for path, subdirs, files in smbclient.walk(dir_path):
            for name in files:
                filePath = os.path.join(path, name)
                relativePathDir = filePath.replace(dir_path,"").replace("/","\\")
                pathWithoutFilename = relativePathDir.replace(name,"")
                # hàm lấy giá trị filesize (đơn vị byte)
                fileSize = smbclient.stat(filePath).st_size
                element = [pathWithoutFilename, name, relativePathDir, fileSize]
                listFiles.append(element)
        # listToStr = '\n'.join([str(elem) for elem in listFiles])
        # with open("temp.txt", 'w', encoding="utf-8") as f:
        #     f.write(listToStr)
        # print(list(enumerate(listFiles)))
    except FileNotFoundError:
        print(f"The directory {dir_path} does not exist")
    except PermissionError:
        print(f"Permission denied to access the directory {dir_path}")
    except OSError as e:
        print(f"An OS error occurred: {e}")
    return listFiles
# Note: Chưa xử lý đc chỗ điều kiện exception


# function to get all files recursively on the diretory 
def getFiles(dir_path):
    listFiles = []
    try:
        for path, subdirs, files in os.walk(dir_path):
            for name in files:
                filePath = os.path.join(path, name)
                relativePathDir = filePath.replace(dir_path,"")
                pathWithoutFilename = relativePathDir.replace(name,"")
                # hàm lấy giá trị filesize (đơn vị byte)
                fileSize = os.stat(filePath).st_size
                element = [pathWithoutFilename, name, relativePathDir, fileSize]
                listFiles.append(element)
    except FileNotFoundError:
        print(f"The directory {dir_path} does not exist")
    except PermissionError:
        print(f"Permission denied to access the directory {dir_path}")
    except OSError as e:
        print(f"An OS error occurred: {e}")
    return listFiles
# Note: Chưa xử lý đc chỗ điều kiện exception


def compareList(list1, list2):
    result = []
    serial = 0
    cloneList1 = list1.copy()
    cloneList2 = list2.copy()
    for i in cloneList2:
        for j in cloneList1:
            if i[2] == j[2]:
                # So sánh file trước và file sau
                changedSize = i[3]-j[3]
                # Nếu dung lượng không thay đổi -> bỏ qua
                if changedSize == 0:
                    cloneList1.remove(j)
                    break
                # Nếu dung lượng file thay đổi -> lưu bản ghi
                else:
                    serial += 1
                    # Đổi đơn vị từ byte thành KB
                    oldSizeKB = round (j[3] / 1024, 2) 
                    newSizeKB = round (i[3] / 1024, 2)
                    status = "Sửa" 
                    note = checkFilesWithLargeFilesize(status, changedSize, oldSizeKB)
                    element =  [serial, j[2], status, oldSizeKB, newSizeKB, changedSize, "Thay đổi thông tin", note]
                    result.append(element)
                    cloneList1.remove(j)
                    break
            else:
                if j == cloneList1[-1]:
                    serial += 1
                    filesizeKB = round (i[3] / 1024, 1)
                    status = "Thêm mới" 
                    note = checkFilesWithLargeFilesize(status, i[3], None)
                    element =  [serial, i[2], status, None, filesizeKB, i[3], "Tạo mới", note]
                    result.append(element)
                    break
                else:
                    continue
    for k in cloneList1:
        serial += 1
        filesizeKB = round (k[3] / 1024, 1)
        element =  [serial, k[2],"Xóa", filesizeKB, None, -k[3], "Không còn sử dụng", note]
        result.append(element)

    return result


def countFiles(listFiles):
    return str(len(listFiles))

def totalSize(listFiles):
    total = 0
    for i in listFiles:
        total += i[3]
    totalMB = round(total / (1024*1024), 4)
    return str(totalMB)

# Function check files with large filesize
def checkFilesWithLargeFilesize(status, sizeChange, oldSize):
    warning = None
    sizeChangeKB = round(sizeChange / 1024, 2)
    if status == "Thêm mới":
            if sizeChangeKB > 1024:
               warning = "File có kích thước lớn: " +  '{:.2f}'.format(sizeChangeKB) + " (KB)"
    elif status == "Sửa":
            # If the file already exists, check if the file size after editing is more than 15%, then give a warning
            if (oldSize >= 1024 and  sizeChangeKB > (oldSize * 15 / 100)) or (oldSize < 1024 and sizeChangeKB > (oldSize * 50 / 100)):
                warning = "File sau khi chỉnh sửa có kích thước lớn hơn nhiều so với file cũ: " + '{:.2f}'.format(sizeChangeKB) + " (KB)"
    return warning

def writeToExcelFile(filesDir1, filesDir2, resultList, dir1, dir2, version, productName, outputFile):
    wb = openpyxl.Workbook()
    # wb = openpyxl.load_workbook(outputFile)
    ws = wb.active
    ws["A1"] = "BẢNG KHAI BÁO CẤU TRÚC VÀ DUNG LƯỢNG PHÁT HÀNH SẢN PHẨM: " + productName
    ws.merge_cells("A1:H1")
    ws["A2"] = "Phiên bản:"
    ws["B2"] = dir1
    ws["F2"] = "Số files: " +  countFiles(filesDir1) + " - Dung lượng: " + totalSize(filesDir1) + "MB"
    ws["B3"] = dir2
    ws["F3"] = "Số files: " +  countFiles(filesDir2) + " - Dung lượng: " + totalSize(filesDir2) + "MB"
    fieldNames = ["STT", version, "Tình trạng", "Dung lượng cũ (KB)", "Dung lượng mới (KB)", "Chênh lệch (B)", "Mục đích sử dụng", "Ghi chú"]
    ws.append(fieldNames)
    for i in resultList:
        ws.append(i)

    # Create a few styles
    center_aligned_text = Alignment(horizontal="center", vertical="center")
    big_bold_blue_font = Font(color = '173B9E', bold=True, size = 14)
    double_border_side = Side(border_style='thin')
    square_border = Border(top=double_border_side,right=double_border_side,bottom=double_border_side,left=double_border_side)
    bold12 = Font(bold=True, size = 12)
    gray_background = PatternFill('solid', start_color = 'B1B1B2')
    pink_background = PatternFill('solid', start_color = 'FFCBCB')

    ws["A1"].font = big_bold_blue_font
    ws["A1"].alignment = center_aligned_text
    ws["A2"].font = bold12
    ws.row_dimensions[4].height = 28

    for cell in ws[4]:
        cell.font = bold12
        cell.fill = gray_background
        cell.border = square_border
        cell.alignment = center_aligned_text

    for i in range (4, ws.max_row+1):
        ws["A"+ str(i)].alignment = center_aligned_text
    
    for i in range (5, ws.max_row+1):
        if ws['H' + str(i)].value is not None:
            for cell in ws[i]:
                cell.fill = pink_background

    # Custom column width size
    ws.column_dimensions["A"].width = len(ws["A2"].value) + 2


    columns = ['B', 'C', 'D', 'E', 'F', 'G', 'H']
    for index, column_letter in enumerate(columns):
        values = [ws.cell(row=i,column=index+2).value for i in range(1,ws.max_row+1)]
        max_width = 0
        for value in values:
            if value == None: continue
            elif max_width <= len(str(value)): max_width = len(value) + 8
        ws.column_dimensions[str(column_letter)].width = max_width
    
    wb.save(filename=outputFile)

def detectHeaderFile(pathToFile):
    
    # fileType = magic.from_file(pathToFile)
    fileType = magic.from_file(pathToFile)
    # fileType = magic.from_buffer(open(pathToFile, "rb").read(2048))
    return fileType