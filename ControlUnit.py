@block
def ControlUnit(opcode, alu_control, write_enable, read_addr1, read_addr2, write_data):
    """
    A Simple control unit for the RISC processor.
    """

    @always(opcode)
    def decode():
        if opcode == 0: #ADD instruction
            alu_control.next = 0
            write_enable.next = True
        elif opcode == 1: #SUB instruction
            alu_control.next = 1
            write_enable.next = True
        elif opcode == 2: #LOAD instruction
            write_enable.next = False
        elif opcode == 3: #STORE instruction
            write_enable.next = False
        else:
            write_enable.next =  False # No operation

     return decode
