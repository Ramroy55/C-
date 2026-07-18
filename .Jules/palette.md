# Palette's Journal - Critical Learnings Only

## 2025-07-18 - Handling Asset Fallbacks and Rendering Alignment in Headless Pygame
**Learning:** In headless environments (like when verifying Pygame UIs), missing graphic assets (e.g., .png sprites) must be gracefully handled with fallback colors (Blue for player, Red for enemy) using pre-defined dimensions (like car_width/car_height) to avoid crashes. For visual feedback and alignment, text centering is best handled with `text.get_rect(center=(x, y))`, and Pygame fonts should be initialized once outside of the game loop to optimize performance.
**Action:** Always wrap image loading in a try-except block catching `pygame.error` and `FileNotFoundError`. Explicitly break the game loop on collision before exiting, and use standard UI color constants to improve code clarity and readability.
