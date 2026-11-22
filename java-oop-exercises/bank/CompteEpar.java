package bank;

public class CompteEpar extends Compte {
    private double tauxInteret;

    public CompteEpar(String numero, double solde, Client titulaire, double tauxInteret) {
        super(numero, solde, titulaire);
        this.tauxInteret = tauxInteret;
    }

    public double getTauxInteret() {
        return tauxInteret;
    }

    public void setTauxInteret(double tauxInteret) {
        this.tauxInteret = tauxInteret;
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
      if (montant > 0 && montant <= solde) {
          solde -= montant;
          System.out.println("Retrait effectué : " + montant);
          return;   
      }
        System.out.println("Fonds insuffisants pour le retrait de : " + montant);
  }
  public double calculerInterets() {
     double interets = solde * tauxInteret / 100;
     System.out.println("Intérêts calculés : " + interets);
         return interets;
    }  
    @Override
    public void afficher() {
        System.out.println("CompteEpar [numero=" + numero + ", solde=" + solde + ", titulaire=" + titulaire.getNom() + " " + titulaire.getPrenom() + ", tauxInteret=" + tauxInteret + "]");
    }
    
}
