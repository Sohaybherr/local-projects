package bibleo;

import java.util.List;

public class Bibleo {
    protected List<Document> bib= new java.util.ArrayList<Document>();
    protected String name;
    protected int size;
    public Bibleo(int a ,String b){
        this.size=a;
        this.name=b;
    }
 public void showall(){
    for(Document e:this.bib){
        System.out.println(e.toString());
    }
 } 
 public void findByTitle( String a){
     for(Document e:this.bib){
        if (e.getTitle().equals(a)) {
            System.out.println(e.toString());
            return;
        }     
    }
    System.out.println("Document not found");
 } 
 public void addDoc(Document a)throws PlusDePlace{
  if(this.bib.size()>=this.size){
   throw new PlusDePlace("NO MORE PLACES");
  }
  else{
    this.bib.add(a);
  }
 } 
}
