package Vehicul;
public class Moto extends Vehicule {
    protected String cylindre;

    public Moto(String id, String marque, int vitesse) {
        super(id, marque, vitesse);
        this.cylindre = "1L/100km";

    }
@Override
    void consommer() {
        System.out.println("La moto consomme " + this.cylindre);
    }
@Override
    public String toString() {
        return super.toString() + " " + this.cylindre;
    }    


}
