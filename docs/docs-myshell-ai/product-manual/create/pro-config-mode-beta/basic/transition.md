# Transition

The `Transition` type can be one of the following:

-   `string`: In this simplest case, the bot will transition to the provided target state.
    
-   : The bot will transition to the target state only if the `condition` is evaluated as `true`.
    

The capability for a state to transition to any other state, including itself, hinges on being able to reference a target state, which can be done through either absolute indexing or relative indexing. Here's a bit more detail:

-   **Relative Indexing:** This method allows navigation amongst states in relation to the current state:
    
    -   `sibling` refers to another state at the same level as the current one.
        
    -   `.child` specifies a sub-state of the current state.
        
    -   `sibling.child.grandchild` indicates a more complex path from a state at the same level to a grandchild state.
        
    
-   **Absolute Indexing:** This approach uses a unique identifier to directly reference any state, regardless of the current state:
    
    -   `#id` directly points to a state with the specified identifier.
        
    -   `#id.child` combines the use of an identifier with relative paths to specify a state that is a child of the identified state.
        
    

This structure provides great flexibility in the flow control within a bot, permitting intricate navigation across the states depending on the desired bot behavior or user interactions.

The bot will evaluate the conditions of each `TransitionCase` in the given array one by one. It will transition to the target state of the first `TransitionCase` whose `condition` is satisfied.