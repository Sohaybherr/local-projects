sudoku4(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P):-
A #= 1
G #= 3
J #= 4
P #= 2
Vars=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P] ,
Vars ins 1..4,
all_different([A,B,C,D]),
all_different([E,F,G,H]),
all_different([I,J,K,L]),
all_different([M,N,O,P]),
all_different([A,E,I,M]),
all_different([B,F,J,N]),
all_different([C,G,K,O]),
all_different([D,H,L,P]),
all_different([A,F,K,P]),
all_different([D,G,J,M]),
labeling([],Vars).
