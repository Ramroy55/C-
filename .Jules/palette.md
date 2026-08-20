## 2025-05-18 - Centering Pygame Text Overlays
**Learning:** Pygame `Surface.blit` with explicit coordinates often causes visual offset for dynamically sized text. Using `text.get_rect(center=(x, y))` ensures perfect alignment for game state messages like scores and titles.
**Action:** Always compute centered bounding boxes with `get_rect(center=...)` when rendering text in Pygame UIs.
