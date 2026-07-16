## 2024-07-16 - Robust Asset Fallbacks in Pygame
**Learning:** In headless or asset-constrained environments, Pygame applications often crash due to missing images. Implementing a 'try-except' fallback pattern that replaces missing sprites with simple colored rectangles (using defined dimensions) ensures the application remains functional and testable without requiring visual assets.
**Action:** Always wrap `pygame.image.load` in try-except blocks and provide a `pygame.draw.rect` fallback in the rendering logic.
