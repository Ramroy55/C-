# Palette's UX and Accessibility Journal

## 2025-02-17 - Robust Image Fallbacks & Scoring Systems in Pygame
**Learning:** Pygame games running in headless environments can crash unexpectedly if expected asset files (e.g., `car.png`) are missing. Providing a robust, try-except wrapped image loader that falls back to beautifully-rendered vector or solid rectangle shapes prevents crashes while keeping the UI clear and playable. Additionally, incorporating immediate visual feedback like an on-screen score and a centered "Game Over" layout significantly improves player engagement and micro-UX delight.
**Action:** Always wrap image resource loading in try-except statements to catch `pygame.error` and `FileNotFoundError`. When fallback is needed, draw semantic colored shapes using pre-defined dimensions (e.g., `car_width`) instead of hardcoded magic numbers, and use `get_rect(center=(x, y))` to center text perfectly.
