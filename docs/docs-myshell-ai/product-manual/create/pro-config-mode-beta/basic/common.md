# Common

## Naming

For any user-defined variable or key names, we mandate the use of lowercase snake\_case format. Be aware that names incorporating any special characters, apart from periods (.), may result in unpredictable behaviour. Please review documentation to determine permissible use of periods (dots).

Uppercase names are exclusively reserved for specific, system-defined uses.

Field names in `AtomicState` and `Automata` are also reserved to prevents issues.

Example:

Copy

```
// correct:
{
  "context": {
    "prompt": {},
    "other_var": {}
  },
  "states": {
    "home_page": {},
    "chat": {
      "outputs": {
        "context.prompt": ""
      },
      "transitions": {
        "goto.some_place": {}
      }
    }
  }
}

// wrong:
{
  "context": {
    "outputs": {}, // use reserved field name
    "otherVar": {}, // not snake_case
    "$var": {}, // use special characters
    "a.b": {} // dots are not allowed for context
  },
  "states": {
    "inputs": {}, // use reserved field name
    "$var": {}, // use special characters
    "a.b": {}, // dots are not allowed for states
    "Chat": {
      // not snake_case
      "outputs": {
        "inputs.prompt": "" // use reserved field name as namespace
      },
      "transitions": {
        "..some_place": {} // consective dots are not allowed for transition keys
      }
    }
  }
}
```

## Expression

An `Expression` is a string using double curly brackets that allows you to reference accessible variables. You're free to use `Expression` anywhere a simple `string` is anticipated. When you're dealing with other fields requiring a different type, only expressions that result in the expected type are valid. Take for instance a `condition` field that demands a boolean—you can only pass boolean expressions like `"{{ 10 > 5 }}"` in that case.

The variables' accessibility is determined by the sequence in which `AtomicState` and `Automata` execute.

For `AtomicState`, the order is: `inputs` create variables, followed by `tasks`, then `outputs`, and finally, `render`, which does not create variables.

In `Automata`, variables are processed in this sequence: `inputs`, then `context`, followed by sequence of `states`, and lastly `outputs`.

The expression could be written in [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide), adhering to the [ECMAScript 5.1](https://262.ecma-international.org/5.1/) standard plus certain ECMAScript 6+ features.

The supported ECMAScript 6+ features include:

-   Block-scoped declaration (`let` and `const`)
    
-   ES6 class support
    
-   Arrow functions
    
-   Template literals
    
-   Destructuring assignments
    
-   Default function parameters
    
-   Spread and rest properties
    
-   Optional chaining
    
-   Nullish coalescing operator
    
-   Symbol
    
-   Map, Set
    
-   Proxy
    
-   Typed Arrays
    
-   Reflect
    
-   for-of
    
-   Optional catch binding
    