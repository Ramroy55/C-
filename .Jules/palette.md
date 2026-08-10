## 2025-02-15 - Headless Pygame Environment Verification
**Learning:** Pygame UIs can't be tested using web-based automation like Playwright; instead, visual layout must be verified by saving screen captures locally and rendering/inspecting them with tools.
**Action:** Always capture game surface state to an image file when running in headless mode, and use local inspection tools to check layout accuracy.
