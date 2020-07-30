import os,glob,shutil,sys,json
#extensionDict = requests.get(url = 'https://raw.githubusercontent.com/dyne/file-extension-list/master/pub/categories.json').json()
extensionDict =json.loads('{"web":"css less scss wasm ","audio":"aac aiff ape au flac gsm it m3u m4a mid mod mp3 mpa pls ra s3m sid wav wma xm ","code":"c cc class clj cpp cs cxx el go h java lua m m4 php pl po py rb rs swift vb vcxproj xcodeproj xml diff patch html js ","slide":"ppt odp ","sheet":"ods xls xlsx csv ics vcf ","image":"3dm 3ds max bmp dds gif jpg jpeg png psd xcf tga thm tif tiff ai eps ps svg dwg dxf gpx kml kmz webp ","archiv":"7z a apk ar bz2 cab cpio deb dmg egg gz iso jar lha mar pea rar rpm s7z shar tar tbz2 tgz tlz war whl xpi zip zipx xz pak ","book":"mobi epub azw1 azw3 azw4 azw6 azw cbr cbz ","text":"doc docx ebook log md msg odt org pages pdf rtf rst tex txt wpd wps ","exec":"exe msi bin command sh bat crx ","font":"eot otf ttf woff woff2 ","video":"3g2 3gp aaf asf avchd avi drc flv m2v m4p m4v mkv mng mov mp2 mp4 mpe mpeg mpg mpv mxf nsv ogg ogv ogm qt rm rmvb roq srt svi vob webm wmv yuv "}')
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
