import huffman
import pickle
import re
import sys
import pandas as pd

from base_classes.base_archiver import Archiver


class Huffman(Archiver):
    def ZipFromTo(self, source, target):
        text = open(source, mode='rb').read()

        text = self.ZipData(text)

        with open(target, 'wb') as f:
            pickle.dump(text, f)

    def UnZipFromTo(self, source, target):
        file = open(source, 'rb')
        file = pickle.load(file)

        file = self.UnZipData(file)

        open(target, mode='wb').write(file)


    def ZipData(self, file):
        out = {}
        out['size'] = len(file)

        # get dict
        dic = huffman.codebook(
            pd.DataFrame({'value': bytearray(file)}).
                groupby('value').value.
                count().items())

        # get reversed dict for decoding
        out['dict'] = dict(zip(dic.values(), dic.keys()))

        # get huffman code
        data = ''.join([dic[ch] for ch in file])

        # get bytes
        data = re.findall(pattern=r'\d{1,8}', string=data)
        while len(data[-1]) < 8:
            data[-1] += '0'
        print(data)

        out['data'] = bytes([int(b, 2) for b in data])

        return out


    def UnZipData(self, file):
        # remove unuseful
        huf_code = [bin(ch)[2:] for ch in file['data']]
        for i in range(len(huf_code)):
            while(len(huf_code[i]) < 8):
                huf_code[i] = '0' + huf_code[i]

        huf_code = ''.join(huf_code)
        key = ''
        decoded = []
        for bit in huf_code:
            key += bit
            if key in file['dict']:
                decoded += [file['dict'][key]]
                key = ''
            if len(decoded) == file['size']:
                break

        decoded = bytes(decoded)

        return decoded







