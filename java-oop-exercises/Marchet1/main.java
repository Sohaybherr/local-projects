package Marchet1;

public class main {
  public static void main(String[] args) {
        Produit p1=new Produit(1,"Pain",2.5);
        Produit p2=new Produit(2,"Lait",3.0);
        Produit p3=new Produit(3,"fromage",0);
        ProduitService ps=new ProduitService();
        try{
            ps.create(p1);
            ps.create(p2);
        }catch(InvalidPriceException e){
            System.out.println(e.getMessage());
        }
        try{
            ps.create(p3);
        }catch(InvalidPriceException e){
            System.out.println(e.getMessage());
        }
        ps.findAll().stream().sorted((a,b)->a.toCompareTo(b)).forEach(a->System.out.println(a.toString()));

        }
  }  

