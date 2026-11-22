package Vehicul;

public class Voiture extends Vehicule {
    protected String typeCarburant;

    public Voiture(String id, String marque, int vitesse) {
        super(id, marque, vitesse);
        this.typeCarburant = "4L/100km";

    }
@Override
    void consommer() {
        System.out.println("La voiture consomme " + this.typeCarburant);
    }
@Override
    public String toString() {
        return super.toString() + " " + this.typeCarburant;
    }    


}
