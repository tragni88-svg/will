# Game Design Document: Project: Decay

## 1. Title & Vision

*   **Working Title:** Project: Decay
*   **Elevator Pitch:** A hyper-realistic, single-player survival horror game set in the immediate aftermath of a viral outbreak. It combines brutal, physics-based combat with a deeply systemic world, all rendered in stunning 8K on the NEXON Prime.
*   **Core Pillars:**
    *   **Unflinching Realism:** Every mechanic is grounded in reality, from weapon handling to human needs.
    *   **Systemic World:** The environment and its inhabitants are governed by interconnected systems, creating emergent gameplay.
    *   **Psychological Dread:** The true horror comes not from jump scares, but from the oppressive atmosphere, resource scarcity, and the constant threat of a gruesome, permanent death.

---

## 2. Gameplay Mechanics

*   **Combat: The "Anatomy Engine"**
    *   **Leveraging NEXON Prime's CPU:** This is not a simple headshot-focused shooter. The Anatomy Engine simulates the entire physiology of the infected. Bullets and melee weapons cause localized damage to bone, muscle, and organs.
    *   **Dynamic Incapacitation:** Shooting a zombie in the leg will shatter its femur, causing it to crawl. A blow to the arm might break it, rendering that limb useless. Only destroying the brainstem guarantees a kill.
    *   **Physics-Based:** All interactions are driven by a robust physics engine. The weight of your weapon affects your swing; the force of a blow can stagger an enemy or send it tumbling over an obstacle.

*   **Survival: The "Metabolism System"**
    *   The player must manage not just hunger and thirst, but also body temperature, fatigue, and illness.
    *   Food can spoil. Water must be purified. Injuries, if not properly treated with the correct supplies (bandages, antiseptics), can become infected and lead to a slow, agonizing death.

*   **The Infected: "Horde AI"**
    *   **Leveraging NEXON Prime's CPU & SSD:** The Horde AI is a swarm intelligence system. There are no arbitrary limits on the number of on-screen infected. Their behavior is governed by simple, animalistic drives: sight, sound, and smell.
    *   A single gunshot can be heard for miles, drawing in any infected within earshot. The smell of blood from a recent fight will attract others.
    *   The PCIe 5.0 SSD allows for hundreds of infected to be streamed into the game world seamlessly, creating truly massive and terrifying hordes that are a force of nature, not a scripted event.

*   **Audio: NEXON "Aura" 3D Audio**
    *   Sound is a primary gameplay mechanic. The dedicated audio hardware of the NEXON Prime is used to create a terrifyingly realistic soundscape.
    *   Players can track the location of a single infected by the sound of its shuffling feet from two floors above, or pinpoint the direction of a distant scream. Every creak of a floorboard could be your last.

---

## 3. Narrative & Setting

*   **Setting:** The fictional, once-bustling metropolis of "Aethelburg," a dense urban environment with a mix of modern skyscrapers, historic districts, and sprawling suburbs. The game takes place in the first 72 hours of the outbreak.
*   **Story:** You are not a soldier or a superhero. You are an ordinary citizen—a paramedic, a construction worker, a teacher—caught in the chaos. The narrative is emergent, told through environmental details, radio broadcasts, and the desperate notes left behind by others. The only goal is to survive.

---

## 4. Technical Goals (NEXON Prime)

*   **Resolution & Framerate:** 8K Native Resolution at a locked 60 FPS. A high-performance 4K mode at 120 FPS will also be available.
*   **Ray Tracing:** Full, real-time ray tracing for lighting, shadows, and reflections to create an unparalleled sense of immersion and dread.
*   **Loading:** No loading screens. The entire city of Aethelburg is a single, seamless map, streamed in real-time from the SSD.
