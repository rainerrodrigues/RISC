# Simple register file to hold a small set of registers
@block
def RegisterFile(r0, r1, r2, r3, clk, write_enable, write_data, read_addr1,read_addr2, read_data1, read_data2):
    """
    Simple register file with 4 registers: r0 to r3
    """

    registers = [r0, r1, r2, r3]

    @always(clk.posedge)
    def write():
        if write_enable:
            registers[read_addr1].next = write_data

    @always(clk.posedge)
    def read():
        read_data1.next = registers[read_addr1]
        read_data2.next = registers[read_addr2]

    return write, read
