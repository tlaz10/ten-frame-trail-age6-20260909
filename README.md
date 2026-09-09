# Make Ten Adventure

A dependency-free interactive mathematics lesson for approximately age 6.

## Run locally

Requires any current Python 3 installation only to serve the static files:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/`.

No build step or package installation is required. The lesson itself is plain HTML/CSS/JavaScript and works without a server when opened directly, although a local HTTP server best matches production.

## Browser/runtime expectations

Test target: current stable Chrome/Edge/Firefox/Safari. Core activity does not require network access. Optional read-aloud uses the browser `speechSynthesis` API after an intentional button press and never blocks play.

## Architecture

All lesson state is held in JavaScript memory. `makeFrame()` renders the ten-slot model; build, number-bond, and story activities each own small bounded state. Story correctness is defined by the arithmetic data, not counter position. There are no remote APIs, analytics, trackers, accounts, or persistent learner data.

## Deployment

Serve repository root as static HTTPS. GitHub Pages is sufficient.

## Known limitations

Browser voice availability and pronunciation vary. The visible text is always the authoritative fallback. This is practice, not an assessment or claim of age-universal suitability.
