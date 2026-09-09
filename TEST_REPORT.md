# Test Report

Tested 2026-09-09 on Windows with local static files and Google Chrome headless rendering.

## Automated checks

`python test_app.py` — PASS 12/12.

Covered: responsive viewport, three activities, ten distinct ten-frame slots, 0–10 quantity coverage including 0 and 10, at least five number-bond starts including 0/5/10, seven story problems, both addition and subtraction, optional read-aloud, two selectable scaffold levels, reset/replay controls, no speed/lives/ranking language, and >=48px control targets.

## Render checks

Chrome rendered all three core activities without network dependencies at:
1. `screenshots/01-build-1280.png` — Build a quantity, 1280px.
2. `screenshots/02-make-ten-768.png` — Make ten, 768px.
3. `screenshots/03-stories-mobile-360.png` — Story problems, 360px mobile width.

## Manual interaction checklist

- Keyboard: native buttons are tab-focusable; visible focus style is defined.
- Touch/non-drag: every learner manipulation is click/tap based; no dragging is required.
- Reset/retry: each activity has a reset path; incorrect answers preserve a usable state and allow unlimited retry.
- Feedback: correct and incorrect attempts return strategy-oriented text rather than lives or speed penalties.
- Reduced motion: `prefers-reduced-motion` disables transitions/animation; the lesson contains no flashing content.
- Privacy: no forms, login, storage, analytics, tracking, ads, uploads, chat, or remote grading.

## Math spot checks

- Deliberate zero target is included.
- 10 target is included.
- Make-ten examples include 0 + 10, 5 + 5, and 7 + 3.
- Story set includes 9 - 4 = 5.
- Final fresh story asks 7 + 3 = 10.
