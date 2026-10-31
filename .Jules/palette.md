## 2025-05-18 - Pygame UI Immediate Feedback and Dynamic Visual Centering
**Learning:** In simple arcade loops without HUD elements, players lack immediate feedback on dodging success and sense of accomplishment; adding a live HUD score along with center-aligned (`get_rect(center=...)`) game-over typography provides clear feedback and readability without screen clutter.
**Action:** Always provide persistent score feedback in arcade interfaces and dynamically center game-over text using bounding box coordinates.
