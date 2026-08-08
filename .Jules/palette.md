## 2024-08-08 - Fallback Rendering for Pygame Graphical Assets
**Learning:** Headless environments or missing custom graphics should never prevent a game from being playable or break its visual layout. Relying strictly on asset existence causes immediate crashes. Utilizing try-except blocks coupled with dynamic fallback rectangle geometry ensures uninterrupted user playability.
**Action:** Always wrap `pygame.image.load` in safety handlers and provide fallback vector drawing matching defined entity bounding-box dimensions.
