## 2025-05-15 - Pygame UI Centering and Robustness
**Learning:** In Pygame, using `text.get_rect(center=(x, y))` is the most reliable way to ensure UI elements like "Game Over" or "Score" are perfectly aligned regardless of their dimensions. Additionally, the lack of image assets in some environments can cause immediate crashes if not handled gracefully.
**Action:** Always use `get_rect` with explicit coordinates for UI text and implement `try-except` blocks with `pygame.Surface` fallbacks when loading external assets to ensure application stability.
