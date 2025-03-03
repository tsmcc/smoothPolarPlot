# smoothPolarPlot
Smoothed polar plot for representing polar data of any type. Inspired by ship DP capability plots.

example of output:

![image](https://github.com/user-attachments/assets/8cbd415a-69df-4108-a6c2-d956175c72b4)

Notes: 
- the polar axis are offset 30 degrees (0, 30, 60, 90, ...)
- the polar axis is oriented to 0 degrees UP
- uses scipy.interpolate > make_interp_spline to smooth out the transition between each radial point (looks nice)
- automatically scales the plot size AND labels based on 1.2 times the largest radial point

Additional radial point sets can be added (radii_set4, radii_set5, ...) - just be sure to define a COLOR for each additional set, and include the set in CREATE_POLAR_PLOT at the end. 
