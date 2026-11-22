package PointT;

public class Point {
    private double x;
    private double y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
    public Point() {
       this(0,0);
    }
    void deplacer(double dx, double dy) {
        this.x += dx;
        this.y += dy;
    }
    void afficher() {
        System.out.println("Point(" + x + ", " + y + ")");
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }
}