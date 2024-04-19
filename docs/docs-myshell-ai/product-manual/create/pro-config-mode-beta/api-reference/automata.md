# Automata

`Automata` shares many fields with `AtomicState`. It differs by:

-   the lack of `properties.is_chat_allowed` and `tasks` fields.
    
-   the different special event it can handle
    
-   `initial` , `states` and `context` fields.
    

`Automata` (only difference)

| Field's Name | Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
type

 | 

"automata" (Optional)

 | 

Indicates the type of structure, which here would be 'automata'.

 | 

'automata'

 |
| 

context

 | 

Object (Optional)

 | 

These are variables that are shared among all child states. These can be of type Variable. The key should be in lowercase, snake\_case format.

 | 

{ "prompt": { "type": "text" } }

 |
| 

context\[variable\_name\]

 | 

Variable (Required)

 | 

Variable can have an initial value or just a specified type.

 | 

{ "type": "text", value: "Welcome" }

 |
| 

initial

 | 

string (Required)

 | 

This is the name of the initial state that the automata should start in.

 | 

'initial\_state'

 |
| 

states

 | 

Object (Required)

 | 

This holds all available states in the automata. Each state could be an AtomicState or Automata

 | 

 |
| 

transitions

 | 

Object (Optional)

 | 

Automata can trigger special events, including DONE.

 | 

 |