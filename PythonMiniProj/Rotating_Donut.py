
import os
import pygame
import colorsys
from math import cos, sin

# Constants for screen and rendering
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 800
FPS = 60

# Pixel spacing (resolution of the output characters)
PIXEL_WIDTH = 20
PIXEL_HEIGHT = 20
GRID_COLS = WIDTH // PIXEL_WIDTH
GRID_ROWS = HEIGHT // PIXEL_HEIGHT
GRID_SIZE = GRID_COLS * GRID_ROWS

# Donut rendering constants
R1 = 10   # Inner radius
R2 = 20   # Outer radius
K2 = 200  # Distance from viewer
K1 = GRID_ROWS * K2 * 3 / (8 * (R1 + R2))  # Perspective projection constant

# Angle increment steps (smaller = more detailed but slower)
THETA_STEP = 20
PHI_STEP = 10

# ASCII characters for shading
LUMINANCE_CHARS = ".,-~:;=!*#$@"

# Set up pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Courier New', 20, bold=True)
pygame.display.set_caption("3D Donut Rotation")

def hsv_to_rgb(h, s, v):
    # Convert HSV to RGB color
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def draw_char(char, x, y, color):
    # Render a single character at a pixel location
    text_surface = font.render(str(char), True, color)
    rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, rect)

def render_frame(angle_a, angle_b, hue):
    # Render one frame of the spinning donut
    output = [' '] * GRID_SIZE
    zbuffer = [0] * GRID_SIZE

    cos_a = cos(angle_a)
    sin_a = sin(angle_a)
    cos_b = cos(angle_b)
    sin_b = sin(angle_b)

    for theta in range(0, 628, THETA_STEP):
        costheta = cos(theta / 100)
        sintheta = sin(theta / 100)
        for phi in range(0, 628, PHI_STEP):
            cosphi = cos(phi / 100)
            sinphi = sin(phi / 100)

            circle_x = R2 + R1 * costheta
            circle_y = R1 * sintheta

            x = circle_x * (cos_b * cosphi + sin_a * sin_b * sinphi) - circle_y * cos_a * sin_b
            y = circle_x * (sin_b * cosphi - sin_a * cos_b * sinphi) + circle_y * cos_a * cos_b
            z = K2 + cos_a * circle_x * sinphi + circle_y * sin_a
            ooz = 1 / z

            xp = int(GRID_COLS / 2 + K1 * ooz * x)
            yp = int(GRID_ROWS / 2 - K1 * ooz * y)
            pos = xp + GRID_COLS * yp

            luminance = cosphi * costheta * sin_b - cos_a * costheta * sinphi - sin_a * sintheta + cos_b * (cos_a * sintheta - costheta * sin_a * sinphi)
            if 0 <= pos < GRID_SIZE and ooz > zbuffer[pos]:
                zbuffer[pos] = ooz
                index = int(luminance * 8)
                output[pos] = LUMINANCE_CHARS[max(0, min(index, len(LUMINANCE_CHARS) - 1))]

    screen.fill(BLACK)
    for i in range(GRID_ROWS):
        for j in range(GRID_COLS):
            idx = i * GRID_COLS + j
            draw_char(output[idx], j * PIXEL_WIDTH + PIXEL_WIDTH // 2, i * PIXEL_HEIGHT + PIXEL_HEIGHT // 2, hsv_to_rgb(hue, 1, 1))

def main():
    running = True
    paused = False
    angle_a = 0
    angle_b = 0
    hue = 0

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    paused = not paused

        if not paused:
            render_frame(angle_a, angle_b, hue)
            pygame.display.update()
            angle_a += 0.15
            angle_b += 0.035
            hue = (hue + 0.005) % 1

    pygame.quit()

if __name__ == "__main__":
    main()
