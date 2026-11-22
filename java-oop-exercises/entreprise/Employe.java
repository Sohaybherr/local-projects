package entreprise;

public class Employe {
    protected String nom;
    protected String matricul;
    protected double ind_salaire;
    protected double val_ind;
    public Employe(String nom, String matricul, double ind_salaire, double val_ind) {
        this.nom = nom;
        this.matricul = matricul;
        this.ind_salaire = ind_salaire;
        this.val_ind = val_ind;
    }
    String getNom() {
        return nom;
    }
    String getMatricul() {
        return matricul;
    }
    double getInd_salaire() {
        return ind_salaire;
    }
    double getVal_ind() {
        return val_ind;
    }
    void setNom(String nom) {
        this.nom = nom;
    }
    void setMatricul(String matricul) {
        this.matricul = matricul;
    }
    void setInd_salaire(double ind_salaire) {
        this.ind_salaire = ind_salaire;
    }
    void setVal_ind(double val_ind) {
        this.val_ind = val_ind;
    }
    public void afficher() {
        System.out.println("Nom: " + nom);
        System.out.println("Matricule: " + matricul);
        System.out.println("Indemnité de salaire: " + ind_salaire);
        System.out.println("Valeur de l'indemnité: " + val_ind);
        System.out.println("poste: Employé");
    }
    public double calculerSalaire() {
        System.out.println("Salaire de l'employé: " + (ind_salaire * val_ind));
        return ind_salaire * val_ind;
    }
}
