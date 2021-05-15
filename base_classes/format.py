import os
import pickle as pk
from archivers.archiver_00 import AddZero
from archivers.huffman_archiver import Huffman
from archivers.ariphmetical_archiver import Ariphmetical
from archivers.solomon import Solomon
from base_classes.extention import Extention


class Format:
    def __init__(self):
        self.zip_methods = {'huffman': Huffman().Zip, 'none': lambda data: data,
                            'add_zero': AddZero().Zip, 'arithmetical': Ariphmetical().Zip,
                            'solomon': Solomon().Zip, }
        self.unzip_methods = {'huffman': Huffman().UnZip, 'none': lambda data: data,
                              'add_zero': AddZero().UnZip, 'arithmetical': Ariphmetical().UnZip,
                              'solomon': Solomon().UnZip, }
        self.zipped = {'name': None, 'zip_method': None, 'data': None}

        self.extention = Extention()

    def Zip(self, source, target, zip_method):
        data = open(source, mode='rb').read()

        name = os.path.basename(source)
        data = self.zip_methods[zip_method](data)
        data = self.extention.Zip(data, name, zip_method)

        open(target, mode='wb').write(data)

    def UnZip(self, source, target):
        data = open(source, mode='rb').read()

        data = self.extention.UnZip(data)
        method = data['zip_method']
        data = self.unzip_methods[method](data['data'])

        open(target, mode='wb').write(data)

def test():
    f = Format()
    sourse = r"C:\Users\ilya\Desktop\1.png"
    target = r"C:\Users\ilya\Desktop\2.txt"

    methods = ['huffman', 'none', 'add_zero', 'arithmetical', 'solomon']
    f.Zip(sourse, target, zip_method=methods[4])

    sourse = target
    target = r"C:\Users\ilya\Desktop\3.png"
    f.UnZip(sourse, target)

#test()