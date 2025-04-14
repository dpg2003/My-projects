
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.geom.Line2D;
import java.util.Random;

public class BarChart {
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.setTitle("Random Bar Chart");
        frame.setSize(500, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ChartPanel panel = new ChartPanel();
        frame.add(panel);

        JButton button = new JButton("Redraw");
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                panel.repaint();
            }
        });
        frame.add(button, BorderLayout.SOUTH);
        frame.setVisible(true);
    }
}

class ChartPanel extends JPanel {
    private Random random;

    public ChartPanel() {
        random = new Random();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        int panelWidth = getWidth();
        int panelHeight = getHeight();

        g2d.setColor(Color.LIGHT_GRAY);
        g2d.fillRect(0, 0, panelWidth, panelHeight);

        int chartWidth = (int) (panelWidth * 0.8);
        int chartHeight = (int) (panelHeight * 0.8);
        int offsetX = (panelWidth - chartWidth) / 2;
        int offsetY = (panelHeight - chartHeight) / 2;

        int gridSizeX = chartWidth / 10;
        int gridSizeY = chartHeight / 10;
        chartWidth = gridSizeX * 10;
        chartHeight = gridSizeY * 10;

        g2d.setColor(Color.black);
        for (int i = 0; i <= chartWidth; i += gridSizeX) {
            g2d.drawLine(offsetX + i, offsetY, offsetX + i, offsetY + chartHeight);
        }
        for (int j = 0; j <= chartHeight; j += gridSizeY) {
            g2d.drawLine(offsetX, offsetY + j, offsetX + chartWidth, offsetY + j);
        }

        int numBars = 10;
        g2d.setStroke(new BasicStroke(10f));

        for (int i = 0; i < numBars; i++) {
            int x = offsetX + (i * gridSizeX) + (gridSizeX / 2);
            int barHeight = random.nextInt(chartHeight - gridSizeY);
            int barY = offsetY + (chartHeight - barHeight);

            g2d.setColor(new Color(random.nextInt(256), random.nextInt(256), random.nextInt(256)));
            g2d.draw(new Line2D.Double(x, offsetY + chartHeight, x, barY));
        }
    }
}
