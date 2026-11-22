package bibleo;

public class Livre extends Document {
    protected int pagenum;
public Livre(int a, String b,String c,int d){
    super(a, b, c);
    this.pagenum=d;
}
@Override
public String toString(){
    return super.toString()+", nombre de pages: "+this.pagenum;

}
@Override
public String getTitle() {
    return this.titre;
}
}