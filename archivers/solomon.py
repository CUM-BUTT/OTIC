import unireedsolomon as rs
from base_classes.base_archiver import Archiver

class Solomon(Archiver):
    unzipped_chunk_size = 200
    zipped_chunk_size = 250

    def ZipChunk(self, chunk):
        lenght = len(chunk)
        coder = rs.RSCoder(self.zipped_chunk_size, lenght)
        coded = coder.encode_fast(chunk)#coder.encode(chunk)
        return coded

    def UnZipChunk(self, chunk, unzipped_chunk_size, zipped_chunk_size):
        coder = rs.RSCoder(zipped_chunk_size, unzipped_chunk_size)
        return coder.decode_fast(chunk)[0]#coder.decode(chunk)[0]


    def ZipData(self, data):
        unzipped_chunks = [data[begin:begin + self.unzipped_chunk_size]
                           for begin in range(0, len(data), self.unzipped_chunk_size)]
        last_size =  len(unzipped_chunks[-1])
        chunks = [self.ZipChunk(ch) for ch in unzipped_chunks]
        data = ''.join(chunks)
        return {'data': data, 'unzipped_chunk_size': self.unzipped_chunk_size,
                'last_unzipped_size': last_size, 'zipped_size': self.zipped_chunk_size, }

    def UnZipData(self, data):
        chunk_size = data['unzipped_chunk_size']
        last_chunk = data['last_unzipped_size']
        new_chunk = data['zipped_size']

        chunks = [data['data'][begin:begin + new_chunk]
                  for begin in range(0, len(data['data']), new_chunk)]
        chunks = [self.UnZipChunk(ch, chunk_size, new_chunk) for ch in chunks[:-1]] + \
                 [self.UnZipChunk(chunks[-1], last_chunk, new_chunk)]
        decoded = ''.join(chunks)

        return decoded.encode('utf-8')


def test():
    s = Solomon()
    data = b'adwdwa dadawd adwad awd da d 1234567890=-= dawd aw; dk;awjd;awdj awda-*/-*/**wdawdawd'
    print(data)

    data = s.ZipData(data)
    data['data'] = '312oo' + data['data'][5:]
    print(repr(data['data']))

    data = s.UnZipData(data)
    print(data)

#test()