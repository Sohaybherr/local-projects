package Pairtable;

public class main {
    public static void main(String[] args) {
        Apptable pt = new Apptable();
        try {
            pt.add(4);
            pt.add(7);
            pt.add(10);
            pt.add(3); // This will throw NomNotPair exception
        } catch (NomNotPair e) {
            System.out.println(e.getMessage());
        }
        try {
            pt.add(8);
            pt.add(12);
            pt.add(10);
            pt.add(6);
        pt.add(5);
        } catch (NomNotPair e) {
            System.out.println(e.getMessage());
        }

        System.out.println("Exist 7: " );
        try {
            System.out.println(pt.exist(7));
        } catch (NomNotPair e) {
            System.out.println(e.getMessage());
        }
        System.out.println("Index of 10: ");
        try{
            System.out.println(pt.getindice(10));
        }
        catch(NomNotPair e){
            System.out.println(e.getMessage());
        }
        pt.show();
    }

    
}
