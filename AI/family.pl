female(pam).
female(alice).
female(liz).
male(jim).
male(tom).
male(peter).

parent(jim, alice).
parent(pam, alice).
parent(alice, tom).
parent(alice, liz).
parent(pam, peter).

mother(X, Y):- parent(X, Y) , female(X).
father(X, Y):- parent(X, Y) , male(X).
sibling(X, Y):- parent(Z, X), parent(Z, Y), X\==Y.
brother(X, Y):- parent(Z, X), parent(Z, Y), male(x), X\==Y.
sister(X, Y):- parent(Z, X), parent(Z, Y), female(X), X\==Y.

haschild(X, _):- parent(X, _).
grandparent(X, Y):- parent(X, Z), parent(Z, Y).
grandfather(X, Y):- parent(X, Z), parent(Z, Y), male(X).
grandmother(X, Y):- parent(X, Z), parent(Z, Y), female(X).

wife(X, Y):-parent(X, Z), parent(Y, Z), female(X), male(Y).
