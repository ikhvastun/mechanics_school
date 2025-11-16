import marimo

__generated_with = "0.17.8"
app = marimo.App(width="full")


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    # --- 1. Set up the t values ---

    # Create a smooth curve for the background path (1000 points)
    # extend a bit so we could see the vectors of velocity and acceleration
    t_curve = np.linspace(-0.2, 1.2, 1000)

    # Create the 10 discrete points for the vectors
    # np.linspace(0, 1, 10) creates 10 points *including* 0 and 1
    t_points = np.linspace(0, 1, 10)


    # --- 2. Define Position Functions ---
    def x_func(t):
        return 3 * t**2 + 5 * t


    def y_func(t):
        return 5 * t**3 + 2 * t**2 - 10 * t + 5


    # Calculate path for the smooth curve
    x_curve = x_func(t_curve)
    y_curve = y_func(t_curve)

    # Calculate positions for the 10 discrete points
    x_points = x_func(t_points)
    y_points = y_func(t_points)


    # --- 3. Define Velocity Functions (1st Derivative) ---
    def vx_func(t):
        return 6 * t + 5


    def vy_func(t):
        # 15t^2 + 4t - 10
        return 15 * t**2 + 4 * t - 10


    # Calculate velocity vectors at the 10 points
    vx_points = vx_func(t_points)
    vy_points = vy_func(t_points)


    # --- 4. Define Acceleration Functions (2nd Derivative) ---
    def ax_func(t):
        # Constant 6
        return np.full_like(t, 6)  # Use np.full_like to get an array of 6s


    def ay_func(t):
        return 30 * t + 4


    # Calculate acceleration vectors at the 10 points
    ax_points = ax_func(t_points)
    ay_points = ay_func(t_points)

    # --- 5. Create the Plot ---
    plt.figure(figsize=(10, 8))

    # Plot the smooth background path
    plt.plot(
        x_curve,
        y_curve,
        label="Path y(x)",
        color="blue",
        linestyle="--",
        alpha=0.4,
    )

    # Plot the 10 discrete points
    plt.plot(x_points, y_points, "o", color="black", label="10 Points (t=0 to 1)")

    # Plot the velocity vectors (Green)
    # We use 'quiver' to draw arrows.
    # We need to set a 'scale' value to make the arrows a reasonable size.
    # A larger 'scale' value makes the arrows *smaller*.
    plt.quiver(
        x_points,
        y_points,
        vx_points,
        vy_points,
        color="green",
        label="Velocity Vectors",
        angles="xy",
        scale_units="xy",
        scale=10,
        width=0.005,
    )

    # Plot the acceleration vectors (Red)
    plt.quiver(
        x_points,
        y_points,
        ax_points,
        ay_points,
        color="red",
        label="Acceleration Vectors",
        angles="xy",
        scale_units="xy",
        scale=10,
        width=0.005,
    )

    # --- 6. Add Labels, Title, and Legend ---
    plt.xlabel("x(t) = 3t$^2$ + 5t")
    plt.ylabel("y(t) = 5t$^3$ + 2t$^2$ - 10t + 5")
    plt.title("Parametric Plot with Velocity and Acceleration Vectors (t=0 to 1)")
    plt.grid(True)
    plt.legend(loc="upper left")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
