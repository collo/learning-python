#!/usr/bin/env python

import tarfile


def add_to_tar(file_path, tar_file):
    tar = tarfile.open(tar_file, 'w|gz')
    tar.add(file_path)
    tar.close()

if __name__ == '__main__':
    add_to_tar('test.txt', 'test.tar.gz')
