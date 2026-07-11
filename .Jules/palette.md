## 2025-07-11 - Asset Fallbacks and Centered Game Over UI
**Learning:** In headless environments or incomplete asset packs, implementing robust fallbacks (e.g., colored Surfaces) ensures the application remains functional. Additionally, centering UI elements using `get_rect(center=...)` significantly improves the professional feel and accessibility of feedback screens.
**Action:** Always wrap asset loading in try-except blocks with visual fallbacks and use relative positioning for critical UI text.
