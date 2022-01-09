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


class Code():
    def __init__(self, number, source):
        self.number = number
        self.source = source
        self.op = None ######### zheli
        self.src = None
        self.prepare_source()

    def prepare_source(self):


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
        if not source:
            continue
        if ';' in source:
            math = annotation.match(source)
            source = math.group(1)
        code = Code(index + 1, source)
        print(code)
        codes.append(code)


def main():
    try:
        compile_program()
    except SyntaxError as e:
        print(f'Syntax error at {e.code}')
        return
    print('Compile finished!!!')


if __name__ == '__main__':
    main()
