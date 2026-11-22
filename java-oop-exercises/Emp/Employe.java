package Emp;

public class Employe {
protected static int id_num;    
protected  String id;
protected  String nom;
protected  Double sal;
    public Employe(String nom,double sal){
    this.nom=nom;
    this.sal=sal;
    this.id="IA"+this.id_num;
    this.id_num++;
}
public String getNom(){
    return this.nom;
}
public String getId(){
    return this.id;
}
public Double getSal(){
    return this.sal;
}
public void setNom(String nom){
    this.nom=nom;
}
public void setSal(Double sal){
    this.sal=sal;
}
public void setID(String id){
    this.id=id;
}
public String toStrig(){
return "nom:"+this.nom+"\n sal:"+this.sal+"\n id:"+this.id;
}
public int compId(Employe oth){
    return this.id.compareTo(oth.id);
}
public int compNom(Employe oth){
    return this.nom.compareTo(oth.nom);
}
public int compSal(Employe oth){
    return Double.compare(this.sal,oth.sal);
}


    
}