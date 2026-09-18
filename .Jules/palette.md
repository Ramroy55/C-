# Palette's Journal

## 2024-05-04 - Graceful Asset Fallbacks in Pygame
**Learning:** In Pygame applications without guaranteed static assets, attempting to load missing image files causes unhandled FileNotFoundError / pygame.error crashes. Providing filled Surface fallbacks matching sprite dimensions keeps the UI playable and visually coherent.
**Action:** Always wrap `pygame.image.load` in try-except blocks with colored Surface fallbacks using defined width/height constants.
