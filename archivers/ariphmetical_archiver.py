from base_classes.base_archiver import Archiver


class Segment:
    left = 0
    right = 0

class SegmentDecode(Segment):
    character = None

class Ariphmetical(Archiver):
    chunk = 20

    def define_segments(self, letters, probability):
        l = 0
        segments = {letter: Segment() for letter in letters}


        for i in range(len(letters)):
            segments[letters[i]].left = l
            segments[letters[i]].right = l + probability[i]
            l = segments[letters[i]].right
        return segments


    def ZipChunk(self, bytes):
            bytes = bytearray(bytes)
            size = len(bytes)
            #probability = [bytes.count(i) for i in (set(list(bytes)))]


            segments = self.define_segments(self.letters, self.probability)
            left = .0
            right = 1.0

            for i, ch in enumerate(bytes):
                symb = bytes[i]
                new_right = left + (right - left) * (segments[symb].right)
                new_left = left + (right - left) * (segments[symb].left)
                left = new_left
                right = new_right

            data = (left + right) / 2

            return data


    def define_segments_decode(self, letters, probability):
        l = 0
        segments = [SegmentDecode() for __, __ in enumerate(letters)]

        for i, letter in enumerate(letters):
            segments[i].left = l
            segments[i].right = l + probability[i]
            segments[i].character = letter
            l = segments[i].right

        return segments


    def UnZipChunk(self, chunk, chunk_size):
        segments = self.define_segments_decode(self.letters, self.probability)
        s = []

        for i in range(chunk_size):
            for j, __ in enumerate(self.letters):
                if segments[j].left <= chunk < segments[j].right:
                    s.append(segments[j].character)
                    chunk = (chunk - (segments[j].left)) / (segments[j].right - segments[j].left)
                    break
        return bytes(s)

    def ZipData(self, bytes):
        self.letters = list(set(list(bytes)))
        self.probability = [bytes.count(i) / len(bytes) for i in (set(list(bytes)))]

        chunks = [bytes[begin:begin + self.chunk] for begin in range(0, len(bytes), self.chunk)]

        return {'data': [self.ZipChunk(ch) for ch in chunks],
                'letters': self.letters, 'probability': self.probability,
                'chunk_size': len(chunks[0]), 'last_size': len(chunks[-1])}

    def UnZipData(self, data):
        self.letters = data['letters']
        self.probability = data['probability']
        chunks = [self.UnZipChunk(chunk, data['chunk_size']) for chunk in data['data'][:-1]] + \
                 [self.UnZipChunk(data['data'][-1], data['last_size'])]
        decoded = b''.join(chunks)
        return decoded


def main():
    string = b'iuhdad/ wlk   ;m;awlkdj kawdawdddd135165 65454d  dadwa ddad awdawdaw daddadwaa;k;opoopkpj;;l4lj ankjdnawkdn'
    print(string)
    a = Ariphmetical()
    res = a.ZipData(string)
    print(res)
    res = a.UnZipData(res)
    print(res)
#main()
