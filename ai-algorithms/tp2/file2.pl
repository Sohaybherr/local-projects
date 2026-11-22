Etudiant("saurez",12,15).
Etudiant("messi",14,18).
Etudiant("neymar",13,17).
Moyenne(Nom,Moy) :- Etudiant(Nom,Note1,Note2), Moy is Note1*0.25+Note2*0.75.
Montion(Nom,"tres bein"):-Moyenne(Nom,Moy),Moy>=16.
Montion(Nom,"bien"):-Moyenne(Nom,Moy),Moy>=14,Moy<16.
Montion(Nom,"passable"):-Moyenne(Nom,Moy),Moy>=10,Moy<14.
Montion(Nom,"echec"):-Moyenne(Nom,Moy),Moy<10.
Existe(Nom):- Etudiant(Nom,_,_).
List_moy:-
    Etudiant(Nom,_,_),
    Moyenne(Nom,Moy),
    write(Nom),write(" : "),write(Moy),nl,
    fail.
List_moy. 
List_mot:-
    Etudiant(Nom,_,_),
    Montion(Nom,Mot),
    write(Nom),write(" : "),write(Mot),nl,
    fail.
List_moy.
Ratt:-
    Etudiant(Nom,Note1,Note2),
    Moyenne(Nom,Moy),
    Moy<10,
    write(Nom),write(" : "),write(Moy),nl,
    fail. 
Ratt.          