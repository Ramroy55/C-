# Palette's UX Journal

## 2026-11-02 - Headless Arcade UI Fallbacks & Immediate Feedback Loops
**Learning:** Pygame canvas UIs lack browser DOM accessibility semantics, so immediate visual feedback loops (such as real-time HUD scoring and centered, high-contrast game over states) and resilient asset fallbacks are essential to keep the game playable and informative even when external asset files fail to load.
**Action:** When working on Pygame/canvas games, always implement graceful colored surface fallbacks for missing sprite assets and use centered text rects with high-contrast color pairings for state announcements like game over screens.
