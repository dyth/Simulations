import java.awt.Graphics;
import java.awt.GraphicsEnvironment;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;
import java.awt.Color;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionListener;
import java.awt.Point;

public class World extends JPanel implements ActionListener, MouseMotionListener {
	
	private final int SCALE;
	private final int X_LENGTH;
	private final int Y_LENGTH;
	private Food food;
	private Waste waste;
	private Creature creature;
	private Point point;
	private Point direction;
	
	public World(int X_LENGTH, int Y_LENGTH, int SCALE, double reactionRate, double diffusionRate) {
		this.addMouseMotionListener(this);
		this.X_LENGTH = X_LENGTH;
		this.Y_LENGTH = Y_LENGTH;
		this.SCALE = SCALE;
		food = new Food(X_LENGTH, Y_LENGTH, diffusionRate, reactionRate);
		waste = new Waste(X_LENGTH, Y_LENGTH, diffusionRate, reactionRate);
		creature = new Creature(X_LENGTH*SCALE / 2, Y_LENGTH*SCALE / 2);
		direction = new Point(X_LENGTH*SCALE/2, Y_LENGTH*SCALE/2);
		new Timer(100, this).start();
	}

	public int cap(double x) {
		if (x > 255.0)
			return 255;
		else if (x < 0.0)
			return 0;
		else
			return (int) x;
	}

	public int logistic(double x) {
		return (int) (255.0 / (1.0 + Math.pow(Math.E, 2.0 - 2.0*x/127.5)));
	}
	
	public void paint(Graphics graphics) {
		for (int x = 0; x < X_LENGTH; x++) {
			for (int y = 0; y < Y_LENGTH; y++) {
				final int WASTE = logistic(waste.get(x, y));
				final int FOOD = logistic(food.get(x, y));
				graphics.setColor(new Color(0, 0, 255, FOOD));
				graphics.fillRect(x*SCALE, y*SCALE, SCALE, SCALE);
				graphics.setColor(new Color(255, 0, 0, WASTE));
				graphics.fillRect(x*SCALE, y*SCALE, SCALE, SCALE);
			}
		}
		creature.move(direction.getX(), direction.getY(), (double) SCALE);
		graphics.setColor(Color.black);
		graphics.fillOval(creature.getX()-15, creature.getY()-15, 30, 30);
	}

	public void mouseMoved(MouseEvent e) {
		direction = e.getPoint();
		repaint();
    }

	public void mouseDragged(MouseEvent e) {
		point = e.getPoint();
		waste.dump(point.getX(), point.getY(), (double) SCALE, food);
		food.eat(point.getX(), point.getY(), (double) SCALE);
		repaint();
    }
	
	public void actionPerformed(ActionEvent actionEvent) {
		food.diffuse();
		waste.diffuse();
		food.react(waste);
		waste.react();
		repaint();
	}

	public static void main(String[] args) {
		double diffusionRate;
		double reactionRate;
		if (args.length == 2) {
			diffusionRate = Double.parseDouble(args[0]);
			reactionRate = Double.parseDouble(args[1]);
		} else {
			diffusionRate = 0.2;
			reactionRate = 0.01;
		}
		final int SCALE = 2;
		GraphicsEnvironment g=GraphicsEnvironment.getLocalGraphicsEnvironment();
		final int X_LENGTH = (g.getMaximumWindowBounds().height - 20) / SCALE;
		final int Y_LENGTH = X_LENGTH;
		
		JFrame frame = new JFrame("Reaction-Diffusion");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(X_LENGTH * SCALE, Y_LENGTH * SCALE);
		frame.add(new World(X_LENGTH, Y_LENGTH, SCALE, reactionRate, diffusionRate));
		frame.setVisible(true);
	}
	
}
