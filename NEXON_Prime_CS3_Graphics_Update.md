# NEXON Prime - Counter-Strike 3 - Graphics Technology Brief

**Project Goal:** To deliver a generational leap in visual fidelity for Counter-Strike 3, leveraging the full power of the NEXON Prime's custom AMD Zen 5/RDNA 4 architecture and PrimeOS.

**Engine:** Source 2 Engine - Heavily Modified for NEXON Prime

**Key Graphical Enhancements:**

1.  **Performance Targets:**
    *   **Fidelity Mode:** Native 4K (3840x2160) resolution at a locked 120 FPS.
    *   **Performance Mode:** 1440p resolution at a target of 240 FPS for competitive play.
    *   Utilizes AMD FidelityFX Super Resolution 3 (FSR 3) for advanced upscaling and frame generation.

2.  **Advanced Lighting Engine:**
    *   **Hardware-Accelerated Ray Tracing:**
        *   **Ray-Traced Global Illumination (RTGI):** Provides physically accurate indirect lighting for incredibly realistic scene lighting.
        *   **Ray-Traced Reflections:** Creates true-to-life reflections on surfaces like water, glass, and polished weapons.
        *   **Ray-Traced Shadows:** Renders soft, realistic shadows with natural penumbras.

3.  **Asset & Texture Overhaul:**
    *   **Ultra-High-Resolution Textures:** All assets rebuilt with 4K Physically Based Rendering (PBR) materials for realistic surface properties.
    *   **Photogrammetry:** Real-world locations and objects scanned to create hyper-realistic map assets.
    *   **Increased Geometric Detail:** Significant increase in polygon count for characters, weapons, and environments.

4.  **Enhanced Visual Effects (VFX):**
    *   **Volumetric Smoke & Fog:** Smoke grenades will now create true volumetric clouds that realistically fill spaces and interact with light.
    *   **GPU-Accelerated Particle System:** Drastically improved particle counts for muzzle flashes, explosions, and environmental debris.
    *   **Fluid Dynamics:** Realistic water caustics, ripples, and splashes.

5.  **PrimeOS Integration:**
    *   **Low-Level API Access:** Direct-to-hardware access via custom PrimeOS APIs, minimizing overhead and maximizing performance.
    *   **Dedicated Ray-Tracing Cores:** Full utilization of the RDNA 4 architecture's dedicated hardware for ray tracing calculations.
