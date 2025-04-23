def reg_to_bin(reg):
    """Convert register (e.g., R0) to 3-bit binary."""
    return format(int(reg[1:]), "03b")

def signed_to_bin(value, bits):
    """Convert signed integer to binary of given bit width."""
    if value < 0:
        value = (1 << bits) + value  # Convert to two's complement
    return format(value, f"0{bits}b")

def signed_to_signed_bin(value, bits):
    """Convert signed integer to signed binary representation."""
    if value < 0:
        return "1" + format(abs(value), f"0{bits - 1}b")
    return format(value, f"0{bits}b")

# Read input file
with open("code.txt", "r") as file:
    lines = file.readlines()

# Opcodes and instruction types
opcodes = {
    "add": "0000", "sub": "0010", "mul": "0011", "adi": "0001", 
    "and": "0100", "ora": "0101", "imp": "0110", "lhi": "1000", 
    "lli": "1001", "lw": "1010", "sw": "1011", "beq": "1100", 
    "jal": "1101", "jlr": "1111", "j": "1110"
}

r_type = ["add", "sub", "mul", "and", "ora", "imp"]
i_type = ["adi", "lw", "sw", "beq", "jlr"]
j_type = ["lli", "lhi", "jal", "j"]

# Open output file
with open("program.txt", "w") as outputfile:
    for line_num, line in enumerate(lines):
        line = line.strip()
        if line_num < 512:
            # Parse instructions
            parts = [part.strip() for part in line.replace(",", " , ").split()]
            if not parts:
                print(f"Error: Don't put spaces between lines. \nLine: {line_num + 1}")
                continue

            mnemonic = parts[0].lower()

            if mnemonic == "nop":
                binary = "0111" + "0" * 12
            elif mnemonic == "data":
                binary = signed_to_bin(int(parts[1]), 16)
            elif mnemonic in r_type:  # R-type
                opcode = opcodes[mnemonic]
                rc = reg_to_bin(parts[1].strip(','))
                ra = reg_to_bin(parts[3].strip(','))
                rb = reg_to_bin(parts[5].strip(','))
                unused = "000"
                binary = opcode + ra + rb + rc + unused
            elif mnemonic in i_type:  # I-type
                opcode = opcodes[mnemonic]
                
                r1 = reg_to_bin(parts[1].strip(','))
                r2 = reg_to_bin(parts[3].strip(','))

                if mnemonic != "adi":
                    ra = r1
                    rb = r2
                else:
                    rb = r1
                    ra = r2
                
                if mnemonic != "jlr":
                    imm = signed_to_signed_bin(int(parts[5]), 6)
                else:
                    imm = signed_to_signed_bin(0, 6)
                binary = opcode + ra + rb + imm
            
            elif mnemonic in j_type:  # J-type
                if mnemonic != "j":
                    opcode = opcodes[mnemonic]
                    ra = reg_to_bin(parts[1].strip(','))
                    imm = signed_to_signed_bin(int(parts[3]), 9)
                    binary = opcode + ra + imm
                else:
                    opcode = opcodes["j"]
                    imm = signed_to_signed_bin(int(parts[-1]), 9)
                    binary = opcode + "000" + imm
            else:
                print(f"Invalid instruction on line {line_num + 1}: {line}")
                continue

            # Ensure binary is exactly 16 bits and write to file
            if len(binary) != 16 or '-' in binary:
                print(f"Invalid instruction on line {line_num + 1}\nCheck for negative values and data range.")
            else:
                outputfile.write(binary + "\n")
                
        else:
            break
