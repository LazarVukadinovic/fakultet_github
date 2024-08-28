import zipfile, os

primer_zip = zipfile.ZipFile('zipFajl.zip')
files = primer_zip.namelist()

for file in files:
    fileInfo = primer_zip.getinfo(file)
    print(f'File {file} => size: {fileInfo.file_size}, zip size: {fileInfo.compress_size}')
primer_zip.close()