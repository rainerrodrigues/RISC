@block
def RISCProcessorTestbench():
    # Signals
    clk = Signal(bool(0))
    reset = Signal(bool(0))
    r0 = Signal(intbv(0)[8:])
    r1 = Signal(intbv(0)[8:])
    r2 = Signal(intbv(0)[8:])
    r3 = Signal(intbv(0)[8:])
    mem = [Signal(intbv(0b00000000)[8:])]  # Memory with initial instruction (ADD r0, r1)
    
    # Instantiate the processor
    processor = RISCProcessor(clk, reset, mem, r0, r1, r2, r3)
    
    # Clock generator
    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
        # Initialize test
        print("Starting test...")
        
        # Test ADD instruction (ADD r0, r1)
        r0.next = 5
        r1.next = 10
        mem[0].next = 0b00000000  # ADD r0, r1

        # Run the simulation
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        
        print(f"r0: {r0}, r1: {r1}, r2: {r2}, r3: {r3}")
        
        # Check result
        assert r0 == 15, f"Test failed, expected 15, got {r0}"
        print("Test passed!")

    return processor, clkgen, stimulus

def test_processor():
    tb = RISCProcessorTestbench()
    tb.config_sim(trace=True)
    tb.run_sim()
