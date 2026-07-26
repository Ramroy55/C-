# Palette's UX & Accessibility Journal

## 2025-02-14 - Headless Pygame UI Fallbacks and Feedback Loops
**Learning:** In headless or asset-deficient testing environments, loading external sprite images can crash Pygame applications instantly. Providing robust try-except error handling that falls back to drawing standard colored rectangles (Blue/Red) with defined variables (no magic numbers) ensures graceful degradation. Additionally, utilizing text.get_rect(center=(x, y)) provides perfectly centered typography for Game Over and score feedback, vastly improving readability and accessibility.
**Action:** Always wrap image loading in Pygame with a comprehensive fallback mechanism that catches both pygame.error and FileNotFoundError, using standard UI colors (BLUE, RED, WHITE, BLACK, GRAY) and defined sprite dimensions. Always initialize Pygame fonts once outside the main game loop, and break the game loop on game over to avoid display rendering crashes.
