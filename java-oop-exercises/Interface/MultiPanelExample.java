package Interface;

import java.awt.*;
import javax.swing.*;

public class MultiPanelExample extends JFrame {

    public MultiPanelExample() {

        // ===== JFrame =====
        setTitle("JFrame avec plusieurs JPanel");
        setSize(500, 400);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // ===== Panel NORTH (FlowLayout) =====
        JPanel panelNorth = new JPanel();
        panelNorth.setLayout(new FlowLayout());

        panelNorth.add(new JButton("Button 1"));
        panelNorth.add(new JButton("Button 2"));
        panelNorth.add(new JButton("Button 3"));

        // ===== Panel CENTER (GridLayout) =====
        JPanel panelCenter = new JPanel();
        panelCenter.setLayout(new GridLayout(2, 2));

        panelCenter.add(new JButton("1"));
        panelCenter.add(new JButton("2"));
        panelCenter.add(new JButton("3"));
        panelCenter.add(new JButton("4"));

        // ===== Panel SOUTH (BorderLayout) =====
        JPanel panelSouth = new JPanel();
        panelSouth.setLayout(new BorderLayout());

        panelSouth.add(new JButton("OK"), BorderLayout.WEST);
        panelSouth.add(new JButton("Cancel"), BorderLayout.EAST);

        // ===== Ajouter les panels au JFrame =====
        add(panelNorth, BorderLayout.NORTH);
        add(panelCenter, BorderLayout.CENTER);
        add(panelSouth, BorderLayout.SOUTH);

        setVisible(true);
    }

    public static void main(String[] args) {
        new MultiPanelExample();
    }
}
