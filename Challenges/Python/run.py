import pygame
import random
import math
import sys
import imageio

class Robot:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.direction = random.uniform(0, math.pi * 2)

    def update(self, width, height):
        # Move the robot in a straight line
        dx = self.speed * math.cos(self.direction)
        dy = self.speed * math.sin(self.direction)
        self.x += 0.05*dx
        self.y += 0.05*dy

        # Bounce off the screen edges
        if self.x < self.size / 2 or self.x > width - self.size / 2:
            self.direction = random.uniform(0, math.pi * 2)
            self.x = min(max(self.x, self.size / 2), width - self.size / 2)

        if self.y < self.size / 2 or self.y > height - self.size / 2:
            self.direction = random.uniform(0, math.pi * 2)
            self.y = min(max(self.y, self.size / 2), height - self.size / 2)

        # Generate random motion
        dtheta = random.uniform(-0.1, 0.1)

        # Update robot direction
        self.direction += dtheta

    def draw(self, screen):
        pygame.draw.circle(screen, (173, 216, 230), (int(self.x), int(self.y)), self.size)
        x2 = self.x + self.size / 2 * math.cos(self.direction)
        y2 = self.y + self.size / 2 * math.sin(self.direction)
        pygame.draw.line(screen, (0, 255, 0), (self.x, self.y), (x2, y2), 2)

class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.robot = Robot(width / 2, height / 2, 20, 2)
        self.theta = 0.1

        # Create Pygame screen
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Brownian Motion")

    def run(self):
        # Create an empty list to store the frames
        frames = []

        # Main loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update the robot
            self.robot.update(self.width, self.height)

            # Draw the robot
            self.screen.fill((255, 255, 255))
            self.robot.draw(self.screen)

            # Append the current frame to the list
            #frames.append(pygame.surfarray.array3d(self.screen))

            # Update Pygame display
            pygame.display.flip()

        # Save the frames as a GIF
        imageio.mimsave('animation.gif', [imageio.imread(f) for f in sorted(os.listdir('frames'))], fps=30)

        imageio.mimsave('simulation.gif', frames)

        # Quit Pygame
        pygame.quit()


if __name__ == '__main__':
    sim = Simulation(500, 500)
    sim.run()
