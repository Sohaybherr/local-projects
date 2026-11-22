homme(mohammed).
homme(ahmed).
homme(mourad).
homme(adel).
homme(karim).
homme(kamal).
homme(ilyass).
homme(taha).
femme(bassma).
homme(nabil).
femme(fatima).
femme(sara).
femme(douae).
femme(imane).
femme(fadoua).
femme(hind).
femme(meryem).
femme(nada).
femme(manal).
femme(ibtissam).
parent(mohammed, ahmed).
parent(fatima, ahmed).

parent(mohammed, douae).
parent(fatima, douae).

parent(mohammed, karim).
parent(fatima, karim).

parent(mohammed, imane).
parent(fatima, imane).

parent(mohammed, fadoua).
parent(fatima, fadoua).

parent(sara, mourad).
parent(ahmed, mourad).

parent(sara, manal).
parent(ahmed, manal).

parent(sara, adel).
parent(ahmed, adel).

parent(karim, hind).
parent(imane, hind).

parent(karim, kamal).
parent(imane, kamal).

parent(fadoua, meryem).
parent(douae, meryem).

parent(fadoua, ilyass).
parent(douae, ilyass).

parent(hind, taha).
parent(kamal, taha).

parent(hind, bassim).
parent(kamal, bassim).

parent(meryem, nada).
parent(ilyass, nada).

parent(meryem, nabil).
parent(ilyass, nabil).

parent(mourad, ibtissam).
parent(manal, ibtissam).

fils(X,Y):- homme(X),parent(Y,X).
fille(X,Y):- femme(X),parent(Y,X).
enfant(X,Y):- parent(Y,X).
mere(X,Y):- femme(X),parent(X,Y);enfant(Y,X).
pere(X,Y):- homme(X),parent(X,Y);enfant(Y,X).
gr_parent(X,Y):- parent(X,Z),parent(Z,X).
gr_mere(X,Y):- femme(X),gr_parent(X,Y).
gr_pere(X,Y):- homme(X),gr_parent(X,Y).
sis(X,Y):-femme(X),parent(Z,X),parent(Z,Y),X\=Y.
bro(X,Y):-homme(X),parent(Z,X),parent(Z,Y),X\=Y.
tante(X,Y):-parent(Z,Y),sis(X,Z).
oncle(X,Y):-parent(Z,Y),bro(X,Z).
cousin(X,Y):-homme(X),(parent(Z,X),(tante(Z,Y);oncle(Z,Y))).
cousine(X,Y):-femme(X),(parent(Z,X),(tante(Z,Y);oncle(Z,Y))).


