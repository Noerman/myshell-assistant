# Module

The system currently supports a powerful customizable module to utilize any widget in MyShell workshop.

Other types of modules are essentially `AnyWidgetModule` without `widget_id`.

`SupportModule`

| Field's Name | JSON Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
module\_type

 | 

"AnyWidgetModule" | “LLMModule” | “LLMFunctionModule” | “TtsModule” | “GoogleSearchModule”｜ (Required)

 | 

The module type defines the module config.

 | 

 |
| 

module\_config

 | 

“AnyWidgetConfig" | “LLMConfig” | “LLMFunctionConfig” | “TTSConfig” | “GoogleSearchConfig” | (Required)

 | 

The configuration takes inputs and produces a result. All module\_config have a output\_name field for the execution result.

 | 

 |
| 

name

 | 

string (Optional)

 | 

The name of the module is primarily for identification and comprehension.

 | 

‘generate\_img\_for\_user\_reply’

 |