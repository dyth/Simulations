import java.util.Random;

public class Matter {

	protected final int X_LENGTH;
	protected final int Y_LENGTH;
	protected double[][] matter;
	protected double diffusionRate;
	protected double reactionRate;
	
	public Matter(int X_LENGTH, int Y_LENGTH, double diffusionRate, double reactionRate) {
		this.X_LENGTH = X_LENGTH;
		this.Y_LENGTH = Y_LENGTH;
		this.diffusionRate = diffusionRate;
		this.reactionRate = reactionRate;
		matter = new double[X_LENGTH][Y_LENGTH];
		random();
	}

	public void random() {
		Random random = new Random();
		for (int x = 0; x < X_LENGTH; x++) {
			for (int y = 0; y < Y_LENGTH; y++) {
				matter[x][y] = 255 * random.nextFloat();
			}
		}
	}
	
	public void diffuse() {
		double[][] matterNew = new double[X_LENGTH][Y_LENGTH];
		for (int x = 0; x < X_LENGTH; x++) {
			for (int y = 0; y < Y_LENGTH; y++) {
				// diffusion
				int x_neg = (x - 1 + X_LENGTH) % X_LENGTH;
				int x_pos = (x + 1 + X_LENGTH) % X_LENGTH;
				int y_neg = (y - 1 + Y_LENGTH) % Y_LENGTH;
				int y_pos = (y + 1 + Y_LENGTH) % Y_LENGTH;
				matterNew[x][y] = diffusionRate *
					(matter[x_neg][y] + matter[x][y_neg] +
					 matter[x_pos][y] + matter[x][y_pos]) +
					(1.0 - 4.0*diffusionRate)*matter[x][y];
			}
		}
		matter = matterNew;
	}

	public double get(int x, int y) {
		return matter[x][y];
	}

	public void set(int x, int y, double value) {
		matter[x][y] = value;
	}
	
}
