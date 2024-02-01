include emu8086.inc

org 100h

;asking for an input
mov dx,60
lea di, string ; string 
call GET_STRING
putc 0ah
putc 0dh

mov dx,di
mov flag, 1

word_set:
mov di,dx
lea si,word ; word
;scanning for word
word_loop1:
mov al,[di]
cmp al, ' ' ; if space
je space
cmp al, 0 ; if endl
je space_last
mov [si], al
inc di
inc si 
inc counter
jmp word_loop1 ; loop

; saving checkpoint and reseting si


space:
inc di
mov dx,di ; checkpoint for string
jmp algorithm

space_last:
mov al, [si]
cmp al, 0
mov flag, 0


algorithm:
lea di, word
mov cx, di
dec si

run:
cmp cx, si
je true
mov al,[si]
mov bl,[di]

cmp al,bl
jne err ; if it's different
inc di
dec si
jmp run

true:
inc count
jmp err

print:
add count, '0'
lea si, count
call PRINT_STRING
putc " " 
lea si, positive
call PRINT_STRING
putc 0ah
putc 0dh
jmp return
 




err:
mov cl, flag
cmp cl, 1
je word_set
cmp count, 0
jg print
lea si, negative
call PRINT_STRING
putc 0ah
putc 0dh 
jmp return


return:
ret
DEFINE_GET_STRING
DEFINE_PRINT_STRING
string db 60 dup(0)
compare db 10 dup(0)
word db 10 dup(0)
negative db "no palindrome",0
positive db "palindrome" ,0  
counter dw 0
flag db 0 
count db 0, 0




