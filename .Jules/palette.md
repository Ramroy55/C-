## 2025-05-18 - Pygame UI Positioning and Real-time Gameplay Feedback

**Learning:** In Pygame, hardcoded pixel coordinates for text often cause misalignment across screen resolutions or variable string lengths. Centering text dynamically with `surface.get_rect(center=(x, y))` and rendering live scoring HUD elements significantly improves player feedback and engagement.

**Action:** Always pre-calculate dynamically centered rects for Pygame text surfaces on screen-end overlays and instantiate font objects outside main rendering loops.
