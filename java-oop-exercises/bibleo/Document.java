package bibleo;

public abstract class Document {
protected int num;
protected String auteur;
protected String titre;
public Document(int a, String b,String c){
    this.num=a;
    this.auteur=b;
    this.titre=c;
}
public String toString(){
    return "num: "+this.num+", auteur: "+this.auteur+", titre: "+this.titre;
}
public String getTitle() {
    return "";
}
}
