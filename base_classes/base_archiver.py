import pickle as pk
class Archiver:
    def ZipData(self, data):
        pass

    def UnZipData(self, data):
        pass

    def Zip(self, data):
        data = self.ZipData(data)
        data = pk.dumps(data)
        return data

    def UnZip(self, data):
        data = pk.loads(data)
        data = self.UnZipData(data)
        return data