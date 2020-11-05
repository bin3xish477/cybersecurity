; Author   : Alexis rodriguez
; Date     : 06/30/2020
; File     : mul_div.nasm
; IS       : x86 Assembly

global _start

section .text
_start:
	; unsigned r/m8 multiplicaton
	mov eax, 0x0
	
	; multiplying al by bl
	; because 10*2 can be stored with 8 bits
	; only the lower half of ax is used
	mov al, 0x10
	mov bl, 0x2
	mul bl
	
	; moving FF into al and multiplying by 2 will
	; overflow the al register and thus require
	; the ah store aditional bits	
	mov al, 0xFF
	mul bl

	; unsinged r/m8 multiplication
	mov eax, 0x0
	mov ebx, 0x0
	
	mov ax, 0x1122
	mov bx, 0x0002
	mul bx

	mov ax, 0x1122
	mov bx, 0x1122
	mul bx	
	
	; unsigned r/m32 multiplication
	mov eax, 0x11223344
	mov ebx, 0x00000002
	mul ebx
	
	mov eax, 0x11223344
	mov ebx, 0x55667788
	mul ebx
	
	; multiplication using memory locations
	mul byte [var1]
	mul word [var2]
	mul dword [var3]
	
	; divinsion using r/m16
	mov dx, 0x0
	mov ax, 0x7788
	mov cx, 0x2
	div cx
	
	mov ax, 0x7788 + 0x1
	mov cx, 0x2
	div cx

	; exit program
	mov eax, 0x1
	mov ebx, 0x0
	int 0x80

section .data
	var1: db 0x05
	var2: dw 0x1122
	var3: dd 0x11223344
