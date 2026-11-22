package Facu;

public class Etudiant {
   protected int i=0; 
   protected String id;
   protected String nom;
   protected String email;
 public Etudiant(String a, String b){
    this.id="E00"+this.i;
    this.nom=a;
    this.email=b;
    i++;
 }
 public String getId(){
    return this.id;
 }
 public String toString(){
    return "Etudiant [id="+this.id+", nom="+this.nom+", email="+this.email+"]";
 }
}
