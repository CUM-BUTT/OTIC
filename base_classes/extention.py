
class Extention:
    extention_name = b'ext'
    # {
    # имя расширения (3 байта),
    # длина имени файла (4 байта), имя файла,
    # длина метода архивации (4 байта), метод архивации,
    # сам файл
    # }


    def Zip(self, data: bytes, filename: str, zip_method: str):
        zipped = self.extention_name + \
                 len(filename).to_bytes(4, byteorder="little", signed=False) + \
                 bytes(filename, encoding='utf-8') + \
                 len(zip_method).to_bytes(4, byteorder="little", signed=False) + \
                 bytes(zip_method, encoding='utf-8') + \
                 data

        return zipped

    def UnZip(self, data: bytes):
        if data[:len(self.extention_name)] == self.extention_name:
            ext = data[:len(self.extention_name)]

            current_byte = len(self.extention_name)
            file_name_len = data[current_byte: current_byte + 4]
            file_name_len = int.from_bytes(file_name_len, byteorder='little', signed=False)

            current_byte += 4
            file_name = data[current_byte: current_byte + file_name_len]
            file_name = str(file_name, encoding='utf-8')

            current_byte += file_name_len
            zip_method_len = data[current_byte: current_byte + 4]
            zip_method_len = int.from_bytes(zip_method_len, byteorder='little', signed=False)

            current_byte += 4
            zip_method = data[current_byte: current_byte + zip_method_len]
            zip_method = str(zip_method, encoding='utf-8')

            current_byte += zip_method_len
            data = data[current_byte:]

            return {'ext': ext, 'name': file_name, 'zip_method': zip_method, 'data': data}





def Test():
    e = Extention()
    d = e.Zip(b'data', 'filename', 'none')
    print(d)
    d = e.UnZip(d)
    print(d)

