import os,glob,shutil,sys,requests,json
extensionDict = requests.get(url = 'https://raw.githubusercontent.com/dyne/file-extension-list/master/pub/categories.json').json()

path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
def folderGeneratorCommon():
    for folder in extensionDict.keys():
        folderDir = os.path.join(path,folder)
        if not os.path.exists(folderDir):
            os.makedirs(folderDir)
            print('Created folder : ',folderDir)
        yield folder, extensionDict[folder]
def folderGeneratorSpecial():
    for x in [f for f in os.listdir() if os.path.isfile(os.path.join(path, f))]:
        filename,extension = os.path.splitext(x)
        extension = extension[1:]
        extensionList.append(extension) if extension not in extensionList and extension != '' else False
    for folder in extensionList:
        folderDir = os.path.join(path,folder)
        if not os.path.exists(folderDir):
            os.makedirs(folderDir)
            print('New folder created : ',folderDir)
            yield folder,folderDir
        else:
            yield folder,folderDir
def organizeCommonFiles():
    for folder,folderExtensions in folderGeneratorCommon():
        for file in glob.glob(os.path.join(path,'*.'+folderExtensions)):
            try:
                shutil.move(file,os.path.join(path,folder)+ '\\')
                print('Moved file : ',file)
            except shutil.Error as err:
                print(err)
def organizeSpecialFiles():
    specialFolder = os.path.join(path,'others')
    os.makedirs(specialFolder) if not os.path.exists(specialFolder) else True
    for file in [f for f in os.listdir() if os.path.isfile(os.path.join(path, f))]:
        try:
            shutil.move(os.path.join(path,file),specialFolder+'\\')
            print('Moved file : ',file)
        except shutil.Error as err:
            print(err)
organizeCommonFiles()
organizeSpecialFiles()
