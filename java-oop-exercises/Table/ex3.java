package Table;

public class ex3 {
    public static void main(String[] args) {
        int[][] matrice =new int[5][6];
        for (int i = 0; i < matrice.length; i++) {
            for (int j = 0; j < matrice[i].length; j++) {
                matrice[i][j]= (i+1)*(j+1);
            }
        }
        
        for (int i = 0; i < matrice.length; i++) {
            for (int j = 0; j < matrice[i].length; j++) {
                System.out.print(matrice[i][j] + "\t");
            }
            System.out.println();
        }
      int [][] matrice_transpo=new int[6][5];
      for(int i=0;i<matrice_transpo.length;i++){
        for(int j=0;j<matrice_transpo[i].length;j++){
            matrice_transpo[i][j]=matrice[j][i];
        }
      }
        System.out.println("++++++++++++++++++++++++++++++++");
      for(int i=0;i<matrice_transpo.length;i++){
        for(int j=0;j<matrice_transpo[i].length;j++){
            System.out.print(matrice_transpo[i][j] + "\t");
        }
        System.out.println();
      }

    }
}
