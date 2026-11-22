package Table;

public class Testclient {
    public static void main(String[] args) {
        Client client1= new Client("rivaldo","I12");
        client1.afficher();
        ClientSpe clientspe1= new ClientSpe("rivaldo", "I123", 2.5f);
        clientspe1.afficher();
        Client client2 = new Client("rivaldo","I234");
        String a= client1.toString();
        boolean b= client1.equals(client2);
        boolean c= client1.hachcode(client2);
        System.out.println(a);
        if(b){
            System.out.println("ils sont egaux");
        }
        else{
           System.out.println("ils ne sont pas egaux"); 
        }
        if(c){
            System.out.println("ils ont meme hachcod"); 
        }
        else{
         System.out.println("ils ont different hachcod");    
        }


    }
}
