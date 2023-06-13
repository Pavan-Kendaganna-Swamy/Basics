
Few Directives used in LT SPICE


.include:	Includes an external file containing additional SPICE netlist definitions.
Example:
 .include myfile.cir
 
 
.subckt and .ends:	Defines a subcircuit, which is a reusable circuit block.
Example:
.subckt opamp in+ in- out
* Op-Amp circuit definition goes here
.ends opamp


.param:		Assigns values to parameters used in the circuit.
Example: .param R1=1k C1=1u

.model:		Defines or modifies the model parameters of a device, such as transistors.
Example: .model NMOS NMOS (Level=3 Vto=1 Kp=100)


.tran:		Sets up parameters for transient analysis, which analyzes the circuit's behavior over time.
Example: .tran 1us 10ms


.ac:		Sets up parameters for AC analysis, which analyzes the frequency response of the circuit.
Example: .ac dec 10 1Hz 1MHz


.dc:		Sets up parameters for DC analysis, which analyzes the circuit's response at different DC operating points.
Example: .dc Vin 0 5 1


.op:		Performs DC operating point analysis, calculating the DC voltages and currents in the circuit.
Example: .op


.plot:		Specifies which variables to plot during the simulation.
Example: .plot V(out) I(R1)


.print:		Specifies which variables to print during the simulation.
Example: .print V(out) I(R1)



