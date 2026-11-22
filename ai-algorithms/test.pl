hailston(1).
hailston(N) :-
    N > 1,
    N mod 2 =:= 0,
    N1 is N // 2,
    hailston(N1).
hailston(N) :-
    N > 1,
    N mod 2 =\= 0,
    N1 is 3 * N + 1,
    hailston(N1).