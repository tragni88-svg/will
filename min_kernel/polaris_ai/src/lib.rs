
// Main library for the Polaris AI Subsystem

#![no_std]
pub mod synapse;
pub mod cortex;

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
