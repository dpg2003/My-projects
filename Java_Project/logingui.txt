import javax.swing.*;

public class loginpage {
    public static void main(String[] args) {
        JPanel panel = new JPanel();
        JFrame frame = new JFrame("Login Page");
        frame.setSize(350,200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(panel);
        panel.setLayout(null);
        //username label output
        JLabel userLabel = new JLabel("Username");
        userLabel.setBounds(40, 20, 80, 25);
        panel.add(userLabel);
        //creating user text box
        JTextField userTxt = new JTextField(40);
        userTxt.setBounds(110, 20, 165, 25);
        panel.add(userTxt);

        //password label output
        JLabel passwordLabel = new JLabel("Password");
        passwordLabel.setBounds(40, 50, 80, 25);
        panel.add(passwordLabel);

        //creating password text box
        JPasswordField passwordTxt = new JPasswordField(40);
        passwordTxt.setBounds(110, 50, 165, 25);
        panel.add(passwordTxt);

        //button for login
        JButton loginButton = new JButton("Login");
        loginButton.setBounds(150, 100, 80, 25);
        panel.add(loginButton);

        frame.setVisible(true);


    }
}
