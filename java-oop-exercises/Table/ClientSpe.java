package Table;
public class ClientSpe extends Client {
    private float tauxReduction;
    public ClientSpe(String nom, String id, float tauxReduction ) {
        super(nom, id);
        this.tauxReduction= tauxReduction;
    }
    public void afficher(){
        super.afficher();
        System.out.println("Adresse du client: " + this.tauxReduction);

    }
}