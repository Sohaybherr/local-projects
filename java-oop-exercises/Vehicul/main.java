package Vehicul;

import java.util.ArrayList;
import java.util.List;

public class main {
    public static void main(String[] args) {
        List<Vehicule> vehicules = new ArrayList<Vehicule>();
  

        Vehicule v1=new Voiture("1","BMW",120);
        Vehicule v2=new Moto("2","Yamaha",100);
        Vehicule v3=new Voiture("3","Mercedes",130);
        Vehicule v4=new Moto("4","Honda",90);
        vehicules.add(v1);
        vehicules.add(v2);
        vehicules.add(v3);
        vehicules.add(v4);
        int[] vitesses = {110, 100, 105, 80};
        for (int i = 0; i < vehicules.size(); i++) {
            try {
                vehicules.get(i).setVitesseMax(vitesses[i]);
            } catch (VitesseInvalidExption e) {
                System.out.println(e.getMessage());
            }
        }
        List<Vehicule> sortedVehicules = new ArrayList<>(vehicules);
        sortedVehicules.sort(null);
        System.out.println("Sorted Vehicules:");
        for (Vehicule v : sortedVehicules) {
            System.out.println(v);
        }
        for (Vehicule v : vehicules) {
            if(v instanceof Voiture) {
                Thread t1 = new Thread(new SuiviVehicule(v));
                t1.start();
                try {
                    t1.join();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            } else if (v instanceof Moto) {
                Thread t2 = new Thread(new SuiviVehicule(v));
                t2.start();
                try {
                    t2.join();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }   
    }
}
