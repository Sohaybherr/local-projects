package PointT;
public class Cercle {
    private Point centre;
    private double rayon;

    public Cercle(Point centre, double rayon) {
        this.centre = centre;
        this.rayon = rayon;
    }
    public void translater(double dx, double dy) {
        centre.deplacer(dx, dy);
    }

    public void afficherCercle() {
        System.out.print("Cercle de centre ");
        centre.afficher();
        System.out.println(" et de rayon " + rayon);
    }
}