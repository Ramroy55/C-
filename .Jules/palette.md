## 2025-05-15 - Pygame Performance: Font Initialization
**Learning:** Initializing fonts with `pygame.font.SysFont` inside a game loop (60 FPS) causes significant performance degradation ("jank") because it repeatedly searches the system for font files.
**Action:** Always pre-initialize `pygame.font` objects once outside the main game loop and reuse them during rendering.

## 2025-05-15 - Defensive Asset Loading in Pygame
**Learning:** Pygame games often crash if external asset files (PNG/JPG) are missing, which is a poor user experience.
**Action:** Use a `load_image` helper with `try-except` blocks to provide colored `pygame.Surface` fallbacks when assets are missing, ensuring the game remains playable.
