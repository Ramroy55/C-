# Palette's UX and Accessibility Journal

## 2024-07-28 - Pygame Micro-UX & Asset Resiliency Patterns
**Learning:** In lightweight game development, unexpected asset loading failures can lead to immediate crashes, completely blocking user accessibility. Furthermore, static text placement coordinates (e.g. static offsets) can cause overlapping and disjointed visual hierarchy across different screens. Using robust Try-Except fallbacks with dynamic shapes (matching defined entity sizes) maintains game playability. Coupling this with text centering using Pygame's `get_rect(center=(x, y))` ensures perfectly balanced layouts across all resolutions.
**Action:** Always wrap Pygame asset loaders with size-safe/color-safe Surfaces as fallback, and use dynamic geometry centering (`get_rect(center=...)`) for any full-screen or overlaid UI text.
