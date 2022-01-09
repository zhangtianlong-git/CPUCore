import os
import pin
import assembly as ASM
import re


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'program.asm')
outputfile = os.path.join(dirname, 'program.bin')

annotation = re.compile(r"(.*?);.*")

codes = []

OP2 = {
    'MOV': ASM.MOV,
}

OP1 = {

}

OP0 = {
    'NOP': ASM.NOP,
    'HLT': ASM.HLT
}

OP2SET = set(OP2.values())
OP1SET = set(OP2.values())
OP0SET = set(OP2.values())
REGISTERS = {
    "A": pin.A,
    "B": pin.B,
    "C": pin.C,
    "D": pin.D,
}


class Code():
    def __init__(self, number, source):
        self.number = number
        self.source = source.upper()
        self.op = None
        self.dst = None
        self.src = None
        self.prepare_source()

    def get_op(self):
        if self.op in OP2:
            return OP2[self.op]
        if self.op in OP1:
            return OP1[self.op]
        if self.op in OP0:
            return OP0[self.op]
        raise SyntaxError(self)

    def get_am(self, addr):
        if not addr:
            return 0, 0
        if addr in REGISTERS:
            return pin.AM_REG, REGISTERS[addr]
        if re.match(r'^[0-9]+$', addr):
            return pin.AM_INS, int(addr)
        if re.match(r'^0X[0-9A-F]+$', addr):
            return pin.AM_INS, int(addr, 16)
        raise SyntaxError(self)

    def prepare_source(self):
        tup = self.source.split(',')
        if len(tup) > 2:
            raise SyntaxError(self)
        if len(tup) == 2:
            self.src = tup[1].strip()

        tup = re.split(r' +', tup[0])
        if len(tup) > 2:
            raise SyntaxError(self)
        if len(tup) == 2:
            self.dst = tup[1].strip()

        self.op = tup[0].strip()

    def compile_code(self):
        op = self.get_op()
        amd, dst = self.get_am(self.dst)
        ams, src = self.get_am(self.src)

        if op in OP2SET:
            ir = op | (amd << 2) | ams
        elif op in OP1SET:
            ir = op | amd
        else:
            ir = op

        return [ir, dst, src]

    def __repr__(self):
        return f'[{self.number} - {self.source}]'


class SyntaxError(Exception):
    def __init__(self, code=Code, *args: object):
        super().__init__(*args)
        self.code = Code


def compile_program():
    with open(inputfile, encoding='utf8') as file:
        lines = file.readlines()

    for index, line in enumerate(lines):
        source = line.strip()
        if ';' in source:
            math = annotation.match(source)
            source = math.group(1)
        if not source:
            continue
        code = Code(index + 1, source)
        print(code)
        codes.append(code)

    with open(outputfile, 'wb') as file:
        for code in codes:
            values = code.compile_code()
            for value in values:
                result = value.to_bytes(1, byteorder='little')
                file.write(result)


def main():
    try:
        compile_program()
    except SyntaxError as e:
        print(f'Syntax error at {e.code}')
        return
    print('Compile finished!!!')


if __name__ == '__main__':
    main()
