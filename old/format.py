import os
import pickle as pk
from archivers.archiver_00 import AddZero
from archivers.huffman_archiver import Huffman
from archivers.ariphmetical_archiver import Ariphmetical
from archivers.solomon import Solomon
from base_classes.extention import Extention


class Format:
    def __init__(self):
        self.zip_methods = {'huffman': Huffman().ZipData, 'none': lambda data: data,
                            'add_zero': AddZero().ZipData, 'arithmetical': Ariphmetical().ZipData,
                            'solomon': Solomon().ZipData, }
        self.unzip_methods = {'huffman': Huffman().UnZipData, 'none': lambda data: data,
                              'add_zero': AddZero().UnZipData, 'arithmetical': Ariphmetical().UnZipData,
                              'solomon': Solomon().UnZipData, }
        self.zipped = {'name': None, 'zip_method': None, 'data': None}

        self.extention = Extention()

    def Zip(self, source, target, zip_method):
        data = open(source, mode='rb').read()

        name = os.path.basename(source)
        data = self.zip_methods[zip_method](data)
        data = pk.dumps(data)
        data = self.extention.Zip(data, name, zip_method)

        open(target, mode='wb').write(data)

    def UnZip(self, source, target):
        data = open(source, mode='rb').read()

        data = self.extention.UnZip(data)
        method = data['zip_method']
        data = pk.loads(data['data'])
        data = self.unzip_methods[method](data)

        open(target, mode='wb').write(data)

def test():
    f = Format()
    sourse = r"C:\Users\ilya\Desktop\1.py"
    target = r"C:\Users\ilya\Desktop\2.txt"

    methods = ['huffman', 'none', 'add_zero', 'arithmetical', 'solomon']
    f.Zip(sourse, target, zip_method=methods[2])

    sourse = target
    target = r"C:\Users\ilya\Desktop\3.py"
    f.UnZip(sourse, target)

#test()