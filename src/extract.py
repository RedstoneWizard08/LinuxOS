#!/usr/bin/env python3.8

'''Extracts files recursively.'''
import os
import tarfile
import shutil


def extract(root: str, target: str):
    '''Extracts files recursively to a target directory.'''

    if not os.path.exists(target):
        os.mkdir(target)

    for directory in os.listdir(root):
        if directory.startswith(".") or os.path.isfile(directory):
            continue

        for subdir in os.listdir(root + "/" + directory):
            if subdir.startswith(".") or os.path.isfile(subdir):
                continue

            for file in os.listdir(root + "/" + directory + "/" + subdir):
                if file.startswith("."):
                    continue

                if not (
                    os.path.isfile(file) or
                    file.endswith(".gz") or
                    file.endswith(".xz") or
                    file.endswith(".bz2")
                ):
                    if file.endswith(".patch"):
                        fullpath = root + "/" + directory + "/" + subdir + "/" + file
                        targetpath = target + "/" + directory + "/" + subdir + "/" + file

                        if not os.path.exists(targetpath):
                            print(f"Copying {file}...")
                            shutil.copyfile(fullpath, targetpath)
                        
                        continue

                fullpath = root + "/" + directory + "/" + subdir + "/" + file
                targetpath = target + "/" + directory + "/" + subdir

                if not os.path.exists(targetpath):
                    print(f"Extracting {file}...")
                    if file.endswith(".tar.gz"):
                        tarball = tarfile.open(fullpath, "r:gz")
                        tarball.extractall(targetpath)
                        tarball.close()
                    elif file.endswith(".tar.xz"):
                        tarball = tarfile.open(fullpath, "r:xz")
                        tarball.extractall(targetpath)
                        tarball.close()
                    elif file.endswith(".tar.bz2"):
                        tarball = tarfile.open(fullpath, "r:bz2")
                        tarball.extractall(targetpath)
                        tarball.close()
