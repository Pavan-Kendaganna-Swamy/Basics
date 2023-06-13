*** Library Insertion ***

* insert library path here
.op


*** Instance creation***

V1 0 Vdd 1.8
V2 0 B PULSE(0 1.8 1p .5n .5n 5n 10n)
V3 0 B PULSE(0 1.8 1p .5n .5n 5n 20n)
C1 0 out .5p
* Drain Gate Source Body 
M1 out	 B	 N001	0 	CMOSN 1=180 w=10u
M2 N001	 A	 0		0	CMOSN 1=180 w=10u
M3 out 	 B 	 Vdd	Vdd CMOSP 1=180 w=20u
M4 out   A	 Vdd 	Vdd CMOSP 1=180 w=20u


*** Operation ***
.tran 0 50n .1n .1
.end