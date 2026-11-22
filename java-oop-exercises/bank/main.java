package bank;

public class main { 
    public static void main(String[] args) {
        Client client1 = new Client("Messi", "Batistuta", "123St");
        Client client2 = new Client("Ronaldo", "Costa", "456st");
        client1.afficher();
        client2.afficher();
        CompteCour com1= new CompteCour("123344555", 0, client2, 0);
        com1.afficher();
    com1.setSolde(1000000);
    com1.retirer(10000000);
    com1.setDecouvertAutorise(9000000);
    com1.retirer(10000000);
    com1.afficher();
    CompteEpar com2= new CompteEpar("987654321", 5000, client1, 5);
    com2.afficher();
    com2.deposer(2000);
    com2.calculerInterets();
    com2.afficher();

    }
    
}
