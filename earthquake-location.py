
## A program to calculate the (x,y) location of an earthquake_CSP2023.SD

## this code is a basic representation for educational purposes and doesn't
## involve real seismic data or advanced algorithms used in actual earthquake location systems.
## In real scenarios, a complex network of seismometers and advanced techniques are used
## to accurately locate the earthquake epicenter. The speed of seismic waves used in this
## example is arbitrary and may not reflect real-world values. In practice, seismic wave speeds
## depend on the properties of the Earth's crust and mantle.
## answer: Estimated earthquake epicenter (x, y) positions: [3.33333333 3.33333333].
################################################################################################
################################################################################################
# Centre for Seismological Phenomena Aug.2023©. All rights reserved - Sudan.
# by Hussein Muhammed; Abdelhafiz Gadelmula Taha.
################################################################################################
################################################################################################

import numpy as np


# python function to calculate earthquake location
def locate_earthquake(p_wave_times, s_wave_times, station_coords):
    # Calculate time differences between P-waves and S-waves
    time_diffs = s_wave_times - p_wave_times

    # Speed of P-waves and S-waves in km/s (you can adjust these values)
    p_wave_speed = 6.0
    s_wave_speed = 3.5

    # Calculate distances from each station to the earthquake epicenter
    distances = time_diffs * (p_wave_speed + s_wave_speed) / 2.0

    # Triangulation - find epicenter (average of station coordinates)
    epicenter = np.mean(station_coords, axis=0)

    return epicenter


# Example usage
if __name__ == "__main__":
    # Simulated arrival times of P-waves and S-waves (in seconds)
    p_wave_times = np.array([5.0, 7.0, 6.0])
    s_wave_times = np.array([14.0, 17.0, 16.0])

    # Station coordinates (x, y) in km
    station_coords = np.array([[0, 0], [10, 0], [0, 10]])

    # Call the function to locate the earthquake
    epicenter = locate_earthquake(p_wave_times, s_wave_times, station_coords)

    print("Estimated earthquake epicenter (x, y)-position is:", epicenter)
