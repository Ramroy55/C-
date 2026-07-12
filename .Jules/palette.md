## 2025-07-12 - Pygame Asset Fallbacks and UX Feedback
**Learning:** In headless or asset-missing environments, providing immediate visual fallbacks (like colored Surfaces) prevents crashes and maintains playability. Immediate feedback loops (like a scoring system) and clear game-state transitions (centered Game Over screen with final results) significantly enhance player engagement.
**Action:** Always wrap asset loading in try-except blocks and provide sensible defaults. Ensure critical information (score, game status) is clearly communicated and visually centered.
