:- use_module(library(clpfd)).

cube([A,B,C,D,E,F,G,H,I]):-
Vars=[A,B,C,D,E,F,G,H,I],
Vars ins 1..9,
all_different(Vars),
A+B+C #= 15,
D+E+F #= 15,    
G+H+I #= 15,

A+D+G #= 15,
B+E+H #= 15,    
C+F+I #= 15,

A+E+I #= 15,
C+E+G #= 15,
labeling([],Vars).


