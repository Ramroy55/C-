# Palette's UX and Accessibility Journal

## 2025-05-18 - Graceful Asset Fallbacks in Pygame
**Learning:** In headless or resource-constrained environments where game assets (like image sprites) might be missing, the game should never crash at startup. Instead, falling back to clean, semantic vector/colored rect shapes with proper dimensions prevents critical failure while keeping gameplay fully functional and accessible.
**Action:** Always wrap image loaders in try-except blocks catching both Pygame and file errors, and fall back to drawing geometric shapes using predefined dimensions.
