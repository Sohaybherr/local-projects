package Point;

public class Point {
protected int x;
protected int y;
public Point(int a ,int b ){this.x=a;this.y= b;}
public Point(){this.x=0;this.y=0;}
public void setX(int a){this.x=a;}
public void setY(int b){this.y=b;}
public int getX(){return this.x;}
public int getY(){return this.y;}
public void printPoint(){System.out.println("{"+x+","+y+"}");}
}
