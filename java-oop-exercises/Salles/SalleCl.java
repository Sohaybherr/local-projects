package Salles;

public class SalleCl {
    private static int idinc=0;
    private String  id;
    private  int code;
    private String libelle;
    public SalleCl( int code, String libelle){
        this.id="I0"+(++idinc);
        this.code=code;
        this.libelle=libelle;
    }
    public void setId(String id){
        this.id =id;
    } 
    public void setCode(int code){
        this.code=code;
    }
    public void setLibelle(String libelle){
        this.libelle=libelle;
    } 
    public String toString(){
        return "SalleCl [id="+this.id+", code="+this.code+", libelle="+this.libelle+"]";
    }  
    public int compareTo(SalleCl s){
        return this.libelle.compareToIgnoreCase(s.libelle);
    }  
}
