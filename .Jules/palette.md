## 2025-05-15 - [Asset Fallback for Robustness]
**Learning:** In game development, missing external assets (like images) can lead to immediate crashes if not handled. Providing a visual fallback (like colored rectangles) ensures the application remains functional and playable even in a degraded state.
**Action:** Always wrap asset loading in try-except blocks and provide sensible defaults or placeholders to improve application resilience.
