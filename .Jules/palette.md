## 2025-05-15 - Robust Asset Fallbacks in Game UI
**Learning:** In environments where assets like images may be missing or failed to load (especially in containerized or headless CI/CD environments), UI-driven applications should provide graceful fallbacks. Using colored surfaces instead of crashing prevents a total loss of user experience and allows for visual verification even when artifacts are missing.
**Action:** Always wrap asset loading in try-except blocks and provide a `pygame.Surface` fallback with meaningful colors to maintain application stability and UX continuity.
