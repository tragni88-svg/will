#![no_std]
#![no_main]
#![feature(alloc_error_handler)]

extern crate alloc;
extern crate min_kernel;

use core::panic::PanicInfo;
use min_kernel::allocator;
use min_kernel::vga_buffer;
use alloc::boxed::Box;
use alloc::vec::Vec;

#[no_mangle]
pub extern "C" fn _start() -> ! {
    vga_buffer::print_something();

    allocator::init_heap();

    // Test allocation
    let _heap_value = Box::new(42);
    let mut vec = Vec::new();
    vec.push(1);
    vec.push(2);

    // If we get here without crashing, heap is working!
    // We can print something to confirm.
    // vga_buffer::print_something(); // Print again

    loop {}
}

#[alloc_error_handler]
fn alloc_error_handler(layout: alloc::alloc::Layout) -> ! {
    panic!("allocation error: {:?}", layout)
}

/// This function is called on panic.
#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}
