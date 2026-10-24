## 2026-10-24 - Pygame Asset Fallbacks and Centered Game Over Layout

**Learning:** Missing asset files cause immediate application crashes in desktop/canvas games if unhandled. Adding fallback colored primitive surfaces allows games to run gracefully while preserving layout and entity boundaries. Furthermore, using `text.get_rect(center=(x, y))` ensures score and game status text are properly centered regardless of screen size or string length.

**Action:** Always wrap `pygame.image.load` in try-except blocks with colored surface fallbacks matching entity dimensions, and center UI text overlays using bounding rectangle centers.
