package PointT;

public class main {
    public static void main(String[] args) {
        Point p1 = new Point(2, 3);
        Point p2 = new Point();
        p2.setX(5);
        p2.setY(7);
        p1.afficher();
        p2.afficher();
        p1.deplacer(1.5, -2);
        p1.afficher();
         Cercle c = new Cercle(p1, 4);
        c.afficherCercle();
        c.translater(2, 3);
        c.afficherCercle();
    }
}
