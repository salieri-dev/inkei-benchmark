# Inkei-Bench

**Inkei-Bench** is a specialized benchmark designed to evaluate Large Language Models on **cross-language code migration** and **complex geometric reasoning**.

Inspired by the impressive project of `inkei.net`, this benchmark challenges an LLM to interpret legacy JavaScript mathematics and port them into modern Python environments, or to generate complex biological parameterizations from scratch.

**Actually... this is a benchmark for LLM penis generation**

## ⚖️ Attribution & Legal

**No ownership is claimed regarding the source code provided in this repository.**

The logic and geometric algorithms are the intellectual property of the original creator of **inkei.net**. The source code included in `inkei_sourcecode.md` was retrieved via public browser developer tools (client-side JavaScript).

**Original Creator:** [@inkeinet](https://twitter.com/inkeinet) (ララ / @rarapima)

**Takedown Policy:**
At the request of the owner, the source code file will be immediately deleted from this repository.

## 📂 The Dataset
The benchmark utilizes `inkei_sourcecode.md`, which contains the original logic, rotation matrices, and Bezier curve data used in the original web application. Attach this file in the LLM request.

## 🏆 The Benchmark Levels

The benchmark consists of four progressive tiers of difficulty. The prompts below are **reference examples**; the goal is to assess if the LLM can derive the correct mathematical logic, regardless of the specific phrasing used.

### Level 1: The Static Port
**Objective:** Syntax translation (JS → Python)
> **Reference Prompt:** "I have attached source code in JavaScript / HTML. Can you convert this code to the Python to render final state (no animation)?"

*   **Pass:** Python code runs without error; output matches the source geometry.
*   **Fail:** Broken syntax, hallucinated libraries, or failure to implement the scaling logic.

### Level 2: The Animation Port
**Objective:** 3D projection logic and animation loops.
> **Reference Prompt:** "I have attached source code in JavaScript / HTML. Can you convert this code to the Python to render final state (with animation in one projection just like in original code)?"

*   **Pass:** A smooth rotating GIF/MP4. The mesh must not "twist" or invert coordinates during rotation (a common issue in direct ports).
*   **Fail:** Static image only, or mesh artifacts (vertices crossing incorrectly).

### Level 3: Ab Initio Visualization (Static)
**Objective:** Semantic understanding of geometry and organic constraints.
> **Reference Prompt:** "Write a Python script to procedurally generate a visualization of a male penis. Do not use simple primitives (spheres/cylinders). Use Bezier curves or splines to create a natural, organic profile. The script must be parametric (length, girth, curve)."

*   **Pass:** Organic shape using splines; distinct anatomical features (glans/shaft); parameters successfully alter the shape.
*   **Fail:** Output uses simple geometric primitives (e.g., rigid cylinders), looks like a balloon animal, or lacks parametric control.

### Level 4: Ab Initio Visualization (Animation)
**Objective:** Physics simulation and performance optimization.
> **Reference Prompt:** "Extend the previous visualization script to create a 3D rotating animation. Implement a 'soft body' physics simulation or elasticity algorithm: as the object rotates, apply a slight sine-wave oscillation or 'wobble' to the tip vertices relative to the base to simulate soft tissue dynamics."

*   **Pass:** 3D mesh with visible independent vertex oscillation (jiggle physics).
*   **Fail:** Rigid body rotation only.