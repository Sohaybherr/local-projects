package Vehicul;

abstract public class Vehicule implements Comparable<Vehicule> {
protected String id;
protected String marque;
protected  int vitesseMax;
public Vehicule(String id,String marque,int vitesse){
    this.id=id;
    this.marque=marque;
    this.vitesseMax=vitesse;
}
abstract void  consommer();
public void setVitesseMax(int v)throws VitesseInvalidExption{
    if(v<=20 || v>120){
        throw new VitesseInvalidExption("Invalid Vitesse");
    }
    else{
        this.vitesseMax=v;
    }
}
public int getvitesse(){
    return this.vitesseMax;
}
public String getmarque(){
    return this.marque;
}
@Override
public int compareTo(Vehicule o){
    if(this.vitesseMax==o.getvitesse()){
        return this.marque.compareTo(o.getmarque());
    }
    else{
        return -this.vitesseMax+o.getvitesse();
    }

}
public String toString(){
    return "\n"+this.id+" "+this.marque+" "+this.vitesseMax;
}
}
