; Author : Alexis Rodriguez
; Date   : 06/28/2020
; File   : datatypes.asm
; IS     : IA-32

; use _start as the entry point into the program, similar to main function
global _start

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

    ; defining different data types:
    ; db, dw, dd
    var1: db 0xAA
    var2: db 0xBB, 0xCC, 0xDD
    var3: dw 0xEE, 0x00
    var4: dd 0xAABBCCDD
    var5: dd 0x112233
    var6: TIMES 6 db 0xFF      ; using TIMES to repeat a definition multiple times
	message: db "Hello World!" ; defining data that will be used in program
	mlen: equ $-message		   ; store the length of 'message' in mlen

; the .bss section stores all uninitialized data
section .bss

    ; reserving but uninitialing bytes
    var7: resb 100
    var8: resw 20

; running program
; nasm -f elf32 -o datatypes.o datatypes.asm
; ld -m elf_i386 -s -o datatypes datatypes.o
; echo $? to check if program returned 5 as expected (line 20)
