package Point;

public class Point3D extends Point {
    protected int z;
    public Point3D(int a,int b,int c){
        super(a, b);
        this.z=c;
    }
    public void setZ(int a){
        this.z=a;
    }
    public int getZ(){
        return this.z;
    }
    public void printPoint3D(){
        System.out.println("{"+this.x+","+this.y+","+this.z+"}");
    }
}