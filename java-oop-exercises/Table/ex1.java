package Table;

import java.util.Scanner;

public class ex1 {
    public static void main(String[] args) {
        float [] tableau = new float[5];
        Scanner scanner = new Scanner(System.in);
        System.out.print("Entrez un nombre à rechercher dans le tableau: ");
        for (int i = 0; i < tableau.length; i++) {
            System.out.println("Index " + i + ": ");
            float nombre = scanner.nextFloat();
            tableau[i]=nombre;
        }
        for (int i = 0; i < tableau.length; i++) {
            if(i==0){
                System.out.println("Les éléments du tableau sont :{");
            }
            System.out.println( tableau[i]+ ",");
        }
        System.out.println("}");
        scanner.close();
    }
   
}
