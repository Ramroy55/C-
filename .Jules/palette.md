# Palette's UX & Accessibility Journal

This journal documents critical learnings, design constraints, and patterns discovered while working on user interfaces and game accessibility.

## 2024-07-29 - Robust Asset Failbacks and Immersive Progress Tracking in Pygame
**Learning:** In headless game environments or when local assets (images) are missing, a robust fallback strategy using try-except catching `pygame.error` and `FileNotFoundError` is required to prevent immediate crashes. Displaying real-time progression like score updates during play keeps users engaged, while properly centered UI text on game over elements provides seamless user-centered design without unexpected layout shifts.
**Action:** Always wrap `pygame.image.load` in safety catches and draw standard shapes (like rectangles of standard dimension constants) if images fail to load. Use `text.get_rect(center=(x, y))` to dynamically and perfectly center layout typography.
