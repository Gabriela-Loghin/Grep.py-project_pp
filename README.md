# Grep.py-project_pp
In cadrul acestui proiect s-a creat in limbajul python o versiune a functiei grep din Linux !
1.Am o functie principala "main_function" in care determin din lista de argumente data de la tastatura in linia de comanda ce optiuni am , dupa care , verfic daca pathul meu duce 
direct la un fisier sau la un director .
2.Daca pathul meu duce la un fisier apelez functia "grep_file" in care verific prin intermediul librariei "os" daca exista fisierul , in caz afirmativ il deschid in modul de citire
,prin readlines() citesc toate liniile,apoi verific potrivirile in functie de optiunile date .
-daca am optiunea ignore_case : atunci prin metoda lower() ,miscorez literele mari din regex si de pe linie si verific daca exista match;
-daca prin metoda match a obiectului creat prin compilarea regexului se obtine potrivire iar ignore_case e false se afiseaza linia cu potrivirea
-daca am optiunea count : aceasta se obtine prin numararea numarului de aparitii a fiecarei potriviri
-daca am optiunea not : in cadrul verificarilor parcurse linie cu linie se verifica daca exista potriviri sau nu prin crearea unui boolean de care ne folosim pt a genera un rezultat
in cadrul optiunii aacesteia;
- cautarea dupa expresii regulate se face folosind libraria re special creata pt a verifica daca exista match intre un string si o expresie regulata prin metoda match()
3. In cazul in care pathul respectiv duce la un director noi vom cauta fisierul in director recursiv ,adica: verificam daca directorul exista , daca da , ii listam componentele si le
parcurgem , daca acea componenta este fisier apelam functia grep_file , daca este tot director reapaelam functia mama grep_for_dir.
