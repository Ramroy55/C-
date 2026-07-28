# Palette's UX & Accessibility Journal

## 2025-07-28 - Pygame UI Asset Resilience and Performance
**Learning:** Pygame applications can easily crash on startup if external assets are missing or if fonts are repeatedly initialized inside rendering frames. Utilizing safe try-except loading fallbacks to simple geometric representations (using existing dimensions/variables) keeps the application functional, while initializing fonts once outside of the loop ensures optimal performance. Centering multi-line feedback texts like "Game Over" and final scores on the screen via `get_rect(center=(...))` delivers a polished user experience.
**Action:** Always load external assets with explicit fallback blocks, initialize font resources strictly once at initialization time, and center typography using screen-relative rect bounds.
