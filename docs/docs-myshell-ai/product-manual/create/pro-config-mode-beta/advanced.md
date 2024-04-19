# Advanced

## Event **Propagation**

Event propagation refers to the way an event moves through the state machine’s hierarchy. When an event is triggered, if the current state doesn't have a handler(transition) for it, the event is then passed up to the parent automata. This process continues up the chain until it either reaches an automata that can handle it or arrives at the root.

This feature is particularly advantageous for managing global transitions, as it allows a single handler at a higher-level state to respond to events from various child states, simplifying event management across the entire application.

## Special Events

Special events differ from user-defined events as they do not propagate to the parent when triggered.

-   `AtomicState` handles `"CHAT"` and `"ALWAYS"` events:
    
    -   `“CHAT”` occurs upon user input in instant messaging.
        
    -   `"ALWAYS"` ensures the state transitions immediately once its condition is met, following task execution.
        
    
-   `Automata` recognizes the `"DONE"` event:
    
    -   `"DONE"` is activated once any of the automaton's final states are reached.
        
    