package Table;

import java.util.Scanner;

public class ex2 {
    public static void main(String[] args) {
        int n;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Entrez la taille du mot ");
        n = scanner.nextInt();
        String [] tableau = new String[n];
        for (int i = 0; i < tableau.length; i++) {
            System.out.println("Index " + i + ": ");
            String caractere = scanner.next();
            tableau[i]=caractere;
        }
        
        System.out.println("entrer le mot : ");
        String mot = scanner.next();
        
       for (int i = 0; i < tableau.length; i++) {
        if(mot.equals(tableau[i])){
            System.out.println("le mot est trouvé à l'index : " + i);
            return;
        }
        scanner.close();
    }
    
}
}
