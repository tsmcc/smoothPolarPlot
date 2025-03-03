import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# define a function to create a polar plot with given angles and radial points
def create_polar_plot(angles, radii_sets, colors):
    # create polar plot
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    for radii, color in zip(radii_sets, colors):
        # smooth the transition between points
        angles_smooth = np.linspace(angles.min(), angles.max(), 300)
        spl = make_interp_spline(angles, radii, k=3)
        radii_smooth = spl(angles_smooth)

        # Plot the lines and fill the area under the plot with the line color
        ax.plot(angles_smooth, radii_smooth, color=color)
        ax.fill(angles_smooth, radii_smooth, color=color, alpha=0.3)

    # Set the title
    ax.set_title("30deg Polar Plot")

    # Set the angle labels, excluding the 360 degree label (overlaps), use small font
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([f"{int(round(np.rad2deg(angle)))}°" for angle in angles[:-1]], fontsize='small')
    
    # Rotate the plot 90deg counterclockwise, and reverse the plot order
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Automatically scale the radii labels based on the maximum value from all radii sets
    max_radius = max(max(radii) for radii in radii_sets) * 1.2
    ax.set_ylim(0, max_radius)

    # Change the radii label text to gray (easier to read)
    ax.tick_params(axis='y', colors='gray', direction='in', labelsize='small')

    # create the plot
    plt.show()

# define angles (theta)
theta = np.deg2rad([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360])

# radial points for three sets (ref above angles) 
# to add radii_sets, define here, define COLOR below, and add to CREATE_POLAR_PLOT 
radii_set1 = [0, 51, 84, 101, 84, 52, 0, 51, 84, 101, 84, 52, 0]
radii_set2 = [0, 24, 44, 51, 44, 24, 0, 24, 44, 51, 44, 24, 0]
radii_set3 = [0, 29, 65, 83, 70, 28, 0, 29, 65, 83, 70, 28, 0]

# color each radii set
colors = ['blue', 'red', 'green']

# add input values to the plot
create_polar_plot(theta, [radii_set1, radii_set2, radii_set3], colors)

