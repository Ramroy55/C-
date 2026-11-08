## 2025-05-18 - Resilient Asset Fallbacks and Immediate Scoring HUD
**Learning:** Pygame arcade games without bundled image assets immediately crash on launch unless graceful Surface fallbacks (contrasting colored rectangles) are provided. Additionally, arcade racing experiences lack positive feedback loops without an in-game HUD score tracker and final score summary on collision.
**Action:** Always wrap Pygame asset loaders with try-except blocks creating fallback colored Surfaces, and provide live HUD feedback paired with centered game-over score metrics.
