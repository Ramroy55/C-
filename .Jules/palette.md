## 2025-05-18 - Pygame Asset Fallback and Text Alignment
**Learning:** Missing image assets in Pygame cause silent crashes on startup; providing colored Surface fallbacks prevents app failure and preserves basic gameplay UX.
**Action:** Always wrap `pygame.image.load` in try-except blocks with fallback surfaces using defined dimensions when building Pygame UIs.
