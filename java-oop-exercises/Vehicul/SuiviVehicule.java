package Vehicul;

public class SuiviVehicule implements  Runnable {
    private Vehicule v;
    public SuiviVehicule(Vehicule v){
        this.v=v;
    }
    @Override
    public void run() {
        for(int i=0;i<5;i++){
            v.consommer();
             try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
           
        }
    }
    
}
