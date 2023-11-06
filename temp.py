import datetime
import smbclient
import magic

def write(path1, path2):
    with open(path1, 'rb') as f1:
        content = f1.read()
    with open(path2, 'wb') as f2:
        f2.write(content)
    
# write('DX Hoang_R1_20092023.xlsx', 'temp.xlsx')

def checkDir(path):
    curent_year = datetime.date.today().strftime("%Y")
    name = "DX Hoang_R1_20092023.xlsx"
    partern = 'linhtinh'
    smbclient.ClientConfig(username='sod', password='12345678@Abc')
    listPath = smbclient.listdir(path)
    # print(listPath)
    if curent_year not in listPath:
        smbclient.mkdir(r"" + path + "\\" + curent_year)
    listDeepPath = smbclient.listdir(path + "\\" + curent_year)
    if partern not in listDeepPath:
        smbclient.mkdir(r"" + path + "\\" + curent_year + "\\" + partern)
    with open(name, 'rb') as f1:
        content = f1.read()
    with smbclient.open_file(r"" + path + "\\" + curent_year + "\\" + partern + "\\" +name, mode = 'wb') as f2:
        f2.write(content)

# checkDir('10.1.36.8/shared/LAB_TO_LOCAL/DXHoang')

def detectHeader(filename):
    fileType = magic.from_file(filename)
    print(fileType)

detectHeader('instagram_brands_icon_256555.ico')