; Author : Alexis Rodriguez
; Date   : 06/28/2020
; File   : hello.asm
; IS     : IA-32

global _start ; use _start as the entry point into the program, similar to main function

; the .text section contains the body of our code
section .text
_start:
	; print hello world to stdout
	mov eax, 0x4 		; system call, write
	mov ebx, 0x1 		; file descriptor 1, stdout
	mov ecx, message 	; move address of message variable into ecx reg.
	mov edx, mlen		; compute the message length
	int 0x80			; invoke system call

	; exiting program
	mov eax, 0x1 		; system call, exit
	mov ebx, 0x5		; return 5 after running
	int 0x80			; invoke system call

; the .data section all initialized data
section .data
	message: db "Hello World!" ; defining data that will be used in program
	mlen: equ $-message		   ; store the length of 'message' in mlen

; running program
; nasm -f elf32 -o hello.o hello.asm
; ld -m elf_i386 -s -o hello hello.o
; echo $? to check if program returned 5 as expected (line 20)