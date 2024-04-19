# LLM Function Module

`LLMFunctionModule` is a module used for executing LLM function calls.

Function calls can be seen as a formatting wrapper provided by LLM (currently only supports OpenAI series models), allowing parameters to be input via JSON, and outputting a serial JSON as we defined in `function_parameters`.

Reference:

-   [https://www.promptingguide.ai/applications/function\_calling](https://www.promptingguide.ai/applications/function_calling)
    
-   [https://platform.openai.com/docs/api-reference/chat/create](https://platform.openai.com/docs/api-reference/chat/create)
    

The module input can be specified by each parameter in the config.

The output of the module is a JSON object, which includes the LLM return results and will be automatically output to the state machine output in the form of key-value pairs.

`LLMFunctionConfig` is similar to `LLMConfig`. It only differs by:

-   the lack of `output_name`
    
-   three fields starting with `function_`, which are vital for the LLMFunctionModule as they control the function behavior. They will be placed in the tools field of the LLM Request Body.
    

`LLMFunctionConfig`

| Field's Name | JSON Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
function\_name

 | 

string (Required)

 | 

Specifies the name of the function in LLMFunctionConfig.

 | 

'get\_current\_weather'

 |
| 

function\_description

 | 

string (Required)

 | 

Provides a description of the function in LLMFunctionConfig.

 | 

'Get the current weather in a given location'

 |
| 

function\_parameters

 | 

FunctionParameter\[\] (Required)

 | 

Specifies the parameters of the function in LLMFunctionConfig.

 | 

\[{name: 'city', type: 'string', description: 'The city, e.g. San Francisco, CA'}\]

 |

`FunctionParameter`

| Field's Name | JSON Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
name

 | 

string (Required)

 | 

Specifies the name of the function parameter in FunctionParameter.

 | 

'city'

 |
| 

type

 | 

string (Required)

 | 

Specifies the type of the function parameter in FunctionParameter.

 | 

'list', 'string' or 'number'

 |
| 

description

 | 

string (Required)

 | 

Provides a description of the function parameter in FunctionParameter.

 | 

'The city, e.g. San Francisco, CA'

 |