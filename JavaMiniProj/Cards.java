
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.util.ArrayList;
import java.util.Collections;

public class Main extends JFrame {
    private JPanel cardPanel;
    private JButton shuffleButton;
    private ArrayList<String> cardPaths;
    private static final String IMAGE_PATH = "/Users/arpita/Desktop/cs370/lab5/PairProgramming/cards/";

    public Main() {
        setTitle("Card Randomizer");
        setSize(1200, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        cardPanel = new JPanel(new GridLayout(4, 13, 5, 5));
        add(cardPanel, BorderLayout.CENTER);

        shuffleButton = new JButton("Shuffle");
        shuffleButton.addActionListener(new ShuffleListener());
        add(shuffleButton, BorderLayout.SOUTH);

        loadCardImages();
        displayCards();

        setVisible(true);
    }

    private void loadCardImages() {
        cardPaths = new ArrayList<>();
        String[] suits = {"s", "h", "c", "d"};
        String[] ranks = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};

        for (String rank : ranks) {
            for (String suit : suits) {
                String path = IMAGE_PATH + suit + rank + ".png";
                cardPaths.add(path);
            }
        }
    }

    private void displayCards() {
        cardPanel.removeAll();
        for (int i = 0; i < cardPaths.size(); i++) {
            File file = new File(cardPaths.get(i));
            if (file.exists()) {
                ImageIcon icon = new ImageIcon(cardPaths.get(i));
                Image scaledImage = icon.getImage().getScaledInstance(80, 120, Image.SCALE_SMOOTH);
                ImageIcon scaledIcon = new ImageIcon(scaledImage);
                JLabel label = new JLabel(scaledIcon);
                cardPanel.add(label);
                cardPanel.setBackground(new Color(235, 141, 197));
                System.out.println("Displaying: " + cardPaths.get(i) + " at index " + i);
            } else {
                System.out.println("Missing file at index " + i + ": " + cardPaths.get(i));
            }
        }
        cardPanel.revalidate();
        cardPanel.repaint();
    }

    private class ShuffleListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            Collections.shuffle(cardPaths);
            displayCards();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(Main::new);
    }
}
