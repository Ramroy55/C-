## 2024-08-17 - Graceful Asset Fallbacks and Live HUD Feedback in Pygame
**Learning:** Missing asset files can cause immediate crashes in game loops if uncaught. Providing color-coded fallback surfaces (`pygame.Surface`) ensures UI continuity. Additionally, centering game over text using `get_rect(center=(...))` and providing live HUD score feedback significantly enhances player feedback loops.
**Action:** Always wrap `pygame.image.load` in try-except blocks with fallback surfaces and center text surfaces with `get_rect(center=...)` for clean layout.
