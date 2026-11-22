package Surface;
public class SurfaceForme {

public static float calculSur(float a){
    float res = a * a;
    System.out.println("Calcul de la surface du carré: " + res);
    return res;
}
public static float calculSur(double r){
    float res = (float) (Math.PI * r * r);
    System.out.println("Calcul de la surface du cercle: " + res);
    return res;
}  
public static float calculSur(float l,float L){
   float res=L*l;
    System.out.println("Calcul de la surface du rectangle: " + res);
    return res;
}  
}  