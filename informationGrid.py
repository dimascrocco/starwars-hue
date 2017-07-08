import numpy as np

import sys
import StringIO

import zlib



def create_grid_information(img, a=2):
    lx = int(len(img)/a)
    ly = int(len(img[1])/a)
    kolmogorovGrid = np.zeros_like(entropyGrid)
    for i in range(lx - a):
        for j in range(ly-a):
            imgS = img[i*a:i*a+a, j*a:j*a+a]
            kolmogorovGrid[i][j] = image_kolmogorov_gzip(imgS.flatten())
    return kolmogorovGrid


def image_kolmogorov_gzip(imgString):

    getKbytes = lambda s: sys.getsizeof(s)/100000.
    #zlib.compress('asdf')
    #print(getKbytes(zlib.compress(imgString)))
    #exi
    return getKbytes(zlib.compress(imgString))

#extraido de ...nao lembro
def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    # in Python 3: dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):
    """Decompress a list of output ks to a string."""
    #
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    # in Python 3: dictionary = {i: chr(i) for i in range(dict_size)}

    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()

