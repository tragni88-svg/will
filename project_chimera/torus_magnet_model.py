
import numpy as np
import matplotlib.pyplot as plt

class TorusMagnet:
    """
    Models and visualizes the magnetic field of a superconducting torus.
    This script simplifies the model to a 2D cross-section, showing the poloidal
    field that confines the plasma.
    """
    def __init__(self, major_radius, minor_radius, current, num_windings):
        """
        Initializes the torus magnet model.

        Args:
            major_radius (float): The major radius (center of torus to center of tube) in meters.
            minor_radius (float): The minor radius (radius of the tube) in meters.
            current (float): The current in the superconducting windings in Amperes.
            num_windings (int): The total number of windings in the torus.
        """
        self.R = major_radius
        self.a = minor_radius
        self.I = current
        self.N = num_windings
        self.mu_0 = 4 * np.pi * 1e-7  # Permeability of free space

    def calculate_magnetic_field(self, x, y):
        """
        Calculates the magnetic field vector (Bx, By) at a point (x, y) in the 2D cross-section.
        This is a simplified model treating the torus cross-section as two current bundles.

        Args:
            x (np.ndarray): X-coordinates of the grid.
            y (np.ndarray): Y-coordinates of the grid.

        Returns:
            tuple: (Bx, By) components of the magnetic field vector field.
        """
        # Position of the top and bottom parts of the torus tube
        x_torus = self.R
        
        # Top wire (current out of page)
        r_top_sq = (x - x_torus)**2 + (y - self.a)**2
        B_top_x = -self.mu_0 * self.I * self.N / (2 * np.pi * r_top_sq) * (y - self.a)
        B_top_y =  self.mu_0 * self.I * self.N / (2 * np.pi * r_top_sq) * (x - x_torus)

        # Bottom wire (current into page)
        r_bottom_sq = (x - x_torus)**2 + (y + self.a)**2
        B_bottom_x = self.mu_0 * self.I * self.N / (2 * np.pi * r_bottom_sq) * (y + self.a)
        B_bottom_y = -self.mu_0 * self.I * self.N / (2 * np.pi * r_bottom_sq) * (x - x_torus)

        # Superposition of the two fields
        Bx = B_top_x + B_bottom_x
        By = B_top_y + B_bottom_y
        
        return Bx, By

    def plot_field(self, grid_points=50, filename="toroidal_field_plot.png"):
        """
        Generates and saves a vector plot of the magnetic field.

        Args:
            grid_points (int): The number of points in each dimension of the grid.
            filename (str): The name of the file to save the plot to.
        """
        x = np.linspace(self.R - self.a * 2, self.R + self.a * 2, grid_points)
        y = np.linspace(-self.a * 2, self.a * 2, grid_points)
        X, Y = np.meshgrid(x, y)

        Bx, By = self.calculate_magnetic_field(X, Y)

        # Normalize for visualization
        magnitude = np.sqrt(Bx**2 + By**2)
        # Avoid division by zero
        magnitude[magnitude == 0] = 1.0
        U = Bx / magnitude
        V = By / magnitude

        plt.figure(figsize=(10, 8))
        plt.quiver(X, Y, U, V, color='b', scale=grid_points*0.8, headwidth=4)
        
        # Draw the torus cross-section
        top_coil = plt.Circle((self.R, self.a), self.a / 10, color='r', label='Coil (Current Out)')
        bottom_coil = plt.Circle((self.R, -self.a), self.a / 10, color='k', label='Coil (Current In)')
        plt.gca().add_artist(top_coil)
        plt.gca().add_artist(bottom_coil)

        plt.title("Project Chimera: 2D Cross-Section of Toroidal Magnetic Field")
        plt.xlabel("Radial Distance (m)")
        plt.ylabel("Vertical Distance (m)")
        plt.grid(True)
        plt.axis('equal')
        plt.legend()
        
        plt.savefig(filename)
        print(f"Magnetic field plot saved to {filename}")

if __name__ == '__main__':
    # --- Design Parameters ---
    # A large torus for the vehicle frame
    R_major = 15.0  # meters
    R_minor = 1.5   # meters
    # High current typical of superconducting magnets
    I_superconducting = 5.0e5 # 500,000 Amperes
    N_windings = 1000 # Number of turns

    # --- Simulation ---
    magnet = TorusMagnet(major_radius=R_major, minor_radius=R_minor, current=I_superconducting, num_windings=N_windings)
    magnet.plot_field(filename="c:/Users/bigwi/Documents/trae_projects/google social media/project_chimera/toroidal_field_plot.png")
