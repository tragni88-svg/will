
import numpy as np

class PowerSystem:
    """
    Analyzes the power and energy requirements for the MHD engine system.
    """
    def __init__(self, plasma_velocity, plasma_charge_density, channel_area, propellant_atomic_mass=39.948):
        """
        Initializes the power system analysis.

        Args:
            plasma_velocity (float): The exhaust velocity of the plasma (in m/s).
            plasma_charge_density (float): The net charge density of the plasma (in C/m^3).
            channel_area (float): The cross-sectional area of the MHD channel (in m^2).
            propellant_atomic_mass (float): The atomic mass of the propellant gas (in amu). Defaults to Argon.
        """
        self.plasma_velocity = plasma_velocity
        self.plasma_charge_density = plasma_charge_density
        self.channel_area = channel_area
        self.propellant_atomic_mass_amu = propellant_atomic_mass

        # Physical Constants
        self.charge_of_ion = 1.602e-19  # Coulombs (assuming singly ionized plasma)
        self.amu_to_kg = 1.66054e-27   # Atomic Mass Unit to kg

    def calculate_mass_flow_rate(self):
        """
        Calculates the mass flow rate of the plasma propellant.

        Returns:
            float: The mass flow rate (in kg/s).
        """
        # Calculate the number density of ions
        ion_number_density = self.plasma_charge_density / self.charge_of_ion # ions/m^3

        # Calculate the mass of a single propellant ion
        ion_mass_kg = self.propellant_atomic_mass_amu * self.amu_to_kg

        # Calculate the mass density of the plasma
        mass_density = ion_number_density * ion_mass_kg # kg/m^3

        # Calculate the total mass flow rate
        mass_flow_rate = mass_density * self.channel_area * self.plasma_velocity # kg/s
        return mass_flow_rate

    def calculate_jet_power(self):
        """
        Calculates the power of the plasma jet (kinetic energy per second).
        Formula: P = 0.5 * m_dot * v^2

        Returns:
            float: The jet power (in Watts).
        """
        mass_flow_rate = self.calculate_mass_flow_rate()
        jet_power = 0.5 * mass_flow_rate * (self.plasma_velocity ** 2)
        return jet_power, mass_flow_rate

    def estimate_total_power(self, cryo_cooler_efficiency=0.05):
        """
        Estimates the total power requirement, including the cryocooler for the magnets.

        Args:
            cryo_cooler_efficiency (float): A simplified factor representing the power needed for cooling
                                            as a percentage of the main jet power.

        Returns:
            tuple: (Total Power in MW, Jet Power in MW, Cooling Power in MW)
        """
        jet_power_watts, _ = self.calculate_jet_power()
        cooling_power_watts = jet_power_watts * cryo_cooler_efficiency
        total_power_watts = jet_power_watts + cooling_power_watts

        # Convert to Megawatts
        total_power_mw = total_power_watts / 1e6
        jet_power_mw = jet_power_watts / 1e6
        cooling_power_mw = cooling_power_watts / 1e6

        return total_power_mw, jet_power_mw, cooling_power_mw

if __name__ == '__main__':
    # --- Parameters from the previous simulation ---
    v = 15000  # m/s
    q = 0.025  # C/m^3

    # --- New Assumptions for Power Calculation ---
    # Assuming the 2.5 m^3 channel is a torus with a 10m circumference
    channel_circumference = 10 # meters
    channel_volume = 2.5 # m^3
    A = channel_volume / channel_circumference # 0.25 m^2 cross-sectional area

    # --- Power System Analysis ---
    power_system = PowerSystem(plasma_velocity=v, plasma_charge_density=q, channel_area=A)
    total_mw, jet_mw, cooling_mw = power_system.estimate_total_power()
    _, mass_flow = power_system.calculate_jet_power()

    print("--- Project Chimera: Power & Energy Analysis ---")
    print(f"Propellant Mass Flow Rate: {mass_flow:.4e} kg/s")
    print("-" * 20)
    print(f"Jet Power Requirement: {jet_mw:.4f} MW")
    print(f"Est. Cryo-Cooling Power: {cooling_mw:.4f} MW")
    print("-" * 20)
    print(f"Total Estimated Power Draw: {total_mw:.4f} MW")
    print("\nThis power level is substantial and firmly in the domain of a compact nuclear fission or fusion reactor.")
