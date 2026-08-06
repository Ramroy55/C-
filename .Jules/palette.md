# Palette's Journal - Critical UX and Accessibility Learnings

## 2024-08-06 - Image loading fallback and scoring systems in Pygame
**Learning:** Pygame games need reliable error recovery if asset files like images are missing, which is highly common in headless test environments. Providing colored rectangle fallbacks using precise game car dimensions prevents rendering failures. Furthermore, a scoring system creates an immediate feedback loop which makes the gameplay experience significantly more engaging.
**Action:** Always wrap image loading in try-except blocks catching Pygame and FileNotFoundError. Draw fallback rectangles using defined variables rather than magic numbers. Display live and final score results centered nicely with `get_rect(center=(x, y))`.
