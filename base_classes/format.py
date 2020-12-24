import pickle
import re
from archivers.archiver_00 import AddZero
from archivers.huffman_archiver import Huffman
from archivers.ariphmetical_archiver import Ariphmetical
from archivers.solomon import Solomon

class Format:
    def __init__(self):
        self.zip_methods = {'huffman': Huffman().ZipData, 'none': lambda data: data,
                            'add_zero': AddZero().ZipData, 'arithmetical': Ariphmetical().ZipData,
                            'solomon': Solomon().ZipData, }
        self.unzip_methods = {'huffman': Huffman().UnZipData, 'none': lambda data: data,
                              'add_zero': AddZero().UnZipData, 'arithmetical': Ariphmetical().UnZipData,
                              'solomon': Solomon().UnZipData, }
        self.zipped = {'name': None, 'zip_method': None, 'data': None}

    def LoadZippded(self, source):
        file = open(source, 'rb')
        self.zipped = pickle.load(file)

    def LoadUnzipped(self, source):
        self.zipped['name'] = re.search(pattern=r'[^\\]+\..+', string=source).group()
        self.unzipped = open(source, 'rb').read()


    def ZipData(self, method='none'):
        self.zipped['zip_method'] = method
        method = self.zip_methods[method]

        self.zipped['data'] = method(self.unzipped)

    def UnZipData(self):
        method = self.zipped['zip_method']
        method = self.unzip_methods[method]

        self.unzipped = method(self.zipped['data'])

    def SaveZipped(self, target):
        with open(target, 'wb') as f:
            pickle.dump(self.zipped, f)

    def SaveUnZipped(self, target):
        open(target, mode='wb').write(self.unzipped)

    def UnZipFromTo(self, source, target):
        self.LoadZippded(source)
        self.UnZipData()
        self.SaveUnZipped(target)

    def ZipFromTo(self, source, target, zip_method='none'):
        self.LoadUnzipped(source)
        self.ZipData(zip_method)
        self.SaveZipped(target)

def test():
    f = Format()
    sourse = r"C:\Users\ilya\Desktop\1.txt"
    target = r"C:\Users\ilya\Desktop\2.txt"

    methods = ['huffman', 'none', 'add_zero', 'arithmetical', 'solomon']
    f.ZipFromTo(sourse, target, zip_method=methods[4])

    sourse = target
    target = r"C:\Users\ilya\Desktop\3.txt"
    f.UnZipFromTo(sourse, target)

#test()