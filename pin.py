MSR = 1
MAR = 2
MDR = 3
RAM = 4
IR = 5
DST = 6
SRC = 7
A = 8
B = 9
C = 10
D = 11
DI = 12
SI = 13
SP = 14
BP = 15
CS = 16
D5 = 17
SS = 18
ES = 19
VEC = 20
T1 = 21
T2 = 22

MSR_OUT = MSR
MAR_OUT = MAR
MDR_OUT = MDR
RAM_OUT = RAM
IR_OUT = IR
DST_OUT = DST
SRC_OUT = SRC
A_OUT = A
B_OUT = B
C_OUT = C
D_OUT = D
DI_OUT = DI
SI_OUT = SI
SP_OUT = SP
BP_OUT = BP
CS_OUT = CS
D5_OUT = D5
SS_OUT = SS
ES_OUT = ES
VEC_OUT = VEC
T1_OUT = T1
T2_OUT = T2

_DEST_SHIFT = 5

MSR_IN = MSR << _DEST_SHIFT
MAR_IN = MAR << _DEST_SHIFT
MDR_IN = MDR << _DEST_SHIFT
RAM_IN = RAM << _DEST_SHIFT
IR_IN = IR << _DEST_SHIFT
DST_IN = DST << _DEST_SHIFT
SRC_IN = SRC << _DEST_SHIFT
A_IN = A << _DEST_SHIFT
B_IN = B << _DEST_SHIFT
C_IN = C << _DEST_SHIFT
D_IN = D << _DEST_SHIFT
DI_IN = DI << _DEST_SHIFT
SI_IN = SI << _DEST_SHIFT
SP_IN = SP << _DEST_SHIFT
BP_IN = BP << _DEST_SHIFT
CS_IN = CS << _DEST_SHIFT
D5_IN = D5 << _DEST_SHIFT
SS_IN = SS << _DEST_SHIFT
ES_IN = ES << _DEST_SHIFT
VEC_IN = VEC << _DEST_SHIFT
T1_IN = T1 << _DEST_SHIFT
T2_IN = T2 << _DEST_SHIFT

SRC_R = 2 ** 10
SRC_W = 2 ** 11
DST_R = 2 ** 12
DST_W = 2 ** 13

PC_WE = 2 ** 14
PC_CS = 2 ** 15
PC_EN = 2 ** 16

PC_OUT = PC_CS
PC_IN = PC_CS | PC_WE
PC_INC = PC_CS | PC_WE | PC_EN

CYC = 2 ** 30
HALT = 2 ** 31

ADDR2 = 1 << 7
ADDR1 = 1 << 6

ADDR2_SHIFT = 4
ADDR1_SHIFT = 2
 
AM_INS = 0
AM_REG = 1
AM_DIR = 2
AM_RAM = 3