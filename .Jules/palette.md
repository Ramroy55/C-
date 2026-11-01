## 2026-11-01 - Graceful Asset Fallbacks in Pygame
**Learning:** Pygame crashes immediately on startup if external image assets are missing, creating a terrible user experience before the game even begins. Using colored Surface fallbacks matching the sprite dimensions prevents crashes and keeps the game playable while assets are being loaded or replaced.
**Action:** Always wrap `pygame.image.load` in try-except blocks catching `(pygame.error, FileNotFoundError)` and substitute with appropriately dimensioned colored placeholder surfaces.
