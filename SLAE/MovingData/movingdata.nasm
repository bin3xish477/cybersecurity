; Author : Alexis Rodriguez
; Date   : 06/28/2020
; File   : movingdata.nasm
; IS     ; x86 Assembly

global _start

section .text
_start:
	; move data directly into registers
	mov eax, 0xaaaaaa
	mov al, 0xbb
	mov ah, 0xcc
	mov ax, 0xdddd

	; moving data from register to register
	mov ebx, eax
	mov cl, al
	mov ch, ah
	mov cx, ax

	mov ebx, 0
	mov ecx, 0
	
	; moving data from memory into registers
	mov al, [sample]
	mov ah, [sample+1]
	mov bx, [sample]
	mov ecx, [sample]
	
	; moving data from registers into memory
	mov eax, 0x33445566
	mov byte [sample], al
	mov word [sample], ax
	mov dword [sample], eax

	; move data into memory
	mov dword [sample], 0x33445566
	
	; lea, load effective address usage
	lea eax, [sample]
	lea ebx, [eax]

	; xchg, exchange usage
	mov eax, 0x11223344
	mov ebx, 0xaabbccdd
	xchg eax, ebx
	
	; exiting program with exit code 2
	mov eax, 0x1
	mov ebx, 0x0
	int 0x80

section .data
	sample: db 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x11, 0x22
