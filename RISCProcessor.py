@block
def RISCProcessor(clk, reset, mem, r0, r1, r2, r3):
    """
    A simple RISC processor with a small instruction set.
    """
    opcode = Signal(intbv(0)[2:])  # 2-bit opcode for instruction
    alu_control = Signal(intbv(0)[1:])  # Control for ALU operation
    write_enable = Signal(bool(0))  # Enable write to register
    read_addr1 = Signal(intbv(0)[2:])  # Register addresses
    read_addr2 = Signal(intbv(0)[2:])
    write_data = Signal(intbv(0)[8:])  # Data to be written into registers
    read_data1 = Signal(intbv(0)[8:])
    read_data2 = Signal(intbv(0)[8:])
    
    # Instantiate the components
    alu = ALU(read_data1, read_data2, write_data, alu_control)
    reg_file = RegisterFile(r0, r1, r2, r3, clk, write_enable, write_data, read_addr1, read_addr2, read_data1, read_data2)
    control_unit = ControlUnit(opcode, alu_control, write_enable, read_addr1, read_addr2, write_data)
    
    @always(clk.posedge)
    def execute_instruction():
        # Fetch the instruction from memory (simple model)
        instruction = mem[0]  # For simplicity, we just fetch one instruction.
        opcode.next = instruction[0:2]  # First 2 bits are opcode
        read_addr1.next = instruction[2:4]  # Next 2 bits for register 1
        read_addr2.next = instruction[4:6]  # Next 2 bits for register 2
        # Decode and execute
        control_unit.decode()
        write_enable.next = True  # For simplicity, always enable write
        mem.pop(0)  # Remove the executed instruction
        
    return alu, reg_file, control_unit, execute_instruction

