package Point;
import java.util.Vector;

public class VectorPoint  {
    Vector<Point> points;

    public VectorPoint() {
        points = new Vector<>();
    }

    public void addPoint(Point p) {
        points.add(p);
    }

    public Point getPoint(int index) {
        return points.get(index);
    }
    public void removePoint(int index) {
        Point p1=points.get(index);
        points.remove(p1);
    }                   

    public int getSize() {
        return points.size();
    }
    public void printAllPoints() {
        for (Point p : points) {
            if(p instanceof Point3D){
                ((Point3D) p).printPoint3D();
                continue;
            }
            p.printPoint();
        }
    }
}
