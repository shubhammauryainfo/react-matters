#define BUFFER_SIZE 4

typedef struct {
    int buffer[BUFFER_SIZE];
    int in; // index for next item to produce
    int out; // index for next item to consume
    int count; // number of items in the buffer
} Buffer;

Buffer buffer;
Semaphore empty; // Counts empty slots in the buffer
Semaphore full;  // Counts filled slots in the buffer
Mutex mutex; // Protects access to buffer

Producer() {
    int widget;
    
    while (TRUE) {
        make_item(widget); // create a new item
        
        // Wait for an empty slot
        wait(empty);
        // Lock the buffer
        lock(mutex);
        
        // Produce an item
        buffer.buffer[buffer.in] = widget; // place item in buffer
        buffer.in = (buffer.in + 1) % BUFFER_SIZE; // circular increment
        buffer.count++;
        
        // Unlock the buffer
        unlock(mutex);
        // Signal that there is a new item
        signal(full);
    }
}

Consumer() {
    int widget;
    
    while (TRUE) {
        // Wait for a filled slot
        wait(full);
        // Lock the buffer
        lock(mutex);
        
        // Consume an item
        widget = buffer.buffer[buffer.out]; // get item from buffer
        buffer.out = (buffer.out + 1) % BUFFER_SIZE; // circular increment
        buffer.count--;
        
        // Unlock the buffer
        unlock(mutex);
        // Signal that there is an empty slot
        signal(empty);
        
        consume_item(widget); // consume the item
    }
}

// Initialization code
void init() {
    buffer.in = 0;
    buffer.out = 0;
    buffer.count = 0;
    empty = BUFFER_SIZE; // initially all slots are empty
    full = 0; // initially no slots are filled
    init_mutex(mutex);
}
