# Palette's UX & Accessibility Journal

## 2026-11-01 - Pygame Asset Resilience and Score Feedback
**Learning:** Pygame arcade prototypes crash completely if visual assets fail to load or are missing from the repository, creating an abrupt blocking experience for users. Additionally, without immediate feedback loops such as real-time score display and game over score summaries, players lack motivation and progression context.
**Action:** Always provide graceful visual fallbacks (such as colored shape primitives) using pre-defined dimensions, and render clear HUD and centered end-screen score states with properly calculated bounding boxes.
