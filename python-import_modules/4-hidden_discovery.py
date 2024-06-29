#!/usr/bin/python3
import dis

if __name__ == "__main__":
    with open('hidden_4.pyc', 'rb') as f:
        code = f.read()
    instructions = dis.get_instructions(code)
    names = set()

    for instr in instructions:
        if instr.opname == 'LOAD_GLOBAL' or instr.opname == 'STORE_NAME':
            name = instr.argval
            if not name.startdswith('__'):
                names.add(name)

    for name in sorted(names):
        print(name)
