package entreprise;

public class Main {
    public static void main(String[] args) {
        Employe emp = new Employe("Ronaldo", "E123", 2000, 1.5);
        emp.afficher();
        System.out.println("+++++++++++++++++++++++++++++++++++++++++");
        emp.calculerSalaire();
        System.out.println("+++++++++++++++++++++++++++++++++++++++++");
        
        Responsable resp = new Responsable("Messi", "R456", 3000, 1.8, 500);
        resp.afficher();
        System.out.println("+++++++++++++++++++++++++++++++++++++++++");
        resp.calculerSalaire(); 
        System.out.println("+++++++++++++++++++++++++++++++++++++++++");
        resp.setBonus(800);
        System.out.println("+++++++++++++++++++++++++++++++++++++++++");
        resp.calculerSalaire();
       
    }
}
