def on_a_pressed():
    global Laser
    music.pew_pew.play()
    Laser = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 7 . . . . . . . . 
                    . . . . . . . 7 . . . . . . . . 
                    . . . . . . . 7 . . . . . . . . 
                    . . . . . . . 7 . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.projectile)
    Laser.x = Ship.x
    Laser.y = Ship.y
    Laser.set_velocity(0, -100)
    if Laser.y == 0:
        Laser.destroy()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

Bomb: Sprite = None
Laser: Sprite = None
Ship: Sprite = None
Ship = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . 2 . . . . . . . . 
            . . . . . . . 2 . . . . . . . . 
            . . . . . . 2 2 2 . . . . . . . 
            . . . . . . 2 2 2 . . . . . . . 
            . . . . . 2 f f f 2 . . . . . . 
            . . . . . 2 2 2 2 2 . . . . . . 
            . . . 2 2 2 2 2 2 2 2 2 . . . . 
            . . . 2 2 2 2 2 2 2 2 2 . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
Ship.set_stay_in_screen(True)
controller.move_sprite(Ship)
Shoots = 4

def on_forever():
    global Bomb, Shoots
    while controller.B.is_pressed() and Shoots > 0:
        music.zapped.play()
        Bomb = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 2 . . . . . . . . 
                            . . . . . . d d d . . . . . . . 
                            . . . . . . . d . . . . . . . . 
                            . . . . . . . d . . . . . . . . 
                            . . . . . . d d d . . . . . . . 
                            . . . . . d d d d d . . . . . . 
                            . . . . . . 4 4 4 . . . . . . . 
                            . . . . . . 4 4 4 . . . . . . . 
                            . . . . . . . 2 . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.player)
        Bomb.x = Ship.x
        Bomb.y = Ship.y
        Bomb.set_velocity(0, -69)
        pause(200)
        Bomb.destroy(effects.fire, 500)
        Shoots += -1
forever(on_forever)
