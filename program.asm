    mov d,1
increase:
    inc d
    cmp d,5
    jo increase
decrease:
    dec d
    cmp d,0
    jz increase
    jmp decrease

    hlt