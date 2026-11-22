package Point;

public class main {
    public static void main(String[] args) {
        VectorPoint vp = new VectorPoint();
        Point3D p1 = new Point3D(1, 2, 3);
        Point3D p2 = new Point3D(4, 5, 6);
        Point3D p3 = new Point3D(7, 8, 9);
        Point p4= new Point(10,11);
        

        vp.addPoint(p1);
        vp.addPoint(p2);
        vp.addPoint(p3);
        vp.addPoint(p4);

        vp.printAllPoints();
    }
}
