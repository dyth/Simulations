public class Creature {

	private double x;
	private double y;
	private double movement = 30.0;

	public Creature(int x, int y) {
		this.x = (double) x;
		this.y = (double) y;
	}

	public void move(double X, double Y, double SCALE) {
		final double length = Math.sqrt((X-x)*(X-x) + (Y-y)*(Y-y));
		if (length > movement) {
			x += movement * (X-x) / length;
			y += movement * (Y-y) / length;
		} else {
			x = X;
			y = Y;
		}
	}

	public int getX() {
		return (int) x;
	}
	
	public int getY() {
		return (int) y;
	}
	
}
