#!/bin/bash

echo '[+] Assemblying file with Nasm...'
nasm -f elf32 -o $1.o $1.nasm
echo '[+] Successfuly assembled file...'

echo '[+] Beginning the linking process...'
ld -m elf_i386 -o $1 $1.o
echo '[+] Successfully linked all file references...'
