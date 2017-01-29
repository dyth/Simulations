public class Waste extends Matter {

	public Waste(int X_LENGTH, int Y_LENGTH, double diffusionRate, double reactionRate) {
		super(X_LENGTH, Y_LENGTH, diffusionRate, reactionRate);
	}

	public void react() {
		for (int x = 0; x < X_LENGTH; x++) {
			for (int y = 0; y < Y_LENGTH; y++) {
				matter[x][y] *= (1.0 - reactionRate);
			}
		}
	}

	public void dump(double X, double Y, double SCALE, Food food) {
		final double RADIUS = 30.0 / SCALE;
		X /= SCALE;
		Y /= SCALE;
		for (int x = 0; x < X_LENGTH; x++) {
			for (int y = 0; y < Y_LENGTH; y++) {
				if (RADIUS*RADIUS > (X-x)*(X-x) + (Y-y)*(Y-y)) {
					matter[x][y] += food.get(x, y);
				}
			}
		}
	}
	
}
