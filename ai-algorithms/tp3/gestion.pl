meme_mod(X,Z):- inscrit(X,Z),
    inscrit(Y,Z),
    X \= Y.
meme_mod(X,Y):- meme_mod(Y,X).
ami(X,Y):- inscrit(X,Z),
    inscrit(Y,Z),
    X \= Y.
polyvalent(X):- inscrit(X,Z),inscrit(Y,Z),X \= Y.

isole(X):- etudiant(X),\+ ami(X,_).