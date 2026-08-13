# Palette Journal

## 2024-08-13 - Robust Fallbacks and Immediately Actionable Scoring Feedback
**Learning:** For interactive Pygame arcade applications, immediately rewarding actions via a visual scoring system increases user motivation. Providing robust visual fallbacks (using well-defined dimension variables rather than magic numbers) when image assets are missing ensures the experience remains fully functional and pleasing even when media loads fail. Additionally, centering critical UI texts using Pygame's rect system prevents misalignments across different screens.
**Action:** Always wrap asset loading with fallback options that use defined sprite variables, and display/center live progression scores prominently in the gameplay and final state.
