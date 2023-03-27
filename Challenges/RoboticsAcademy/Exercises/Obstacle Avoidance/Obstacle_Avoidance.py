from GUI import GUI
from HAL import HAL
import math
import time

# Constants
MAX_SPEED = 1.0
MAX_FORCE = 1.0
SAFE_DISTANCE = 0.5

# Helper functions
def normalize(v):
    norm = math.sqrt(v[0]**2 + v[1]**2)
    if norm == 0:
        return (0, 0)
    return (v[0] / norm, v[1] / norm)

def limit_magnitude(v, limit):
    norm = math.sqrt(v[0]**2 + v[1]**2)
    if norm > limit:
        return (v[0] * limit / norm, v[1] * limit / norm)
    return v

def vff_forces(pose, laser_data, target_pose):
    # Calculate repulsive forces from obstacles
    obs_forces = []
    for i in range(90-45, 90+45):
        angle = math.radians(i)
        dist = laser_data.values[i] / 1000.0
        if dist < SAFE_DISTANCE:
            force = MAX_FORCE * (1.0 / dist - 1.0 / SAFE_DISTANCE) / (dist**2)
            obs_forces.append((force * math.cos(angle), force * math.sin(angle)))
    obs_force = tuple(map(sum, zip(*obs_forces))) if len(obs_forces) > 0 else (0, 0)
    
    # Calculate attractive force to target
    target_vec = (target_pose.x - pose.x, target_pose.y - pose.y)
    target_force = limit_magnitude(target_vec, MAX_FORCE)
    
    # Calculate resulting forces
    car_vec = (math.cos(pose.yaw), math.sin(pose.yaw))
    car_force = limit_magnitude(car_vec, MAX_FORCE)
    avg_force = limit_magnitude(tuple(map(sum, zip(obs_force, target_force))), MAX_FORCE)
    return (car_force, obs_force, avg_force, target_force)

# Main loop
while True:
    # Get target pose from GUI
    currentTarget = GUI.map.getNextTarget()
    target_pose = currentTarget.getPose()
    
    # Get robot pose, laser data, and calculate forces
    pose = HAL.getPose3d()
    laser_data = HAL.getLaserData()
    car_force, obs_force, avg_force, target_force = vff_forces(pose, laser_data, target_pose)
    
    # Combine forces to get desired velocity
    total_force = tuple(map(sum, zip(car_force, obs_force, avg_force, target_force)))
    desired_velocity = normalize(total_force)
    desired_velocity = limit_magnitude(desired_velocity, MAX_SPEED)
    
    # Set robot velocity
    HAL.setV(desired_velocity[0])
    HAL.setW(desired_velocity[1])
    
    # Show debug information in GUI
    GUI.showLocalTarget((target_pose.x - pose.x, target_pose.y - pose.y))
    GUI.showForces(tuple(map(lambda x: x * 10, car_force)), 
                   tuple(map(lambda x: x * 10, obs_force)), 
                   tuple(map(lambda x: x * 10, avg_force)))
    
    # Sleep for a short period of time to give the robot time to move
    time.sleep(0.1)
