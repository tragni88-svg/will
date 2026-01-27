# NEXON Console: Hardware Architecture & Specifications

## 1. Vision & Design Philosophy
To deliver a true next-generation leap, the NEXON console is engineered for unparalleled performance, targeting 8K native and 10K upscaled resolutions with high frame rates. The architecture prioritizes data throughput, graphical power, and developer efficiency, creating a balanced ecosystem for both flagship titles like *Counter-Strike 3* and future AAA games.

---

## 2. Core System Architecture: Custom AMD APU

The heart of the console is a custom-designed System-on-Chip (SoC) developed in partnership with AMD, leveraging their most advanced silicon.

*   **CPU (Central Processing Unit):**
    *   **Architecture:** AMD Zen 5 (12-Core / 24-Thread)
    *   **Clock Speed:** 4.2 GHz base, 5.0 GHz precision boost
    *   **Fabrication:** 3nm Process Node
    *   **Rationale:** Provides elite multi-core performance for complex physics, AI, and system-level tasks without bottlenecking the GPU. The high thread count is crucial for managing the extreme asset streaming required for 10K textures.

*   **GPU (Graphics Processing Unit):**
    *   **Architecture:** AMD RDNA 4 (Custom)
    *   **Compute Units:** 80 CUs
    *   **Clock Speed:** 2.8 GHz
    *   **Ray Tracing:** 2nd Generation RT Accelerators with dedicated hardware for BVH traversal.
    *   **AI/ML:** Integrated AI/ML cores for advanced supersampling (NEXON Super Resolution), physics simulation, and NPC behavior.
    *   **Target Performance:** 28 TFLOPS (FP32)
    *   **Rationale:** A massive leap in raw graphical power is necessary for 8K/10K rendering. The custom RDNA 4 architecture is optimized for high-resolution textures and complex shader workloads, with dedicated hardware to make ray tracing viable at extreme resolutions.

---

## 3. Memory Subsystem

*   **Type:** 32 GB GDDR6X Unified Memory
*   **Bus:** 384-bit
*   **Bandwidth:** ~1.2 TB/s
*   **Rationale:** A unified memory pool allows developers maximum flexibility. The high-capacity 32 GB is essential for holding 10K texture assets, while the massive bandwidth ensures the APU is never starved for data, eliminating stutter and enabling near-instantaneous asset loading from the SSD.

---

## 4. Storage

*   **Internal SSD:**
    *   **Type:** PCIe 5.0 NVMe M.2 SSD (Custom Controller)
    *   **Capacity:** 2 TB Usable
    *   **Read Speed (Raw):** 14 GB/s
    *   **Read Speed (Compressed):** 24 GB/s (with dedicated hardware decompression block)
    *   **Rationale:** Eliminates loading screens and enables "DirectStorage" style texture streaming directly to the GPU, a critical component for rendering massive open worlds at 10K.

*   **Expandable Storage:**
    *   User-accessible PCIe 5.0 M.2 slot for certified third-party drives.

---

## 5. Video & Audio Output

*   **Video Output:**
    *   **Primary:** HDMI 2.1a
    *   **Secondary:** DisplayPort 2.1
    *   **Resolutions:** 4K@240Hz, 8K@120Hz, 10K (upscaled)@60Hz
    *   **Features:** VRR (Variable Refresh Rate), ALLM (Auto Low Latency Mode), FRL (Fixed Rate Link).

*   **Audio Engine:**
    *   **Technology:** NEXON "Aura" 3D Audio
    *   **Hardware:** Dedicated Tempest-style audio processing unit for object-based spatial audio.
    *   **Rationale:** Delivers highly realistic and immersive soundscapes, crucial for competitive games like *CS3* where positional audio is key.

---

## 6. Connectivity

*   **Networking:** Wi-Fi 7, 10-Gigabit Ethernet Port
*   **Peripherals:** 3x USB 4.0 Type-C, 1x USB 3.2 Type-A
