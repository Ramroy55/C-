## 2024-07-16 - Robust Asset Fallbacks
**Learning:** In Pygame projects, missing assets (images/sounds) can lead to immediate crashes, which is a poor user experience, especially during initial setup or in restricted environments. Providing simple colored Surfaces as fallbacks ensures the application remains functional.
**Action:** Always wrap `pygame.image.load` in try-except blocks and provide a `pygame.Surface` fallback with appropriate dimensions and a distinguishable color.

## 2024-07-16 - Dynamic UI Centering
**Learning:** Manually calculating text coordinates in Pygame often leads to misaligned UI elements across different screen resolutions or text lengths.
**Action:** Use `text.get_rect(center=(x, y))` to accurately center text elements on the screen, improving visual balance and readability.
