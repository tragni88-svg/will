use linked_list_allocator::LockedHeap;

#[global_allocator]
static ALLOCATOR: LockedHeap = LockedHeap::empty();

pub const HEAP_SIZE: usize = 100 * 1024; // 100 KiB

static mut HEAP_MEM: [u8; HEAP_SIZE] = [0; HEAP_SIZE];

pub fn init_heap() {
    unsafe {
        let heap_start = core::ptr::addr_of_mut!(HEAP_MEM) as usize;
        ALLOCATOR.lock().init(heap_start, HEAP_SIZE);
    }
}
