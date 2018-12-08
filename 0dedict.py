from struct import unpack
from zlib import decompress
import re
import sys

filename = '/System/Library/Assets/com_apple_MobileAsset_DictionaryServices_dictionaryOSX/af0109f62090a48ffb84f6acb7f3707b4eb2af92.asset/AssetData/Dutch.dictionary/Contents/Resources/Body.data'
f = open(filename, 'rb')

def gen_entry():
    f.seek(0x40)
    limit = 0x40 + unpack('i', f.read(4))[0]
    f.seek(0x60)
    while f.tell()<limit:
        sz, = unpack('i', f.read(4))
        buf = decompress(f.read(sz)[8:])

        pos = 0
        while pos < len(buf):
            chunksize, = unpack('i', buf[pos:pos+4])
            pos += 4

            entry = buf[pos:pos+chunksize]
            title = re.search('d:title="(.*?)"', entry).group(1)
            yield title, entry

            pos += chunksize

sys.stdout=open("nl_words.txt","w")
for word, definition in gen_entry():
	print(word)
sys.stdout.close()