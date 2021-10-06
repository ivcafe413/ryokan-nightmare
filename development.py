import logging
import os

import pygame
import pygame.display
import pygame.event

from vagrantengine import game
from vagrantengine import eventhandler
from vagrantengine import rendering
from vagrantengine import driver

# TODO: Environment Variables
from constants import GAME_PATH
SCENES = os.path.join(GAME_PATH, "scenes")
MAPS = os.path.join(GAME_PATH, "maps")

IMAGES = os.path.join(GAME_PATH, "assets", "images")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MENU_WIDTH = 100
MENU_HEIGHT = 600
MENU_LEFT = 50

HUD_HEIGHT = 100

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Debug Surface/HUD
    debug_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()

    # Game State Initialization
    stage = game.Stage()

    # Initial Scene Load
    game.load_scene(SCENES, IMAGES, MAPS, 1, stage)

    # Event Handler config
    eventhandler.register_game(stage)
    # Limit allowed Pygame events (performance)
    pygame.event.set_blocked([
        pygame.MOUSEMOTION
    ])
    key_bindings = {
        pygame.K_UP: "player_character_up",
        pygame.K_DOWN: "player_character_down",
        pygame.K_LEFT: "player_character_left",
        pygame.K_RIGHT: "player_character_right"
    }
    eventhandler.register_key_bindings(key_bindings)

    # Renderer Setup
    renderer = rendering.Renderer(stage
        # , overworld_menu=overworld_menu
        # , battle_hud=battle_hud
        )
    debug_renderer = rendering.DebugRenderer(stage, debug_surface)

    # TODO: Stage Stack

    # Render pipeline defines surface rendering order and functions to use
    renderer.add_pipeline_step(debug_surface, debug_renderer.draw_debug)

    # Game Loop Start
    driver.game_start(stage, renderer)