import models.Datagrp;

public class App {
    public static void main(String[] args)  {
           Datagrp familly=new Datagrp();
        String[] names={"Alice","Bob","Charlie"};
        int[] ages={30,25,35};
        String[] addresses={"123 Main St","456 Oak Ave","789 Pine Rd"};
        for(int i=0;i<3;i++){
            familly.addElement(i, names[i], ages[i], addresses[i]);
        }
        familly.sort();
        familly.display();
    }
}
