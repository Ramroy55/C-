# Palette UX Journal

## 2025-05-15 - Robust Asset Fallbacks
**Learning:** In headless environments or incomplete repositories, missing assets can cause fatal crashes, ruining the UX. Providing semantic fallbacks (colored rectangles) ensures the app remains functional and accessible even when assets are missing.
**Action:** Always wrap image loading in try-except blocks and provide `pygame.Surface` fallbacks using defined dimensions.
