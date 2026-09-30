## 2025-02-14 - Pygame Fallbacks & HUD Score Feedback
**Learning:** In simple Pygame-based applications without pre-packaged image assets, missing textures crash execution immediately unless handled gracefully with standard surface fallbacks. Additionally, providing continuous score updates during gameplay and centering end-of-game stats improves player engagement and feedback loops.
**Action:** Always wrap `pygame.image.load` calls in try-except blocks using colored rectangle fallback surfaces matching defined dimensions, and calculate `get_rect(center=...)` for centered status text.
