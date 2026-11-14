# Axonometric view

`drawbar-axonometric.png` is rendered from `axonometric.html` (three.js 0.160.0, orthographic camera) with `render.js` (Playwright + Chromium):

    npm i three@0.160.0
    node render.js 2 drawbar-axonometric.png

Geometry comes from the plate-part drawings and the design stack-up (Z0 = spindle end face), not from a CAD model.
