from myhdl import block, always, instance, Signal, intbv, delay

# ALU that performs basic arithmetic operations
@block
def ALU(op1,op2,result, control):
    """
    A simple ALU that supports ADD, SUB operations
    control: 0 -> ADD, 1 -> SUB
    """
    @always(op1,op2, control)
    def compute():
        if control == 0:
            result.next = op1 + op2
        elif control == 1:
            result.next = op1 - op2


    return compute
