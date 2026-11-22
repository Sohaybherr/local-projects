package Salles;
import java.util.Scanner;

public class main {
  public static void main(String[] args) {
        SalleService salleService = new SalleService();
            SalleCl salle1 = new SalleCl( 101, "Salle A");
            SalleCl salle2 = new SalleCl( 102, "Salle B");
            SalleCl salle3 = new SalleCl( 103, "Salle C");
            SalleCl salle4 = new SalleCl( 104, "Salle D");
            SalleCl salle5 = new SalleCl( 101, "Salle E");
            SalleCl salle6 = new SalleCl( 102, "Salle F");
            SalleCl salle7= new SalleCl( 103, "Salle G");
            SalleCl salle8 = new SalleCl( 104, "Salle H");

        try {
        salleService.create(salle1);
        salleService.create(salle2);
        salleService.create(salle3);
        salleService.create(salle4);
        salleService.create(salle5);
        salleService.create(salle6);
        salleService.create(salle7);
        salleService.create(salle8);
        
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
       int i=1;
       while(i!=0){
              System.out.println("1- create Salle");
              System.out.println("2- Supprimer Salle");
              System.out.println("3- rechercher Salle");
              System.out.println("4- modifier Salle");
              System.out.println("5- afficher toutes les Salles");
              System.out.println("6-afficher les Salle par Libelle");
              System.out.println("7- Quitter");
              Scanner sc = new Scanner(System.in);
              System.out.println("Choisir une option:");
              i=sc.nextInt();
              switch(i){
                case 1:
                     System.out.println("Creation d'une salle:");
                     System.out.println("Entrez le code de la salle:"+"\n"+"entrez le libelle de la salle:");
                     int code = sc.nextInt();
                     sc.nextLine(); // Consume newline
                     String libelle = sc.nextLine();
                     SalleCl salle = new SalleCl(code, libelle);
                     try {
                         salleService.create(salle);
                     } catch (Exception e) {
                         System.out.println(e.getMessage());
                     }
                     break;
                case 2:
                     System.err.println("Suppression d'une salle:");
                     System.out.println("Entrez  la ID salle à supprimer:");
                     String id = sc.nextLine();
                    
                        SalleCl salleToDelete = salleService.findById(Integer.parseInt(id));
                         salleService.delete(salleToDelete);
                   
                     break;
                case 3:
               System.err.println("Recherche d'une salle:");
                     System.out.println("Entrez  la ID salle à rechercher:");
                     String idr = sc.nextLine();
                    
                        SalleCl salleFound = salleService.findById(Integer.parseInt(idr));
                        if(salleFound != null){
                            System.out.println(salleFound.toString());
                        } else {
                            System.out.println("Salle non trouvée.");
                        }
                     break;
                case 4:
                        System.out.println("Modification d'une salle:");
                        System.out.println("Entrez  la ID salle à modifier:");
                        String idm = sc.nextLine();
                       
                           SalleCl salleToUpdate = salleService.findById(Integer.parseInt(idm));
                           if(salleToUpdate != null){
                               salleService.update(salleToUpdate);
                               System.out.println("Salle mise à jour: " + salleToUpdate.toString());
                           } else {
                               System.out.println("Salle non trouvée.");
                           }
                     break;
                case 5:
                        System.out.println("Affichage de toutes les salles:");
                        for(SalleCl s : salleService.findAll()){
                            System.out.println(s.toString());
                        }
                     break;
                case 6:
                        System.out.println("Affichage des salles par libelle:");
                        salleService.findAll().stream()
                            .sorted((s1, s2) -> s1.compareTo(s2))
                            .forEach(s -> System.out.println(s.toString()));
                     break;
                case 7:
                     i=0;
                        break;
                default:
                     System.out.println("Option invalide. Veuillez réessayer.");
              }
       }
    }
    
}
