package bank;

public class Compte {
    protected String numero;
    protected double solde;
    protected Client titulaire;

    public Compte(String numero, double solde, Client titulaire) {
        this.numero = numero;
        this.solde = solde;
        this.titulaire = titulaire;
    }

    public String getNumero() {
        return numero;
    }

    public double getSolde() {
        return solde;
    }

    public Client getTitulaire() {
        return titulaire;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public void setSolde(double solde) {
        this.solde = solde;
    }

    public void setTitulaire(Client titulaire) {
        this.titulaire = titulaire;
    }

    public void deposer(double montant) {
       
        System.out.println("ici pour retirer");
    }

    public void retirer(double montant) {
System.out.println("le montant a retirer est"+montant);
    }

public void afficher() {
    System.out.println("Compte [numero=" + numero + ", solde=" + solde + ", titulaire=" +  titulaire.getNom() + " " + titulaire.getPrenom() + "]");
    }
}
