# Palette UX and Accessibility Journal

## 2024-08-03 - Accessible Pygame Fallbacks & Scoring Polish
**Learning:** Pygame applications must handle missing file errors gracefully to ensure they do not crash in different runtime environments, utilizing try-except and robust vector graphic fallbacks with defined object dimensions. Incorporating score indicators and perfectly centered final results creates a much stronger feedback loop and enhances player engagement.
**Action:** Always load assets with try-except blocks, provide clear geometric fallbacks with standard colors, and center UI text perfectly using rect alignment (`get_rect(center=(...))`).
