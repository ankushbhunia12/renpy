# ==========================================
# TABLE TENNIS MINIGAME
# ==========================================
init python:
    import sys, os
    game_dir = os.path.join(renpy.config.gamedir)
    if game_dir not in sys.path:
        sys.path.insert(0, game_dir)
    from pong_game import PaddleGame

default tt_winner = ""

init python:

    class TableTennisDisplayable(renpy.Displayable):
        def __init__(self):
            super(TableTennisDisplayable, self).__init__()
            self.game = PaddleGame(width=1280, height=720)
            self.keys = {'up': False, 'down': False}
            self.done = False
            self.winner = ""

        def render(self, width, height, st, at):
            import pygame

            g = self.game

            # One single surface for everything — draw with pygame.draw
            surf = renpy.display.pgrender.surface_unscaled((1280, 720), False)

            # Background
            pygame.draw.rect(surf, (20, 80, 40), (0, 0, 1280, 720))

            # Center dashed line
            for y in range(0, 720, 30):
                pygame.draw.rect(surf, (255, 255, 255), (638, y, 4, 20))

            # Player paddle (red)
            pygame.draw.rect(surf, (220, 50, 50),
                             (int(g.paddle_x), int(g.paddle_y),
                              g.paddle_width, g.paddle_height))

            # Enemy paddle (dark grey)
            pygame.draw.rect(surf, (80, 80, 80),
                             (int(g.enemy_x), int(g.enemy_y),
                              g.paddle_width, g.paddle_height))

            # Ball
            pygame.draw.circle(surf, (255, 255, 255),
                               (int(g.ball_x), int(g.ball_y)), g.ball_radius)

            # Blit the whole surface into a Ren'Py Render
            rv = renpy.Render(1280, 720)
            rv.blit(surf, (0, 0))

            # Score overlay using Ren'Py Text
            score_text = Text(
                "{size=60}{color=#fff}{b}" + str(g.player_score) + "   :   " + str(g.enemy_score) + "{/b}{/color}{/size}"
            )
            score_render = renpy.render(score_text, 1280, 80, st, at)
            rv.blit(score_render, (540, 15))

            # Win condition: first to 5
            if g.player_score >= 5:
                self.winner = "player"
                self.done = True
                renpy.restart_interaction()
            elif g.enemy_score >= 5:
                self.winner = "enemy"
                self.done = True
                renpy.restart_interaction()

            renpy.redraw(self, 0)
            return rv

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    self.keys['up'] = True
                if ev.key == pygame.K_DOWN:
                    self.keys['down'] = True
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_UP:
                    self.keys['up'] = False
                if ev.key == pygame.K_DOWN:
                    self.keys['down'] = False

            self.game.handle_input(self.keys)
            self.game.update(1.0 / 60.0)

            if self.done:
                raise renpy.IgnoreEvent()

        def visit(self):
            return []

screen table_tennis_screen():
    modal True
    add TableTennisDisplayable()
    key "K_ESCAPE" action Return()
