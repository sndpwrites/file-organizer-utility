import os,glob,shutil,sys,json

#path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
#path = 'C:\\Users\\TSEnpLT1\\Downloads\\'

class organizerFunctions:
    def __init__(self,path):
        #self.extensionDict = requests.get(url = 'https://raw.githubusercontent.com/dyne/file-extension-list/master/pub/categories.json').json()
        self.extensionDict = json.loads('{"web":"css less scss wasm ","audio":"aac aiff ape au flac gsm it m3u m4a mid mod mp3 mpa pls ra s3m sid wav wma xm ","code":"c cc class clj cpp cs cxx el go h java lua m m4 php pl po py rb rs swift vb vcxproj xcodeproj xml diff patch html js ","slide":"ppt odp ","sheet":"ods xls xlsx csv ics vcf ","image":"3dm 3ds max bmp dds gif jpg jpeg png psd xcf tga thm tif tiff ai eps ps svg dwg dxf gpx kml kmz webp ","archiv":"7z a apk ar bz2 cab cpio deb dmg egg gz iso jar lha mar pea rar rpm s7z shar tar tbz2 tgz tlz war whl xpi zip zipx xz pak ","book":"mobi epub azw1 azw3 azw4 azw6 azw cbr cbz ","text":"doc docx ebook log md msg odt org pages pdf rtf rst tex txt wpd wps ","exec":"exe msi bin command sh bat crx ","font":"eot otf ttf woff woff2 ","video":"3g2 3gp aaf asf avchd avi drc flv m2v m4p m4v mkv mng mov mp2 mp4 mpe mpeg mpg mpv mxf nsv ogg ogv ogm qt rm rmvb roq srt svi vob webm wmv yuv "}')
        self.path = path
        self.logData = ""

    def log(self,msg):
        print(msg)
        self.logData = self.logData + "\n" + msg

    def getLogData(self):
        return self.logData

    def __folderGeneratorCommon(self):
        for folder in self.extensionDict.keys():
            folderDir = os.path.join(self.path,folder)
            if not os.path.exists(folderDir):
                os.makedirs(folderDir)
                self.log('Created folder : ' + folderDir)
            yield folder, self.extensionDict[folder].split(' ')

    def __folderGeneratorSpecial(self):
        extensionList = list()
        for x in [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]:
            filename,extension = os.path.splitext(x)
            extension = extension[1:]
            extensionList.append(extension) if extension not in extensionList and extension != '' else False
        for folder in extensionList:
            folderDir = os.path.join(self.path,folder)
            if not os.path.exists(folderDir):
                os.makedirs(folderDir)
                self.log('New folder created : ' + folderDir)
            yield folder

    def __organizeCommonFiles(self):
        for folder,folderExtensions in self.__folderGeneratorCommon():
            for fileExt in folderExtensions:
                for file in glob.glob(os.path.join(self.path,'*.'+fileExt)):
                    try:
                        shutil.move(file,os.path.join(self.path,folder)+ '\\')
                        self.log('Moved file : ' + file)
                    except shutil.Error as err:
                        self.log(err)
                        #return False
        for folder in self.__folderGeneratorSpecial():
            for file in glob.glob(os.path.join(self.path,'*.'+folder)):
                try:
                    shutil.move(file,os.path.join(self.path,folder) + '\\')
                    self.log('Moved file : '+ file)
                except shutil.Error as err:
                    self.log(err)
                    #return False
        return True

    def cleaner(self):
        self.log("Cleanup started!")
        clean = self.__organizeCommonFiles()
        return clean