package entreprise;

public class Responsable extends Employe {
    double bonus;
    public Responsable(String nom, String matricul, double ind_salaire, double val_ind, double bonus) {
        super(nom, matricul, ind_salaire, val_ind);
        this.bonus = bonus; 
    }
    public double getBonus() {
        return bonus;
    }
    public void setBonus(double bonus) {
        this.bonus = bonus;
    }
@Override
    public double calculerSalaire() {
        double salaire = (ind_salaire * val_ind) + bonus;
        System.out.println("Salaire du responsable avec bonus: " + salaire);
        return salaire;
    }
    @Override
    public void afficher() {
        System.out.println("Nom: " + nom);
        System.out.println("Matricule: " + matricul);
        System.out.println("Indemnité de salaire: " + ind_salaire);
        System.out.println("Valeur de l'indemnité: " + val_ind);
        System.out.println("Bonus: " + bonus);
        System.out.println("Poste: Responsable");
    }
}
