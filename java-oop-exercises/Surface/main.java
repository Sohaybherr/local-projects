package Surface;
public class main {
    public static int sum(int a , int b){
        return a+b;
    }
    public static void main(String[] args) {
        SurfaceForme sf = new SurfaceForme();
        sf.calculSur(5);
        sf.calculSur(3);
        sf.calculSur(4, 6);
        int b=sum(2,2);
        System.out.println(b);
}
}
