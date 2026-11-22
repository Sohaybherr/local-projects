package bibleo;

public class main {
    public static void main(String[] args) {
        Livre l1 = new Livre(1, "Auteur1", "Titre1", 300);
        Livre l2 = new Livre(2, "Auteur2", "Titre2", 150);
        Roman r1 = new Roman(3, "Auteur3", "Titre3", 19.99);
        Roman r2 = new Roman(4, "Auteur4", "Titre4", 9.99);
        Bibleo biblio = new Bibleo(3, "Ma Bibliotheque");
        try {
            biblio.addDoc(l1);
            biblio.addDoc(l2);
            biblio.addDoc(r1);
            biblio.addDoc(r2); // Ceci devrait lancer une exception
        } catch (PlusDePlace e) {
            System.out.println(e.getMessage());
        }
        biblio.showall();
        biblio.findByTitle("Titre2");
    }
}