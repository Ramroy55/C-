## 2025-07-10 - Robust Asset Fallbacks and Score Feedback
**Learning:** In Pygame environments, missing assets can cause immediate crashes, which is a poor user experience. Providing colored surface fallbacks ensures the game remains playable even if assets are missing. Additionally, providing immediate score feedback via a UI element improves engagement by giving users a sense of progress.
**Action:** Always wrap asset loading in try-except blocks with sensible visual fallbacks, and ensure key game metrics like score are always visible to the user.
