package Marchet1;

public class Produit {
    protected int id;
    protected String nom;
    protected double prix;
    public Produit(int id, String nom, double prix){
        this.id=id;
        this.nom=nom;
        this.prix=prix;
    }
    public Produit(){
        this.id=0;
        this.nom="";
        this.prix=0.0;
    }
    public int getId(){
        return id;
    }
    public String getNom(){
        return nom;
    }
    public double getPrix(){
        return prix;
    }
    public void setId(int id){
        this.id=id;
    }
    public void setNom(String nom){
        this.nom=nom;
    }
    public void setPrix(double prix){
        this.prix=prix;
    }
    public String toString(){
        return "Produit [id="+this.id+", nom="+this.nom+", prix="+this.prix+"]";
    }
    public int toCompareTo(Produit p){
        return Double.compare(this.prix, p.prix);
    }
    

}
