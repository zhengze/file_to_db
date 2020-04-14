import codecs
import os
from chardet.universaldetector import UniversalDetector
import sys


def detectCode(path):
    detector = UniversalDetector()
    with open(path, 'rb') as f:
        def read_with_chunks(f):
            while True:
                chunk_data = f.read(1024*1024)
                if not chunk_data:
                    break
                yield chunk_data
        for chunk_data in read_with_chunks(f):
            detector.feed(chunk_data)
        detector.done
        detector.close()
    return detector.result['encoding']

if __name__ == '__main__':
    path = sys.argv[1]
    print(detectCode(path))

