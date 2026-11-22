package Table;

public class Client {
    protected String nom;
    protected String id;
    public Client(String nom, String id) {
        this.nom = nom;
        this.id = id;
    }
    public Client() {
        this.nom = "";
        this.id = "";
    }
    public String getName(){
        return nom;
    }
     public String getId(){
        return id;
    }
    public void afficher(){
        System.out.println("Nom du client: " + nom);
        System.out.println("ID du client: " + id);
    }
    
    public String toString(){
return "Nom du client: " + nom+"  ID du client: " + id;
    }
    public boolean equals(Client c){
        boolean b= false;
        
        if(this.nom.equals(c.getName())){
            if(this.nom.equals(c.getId())){
                b=true;
            }
        }
        return b;
    }
    public boolean hachcode(Client c){
        boolean b= false;
        if(this.hashCode()==c.hashCode()){
            b=true;
        }
        return b;
    }  
}
