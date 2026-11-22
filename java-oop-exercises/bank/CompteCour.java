package bank;
public class CompteCour extends Compte {
    private double decouvertAutorise;

    public CompteCour(String numero, double solde, Client titulaire, double decouvertAutorise) {
        super(numero, solde, titulaire);
        this.decouvertAutorise = decouvertAutorise;
    }

    public double getDecouvertAutorise() {
        return decouvertAutorise;
    }

    public void setDecouvertAutorise(double decouvertAutorise) {
        this.decouvertAutorise = decouvertAutorise;
    }
@Override
    public void deposer(double montant) {
        if (montant > 0) {
            solde += montant;
            System.out.println("Dépôt effectué : " + montant);
            return;
        }
        System.out.println("Montant de dépôt invalide : " + montant);
    }

    @Override
    public void retirer(double montant) {
        if (montant > 0 && montant <= (solde + decouvertAutorise)) {
            solde -= montant;
            System.out.println("Retrait effectué : " + montant);
            return;
        }
        System.out.println("Fonds insuffisants pour le retrait de : " + montant);
    }

    @Override
    public void afficher() {
        super.afficher();
        System.out.println("CompteCour [numero=" + numero + ", solde=" + solde + ", titulaire=" + titulaire.getNom() + " " + titulaire.getPrenom() + ", decouvertAutorise=" + decouvertAutorise + "]");
    }
}