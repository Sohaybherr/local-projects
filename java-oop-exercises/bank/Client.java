package bank;

public class Client {
private static int idCounter = 0;    
protected String nom;
protected String prenom;
protected String adresse;
protected String id;
public Client(String nom, String prenom, String adresse) {
    this.nom = nom;
    this.prenom = prenom;
    this.adresse = adresse;
    this.id = "ID" + (++idCounter);
}
public String getNom() {
    return nom;
}

public String getPrenom() {
    return prenom;
}

public String getAdresse() {
    return adresse;
}

public String getId() {
    return id;
}
public void setAdresse(String adresse) {
    this.adresse = adresse;}
public void setId(String id) {
    this.id = id;}
public void setNom(String nom) {
    this.nom = nom;}
public void setPrenom(String prenom) {
    this.prenom = prenom;}
public void afficher() {
    System.out.println("Client [nom=" + nom + ", prenom=" + prenom + ", adresse=" + adresse + ", id=" + id + "]");    
}
}