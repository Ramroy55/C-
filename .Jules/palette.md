## 2025-07-12 - [Asset Fallback UX]
**Learning:** [In environments where assets might be missing (CI/CD, headless, initial setup), the application should remain functional and playable. Hard crashes on missing images provide poor developer and user experience.]
**Action:** [Always implement try-except blocks for asset loading and provide visual fallbacks (like pygame.Surface) to ensure the application remains operable.]
