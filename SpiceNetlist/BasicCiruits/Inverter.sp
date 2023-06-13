*** Library Insertion ***

* insert library path here
.op


*** Instance creation***

V1 0 Vdd 1.8
V2 0 in PULSE(0 1.8 1p .5n .5n 5n 10n)
C1 0 out .1p
M1 out in 0 0 CMOSN 1=180u w=1u
M2 Vdd in Vdd out CMOSP 1=180u w=2u

*** Operation ***
.tran 0 30n 1p 50p
.end