# Transition

The `Transition` type can be one of the following:

-   `string`: In this simplest case, the bot will transition to the provided target state.
    
-   `TransitionCase`: The bot will transition to the target state only if the `condition` is evaluated as `true`.
    

The capability for a state to transition to any other state, including itself, hinges on being able to reference a target state, which can be done through either absolute indexing or relative indexing. Here's a bit more detail:

-   **Relative Indexing:** This method allows navigation amongst states in relation to the current state:
    
    -   `sibling` refers to another state at the same level as the current one.
        
    -   `.child` specifies a sub-state of the current state.
        
    -   `sibling.child.grandchild` indicates a more complex path from a state at the same level to a grandchild state.
        
    
-   **Absolute Indexing:** This approach uses a unique identifier to directly reference any state, regardless of the current state:
    
    -   `#id` directly points to a state with the specified identifier.
        
    -   `#id.child` combines the use of an identifier with relative paths to specify a state that is a child of the identified state.
        
    

This structure provides great flexibility in the flow control within a bot, permitting intricate navigation across the states depending on the desired bot behavior or user interactions.

`TransitionCase`

| Field's Name | Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
target

 | 

string (Optional)

 | 

The target state to which the bot will transition. If not specified, the bot will transition to the current (self) state. Applies to TransitionCase type only.

 | 

"next\_state"

 |
| 

condition

 | 

BoolExpression (Optional)

 | 

A condition that must be evaluated as true for the bot to transition to the target state. If not specified, the condition is treated as true. Applies to TransitionCase type only.

 | 

 |
| 

target\_inputs

 | 

`Object` (Optional)

 | 

Specify the value for the inputs of target state. It will override the default value of the input, but not the value of the input.

 | 

 |

`TransitionCase[]`

The bot will evaluate the conditions of each `TransitionCase` in the given array one by one. It will transition to the target state of the first `TransitionCase` whose `condition` is satisfied.