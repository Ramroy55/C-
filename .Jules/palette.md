## 2025-05-15 - Improving Game UX and Resilience
**Learning:** In Pygame-based games, immediate feedback (scoring) and visual centering are critical for player engagement. Additionally, providing graceful fallbacks for missing assets (using colored Surfaces) ensures the game remains playable in diverse environments, improving overall resilience and micro-UX.
**Action:** Always implement try-except blocks for asset loading and provide basic geometric fallbacks. Use immediate feedback loops like live scores to keep users informed and engaged.
