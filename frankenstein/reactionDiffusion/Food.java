public class Food extends Matter {

	public Food(int X_LENGTH, int Y_LENGTH, double diffusionRate, double reactionRate) {
		super(X_LENGTH, Y_LENGTH, diffusionRate, reactionRate);
	}

	public void react(Waste waste) {
		for (int x = 0; x < X_LENGTH; x++) {
			for (int y = 0; y < Y_LENGTH; y++) {
				matter[x][y] += reactionRate * waste.get(x, y);
			}
		}
	}

	public void eat(double X, double Y, double SCALE) {
		final double RADIUS = 30.0 / SCALE;
		X /= SCALE;
		Y /= SCALE;
		for (int x = 0; x < X_LENGTH; x++) {
			for (int y = 0; y < Y_LENGTH; y++) {
				if (RADIUS*RADIUS > (X-x)*(X-x) + (Y-y)*(Y-y)) {
					matter[x][y] = 0.0;
				}
			}
		}
	}
	
}
