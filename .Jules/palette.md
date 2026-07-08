## 2025-05-14 - Robust Asset Loading Pattern
**Learning:** In Pygame, failing to load an image is a hard error that crashes the game. Providing fallback surfaces ensures the game is playable even when assets are missing.
**Action:** Use a `load_image` helper that catches `FileNotFoundError` and `pygame.error` to return a `pygame.Surface` placeholder.

## 2025-05-14 - Efficient Font Rendering
**Learning:** Initializing fonts inside a high-frequency render loop (60 FPS) is a significant performance bottleneck.
**Action:** Always initialize font objects once outside the game loop and reuse them.
