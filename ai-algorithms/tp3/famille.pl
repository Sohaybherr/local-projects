% Relations parent
pere(ahmed, taha).
pere(karim, meryem).
pere(Kamal, sami).
pere(sami, samia).
pere(adel, imane).
pere(adel, nada).
pere(taha,hind).

% Relations enfant (optionnel لكن مفيد)
fille(sara, taha).
fille(sara, ahmed).
fille(samia, sami).
fille(meryem, karim).

fils(ilyass, sara).

% Relations amis
ami(ahmed, karim).
ami(karim, nada).
ami(samia, hind).
ami(meryem, imane).
ami(meryem, nada).

est_ami(X, Y) :- ami(X, Y).
est_ami(X, Y) :- ami(Y, X).

% Relations connaissance
connaissance(ahmed, adel).
connaissance(karim, adel).

% Relations frères
frere(kamal, ahmed).

lien_famille_direct(X, Y) :- pere(X, Y).
lien_famille_direct(X, Y) :- fille(X, Y).
lien_famille_direct(X, Y) :- fils(X, Y).
lien_famille_direct(X, Y) :- frere(X, Y).

lien_famille(X, Y) :- lien_famille_direct(X, Y).
lien_famille(X, Y) :- lien_famille_direct(Y, X).

famille(X, Y) :- famille_chemin(X, Y, [X]), X \= Y.

famille_chemin(X, Y, _) :- lien_famille(X, Y).
famille_chemin(X, Y, Visites) :-
    lien_famille(X, Z),
    \+ member(Z, Visites),
    famille_chemin(Z, Y, [Z|Visites]).
contact(X, Y) :- est_ami(X, Y); famille(X, Y).
propositions_Ami(X, Y) :- est_ami(X, Z), est_ami(Z, Y), X \= Y.
