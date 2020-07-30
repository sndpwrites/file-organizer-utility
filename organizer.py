import os,glob,shutil,sys
extensionList = list()
path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
def folderGenerator():
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
                              
for folder,folderDir in folderGenerator():
    for file in glob.glob(os.path.join(path,'*.'+folder)):
        try:
            shutil.move(file,folderDir+ '\\')
            print('Moved file : ',file)
        except shutil.Error as err:
            print(err)
