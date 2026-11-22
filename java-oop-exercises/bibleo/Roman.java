package bibleo;

public class Roman extends Document {
    protected double price;
public Roman(int a, String b,String c,double d){
    super(a, b, c);
    this.price=d;   
}   
@Override
public String toString(){
    return super.toString()+", prix: "+this.price;
} 
@Override
public String getTitle() {
    return this.titre;
}

}