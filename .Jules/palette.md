## 2025-02-15 - Pygame Asset Fallbacks and Text Alignment
**Learning:** Standardizing color fallback dimensions with established game variables (instead of magic numbers) guarantees design consistency during asset load failures. Additionally, pre-initializing fonts globally improves runtime execution, and utilizing get_rect(center=(x, y)) provides precise alignment.
**Action:** Always implement image loading in try-except blocks with variable-based shape fallbacks, pre-initialize fonts outside draw loops, and leverage Rect centering for professional UI alignment.
