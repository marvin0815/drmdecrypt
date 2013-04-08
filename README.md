# drmdecrypt
## Synopsis
This is a UNIX(c) Port of the DRMdecrypt i found somewhere on the net. It is capable of extracting the encryption key from the .mdb file and decrypts the .srf to a standard transport stream format.

Working but slooooowwww.

## Building

There is no Makefile at the moment. You will need a C-Compiler

* gcc -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -c aes.c -o aes.o
* gcc -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -c DRMDecrypt.c -o DRMDecrypt.o
* gcc -o drmdecrypt aes.o DRMDecrypt.o

## ToDo

* Fancy output (progressbar, etc.)
* Speedup of decryption (ASM, CPU assisted)
