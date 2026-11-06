# Palette's Journal

## 2024-11-06 - Visual Feedback Loop & Fallback Rendering in Pygame Canvas
**Learning:** Pygame arcade games without visual fallbacks fail completely when asset files are missing, breaking the user experience instantly. Additionally, absence of score tracking removes feedback loops, leaving players unaware of progression or performance on game over.
**Action:** Always provide graceful surface fallbacks with distinct colors (e.g. blue for player, red for enemy) when assets fail to load, and establish clear immediate feedback via high-contrast on-screen scoring and centered end-game summaries.
