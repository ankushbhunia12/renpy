init:
    # 1. THE BACKGROUND
    image bg_base = im.Scale("bg_m4.jpg", 1920, 1080)

    # 2. THE CLICKABLE OBJECT
    image statue_idle = im.Scale("bg_m4c.png", 1920, 1080)
    
    # [FIXED CODE]
    # Instead of 'im.MatrixColor', we define the image using modern ATL.
    # This takes the png and applies a brightness filter automatically.
    image statue_hover:
        "bg_m4c.png"
        matrixcolor BrightnessMatrix(0.1)

    # 3. THE RESULT
    image bg_result = im.Scale("bg_m5.jpeg", 1920, 1080)

    # --- SCREEN DEFINITION ---
    screen statue_click_layer():
        imagebutton:
            idle "statue_idle"
            hover "statue_hover"
            
            focus_mask True 
            
            # COORDINATES (Adjust based on your background)
            xpos 0.50       
            ypos 0.50       
            xanchor 0.5
            yanchor 0.5
            
            action Jump("statue_zoomed_view")
            
            tooltip "Inspect Statue"

init:
    # Character Definitions
    define m = Character("Arjun", color="#00A0FF")
    define f = Character("Priya", color="#FF69B4")
    define g_char = Character("Guard", color="#BDBDBD")

    # Character Sprites - PRIYA (Using Tags for auto-replace)
    image priya p1 = im.Scale("char_f1.png", 480, 720)
    image priya p2 = im.Scale("char_f2.png", 480, 720) 
    image priya p3 = im.Scale("char_f3.png", 480, 720) 
    image priya p4 = im.Scale("char_f4.png", 480, 720) 
    image priya p5 = im.Scale("char_f4.png", 480, 720)
    image priya p6 = im.Scale("char_f4.png", 480, 720)

    # Character Sprites - ARJUN (Using Tags for auto-replace)
    image arjun p1 = "char_m1.png" 
    image arjun p2 = im.Scale("char_m2.png", 480, 720) 
    image arjun p3 = im.Scale("char_m3.png", 480, 720) 
    image arjun p4 = im.Scale("char_m4.png", 480, 720) 
    image arjun p5 = im.Scale("char_m4.png", 480, 720) 
    image arjun p6 = im.Scale("char_m4.png", 480, 720) 
    
    image gaurd p1 = im.Scale("char_g1.png", 480, 720)
    image gaurd p2 = im.Scale("char_g2.png", 480, 720)
    image gaurd p3 = im.Scale("char_g3.png", 480, 720)
    
    # ID Card image for drag mechanic
    image id_card = im.Scale("id_card.png", 200, 200)
    
    # Some backgrounds 
    image bg_m1 = im.Scale("bg_m1.jpg", 1920, 1080)
    image bg_m2 = im.Scale("bg_m2.png", 1920, 1080)
    image bg_m3 = im.Scale("bg_m3.png", 1920, 1080)
    image bg_m4 = im.Scale("bg_m4.jpg", 1920, 1080)
    image bg_m4c = im.Scale("bg_m4c.png", 1920, 1080)
    image bg_m5 = im.Scale("bg_m5.jpeg", 1920, 1080)
    image bg_m6 = im.Scale("bg_m6.jpg", 1920, 1080)
    image bg_m7 = im.Scale("bg_m7.jpg", 1920, 1080)
    image bg_st = im.Scale("bg_st.png", 1920, 1080)
    image bg_st_1 = im.Scale("bg_st_1.png", 1920, 1080)
    image bg_st_2 = im.Scale("bg_st_2.jpg", 1920, 1080)
    image bg_bio = im.Scale("bg_bio.jpg", 1920, 1080)
    image bg_test = im.Scale("bg_test.png", 1920, 1080)
    image bg_i1 = im.Scale("bg_i1.png", 1920, 1080)
    image bg_i2  = im.Scale("bg_i2.png", 1920, 1080)
    image bg_i2a  = im.Scale("bg_i2a.png", 1920, 1080)
    image audi_1  = im.Scale("audi_1.jpg", 1920, 1080)
    image audi_2  = im.Scale("audi_2.jpg", 1920, 1080)
    image audi_3  = im.Scale("audi_3.jpeg", 1920, 1080)
    image black = Solid("#000000")
    image bg_hallway  = im.Scale("bg_hallway.png", 1920, 1080)
    image ping_pong_bg = im.Scale("images/ping_pong_bg.jpeg", 1920, 1080)

    # --- Missing Background Definitions ---

    # Library & DLC Section
    image bg_hallway_split     = im.Scale("bg_hallway_split.png",1920, 1080)
    image bg_saraswati_statue  = im.Scale("bg_saraswati_statue.png",1920, 1080)
    image bg_library_inside    = im.Scale("bg_library_inside.jpeg",1920, 1080)
    image bg_library_view1     = im.Scale("bg_library_view1.jpeg",    1920, 1080)
    image bg_library_view2     = im.Scale("bg_library_view2.jpeg",    1920, 1080)
    image bg_library_view3     = im.Scale("bg_library_view3.jpeg",    1920, 1080)
    image bg_dlc_view1         = im.Scale("bg_dlc_view1.png",        1920, 1080)
    image bg_dlc_view2         = im.Scale("bg_dlc_view2.png",        1920, 1080)
    image bg_dlc_view3         = im.Scale("bg_dlc_view3.png",        1920, 1080)

    # Classroom
    image classroom_pic        = im.Scale("classroom_pic.png",       1920, 1080)

    # Computer Lab
    image comp_lab             = im.Scale("comp_lab.jpeg",            1920, 1080)

    # Greenhouse
    image greenhouse_bg1       = im.Scale("greenhouse_bg1.jpeg",      1920, 1080)
    image bg_green_view1       = im.Scale("bg_green_view1.jpeg",      1920, 1080)
    image bg_green_view2       = im.Scale("bg_green_view2.jpeg",      1920, 1080)
    image bg_green_view3       = im.Scale("bg_green_view3.png",      1920, 1080)

    # Shastri Bhavan
    image shastri_bhavan = im.Scale("shastri_bhavan.jpeg", 1920, 1080)

    # Cafeteria
    image cafeteria_bg           = im.Scale("cafeteria_bg.jpeg",           1920, 1080)
    image cafeteria_view1        = im.Scale("cafeteria_view1.jpeg",        1920, 1080)
    image cafeteria_view2        = im.Scale("cafeteria_view2.jpeg",        1920, 1080)

    # Mess
    image mess_view1            = im.Scale("mess_view1.jpeg",            1920, 1080)
    image mess_view2            = im.Scale("mess_view2.jpeg",            1920, 1080)
    image mess_view3            = im.Scale("mess_view3.jpeg",            1920, 1080)
    image mess_bg            = im.Scale("mess_bg.jpeg",            1920, 1080)

    # Mughal Garden
    image mughal_garden_bg      = im.Scale("mughal_garden_bg.jpeg",      1920, 1080)

    # Basketball Court
    image basketball_court_bg   = im.Scale("basketball_court_bg.jpeg",   1920, 1080)
    image basketball_shed_bg    = im.Scale("basketball_shed_bg.jpeg",    1920, 1080)

    # Basant Bhavan & Helipad
    image basant_bhavan_bg      = im.Scale("basant_bhavan_bg.jpeg",      1920, 1080)
    image helipad_bg            = im.Scale("helipad_bg.jpeg",            1920, 1080)

    # Mandir
    image mandir_bg             = im.Scale("mandir_bg.jpeg",             1920, 1080)
    image mandir_bg2             = im.Scale("mandir_bg2.png",             1920, 1080)

    #Hostel
    image hostel_bg             = im.Scale("hostel_bg.png",             1920, 1080)
    image hostel_bg1             = im.Scale("hostel_bg1.png",             1920, 1080)
    image cor_1             = im.Scale("cor_1.png",             1920, 1080)
    image cor_2             = im.Scale("cor_2.png",             1920, 1080)
    image cor_3             = im.Scale("cor_3.png",             1920, 1080)
    image bg_gym             = im.Scale("bg_gym.png",             1920, 1080)

    #end
    image end             = im.Scale("end.png",             1920, 1080) 


    # Coffee Machine Mini-Game Images
    image coffee_machine_bg1 = im.Scale("coffee_machine_bg1.png", 1920, 1080)
    image coffee_machine_bg = im.Scale("coffee_machine_bg.png", 1920, 1080)

    # Lift Mini-Game Images
    image lift_outside = im.Scale("lift_outside.png", 1920, 1080)
    image lift_inside = im.Scale("lift_inside.png", 1920, 1080)
    image cup_americano = im.Scale("cup_americano.png", 200, 200)
    image cup_latte = im.Scale("cup_latte.png", 200, 200)
    image cup_mocha = im.Scale("cup_mocha.png", 200, 200)
    image coffee_brewing = im.Scale("coffee_brewing.png", 200, 200)

    # Music Definitions
    #Priya
    define audio.bg_music = "bg_s1.mp3"
    #Priya - New Audio Batch
    # Music Definitions
    
    #Priya
    define audio.f816 = "audio/816 f.mp3"
    define audio.f820 = "audio/820 f.mp3"
    define audio.f836 = "audio/836 f.mp3"
    define audio.f838 = "audio/838 f.mp3"
    define audio.f840 = "audio/840 f.mp3"
    define audio.f844 = "audio/844 f.mp3"
    define audio.f846 = "audio/846 f.mp3"
    define audio.f864 = "audio/864 f.mp3"
    define audio.f910 = "audio/910 f.mp3"
    define audio.f939 = "audio/939 f.mp3"
    define audio.f996 = "audio/996 f.mp3"
    define audio.f1008 = "audio/1008 f.mp3"
    define audio.f1009 = "audio/1009 f.mp3"
    define audio.f1024 = "audio/1024 f.mp3"
    define audio.f1032 = "audio/1032 f.mp3"
    define audio.f1042 = "audio/1042 f.mp3"
    define audio.f1052 = "audio/1052 f.mp3"
    define audio.f1054 = "audio/1054 f.mp3"
    define audio.f1056 = "audio/1056 f.mp3"
    define audio.f1058 = "audio/1058 f.mp3"
    define audio.f1074 = "audio/1074 f.mp3"
    define audio.f1076 = "audio/1076 f.mp3"
    define audio.f1124 = "audio/1124 f.mp3"
    define audio.f1139 = "audio/1139 f.mp3"
    define audio.f1155 = "audio/1155 f.mp3"
    define audio.f1177 = "audio/1177 f.mp3"
    define audio.f1179 = "audio/1179 f.mp3"
    define audio.f1187 = "audio/1187 f.mp3"
    define audio.f1190 = "audio/1190 f.mp3"
    define audio.f1193 = "audio/1193 f.mp3"
    define audio.f1196 = "audio/1196 f.mp3"
    define audio.f1201 = "audio/1201 f.mp3"
    define audio.f1365 = "audio/1365 f.mp3"
    define audio.f1435 = "audio/1435 f.mp3"
    define audio.f1455 = "audio/1455 f.mp3"
    define audio.f1457 = "audio/1457 f.mp3"
    define audio.f1474 = "audio/1474 f.mp3"
    define audio.f1485 = "audio/1485 f.mp3"
    define audio.f1493 = "audio/1493 f.mp3"
    define audio.f1507 = "audio/1507 f.mp3"
    define audio.f1520 = "audio/1520 f.mp3"
    define audio.f1528 = "audio/1528 f.mp3"
    define audio.f1530 = "audio/1530 f.mp3"
    define audio.f1531 = "audio/1531 f.mp3"
    define audio.f1542 = "audio/1542 f.mp3"
    define audio.f1544 = "audio/1544 f.mp3"
    define audio.f1572 = "audio/1572 f.mp3"
    define audio.f1576 = "audio/1576 f.mp3"
    define audio.f1581 = "audio/1581 f.mp3"
    define audio.f1633 = "audio/1633 f.mp3"
    define audio.f1653 = "audio/1653 f.mp3"
    define audio.f1655 = "audio/1655 f.mp3"
    define audio.f1675 = "audio/1675 f.mp3"
    define audio.f1691 = "audio/1691 f.mp3"
    define audio.f1693 = "audio/1693 f.mp3"
    define audio.f1732 = "audio/1732 f.mp3"
    define audio.f1734 = "audio/1734 f.mp3"
    define audio.f1743 = "audio/1743 f.mp3"
    define audio.f1748 = "audio/1748 f.mp3"
    define audio.f1750 = "audio/1750 f.mp3"
    define audio.f1764 = "audio/1764 f.mp3"
    define audio.f1766 = "audio/1766 f.mp3"
    define audio.f1782 = "audio/1782 f.mp3"
    define audio.f1785 = "audio/1785 f.mp3"
    define audio.f1790 = "audio/1790 f.mp3"
    define audio.f1794 = "audio/1794 f.mp3"
    define audio.f1799 = "audio/1799 f.mp3"
    define audio.f1802 = "audio/1802 f.mp3"
    define audio.f1807 = "audio/1807 f.mp3"
    define audio.f1809 = "audio/1809 f.mp3"

    #Arjun
    define audio.m888 = "audio/888 m.mp3"
    define audio.m1066 = "audio/1066 m.mp3"
    define audio.m1099 = "audio/1099 m.mp3"
    define audio.m1101 = "audio/1101 m.mp3"
    define audio.m1107 = "audio/1107 m.mp3"
    define audio.m1109 = "audio/1109 m.mp3"
    define audio.m1111 = "audio/1111 m.mp3"
    define audio.m1138 = "audio/1138 m.mp3"
    define audio.m1140 = "audio/1140 m.mp3"
    define audio.m1206 = "audio/1206 m.mp3"
    define audio.m1234 = "audio/1234 m.mp3"
    define audio.m1239 = "audio/1239 m.mp3"
    define audio.m1261 = "audio/1261 m.mp3"
    define audio.m1274 = "audio/1274 m.mp3"
    define audio.m1282 = "audio/1282 m.mp3"
    define audio.m1288 = "audio/1288 m.mp3"
    define audio.m1456 = "audio/1456 m.mp3"
    define audio.m1527 = "audio/1527 m.mp3"
    define audio.m1548 = "audio/1548 m.mp3"
    define audio.m1551 = "audio/1551 m.mp3"
    define audio.m1565 = "audio/1565 m.mp3"
    define audio.m1581 = "audio/1581 m.mp3"
    define audio.m1587 = "audio/1587 m.mp3"
    define audio.m1590 = "audio/1590 m.mp3"
    define audio.m1605 = "audio/1605 m.mp3"
    define audio.m1619 = "audio/1619 m.mp3"
    define audio.m1628 = "audio/1628 m.mp3"
    define audio.m1645 = "audio/1645 m.mp3"
    define audio.m1677 = "audio/1677 m.mp3"
    define audio.m1684 = "audio/1684 m.mp3"
    define audio.m1738 = "audio/1738 m.mp3"
    define audio.m1741 = "audio/1741 m.mp3"
    define audio.m1762 = "audio/1762 m.mp3"
    define audio.m1783 = "audio/1783 m.mp3"
    define audio.m1786 = "audio/1786 m.mp3"
    define audio.m1803 = "audio/1803 m.mp3"
    define audio.m1846 = "audio/1846 m.mp3"
    define audio.m1856 = "audio/1856 m.mp3"
    define audio.m1859 = "audio/1859 m.mp3"
    define audio.m1865 = "audio/1865 m.mp3"
    define audio.m1868 = "audio/1868 m.mp3"
    define audio.m1877 = "audio/1877 m.mp3"
    define audio.m1883 = "audio/1883 m.mp3"
    define audio.m1897 = "audio/1897 m.mp3"
    define audio.m1903 = "audio/1903 m.mp3"
    define audio.m1913 = "audio/1913 m.mp3"
    define audio.m1921 = "audio/1921 m.mp3"
    define audio.m1924 = "audio/1924 m.mp3"
    define audio.m1928 = "audio/1928 m.mp3"
    define audio.m1934 = "audio/1934 m.mp3"
    define audio.m1938 = "audio/1938 m.mp3"







    # Guard voices (g)
    define audio.g972 = "audio/972 g.mp3"
    define audio.g975 = "audio/975 g.mp3"
    define audio.g977 = "audio/977 g.mp3"
    define audio.g984 = "audio/984 g.mp3"
    define audio.g1014 = "audio/1014 g.mp3"
    define audio.g1017 = "audio/1017 g.mp3"
    define audio.g1018 = "audio/1018 g.mp3"
    define audio.g1020 = "audio/1020 g.mp3"
    define audio.g1021 = "audio/1021 g.mp3"
    define audio.g1023 = "audio/1023 g.mp3"
    define audio.g1024 = "audio/1024 g.mp3"
    define audio.g1041 = "audio/1041 g.mp3"
    define audio.g1053 = "audio/1053 g.mp3"
    define audio.g1054 = "audio/1054 g.mp3"
    define audio.g1091 = "audio/1091 g.mp3"
    define audio.g1099 = "audio/1099 g.mp3"
    define audio.g1102 = "audio/1102 g.mp3"





    # Ping Pong Minigame SFX
    define audio.hit = "bat_ball_1.mp3"
    define audio.bounce = "table_ball_1.mp3"






# ==========================================
# PING PONG MINIGAME
# ==========================================
init python:
    import math
    import random
    from datetime import datetime

    # Initialize audio volume for pong sfx
    renpy.music.set_volume(1.0, delay=0, channel='sound')

    # --- TABLE TUNING ---
    table_scale = 1.0
    table_width_offset = 0
    table_height_offset = 0

    b_off_left = 0
    b_off_right = 0
    b_off_top = 250
    b_off_bottom = -250

    edge_y_top = 0
    edge_y_bottom = 0
    # --------------------

    keys_pressed = {"space": False}
    last_frame_time = None

    class SimplePong:
        def __init__(self, width=1280, height=720, target_games=1):
            self.width = width
            self.height = height
            self.target_games = target_games

            # Paddles
            self.paddle_width = 15
            self.paddle_height = 120
            self.paddle_speed = 10
            self.player_x = 50
            self.player_y = height // 2 - self.paddle_height // 2
            self.enemy_x = width - 50 - self.paddle_width
            self.enemy_y = height // 2 - self.paddle_height // 2

            # Ball
            self.ball_x = width // 2
            self.ball_y = height // 2
            self.ball_z = 0.0
            self.ball_vx = 0
            self.ball_vy = 0
            self.max_ball_speed = 18

            # TT State
            self.player_score = 0
            self.enemy_score = 0
            self.player_games = 0
            self.enemy_games = 0
            self.server = "player"
            self.waiting_for_serve = True
            self.ai_serve_timer = 0.0
            self.winner = None

            # Rules Logic
            self.last_hitter = None
            self.player_side_bounces = 0
            self.enemy_side_bounces = 0
            self.rally_active = False
            self.has_processed_bounce = False

            self.reset_ball()

        def play_sfx(self, sfx_type):
            if sfx_type == "hit":
                renpy.play(audio.hit, channel="sound")
            elif sfx_type == "bounce":
                renpy.play(audio.bounce, channel="sound")

        def update(self, dt=0.016):
            if self.winner: return

            time_scale = dt / 0.016

            tx = (self.width - 1280) // 2
            ty = (self.height - 1280) // 2
            hx1 = tx + b_off_left
            hx2 = tx + 1280 + b_off_right
            hy1 = ty + b_off_top
            hy2 = ty + 1280 + b_off_bottom
            table_center_y = (hy1 + hy2) // 2

            mx, my = renpy.get_mouse_pos()
            off_x = 0
            off_y = 0
            self.player_y = (my - off_y) - self.paddle_height // 2
            self.player_x = (mx - off_x) - self.paddle_width // 2
            self.player_y = max(hy1, min(hy2 - self.paddle_height, self.player_y))
            self.player_x = max(hx1, min(hx1 + 50, self.player_x))

            if self.waiting_for_serve:
                if self.server == "player":
                    self.ball_x = self.player_x + self.paddle_width + 5
                    self.ball_y = self.player_y + self.paddle_height // 2
                    if keys_pressed["space"]:
                        self.waiting_for_serve = False
                        self.ball_vx = 12.0; self.ball_vy = random.uniform(-1.0, 1.0)
                        self.last_hitter = "player"; self.rally_active = False
                        self.play_sfx("hit")
                else:
                    target_y = table_center_y - 60
                    target_x = hx2 - 15
                    self.enemy_y += (target_y - self.enemy_y) * 0.1 * time_scale
                    self.enemy_x += (target_x - self.enemy_x) * 0.1 * time_scale
                    self.ball_x = self.enemy_x - 5
                    self.ball_y = self.enemy_y + self.paddle_height // 2
                    self.ai_serve_timer += dt
                    if self.ai_serve_timer >= 2.0:
                        self.waiting_for_serve = False
                        self.ball_vx = -12.0; self.ball_vy = random.uniform(-1.0, 1.0)
                        self.last_hitter = "enemy"; self.rally_active = False
                        self.play_sfx("hit")
                return

            target_y = self.ball_y - self.paddle_height // 2
            dy = target_y - self.enemy_y
            if abs(dy) > 2: self.enemy_y += dy * 0.15 * time_scale
            table_mid_x = (hx1 + hx2) // 2
            desired_x = hx2 - 15 - (50 * max(0.0, (self.ball_x - table_mid_x) / float(table_mid_x - hx1)) if self.ball_vx > 0 else 0)
            dx = desired_x - self.enemy_x
            if abs(dx) > 2: self.enemy_x += dx * 0.1 * time_scale
            self.enemy_y = max(hy1, min(hy2 - self.paddle_height, self.enemy_y))
            self.enemy_x = max(hx2 - 50, min(hx2 + 100, self.enemy_x))

            self.ball_x += self.ball_vx * time_scale
            self.ball_y += self.ball_vy * time_scale

            norm_x = (self.ball_x - hx1) / float(hx2 - hx1)
            norm_x = max(0.0, min(1.0, norm_x))
            if not self.rally_active:
                self.ball_z = abs(math.cos(norm_x * math.pi * 2.0)) * 15.0
            else:
                if self.ball_vx > 0:
                    local_prog = (norm_x - 0.5) / 0.5 if norm_x > 0.5 else 0
                    self.ball_z = abs(math.sin(local_prog * math.pi)) * 15.0 if norm_x > 0.5 else 15.0
                else:
                    local_prog = norm_x / 0.5 if norm_x < 0.5 else 0
                    self.ball_z = abs(math.sin(local_prog * math.pi)) * 15.0 if norm_x < 0.5 else 15.0

            if self.ball_z < 3.5:
                if not self.has_processed_bounce:
                    self.has_processed_bounce = True
                    if (hx1 + 100 <= self.ball_x <= hx2 - 100) and (hy1 + 100 <= self.ball_y <= hy2 - 100):
                        self.play_sfx("bounce")
                    if self.ball_y < hy1 or self.ball_y > hy2:
                        self.point_to("enemy" if self.last_hitter == "player" else "player"); return
                    if self.ball_x < hx1 or self.ball_x > hx2:
                        if self.last_hitter == "player":
                            self.point_to("player" if self.enemy_side_bounces >= 1 else "enemy")
                        else:
                            self.point_to("enemy" if self.player_side_bounces >= 1 else "player")
                        return
                    if self.ball_x < (hx1 + hx2) // 2:
                        self.player_side_bounces += 1
                        if self.player_side_bounces > 1 or (self.rally_active and self.last_hitter == "player"):
                            self.point_to("enemy"); return
                    else:
                        self.enemy_side_bounces += 1
                        if self.enemy_side_bounces > 1 or (self.rally_active and self.last_hitter == "enemy"):
                            self.point_to("player"); return
                    if not self.rally_active and self.player_side_bounces == 1 and self.enemy_side_bounces == 1:
                        self.rally_active = True
            else:
                self.has_processed_bounce = False

            hit_range_x = 55

            if self.ball_vx < 0 and abs(self.ball_x - (self.player_x + self.paddle_width)) < hit_range_x:
                if self.player_y - 20 <= self.ball_y <= self.player_y + self.paddle_height + 20:
                    self.play_sfx("hit")
                    if self.player_side_bounces == 1:
                        self.ball_vx = min(abs(self.ball_vx) * 1.05, self.max_ball_speed)
                        hit_pos = (self.ball_y - self.player_y) / self.paddle_height
                        manual_vy = (hit_pos - 0.5) * 18
                        dist_to_enemy = self.enemy_x - self.ball_x
                        time_to_reach = max(1.0, dist_to_enemy / self.ball_vx)
                        target_vy = (table_center_y - self.ball_y) / time_to_reach
                        self.ball_vy = (manual_vy * 0.6) + (target_vy * 0.4) + random.uniform(-1, 1)
                        self.last_hitter = "player"; self.player_side_bounces = 0; self.enemy_side_bounces = 0
                        self.ball_x = self.player_x + self.paddle_width + 10; self.rally_active = True
                    else:
                        self.point_to("enemy")

            elif self.ball_vx > 0 and abs(self.ball_x - self.enemy_x) < hit_range_x:
                if self.enemy_y - 20 <= self.ball_y <= self.enemy_y + self.paddle_height + 20:
                    self.play_sfx("hit")
                    if self.enemy_side_bounces == 1:
                        self.ball_vx = max(-abs(self.ball_vx) * 1.05, -self.max_ball_speed)
                        hit_pos = (self.ball_y - self.enemy_y) / self.paddle_height
                        manual_vy = (hit_pos - 0.5) * 18
                        dist_to_player = self.ball_x - self.player_x
                        time_to_reach = max(1.0, dist_to_player / abs(self.ball_vx))
                        target_vy = (table_center_y - self.ball_y) / time_to_reach
                        self.ball_vy = (manual_vy * 0.6) + (target_vy * 0.4) + random.uniform(-1, 1)
                        self.last_hitter = "enemy"; self.player_side_bounces = 0; self.enemy_side_bounces = 0
                        self.ball_x = self.enemy_x - 10; self.rally_active = True
                    else:
                        self.point_to("player")

            if self.ball_x < tx - 150: self.point_to("enemy")
            elif self.ball_x > hx2 + 150: self.point_to("player")

        def point_to(self, winner):
            if winner == "player": self.player_score += 1
            else: self.enemy_score += 1
            total_points = self.player_score + self.enemy_score
            self.server = "player" if (total_points // 2) % 2 == 0 else "enemy"
            if self.player_score >= 5 and (self.player_score - self.enemy_score) >= 2:
                self.player_games += 1; self.player_score = 0; self.enemy_score = 0
            elif self.enemy_score >= 5 and (self.enemy_score - self.player_score) >= 2:
                self.enemy_games += 1; self.player_score = 0; self.enemy_score = 0
            if self.player_games >= self.target_games: self.winner = "player"
            elif self.enemy_games >= self.target_games: self.winner = "enemy"
            self.reset_ball()

        def reset_ball(self):
            self.waiting_for_serve = True
            self.ai_serve_timer = 0.0
            self.ball_vx = 0; self.ball_vy = 0; self.ball_z = 0
            self.has_processed_bounce = False
            self.player_side_bounces = 0
            self.enemy_side_bounces = 0
            self.rally_active = False
            self.enemy_x = (self.width - 1280) // 2 + 1215
            self.enemy_y = (self.height - 1280) // 2 + 580

    pong_game = SimplePong(1920, 1080)

    def update_game():
        global last_frame_time
        current_time = datetime.now()
        dt = (current_time - last_frame_time).total_seconds() if last_frame_time else 0.016
        last_frame_time = current_time
        pong_game.update(min(dt, 0.05))

screen pong_game(target_games=1):
    zorder 100
    modal True
    on "show" action Function(pong_game.__init__, 1920, 1080, target_games)
    timer 0.016 repeat True action [Function(update_game)]
    frame:
        xsize 1920 ysize 1080 background "ping_pong_bg" xalign 0.5 yalign 0.5 padding (0, 0)
        python:
            tx = (1920 - 1280) // 2; ty = (1080 - 1280) // 2
            hx1 = tx + b_off_left; hx2 = tx + 1280 + b_off_right
            hy1 = ty + b_off_top; hy2 = ty + 1280 + b_off_bottom
        add "images/tt_table(nobg).png" xpos tx ypos ty
        add im.Scale("images/red.png", 30, 120) xpos int(pong_game.player_x - 7) ypos int(pong_game.player_y)
        add im.Scale("images/black.png", 30, 120) xpos int(pong_game.enemy_x - 7) ypos int(pong_game.enemy_y)
        python:
            b_scale = 1.0 + (pong_game.ball_z / 150.0)
            b_size = int(18 * b_scale)
            bx = int(pong_game.ball_x - b_size//2); by = int(pong_game.ball_y - b_size//2)
        frame:
            xsize b_size + 4 ysize b_size + 4 xpos bx - 2 ypos by - 2
            background Frame(Solid("#000000"), 100, 100)
        add im.Scale("images/ball.png", b_size, b_size) xpos bx ypos by
    frame:
        xalign 0.5 yalign 0.02 background Frame(Solid("#000000aa"), 10, 10) padding (20, 10)
        has hbox:
            spacing 40
        vbox:
            spacing 5
            text "PLAYER" size 16 xalign 0.5 color "#aaa"
            hbox:
                spacing 10 xalign 0.5
                for i in range(pong_game.target_games):
                    $ col = "#ff0000" if i < pong_game.player_games else "#444"
                    add Solid(col, xysize=(15, 15))
            text "[pong_game.player_score]" size 60 xalign 0.5 bold True
        vbox:
            yalign 0.5
            text "VS" size 30 color "#666" italic True
        vbox:
            spacing 5
            text "PRIYA" size 16 xalign 0.5 color "#aaa"
            hbox:
                spacing 10 xalign 0.5
                for i in range(pong_game.target_games):
                    $ col = "#ffffff" if i < pong_game.enemy_games else "#444"
                    add Solid(col, xysize=(15, 15))
            text "[pong_game.enemy_score]" size 60 xalign 0.5 bold True
    if pong_game.waiting_for_serve and not pong_game.winner:
        frame:
            xalign 0.5 yalign 0.4 background Solid("#00000088") padding (40, 20)
            if pong_game.server == "player":
                text "YOUR SERVE - PRESS SPACE" size 40 color "#ffff00" outlines [(2, "#000")]
            else:
                text "AI IS SERVING..." size 40 color "#ffffff" outlines [(2, "#000")]
    if pong_game.winner:
        frame:
            modal True xsize 1920 ysize 1080 background Solid("#000000cc")
            vbox:
                xalign 0.5 yalign 0.5 spacing 30
                if pong_game.winner == "player":
                    text "VICTORY!" size 100 color "#0f0" bold True
                else:
                    text "DEFEAT" size 100 color "#f00" bold True
                textbutton "RETURN TO GAME" action Return(pong_game.winner == "player") xalign 0.5:
                    text_size 40 text_hover_color "#fff"
    key "K_ESCAPE" action Return(False)
    python:
        import pygame
        pressed = pygame.key.get_pressed()
        keys_pressed["space"] = pressed[pygame.K_SPACE]

label play_pong_match(target=1):
    $ renpy.block_rollback()
    call screen pong_game(target_games=target)
    return _return

# ==========================================
# CARD DRAG SYSTEM VARIABLES
# ==========================================
default card_delivered = False
default drag_attempts = 0
default id_verified = False

# ==========================================
# COFFEE MACHINE MINI-GAME VARIABLES
# ==========================================
default coffee_choice = None
default coffee_made = False


# ==========================================
# COFFEE MACHINE SCREEN
# ==========================================
screen coffee_machine_screen():
    modal True

    # --- Layer 1: Room background ---
    add "coffee_machine_bg1.png":
        xalign 0.5
        yalign 0.5
        fit "cover"

    # --- Layer 2: Coffee machine PNG centred on top ---
    add "coffee_machine_bg.png":
        xalign 0.5
        yalign 0.5

    # --- Title banner ---
    frame:
        xalign 0.5
        yalign 0.04
        padding (30, 12)
        background "#1a0a00cc"
        text "☕  Campus Coffee Machine  ☕" size 26 color "#f5c842" bold True text_align 0.5

    # --- Sub-instruction ---
    frame:
        xalign 0.5
        yalign 0.12
        padding (20, 8)
        background "#00000077"
        text "Pick your brew and tap the button to start!" size 18 color "#ffffff" text_align 0.5

    # ==========================================
    # COFFEE MACHINE PANEL (centre)
    # ==========================================
    frame:
        xalign 0.5
        yalign 0.56
        xysize (820, 460)
        background "#1a0a00dd"
        padding (20, 20)

        vbox:
            spacing 18
            xalign 0.5

            # Row of three drink option buttons
            hbox:
                spacing 30
                xalign 0.5

                # ---- AMERICANO ----
                frame:
                    xysize (220, 280)
                    background "#2b1500ee"
                    padding (10, 10)
                    vbox:
                        spacing 10
                        xalign 0.5

                        # Cup image placeholder (swap "cup_americano.png" with your asset)
                        add "cup_americano.png":
                            size (140, 140)
                            xalign 0.5

                        text "Americano" size 20 color "#f5c842" bold True xalign 0.5

                        text "Bold & black.\nPure espresso\nwith hot water." size 14 color "#cccccc" xalign 0.5 text_align 0.5

                        textbutton "Select":
                            xalign 0.5
                            style "coffee_btn"
                            action [SetVariable("coffee_choice", "americano"),
                                    Hide("coffee_machine_screen"),
                                    Jump("coffee_brewing")]

                # ---- LATTE ----
                frame:
                    xysize (220, 280)
                    background "#2b1500ee"
                    padding (10, 10)
                    vbox:
                        spacing 10
                        xalign 0.5

                        add "cup_latte.png":
                            size (140, 140)
                            xalign 0.5

                        text "Latte" size 20 color "#f5c842" bold True xalign 0.5

                        text "Smooth &\ncreamy.\nEspresso with\nsteamed milk." size 14 color "#cccccc" xalign 0.5 text_align 0.5

                        textbutton "Select":
                            xalign 0.5
                            style "coffee_btn"
                            action [SetVariable("coffee_choice", "latte"),
                                    Hide("coffee_machine_screen"),
                                    Jump("coffee_brewing")]

                # ---- MOCHA ----
                frame:
                    xysize (220, 280)
                    background "#2b1500ee"
                    padding (10, 10)
                    vbox:
                        spacing 10
                        xalign 0.5

                        add "cup_mocha.png":
                            size (140, 140)
                            xalign 0.5

                        text "Mocha" size 20 color "#f5c842" bold True xalign 0.5

                        text "Rich chocolate\nespresso blend.\nSweet & bold." size 14 color "#cccccc" xalign 0.5 text_align 0.5

                        textbutton "Select":
                            xalign 0.5
                            style "coffee_btn"
                            action [SetVariable("coffee_choice", "mocha"),
                                    Hide("coffee_machine_screen"),
                                    Jump("coffee_brewing")]

    # --- Cancel / walk away button ---
    textbutton "Walk Away":
        xalign 0.5
        yalign 0.96
        style "coffee_cancel_btn"
        action [Hide("coffee_machine_screen"), Jump("coffee_skipped")]


# ==========================================
# COFFEE BUTTON STYLES
# ==========================================
style coffee_btn:
    background "#6b3a1f"
    hover_background "#a0522d"
    padding (16, 8)
    color "#ffffff"
    hover_color "#f5c842"
    bold True

style coffee_cancel_btn:
    background "#333333aa"
    hover_background "#555555"
    padding (14, 8)
    color "#aaaaaa"
    hover_color "#ffffff"


# ==========================================
# COFFEE BREWING ANIMATION SCREEN
# ==========================================
screen coffee_brewing_screen(drink_name):

    # --- Layer 1: Room background ---
    add "coffee_machine_bg1.png":
        xalign 0.5
        yalign 0.5
        fit "cover"

    # --- Layer 2: Coffee machine PNG ---
    add "coffee_machine_bg.png":
        xalign 0.5
        yalign 0.5

    frame:
        xalign 0.5
        yalign 0.5
        xysize (500, 310)
        background "#1a0a00ee"
        padding (20, 30)

        vbox:
            spacing 10
            xalign 0.5

            text "Brewing your [drink_name]..." size 24 color "#f5c842" bold True xalign 0.5

            # Animated steam/dots using ATL
            hbox:
                spacing 10
                xalign 0.5
                for i in ["●", "●", "●"]:
                    text i size 28 color "#c07030":
                        pass

            add "coffee_brewing.png":
                size (160, 160)
                xalign 0.5

            text "Please wait..." size 16 color "#cccccc" xalign 0.5

# ==========================================
# CARD DRAG SCREEN
# ==========================================
screen id_card_drag_game():
    modal True
    
    # Background (the biometric/gate area)
    add "bg_bio"
    
    # Guard character
    add "char_g3.png":
        xalign 0.0
        yalign 1.0
        zoom 0.8
    
    # Instruction text
    frame:
        xalign 0.5
        yalign 0.05
        padding (15, 10)
        background "#00000088"
        text "Drag your ID card to the guard's checkpoint" size 20 color "#ffcc00" text_align 0.5
    
    # Drop zone indicator (near the guard)
    frame:
        xalign 0.20
        yalign 0.69
        xysize (250, 300)
        background "#ffffff22"
        
        # Visual indicator
        text "VERIFICATION\nZONE" size 18 color "#ffcc00" text_align 0.5 xalign 0.5 yalign 0.5
    
    # Draggable ID Card system
    draggroup:
        # The draggable card
        drag:
            drag_name "id_card"
            child "id_card.png"
            xpos 1300
            ypos 500
            draggable True
            droppable False
            drag_raise True
            dragged card_dragged_handler
            
        # The drop target
        drag:
            drag_name "drop_zone"
            child Null(width=250, height=300)
            xalign 0.20
            yalign 0.69
            draggable False
            droppable True

# ==========================================
# CARD DRAG HANDLER
# ==========================================
init python:
    def card_dragged_handler(drags, drop):
        if not drop:
            # Card was released but not on any drop zone
            renpy.hide_screen("id_card_drag_game")
            renpy.jump("id_card_failed")
            return False
        
        # Check if dropped on the correct zone
        if drop.drag_name == "drop_zone":
            # Success! Card delivered
            renpy.hide_screen("id_card_drag_game")
            renpy.jump("id_card_success")
            return True
        else:
            # Dropped on wrong area
            renpy.hide_screen("id_card_drag_game")
            renpy.jump("id_card_failed")
            return False

label start:
    scene bg_st with fade
    play music bg_music fadein 2.0

    "In the hills of a beautiful place called Waknaghat..."
    
    scene bg_st_1 with dissolve
    "The new student arrives on the JUIT campus."

    show priya p1 at left with moveinleft
    
    # [UPDATED CODE] 
    # Swapped 'play sound' for 'voice' to correctly play the voice line with the text
    voice f816
    f "Hi there! I'm Priya. We're so excited to have you here at JUIT!"

    show priya p2 at left 
    voice f820
    f "I know settling in can be a little overwhelming, but trust me, you'll love it here."
    
    show arjun p1 at right with moveinright
    voice m888
    m "I'm Arjun, and welcome to JUIT! It's a fantastic place a bit chilly sometimes, but the views and the vibe make up for it."

    "After a brief introduction, Priya and Arjun lead you further into the campus."

    hide arjun
    hide priya
    with dissolve
    
    scene bg_st_2 with fade
    show priya p3 at left with moveinleft

    voice f836
    f "And here we are! This is the main gate of JUIT. It's the first point of security."
    voice f838
    f "Before you head to the academic block, you need to know about the security protocols."
    voice f840
    f "Safety is a top priority here, so the guards are on duty 24/7. Always keep your ID card handy!"

    show priya p3 at center with dissolve
    voice f844
    f "One of the most important things you'll use every day is the Biometric System."

    voice f846
    f "Look, there's a guard right there. Let's go over and see how it works."

    # ==========================================
    # BIOMETRIC EXPLANATION SCENE
    # ==========================================
    scene bg_bio with fade
    show gaurd p1 at right with moveinright
    show priya p1 at left with dissolve
     
    voice g972 
    g_char "Halt! New student"

    show gaurd p2 at right with dissolve
    voice g975
    g_char "Before you can proceed, I need to verify your identity and explain our security protocols."
    
    voice g977
    g_char "First things first I'll need to see your student ID card for verification."

    show priya p2 at left with dissolve
    voice f864
    f "Go ahead. Show the guard your ID card. This is standard procedure for all new students."

    show gaurd p1 at right with dissolve
    voice g984
    g_char "Hand it over to me at the verification checkpoint. Make sure you place it properly in the designated zone."

    # ==========================================
    # TRIGGER THE CARD DRAG MINI-GAME
    # ==========================================
    hide priya
    hide gaurd
    with dissolve

    call screen id_card_drag_game

    return

# ==========================================
# CARD VERIFICATION FAILED
# ==========================================
label id_card_failed:
    scene bg_bio
    show gaurd p3 at right
    show priya p3 at left
    
    $ drag_attempts += 1
    
    # Failure message
    window show
    centered "{color=#ff0000}{size=32}{b}Verification Failed!{/b}{/size}{/color}\n{size=20}Please place your ID card in the verification zone.{/size}"
    pause 1.5
    window hide
    
    show gaurd p3 at right
    
    voice g1014
    g_char "Hey! That's not how you do it."
    
    if drag_attempts == 1:

        voice g1017
        g_char "You need to place your ID card directly in the verification zone that's the highlighted area."
        voice g1018
        g_char "Don't just drop it anywhere. Be precise."
    elif drag_attempts == 2:
        voice g1020
        g_char "Come on. Focus! The verification zone is clearly marked."
        voice g1021
        g_char "Center your ID card in that box. It's not that difficult."
    else:
        voice g1023
        g_char "Are you having trouble with basic instructions? This is the third time!"
        voice g1024
        g_char "Look—see that glowing box near me? That's where the ID card goes!"
    
    show priya p4 at left
    voice f910
    f "Don't worry. Just drag it carefully to the verification zone this time."
    
    menu:
        "Try again":
            jump retry_id_verification
        "Give up" if drag_attempts >= 3:
            jump id_verification_timeout

label retry_id_verification:
    scene bg_bio
    show gaurd p2 at right
    show priya p2 at left
    
    voice g1041
    g_char "Alright, let's try this again. Pay attention this time."
    
    hide priya
    hide gaurd
    with dissolve
    
    call screen id_card_drag_game
    
    return

label id_verification_timeout:
    show gaurd p3 at right
    voice g1053
    g_char "I'm sorry, but if you can't follow simple security procedures, I cannot allow you to enter."
    voice g1054
    g_char "Come back when you're ready to cooperate with campus security protocols."

    show priya p4 at left
    voice f939
    f "Oh no, Maybe we should try again another day?"

    "You failed to pass the security checkpoint..."

    # Use the correct filename for the Game Over image
    scene bg_test
    with fade   # Adds a smooth transition instead of a sudden cut

    # IMPORTANT: This pauses the game so the player can see the image.
    # The game will wait here until the player clicks.
    pause

    return

# ==========================================
# CARD VERIFICATION SUCCESS
# ==========================================
label id_card_success:
    scene bg_bio
    show gaurd p2 at right
    show priya p2 at left
    
    # Reset attempts
    $ drag_attempts = 0
    $ card_delivered = True
    $ id_verified = True
    
    # Success message
    
    centered "{color=#00ff00}{size=32}{b}Verification Successful!{/b}{/size}{/color}\n{size=20}ID card accepted.{/size}"
    
    window show
    show gaurd p2 at right
    voice g1091
    g_char "Good. Let me verify this..."
    window hide
    pause 1.0
    
    show id_card at center with dissolve
    pause 1.5
    hide id_card with dissolve
    
    voice g1099
    g_char "ID verified. Student ID number matches our records."
    
    show gaurd p2 at right

    voice g1102
    g_char "You are free to go now."

    # Continue with the rest of the story
    jump after_security_check

# ==========================================
# CONTINUING THE ORIGINAL STORY
# ==========================================
label after_security_check:
    scene bg_st_2 with fade
    show priya p2 at left
    show arjun p2 at right

    voice f996
    f "See? You did great, Now you're officially checked in."

    voice m1066
    m "So, ready to see the rest of the campus?"

    menu:
        "Yes, let's go!":
            jump campus_main_tour
        "Wait, I have a question about the ID card.":
            jump id_question

label id_question:
    show priya p2 at left
    voice f1008
    f "No problem! Your ID card acts as your library pass. Don't lose it!"
    voice f1009
    f "It's basically your key to everything on campus."
    jump campus_main_tour

label campus_main_tour:
    "You walk through the gates, officially starting your journey at JUIT."

    # ==========================================
    # SCENE 1: ACADEMIC PRAISE & NEW JOKE (bg_m1)
    # ==========================================
    scene bg_m1 with fade
    play music bg_music fadein 2.0
    
    show priya p1 at left with moveinleft
    show arjun p1 at right with moveinright

    voice f1024
    f "So, here we are. This is the way to the Academic Block of JUIT."

    # --- THE NEW JOKE ---
    show arjun p3 at right with dissolve
    voice m1099
    m "But, don't get intimidated by all this high-tech talk."
    
    voice m1101
    m "You will soon develop the greatest superpower known to mankind. It is unique to engineering students."

    voice f1032
    f "What? Coding? Math?"

    show arjun p2 at right
    voice m1107
    m "No. Time Dilation."
    
    voice m1109
    m "Einstein said nothing can travel faster than light."

    voice m1111
    m "Einstein clearly never saw a JUIT student covering a 6-month syllabus the night before the final exam."
    
    show priya p4 at left
    voice f1042
    f "He's not wrong! I've seen students learn C++ in 4 hours. It's terrifying, but impressive."

    # ==========================================
    # SCENE 2: DAILY ROUTINE - CASUAL TASKS (bg_m2)
    # ==========================================
    scene bg_m2 with fade
    show priya p1 at left
    show arjun p1 at right
    with dissolve

    voice f1052
    f "Moving on to the daily grind. This is your real survival guide."
    
    voice f1054
    f "First, you have the 'Assignment Marathon'."

    voice f1056
    f "It's where the whole batch unites.It's not just about the grades."

    voice f1058
    f "It's about the shared panic, the group chats buzzing at 2 AM, and the 11:59 PM submission rush."

    show arjun p2 at right
    voice m1138
    m "Between debugging code all night and fighting for five more minutes of sleep,"

    voice m1140
    m "This is where you learn the management skills they don't teach in textbooks."

    # ==========================================
    # SCENE 3: THE PLAZA (bg_m6)
    # ==========================================
    
    scene bg_m6 with fade
    
    "As you walk further, you reach the central plaza."

    show priya p3 at left with dissolve
    show arjun p1 at right with dissolve
    voice f1074
    f "And here is the statue of Swami Vivekananda."
    
    voice f1076
    show arjun p2 at right with dissolve
    f "It's a tradition to pay respects here before exams."

    # CHOICE: Look or Walk (No point-and-click mechanic, just story flow)
    menu:
        "Stop and look at the statue.":
            
            scene bg_base with fade

            show priya p3 at left with dissolve

            show screen statue_click_layer

            "Go ahead, take a closer look."

            "(Click the statue to read the inscription.)"

            $ renpy.pause(hard=True) 
                
            label statue_zoomed_view:
    
            hide screen statue_click_layer
    
            scene bg_result with dissolve
    
            "You step forward to read the golden plaque."

            window hide dissolve

            pause

            scene bg_base with fade

        "Continue walking.":
            
            # The player chooses to ignore it: Brief transition text
            "You nod at the statue but keep your pace, eager to see the rest of the campus."

    # ==========================================
    # SCENE 4: THE ACADEMIC BLOCK (bg_m7)
    # ==========================================
    # Both paths merge here seamlessly
    
    scene bg_m7 with fade
    
    show priya p1 at left
    show arjun p1 at right
    with dissolve
    
    voice f1124
    f "Moving on... welcome to the Academic Block."
    
    voice m1206
    m "This is where the real work happens. And by work, I mean struggling with deadlines."

label campus_entry:
    # 1. Brief glimpse of the Academic Block Interior
    scene bg_i1 with fade

    # 2. Transition to the next view
    scene bg_i2 with dissolve
    
    show priya p1 at left
    show arjun p1 at right
    with dissolve

    voice f1139
    f "We're right at the junction now. To one side is the heart of the building, and to the other... well, see for yourself."

    # 3. The Choice
    menu:
        "Go further into the Academic Block?":
            jump academic_block_route

        "Take a glimpse of the Auditorium first?":
            jump auditorium_glimpse

label auditorium_glimpse:
    # Display the auditorium background
    scene bg_i2a with fade 
    
    show priya p2 at left with moveinleft
    show arjun p3 at right with moveinright

    voice m1234
    m "The Auditorium is where we hold everything from guest lectures to the big cultural fests."
    
    voice f1155
    show priya p4 at left with dissolve
    f "It’s definitely the most impressive room in this wing!"
    
    show arjun p2 at right with dissolve
    voice m1239
    m "Take a look around."

    hide priya
    hide arjun
    with dissolve

    # Automatic Slideshow - No narration
    window hide # Hides the dialogue box for better immersion
    scene audi_1 with dissolve
    pause 2.0
    scene audi_2 with dissolve
    pause 2.0
    scene audi_3 with dissolve
    pause 2.0


    menu:
        "Shall we go further towards the registration office?":
            jump academic_block_route

        "Or play something first?":
            jump table_tennis

label table_tennis:
    show priya p4 at left with moveinleft
    show arjun p3 at right with moveinright

    voice f1177
    f "You may have noticed a table tennis table here, how about playing a match."
    show arjun p2 at right with dissolve
    voice m1261
    m "I shall warn you she plays really well."
    
    "First to win a game wins. Move your mouse to control the paddle, and press SPACE to serve!"
    "Press Esc key to leave the game."

    # Launch the ping pong minigame (best of 1 game)
    call play_pong_match(1)
    $ tt_player_won = _return

    if tt_player_won:
        show priya p4 at left with dissolve
        voice f1187
        f "Whoa! I can't believe you beat me! That was incredible!"
        show arjun p3 at right with dissolve
        voice m1274
        m "Ha! I told you to not underestimate the new student, Priya."
        voice f1190
        f "Alright, alright. You've earned some serious respect. Let's move on."
    else:
        show priya p2 at left with dissolve
        voice f1193
        f "Haha! I did warn you! Don't worry, you'll get better with practice."
        show arjun p3 at right with dissolve
        voice m1282
        m "She's basically unbeatable at this. I've never beaten her either."
        voice f1196
        f "Come on, let's continue the tour. You can challenge me again sometime!"

label academic_block_route:
    scene bg_hallway with fade
    show arjun p3 at right with dissolve
    voice m1288
    m "We've reached the main junction of the block."
    voice f1201
    show priya p4 at left with dissolve
    f "Let's head towards the lift."
    jump lift_return

# ==========================================
# LIFT MINI-GAME VARIABLES
# ==========================================
default lift_current_floor = 0
default lift_destinations_visited = []
default lift_door_open = False

# ==========================================
# LIFT FLOOR DATA
# ==========================================
init python:
    LIFT_FLOORS = [
        {"floor": 1, "label": "classroom",   "name": "Classrooms",    "desc": "1st Floor — Academic Rooms"},
        {"floor": 2, "label": "Computer_labs","name": "Computer Labs", "desc": "2nd Floor — Tech Labs"},
        {"floor": 3, "label": "greenhouse",   "name": "Greenhouse",    "desc": "3rd Floor — BT Wing"},
        {"floor": 4, "label": "coffee",       "name": "Coffee Corner", "desc": "4th Floor — Café Zone"},
    ]

# ==========================================
# LIFT OUTSIDE SCREEN (choose your floor)
# ==========================================
screen lift_outside_screen():
    modal True

    # Layer 1: corridor/outside background
    add "lift_outside.png":
        xalign 0.5
        yalign 0.5
        fit "cover"

    # Dark overlay for readability
    add Solid("#00000099")

    # Title
    frame:
        xalign 0.5
        yalign 0.05
        padding (30, 14)
        background "#1a1a2eee"
        text "🛗  Select Your Floor" size 28 color "#e0c97f" bold True xalign 0.5

    # Subtitle
    frame:
        xalign 0.5
        yalign 0.13
        padding (20, 8)
        background "#00000077"
        text "Press a button to call the lift to your destination." size 17 color "#cccccc" xalign 0.5

    # Floor button panel
    frame:
        xalign 0.5
        yalign 0.58
        xysize (680, 460)
        background "#1a1a2eee"
        padding (20, 20)

        vbox:
            spacing 10
            xalign 0.5

            for entry in [
                    {"floor": 4,  "name": "Greenhouse",    "icon": "🌿", "desc": "4th Floor — BT Wing",             "label": "greenhouse"},
                    {"floor": 3,  "name": "Computer Labs", "icon": "💻", "desc": "3rd Floor — Tech Labs",            "label": "Computer_labs"},
                    {"floor": 2,  "name": "Classrooms",    "icon": "🎓", "desc": "2nd Floor — Academic Rooms",       "label": "classroom"},
                    {"floor": 0,  "name": "Library & DLC", "icon": "📚", "desc": "Ground Floor — Library & DLC Room","label": "library_interior_path"},
                    {"floor": -1, "name": "Coffee Corner", "icon": "☕", "desc": "Basement — Café Zone",             "label": "coffee"},
                ]:
                frame:
                    xysize (640, 66)
                    background "#2d2d5e"
                    padding (8, 8)
                    hbox:
                        spacing 10
                        yalign 0.5
                        # Floor number badge
                        frame:
                            xysize (46, 46)
                            background "#e0c97f"
                            yalign 0.5
                            text str(entry["floor"]) size 18 color "#1a1a2e" bold True xalign 0.5 yalign 0.5
                        # Name + desc block — fixed width to leave room for button
                        vbox:
                            xsize 460
                            yalign 0.5
                            spacing 2
                            hbox:
                                spacing 6
                                text entry["icon"] size 16 yalign 0.5
                                text entry["name"] size 16 color "#ffffff" bold True yalign 0.5
                            text entry["desc"] size 12 color "#aaaaaa"
                        # GO button — pinned inside the row
                        frame:
                            xysize (100, 46)
                            background "#e0c97f"
                            hover_background "#f5e08a"
                            yalign 0.5
                            button:
                                xysize (100, 46)
                                background "#e0c97f"
                                hover_background "#f5e08a"
                                action [SetVariable("lift_current_floor", entry["floor"]),
                                        Hide("lift_outside_screen"),
                                        Jump("lift_enter_animation")]
                                text "GO" size 18 color "#1a1a2e" bold True xalign 0.5 yalign 0.5

# ==========================================
# LIFT INSIDE SCREEN (doors closing, going up)
# ==========================================
screen lift_inside_screen(dest_name):

    # Lift interior image
    add "lift_inside.png":
        xalign 0.5
        yalign 0.5
        fit "cover"

    add Solid("#00000066")

    # Floor display panel (top)
    frame:
        xalign 0.5
        yalign 0.06
        padding (24, 12)
        background "#000000cc"
        hbox:
            spacing 20
            xalign 0.5
            text "🛗" size 26 yalign 0.5
            text "Going to: [dest_name]" size 22 color "#e0c97f" bold True yalign 0.5

    # Animated "doors closing" message
    frame:
        xalign 0.5
        yalign 0.88
        padding (24, 14)
        background "#1a1a2ecc"
        text "⚡ Doors closing... Please hold on." size 18 color "#ccffcc" xalign 0.5

# ==========================================
# LIFT BUTTON STYLE
# ==========================================
style lift_btn:
    background "#e0c97f"
    hover_background "#f5e08a"
    padding (10, 10)
    color "#1a1a2e"
    hover_color "#000000"
    bold True
    text_align 0.5
    size 18

# ==========================================
# LIFT LABEL — ENTRY POINT
# ==========================================
label jump_lift:
    scene lift_outside with dissolve

    show priya p3 at left with moveinleft
    show arjun p2 at right with moveinright

    voice f1365
    f "Hmm, walking to all those floors would take forever. Let's use the lift instead!"
    voice m1456
    m "Good idea. Which floor do you want to hit first?"

    hide priya
    hide arjun
    with dissolve

    show screen lift_outside_screen

    $ renpy.pause(hard=True)

# ==========================================
# LIFT ENTER ANIMATION
# ==========================================
label lift_enter_animation:
    # Work out where we're going
    python:
        dest_map = {
            -1: "Coffee Corner",
            0: "Library & DLC Room",
            2: "Classrooms",
            3: "Computer Labs",
            4: "Greenhouse",
        }
        lift_dest_name = dest_map.get(lift_current_floor, "Unknown")

    # Show the lift interior + doors-closing overlay
    scene lift_inside with dissolve

    show screen lift_inside_screen(lift_dest_name)

    $ renpy.pause(2.5, hard=True)

    hide screen lift_inside_screen

    # Brief arrival message
    centered "{color=#e0c97f}{size=30}{b}Floor [lift_current_floor] — [lift_dest_name]{/b}{/size}{/color}"

    pause 0.8

    # Route to the correct destination label
    if lift_current_floor == -1:
        jump coffee
    elif lift_current_floor == 0:
        jump library_path
    elif lift_current_floor == 2:
        jump classroom
    elif lift_current_floor == 3:
        jump Computer_labs
    elif lift_current_floor == 4:
        jump greenhouse

# ==========================================
# LIFT RETURN — called at end of each stop
# ==========================================
label lift_return:
    python:
        if lift_current_floor not in lift_destinations_visited:
            lift_destinations_visited.append(lift_current_floor)

    # All 5 floors visited — skip lift entirely, go straight to next phase
    if len(lift_destinations_visited) >= 5:
        jump shastri_bhavan

    # Still floors left — show the lift screen again
    scene lift_outside with dissolve

    show priya p2 at left with moveinleft
    show arjun p2 at right with moveinright

    voice f1435
    f "Where to next?"
    voice m1527
    m "We've got more floors to explore. Hop back in!"

    hide priya
    hide arjun
    with dissolve

    show screen lift_outside_screen

    $ renpy.pause(hard=True)

# ==========================================
# ALL FLOORS VISITED
# ==========================================
label lift_complete:
    scene lift_outside with dissolve

    show priya p4 at left with moveinleft
    show arjun p3 at right with moveinright

    voice f1455
    f "And that's the full tour of the building! You've seen it all."
    voice m1548
    m "Classrooms, labs, the greenhouse, and the coffee corner. Not bad for one day."
    voice f1457
    f "Now let's head over to Shastri Bhavan!"
    voice m1551
    m "That's where the cafeteria and the mess are. You're going to want to know where those are."

    hide priya
    hide arjun
    with dissolve

    jump shastri_bhavan

# ==========================================
# IMAGE DEFINITIONS FOR LIFT (add to init)
# ==========================================

label library_path:
    scene bg_hallway_split with dissolve
    show priya p2 at left with moveinleft
    show arjun p3 at right with moveinright

    voice m1565
    m "The corridor splits here."
    
    voice f1474
    show priya p3 at left with dissolve
    f "To our left lies the library, while the statue of Saraswati Mata stands to the right."

    menu:
        "Visit the Statue of Saraswati Mata":
            jump saraswati_statue_path

        "Go straight to the Library":
            jump library_interior_path

label saraswati_statue_path:
    scene bg_saraswati_statue with dissolve
    show priya p1 at left with moveinleft
    show arjun p2 at right with moveinright

    voice f1485
    f "Students often stop here for a moment of peace before their exams."
    show arjun p1 at right with dissolve
    voice m1581
    m "It’s a beautiful spot for a bit of reflection."
    hide priya
    hide arjun
    with dissolve
    # After visiting, we can head back or move to the library
    jump library_interior_path

label library_interior_path:
    scene bg_library_inside with dissolve
    show priya p1 at left with moveinleft
    show arjun p2 at right with moveinright

    voice m1587
    m "And here we are. Thousands of books and total silence."
    voice f1493
    show priya p2 at left with dissolve
    f "The perfect place to lose yourself in study."
    show arjun p1 at right with dissolve
    voice m1590
    m "Have a look around, then we will continue to our next location."

    # Library Slideshow
    hide priya
    hide arjun
    with dissolve
    window hide
    scene bg_library_view1 with dissolve
    pause 2.0
    scene bg_library_view2 with dissolve
    pause 2.0
    scene bg_library_view3 with dissolve
    pause 2.0
    window show

    show priya p3 at left with moveinleft
    show arjun p3 at right with moveinright

    # Transition to the next part of the campus
    voice f1507
    f "Well while coming in towards library you may have noticed another door to the right."
    show arjun p2 at right with dissolve
    voice m1605
    m "That's DLC room, let's take look"

    # DLC Room Slideshow
    hide priya
    hide arjun
    with dissolve
    window hide
    scene bg_dlc_view1 with dissolve
    pause 2.0
    scene bg_dlc_view2 with dissolve
    pause 2.0
    scene bg_dlc_view3 with dissolve
    pause 2.0
    window show

    show priya p4 at left with moveinleft
    show arjun p2 at right with moveinright

    voice f1520
    f "That's a prety well furnished room isn't."
    voice m1619
    m "It sure is! Back to the lift then."
    hide priya
    hide arjun
    with dissolve
    jump lift_return

label classroom:
    scene classroom_pic with dissolve
    show priya p3 at left with moveinleft
    show arjun p2 at right with moveinright
    voice f1528
    f "And here we are this is the one of many classrooms that are here at juit." 
    voice m1628
    m "Well they are prety compact but i think not all the students come to classes anyways ;)"
    voice f1530
    f "I don't actually think that way,i think students here are prety disciplined."
    voice f1531
    f "Anyways let's head to our next location."
    hide priya
    hide arjun
    with dissolve
    jump lift_return


label greenhouse:
    scene greenhouse_bg1 with dissolve
    show priya p3 at left with moveinleft
    show arjun p2 at right with moveinright
    voice f1542
    f "This is the greenhouse maintained majorly by 'BT' Students"
    voice m1645
    m "Yup they sure conduct their experiments here and also take care of all these plants."
    voice f1544
    f "Let's have a look around"

    window hide
    scene bg_green_view1 with dissolve
    pause 2.0
    scene bg_green_view2 with dissolve
    pause 2.0
    scene bg_green_view3 with dissolve
    pause 2.0
    window show

    hide priya
    hide arjun
    with dissolve
    jump lift_return


    jump lift_return

label coffee:
    # ==========================================
    # COFFEE MACHINE MINI-GAME
    # ==========================================
    scene coffee_machine_bg1 with dissolve

    show priya p3 at left with moveinleft
    show arjun p2 at right with moveinright

    voice f1572
    f "Hey Arjun! the classes sometimes make us sleepy, don't they?"
    voice m1677
    m "They sure do... but what about it?"

    show priya p4 at left with dissolve
    voice f1576
    f "Well then, let's grab a coffee from the machine! What do you say?"

    show arjun p3 at right with dissolve
    voice m1684
    m "Ha! Now THAT is the best idea you've had all day."

    voice f1581
    f "Go ahead — pick whatever you're in the mood for!"

    hide priya
    hide arjun
    with dissolve

    # Show the interactive coffee machine screen
    call screen coffee_machine_screen()

    return


# ==========================================
# COFFEE BREWING SCENE (after selection)
# ==========================================
label coffee_brewing:
    scene coffee_machine_bg1 with dissolve

    # Show the brewing screen as an overlay (non-blocking)
    show screen coffee_brewing_screen(coffee_choice)

    # Wait 2.5 seconds while screen is visible, then continue
    $ renpy.pause(2.5, hard=True)

    hide screen coffee_brewing_screen

    # Show result based on choice
    if coffee_choice == "americano":
        jump coffee_result_americano
    elif coffee_choice == "latte":
        jump coffee_result_latte
    elif coffee_choice == "mocha":
        jump coffee_result_mocha
    else:
        jump coffee_skipped


# ==========================================
# AMERICANO RESULT
# ==========================================
label coffee_result_americano:
    scene coffee_machine_bg1 with dissolve

    # Show the finished cup
    show screen coffee_result_display("cup_americano.png", "Americano")

    show priya p2 at left with moveinleft
    show arjun p2 at right with moveinright

    $ coffee_made = True

    voice m1738
    m "An Americano? Bold choice. Just like a true coder — no frills, pure power."
    voice f1633
    f "Exactly! Black coffee, black terminal. That's the JUIT way."
    voice m1741
    m "I have to admit, I respect that."

    hide screen coffee_result_display
    jump coffee_end


# ==========================================
# LATTE RESULT
# ==========================================
label coffee_result_latte:
    scene coffee_machine_bg1 with dissolve

    show screen coffee_result_display("cup_latte.png", "Latte")

    show priya p4 at left with moveinleft
    show arjun p3 at right with moveinright

    $ coffee_made = True

    voice f1653
    f "Mmm, a latte! Creamy, smooth, and just what the doctor ordered after a three-hour lecture."
    voice m1762
    m "Very civilised choice. I approve."
    voice f1655
    f "See? Even the coffee machine understands us."

    hide screen coffee_result_display
    jump coffee_end


# ==========================================
# MOCHA RESULT
# ==========================================
label coffee_result_mocha:
    scene coffee_machine_bg1 with dissolve

    show screen coffee_result_display("cup_mocha.png", "Mocha")

    show priya p1 at left with moveinleft
    show arjun p4 at right with moveinright

    $ coffee_made = True

    voice m1783
    m "A mocha! Chocolate AND coffee. You're treating yourself today."
    voice f1675
    f "Of course! Survival mode requires maximum comfort. Chocolate is non-negotiable."
    voice m1786
    m "You know, I might just get one too."

    hide screen coffee_result_display
    jump coffee_end


# ==========================================
# SKIPPED COFFEE
# ==========================================
label coffee_skipped:
    scene coffee_machine_bg1 with dissolve

    show priya p5 at left with moveinleft
    show arjun p5 at right with moveinright

    voice f1691
    f "Really? You're not getting anything? I thought you were sleepy!"
    voice m1803
    m "Maybe they just enjoy suffering through lectures without caffeine."
    voice f1693
    f "Well, the offer stands — come back anytime!"

    jump coffee_end


# ==========================================
# COFFEE END — CONTINUE STORY
# ==========================================
label coffee_end:
    hide priya
    hide arjun
    with dissolve

    "The coffee machine hums quietly as you take your cup, ready to face whatever the campus has next."

    jump lift_return


# ==========================================
# COFFEE RESULT DISPLAY SCREEN (overlay)
# ==========================================
screen coffee_result_display(cup_image, drink_label):
    frame:
        xalign 0.5
        yalign 0.12
        padding (24, 12)
        background Solid("#1a0a00dd")
        hbox:
            spacing 16
            xalign 0.5
            add cup_image:
                size (50, 50)
                yalign 0.5
            text "☕  Your [drink_label] is ready!" size 22 color "#f5c842" bold True yalign 0.5

label Computer_labs:
    scene comp_lab with dissolve
    show priya p3 at left with moveinleft
    show arjun p2 at right with moveinright
    voice f1732
    f "This is the computer lab not that high tech but managable with those intel i7 CPU's"
    voice m1846
    m "Yeah don't forget telling about different operating systems installed in some parts of the lab."
    voice f1734
    f "Oh yeah they sure comes handy for coding enthusiasts."
    hide priya
    hide arjun
    with dissolve
    jump lift_return

label shastri_bhavan:
    scene shastri_bhavan with dissolve
    show priya p2 at left with moveinleft
    show arjun p3 at right with moveinright

    voice m1856
    m "And now here we are at the Shastri Bhavan."
    voice f1743
    show priya p3 at left with dissolve
    f "This Building includes the Cafeteria and The Anapurna aka Mess."
    show arjun p2 at right with dissolve
    voice m1859
    m "First let's head to the Cafeteria."
    hide priya
    hide arjun
    with dissolve

label Cafeteria:
    scene cafeteria_bg with dissolve
    show priya p4 at left with moveinleft
    show arjun p2 at right with moveinright

    voice f1748
    f "This is the cafeteria."
    show arjun p3 at right with dissolve
    voice m1865
    m "Pretty cool right."
    voice f1750
    show priya p3 at left with dissolve
    f "Students can come here to enjoy snacks, sweets drinks and many more things here."
    show arjun p1 at right with dissolve
    voice m1868
    m "Have a look around"

    hide priya
    hide arjun
    with dissolve
    window hide
    scene cafeteria_view1 with dissolve
    pause 2.0
    scene cafeteria_view2 with dissolve
    pause 2.0
    window show

    show priya p2 at left with moveinleft
    show arjun p3 at right with moveinright

    voice m1877
    m "Now lets Move towards the Anapurna Mess."
    hide priya
    hide arjun
    with dissolve

label Mess:
    scene mess_bg with dissolve
    show priya p4 at left with moveinleft
    show arjun p1 at right with moveinright

    voice f1764
    f "This is the Anapurna Mess pretty spacious right."
    show arjun p2 at right with dissolve
    voice m1883
    m "And also pretty clean."
    voice f1766
    show priya p3 at left with dissolve
    f "The food here is the best as compared to other universities."

    # Mess Slideshow
    hide priya
    hide arjun
    with dissolve
    window hide
    scene mess_view1 with dissolve
    pause 2.0
    scene mess_view2 with dissolve
    pause 2.0
    scene mess_view3 with dissolve
    pause 2.0
    window show

    show priya p2 at left with moveinleft
    show arjun p3 at right with moveinright

    voice m1897
    m "Let's head towards the mughal garden next."
    hide priya
    hide arjun
    with dissolve

label mughal_garden:
    scene mughal_garden_bg with dissolve
    show priya p4 at left with moveinleft
    show arjun p2 at right with moveinright

    voice f1782
    f "Well how about it doesn't it look very beauttiful."
    show arjun p1 at right with dissolve
    voice m1903
    m "Childrens come here to enjoy the view and also relax for a while."
    
    voice f1785
    show priya p3 at left with dissolve
    f "Now let's head down towards the basketball court."
    hide priya
    hide arjun
    with dissolve

label basketball_court:
    scene basketball_court_bg with dissolve
    show priya p2 at left with moveinleft
    show arjun p3 at right with moveinright

    ""
    ""
    m "This is the basketball court."
    voice f1790
    show priya p3 at left with dissolve
    f "You see that shed over there that's where the ball gets issued."
    show arjun p2 at right with dissolve
    voice m1913
    m "Let's head over there."
    hide priya
    hide arjun
    with dissolve
    scene basketball_shed_bg with dissolve
    show priya p2 at left with moveinleft
    show arjun p3 at right with moveinright
    f "You can issue a basketball from here and play at any time you like."

    voice f1794
    show priya p3 at left with dissolve
    f "Let's move on."
    hide priya
    hide arjun
    with dissolve

label bsant_bhavan:
    scene basant_bhavan_bg with dissolve
    show priya p2 at left with moveinleft
    show arjun p3 at right with moveinright

    
    voice m1921
    m "This is the Basant Bhavan."
    voice f1799
    show priya p3 at left with dissolve
    f "The cheif guest's and the CEO of Jaypee stay here when they visit JUIT."
    show arjun p2 at right with dissolve
    
    voice m1924
    m "There's also a helipad towards the rightside of this building lets's check it out."
    hide priya
    hide arjun
    with dissolve
    scene helipad_bg with dissolve
    show priya p4 at left with moveinleft
    show arjun p3 at right with moveinright

    voice f1802
    f "That's pretty cool."
    show arjun p2 at right with dissolve
    
    voice m1928
    m "Yeah it is now let's head towards our next location."
    hide priya
    hide arjun
    with dissolve

label Mandir:
    scene mandir_bg with dissolve
    show priya p1 at left with moveinleft
    show arjun p2 at right with moveinright

    voice f1807
    f "And that right there is the Mandir."
    show arjun p3 at right with dissolve
    
    voice m1934
    m "You can find maximum children here before their exam."
    voice f1809
    show priya p4 at left with dissolve
    f "Hahaha that's for sure."
    hide priya
    hide arjun
    with dissolve 
    scene mandir_bg2 with dissolve
    show priya p2 at left with moveinleft
    show arjun p2 at right with moveinright

    voice m1938
    m "It's getting pretty dark now let's head to the hostels now."
    hide priya
    hide arjun
    with dissolve

label Hostel:
    scene hostel_bg with dissolve
    show priya p2 at left with moveinleft
    show arjun p2 at right with moveinright

    f "Here we are at the entrance of the hostel."
    show arjun p3 at right with dissolve
    m "Let's head in."
    hide priya
    hide arjun
    with dissolve
    scene hostel_bg1
    show priya p3 at left with moveinleft
    show arjun p3 at right with moveinright

    f "This is one of many rooms here."
    show arjun p2 at right with dissolve
    m "Its rare to find a neat one,i guess we were lucky."
    show priya p1 at left with dissolve
    f "Now lets head towards the gym room."
    window hide
    scene cor_1 with dissolve
    pause 2.0
    scene cor_2 with dissolve
    pause 2.0
    scene cor_3 with dissolve
    pause 2.0
    window show
    scene bg_gym with dissolve
    show priya p3 at left with moveinleft
    f "And this is the Gym room.Arjun actually spend alot of time here."
    show arjun p2 at right with dissolve
    m "You know me well huh."

    # ==========================================
    # ENDING SEQUENCE
    # ==========================================
    scene end with dissolve
    show priya p1 at left with dissolve
    show arjun p1 at right with dissolve

    f "And... that's the full tour!"
    m "From the main gate all the way to your room. Not bad for a first day, right?"

    show priya p4 at left with dissolve
    f "JUIT is a lot to take in at first. The buildings, the rules, the biometrics..."

    show arjun p3 at right with dissolve
    m "The 2 AM deadlines, the mess food debates, the race to the coffee machine..."

    show priya p2 at left with dissolve
    f "But trust me — the people here make it all worth it."

    show arjun p2 at right with dissolve
    m "You'll find your crew, your favourite corner of the library, your go-to mess seat."

    show priya p3 at left with dissolve
    f "And someday, you'll be the one giving this tour to the next batch of freshers."

    show arjun p1 at right with dissolve
    m "Who knows — maybe you'll even beat Priya at table tennis by then."

    show priya p4 at left with dissolve
    f "Ha! Don't count on it."

    hide priya
    hide arjun
    with dissolve

    "You look out the hostel window at the JUIT campus stretching into the Waknaghat hills."
    "Somewhere, a batch of seniors is debugging code. Somewhere else, someone just missed a deadline."
    "And somewhere, a new friendship is beginning over a bad cup of coffee from that machine in the basement."

    show priya p2 at left with dissolve
    show arjun p2 at right with dissolve

    f "Welcome to JUIT."
    m "Make it yours."

    

    # Fade to black with a final message
    scene black with fade
    pause 1.0

    centered "{size=36}{b}{color=#e0c97f}Welcome to JUIT.{/color}{/b}{/size}\n\n{size=22}{color=#cccccc}Your journey starts here.{/color}{/size}"

    pause 3.0

    # Roll credits or return to main menu
    $ renpy.full_restart()

