## 2025-07-11 - Asset Resilience and Immediate Feedback in Pygame
**Learning:** Pygame applications can be fragile if external assets are missing, leading to crashes. Providing simple colored surface fallbacks ensures the game remains playable. Immediate feedback through a scoring system and a polished game over screen significantly improves player engagement.
**Action:** Always implement try-except blocks for asset loading with `pygame.Surface` fallbacks and use `get_rect(center=...)` for centering UI elements.
