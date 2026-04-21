import pygame

import math
import random

class PaddleGame:
    def __init__(self, width=1280, height=720):
        self.width = width
        self.height = height
        
        # Tuning factors (match script.rpy)
        self.table_scale = 1.0
        self.table_width_offset = 0
        self.table_height_offset = 0
        
        # Player paddle (left side)
        self.paddle_width = 15
        self.paddle_height = 120
        self.paddle_x = 50
        self.paddle_y = height // 2 - self.paddle_height // 2
        self.paddle_speed = 8
        
        # Ball
        self.ball_radius = 8
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_speed_x = 5
        self.ball_speed_y = 5
        self.max_ball_speed = 12
        
        # Enemy paddle (right side - AI)
        self.enemy_x = width - 50 - self.paddle_width
        self.enemy_y = height // 2 - self.paddle_height // 2
        self.enemy_speed = 6
        
        # Game state
        self.player_score = 0
        self.enemy_score = 0
        self.game_running = True
        
        # Input
        self.player_moving_up = False
        self.player_moving_down = False
    
    def handle_input(self, keys):
        """Handle player input"""
        self.player_moving_up = keys.get('up', False)
        self.player_moving_down = keys.get('down', False)
    
    def update(self, dt):
        """Update game state"""
        if not self.game_running:
            return
        
        # Update player paddle
        if self.player_moving_up and self.paddle_y > 0:
            self.paddle_y -= self.paddle_speed
        if self.player_moving_down and self.paddle_y < self.height - self.paddle_height:
            self.paddle_y += self.paddle_speed
        
        # Update ball
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y
        
        # Ball collision with top and bottom
        if self.ball_y - self.ball_radius < 0 or self.ball_y + self.ball_radius > self.height:
            self.ball_speed_y = -self.ball_speed_y
            self.ball_y = max(self.ball_radius, min(self.height - self.ball_radius, self.ball_y))
        
        # Ball collision with left paddle (player)
        if self.check_paddle_collision(self.paddle_x, self.paddle_y, self.ball_x, self.ball_y):
            self.ball_speed_x = -self.ball_speed_x
            self.ball_x = self.paddle_x + self.paddle_width + self.ball_radius
            # Add spin based on where ball hits paddle
            hit_pos = (self.ball_y - self.paddle_y) / self.paddle_height
            self.ball_speed_y += (hit_pos - 0.5) * 4
            self.ball_speed_y = max(-self.max_ball_speed, min(self.max_ball_speed, self.ball_speed_y))
        
        # Ball collision with right paddle (enemy)
        if self.check_paddle_collision(self.enemy_x, self.enemy_y, self.ball_x, self.ball_y):
            self.ball_speed_x = -self.ball_speed_x
            self.ball_x = self.enemy_x - self.ball_radius
            hit_pos = (self.ball_y - self.enemy_y) / self.paddle_height
            self.ball_speed_y += (hit_pos - 0.5) * 4
            self.ball_speed_y = max(-self.max_ball_speed, min(self.max_ball_speed, self.ball_speed_y))
        
        # Ball out of bounds (left)
        if self.ball_x < 0:
            self.enemy_score += 1
            self.reset_ball()
        
        # Ball out of bounds (right)
        if self.ball_x > self.width:
            self.player_score += 1
            self.reset_ball()
        
        # AI enemy movement
        enemy_center = self.enemy_y + self.paddle_height // 2
        if enemy_center < self.ball_y - 35:
            self.enemy_y += self.enemy_speed
        elif enemy_center > self.ball_y + 35:
            self.enemy_y -= self.enemy_speed
        
        # Keep enemy paddle in bounds
        self.enemy_y = max(0, min(self.height - self.paddle_height, self.enemy_y))
    
    def check_paddle_collision(self, paddle_x, paddle_y, ball_x, ball_y):
        """Check if ball collides with paddle"""
        if ball_x - self.ball_radius < paddle_x + self.paddle_width and \
           ball_x + self.ball_radius > paddle_x and \
           ball_y - self.ball_radius < paddle_y + self.paddle_height and \
           ball_y + self.ball_radius > paddle_y:
            return True
        return False
    
    def reset_ball(self):
        """Reset ball to center"""
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_speed_x = random.choice([-5, 5])
        self.ball_speed_y = random.uniform(-3, 3)
    
    def draw_on_surface(self, surface, width, height):
        """Draw game to pygame surface"""
        import pygame
        import os
        
        # Fill background (black) for areas outside the table
        surface.fill((0, 0, 0))
        
        # Load and draw background table with scalability factors
        try:
            bg_img = pygame.image.load(os.path.join("game", "images", "tt_table(nobg).png"))
            tw = int(1280 * self.table_scale) + self.table_width_offset
            th = int(1280 * self.table_scale) + self.table_height_offset
            tx = (width - tw) // 2
            ty = (height - th) // 2
            
            bg_img = pygame.transform.scale(bg_img, (tw, th))
            surface.blit(bg_img, (tx, ty))
        except:
            pass
        
        # Draw center line (dashed white)
        for y in range(0, height, 30):
            pygame.draw.rect(surface, (255, 255, 255), (width // 2 - 2, y, 4, 20))
        
        # Load images for paddles and ball
        try:
            # SWAPPED: Player is Red, Enemy is Black
            player_img = pygame.image.load(os.path.join("game", "images", "red.png"))
            enemy_img = pygame.image.load(os.path.join("game", "images", "black.png"))
            ball_img = pygame.image.load(os.path.join("game", "images", "ball.png"))
            
            # Maintain proportions (using 30x120 instead of 15x120)
            player_img = pygame.transform.scale(player_img, (30, self.paddle_height))
            enemy_img = pygame.transform.scale(enemy_img, (30, self.paddle_height))
            ball_img = pygame.transform.scale(ball_img, (self.ball_radius * 2, self.ball_radius * 2))
            
            # Center the 30px wide image over the 15px wide hitbox
            surface.blit(player_img, (self.paddle_x - 7, self.paddle_y))
            surface.blit(enemy_img, (self.enemy_x - 7, self.enemy_y))
            surface.blit(ball_img, (int(self.ball_x - self.ball_radius), int(self.ball_y - self.ball_radius)))
            
        except Exception as e:
            # Fallback to solid colors
            pygame.draw.rect(surface, (255, 255, 255), 
                            (self.paddle_x, self.paddle_y, 
                             self.paddle_width, self.paddle_height))
            pygame.draw.rect(surface, (255, 255, 255), 
                            (self.enemy_x, self.enemy_y, 
                             self.paddle_width, self.paddle_height))
            pygame.draw.circle(surface, (255, 255, 255), 
                              (int(self.ball_x), int(self.ball_y)), 
                              self.ball_radius)
        
        return surface
