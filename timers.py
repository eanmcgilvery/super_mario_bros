class Timers:
    """Timers used for animations, movement, screen display, etc"""
    def __init__(self):
        # Update one timer per loop to base everything else on
        self.curtime = 0

        # Display refresh rate
        self.last_display = 0
        self.display_wait = 30

        # Enemies animate together
        self.last_enemy_animation = 0
        self.enemy_animation_wait = 500

        # General movement
        self.last_move = 0
        self.move_wait = 30

        # Piranha Plant animations
        self.piranha_plant_move_wait = 1500
        self.piranha_plant_pipe_wait = 3000
