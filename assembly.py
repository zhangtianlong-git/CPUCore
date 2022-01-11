import pin

FETCH = [
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.IR_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.DST_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.SRC_IN | pin.PC_INC,
]

MOV = (0 << pin.ADDR2_SHIFT) | pin.ADDR2
ADD = (1 << pin.ADDR2_SHIFT) | pin.ADDR2
SUB = (2 << pin.ADDR2_SHIFT) | pin.ADDR2
CMP = (3 << pin.ADDR2_SHIFT) | pin.ADDR2
AND = (4 << pin.ADDR2_SHIFT) | pin.ADDR2
OR = (5 << pin.ADDR2_SHIFT) | pin.ADDR2
XOR = (6 << pin.ADDR2_SHIFT) | pin.ADDR2

INC = (0 << pin.ADDR1_SHIFT) | pin.ADDR1
DEC = (1 << pin.ADDR1_SHIFT) | pin.ADDR1

NOT = (2 << pin.ADDR1_SHIFT) | pin.ADDR1
JMP = (3 << pin.ADDR1_SHIFT) | pin.ADDR1

JO = (4 << pin.ADDR1_SHIFT) | pin.ADDR1
JNO = (5 << pin.ADDR1_SHIFT) | pin.ADDR1
JZ = (6 << pin.ADDR1_SHIFT) | pin.ADDR1
JNZ = (7 << pin.ADDR1_SHIFT) | pin.ADDR1
JP = (8 << pin.ADDR1_SHIFT) | pin.ADDR1
JNP = (9 << pin.ADDR1_SHIFT) | pin.ADDR1

HLT = 0x3f
NOP = 0

INSTRUCTIONS = {
    2: {
        MOV: {
            # e.g., mov a,5
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_W | pin.SRC_OUT,
            ],
            # e.g., mov a,b
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_W | pin.SRC_R,
            ],
            # e.g., mov a, [5]
            (pin.AM_REG, pin.AM_DIR): [
                pin.SRC_OUT | pin.MAR_IN,
                pin.DST_W | pin.RAM_OUT,
            ],
            # e.g., mov a, [b]
            (pin.AM_REG, pin.AM_RAM): [
                pin.SRC_R | pin.MAR_IN,
                pin.DST_W | pin.RAM_OUT,
            ],

            # e.g., mov [5], 1
            (pin.AM_DIR, pin.AM_INS): [
                pin.DST_OUT | pin.MAR_IN,
                pin.SRC_OUT | pin.RAM_IN,
            ],
            # e.g., mov [5], a
            (pin.AM_DIR, pin.AM_REG): [
                pin.DST_OUT | pin.MAR_IN,
                pin.SRC_R | pin.RAM_IN,
            ],
            # mov [5], [1]
            (pin.AM_DIR, pin.AM_DIR): [
                pin.SRC_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_OUT | pin.MAR_IN,
                pin.T1_OUT | pin.RAM_IN,
            ],
            # mov [5], [a]
            (pin.AM_DIR, pin.AM_RAM): [
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_OUT | pin.MAR_IN,
                pin.T1_OUT | pin.RAM_IN,
            ],

            # e.g., mov [a], 1
            (pin.AM_RAM, pin.AM_INS): [
                pin.DST_R | pin.MAR_IN,
                pin.SRC_OUT | pin.RAM_IN,
            ],
            # e.g., mov [a], b
            (pin.AM_RAM, pin.AM_REG): [
                pin.DST_R | pin.MAR_IN,
                pin.SRC_R | pin.RAM_IN,
            ],
            # mov [a], [1]
            (pin.AM_RAM, pin.AM_DIR): [
                pin.SRC_OUT | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_R | pin.MAR_IN,
                pin.T1_OUT | pin.RAM_IN,
            ],
            # mov [a], [b]
            (pin.AM_RAM, pin.AM_RAM): [
                pin.SRC_R | pin.MAR_IN,
                pin.RAM_OUT | pin.T1_IN,
                pin.DST_R | pin.MAR_IN,
                pin.T1_OUT | pin.RAM_IN,
            ],
        },
        ADD: {
            # add a,5
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_ADD | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            # add a,c
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_ADD | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        SUB: {
            # sub a,5
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_SUB | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            # sub a,c
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_SUB | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        CMP: {
            # cmp a,5
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_SUB | pin.ALU_PSW,
            ],
            # cmp a,c
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_SUB | pin.ALU_PSW,
            ],
        },
        AND: {
            # and a,5
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_AND | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            # and a,c
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_AND | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        OR: {
            # or a,5
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_OR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            # or a,c
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_OR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
        XOR: {
            # xor a,5
            (pin.AM_REG, pin.AM_INS): [
                pin.DST_R | pin.A_IN,
                pin.SRC_OUT | pin.B_IN,
                pin.OP_XOR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
            # xor a,c
            (pin.AM_REG, pin.AM_REG): [
                pin.DST_R | pin.A_IN,
                pin.SRC_R | pin.B_IN,
                pin.OP_XOR | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ],
        },
    },
    1: {
        INC: {
            pin.AM_REG: [
                pin.DST_R | pin.A_IN,
                pin.OP_INC | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ]
        },
        DEC: {
            pin.AM_REG: [
                pin.DST_R | pin.A_IN,
                pin.OP_DEC | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ]
        },
        NOT: {
            pin.AM_REG: [
                pin.DST_R | pin.A_IN,
                pin.OP_NOT | pin.ALU_OUT | pin.DST_W | pin.ALU_PSW,
            ]
        },
        JMP: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JO: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JNO: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JZ: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JNZ: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JP: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
        JNP: {
            pin.AM_INS: [
                pin.DST_OUT | pin.PC_IN,
            ],
        },
    },
    0: {
        NOP: [
            pin.CYC,
        ],
        HLT: [
            pin.HALT
        ],
    },
}
