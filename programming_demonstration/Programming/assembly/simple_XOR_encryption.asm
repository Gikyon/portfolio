
include emu8086.inc

org 100h

;asking for input               
mov dx, 26
lea di, string                              
call GET_STRING

putc 0ah
putc 0dh

mov cx, 26 
lea si, string

; comparing first index
CMP string, 'M'
JE encryptM_key

;encrypt if it does not start with M
encryptKey:
xor [si], key
inc si
loop encryptkey
mov control, 'k'
jmp print

;encrypt if it does start with M
encryptM_key:
xor [si], m_key
inc si
loop encryptM_key
mov control, 'm'
 
;print the string 
print:
lea si, string
call PRINT_STRING
putc 0ah
putc 0dh

lea si,string
mov cx, 26
; comparing for decryption
CMP control, 'm'
je decryptM_key

decryptKey:
xor [si], key
inc si
loop decryptKey
jmp print2

decryptM_key:
xor [si], m_key
inc si
loop decryptM_key

print2:
lea si,string
call PRINT_STRING

 


ret 
control db ?
string db 25 dup (0)
m_key EQU 25
key EQU 53
define_GET_STRING
define_PRINT_STRING



