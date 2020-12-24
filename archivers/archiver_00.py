import re
from base_classes.base_archiver import Archiver


class AddZero(Archiver):
    #{size , data}
    def ZipData(self, data):
        data = [bin(ch)[2:] for ch in data]

        for i, __ in enumerate(data):
            while len(data[i]) < 8:
                data[i] = '0' + data[i]

            data[i] += '00'

        data = ''.join(data)
        added_zero_count = 0
        while len(data) % 8 != 0:
            data += '0'
            added_zero_count += 1

        data = re.findall(pattern=r'\d{1,8}', string=data)

        data = bytes([int(b, 2) for b in data])

        return {'data': data, 'added_zero_count': added_zero_count}


    def UnZipData(self, data):
        added_zero_count = data['added_zero_count']
        data = [bin(ch)[2:] for ch in data['data']]

        for i, __ in enumerate(data):

            while len(data[i]) < 8:
                data[i] = '0' + data[i]

        data = ''.join(data)
        data = re.findall(pattern=r'\d{1,10}', string=data[: -added_zero_count])

        data = [d[:-2] for d in data]
        data = bytes([int(b, 2) for b in data])

        return data

