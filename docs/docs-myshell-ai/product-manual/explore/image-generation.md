# Image Generation

Introduction to MyShell's image generation function: From natural language image generation to parameter image generation.

## Natural Language Image Generation

MyShell's natural language image generation allows users to obtain high-quality images at extremely low cost.

You only need to provide a demand, a sentence, or even a word, and the MyShell image generation series of robots can generate high-quality images for you.

To achieve high-quality and fast image generation, MyShell uses the following technical solutions:

-   At the algorithm level, we use large language models (LLMs) to assist users in semantic understanding, so that natural language can be effectively transformed into the complex parameters required by Stable Diffusion; in addition, we have implemented model scheduling, which can call the corresponding checkpoint according to the image style required by the user, demonstrating preliminary scheduling capabilities.
    
-   At the engineering level, we use an asynchronously generated structure to ensure the usability of the image service, making image generation less likely to be interrupted and enhancing the robustness of the service.
    

**Find five robots with specific uses and a large number of robots with special image styles** [**here**](https://app.myshell.ai/explore/search?filter=image_gen)**.**

### Quick start guide

Taking the "Image Magician" and "Avatar Magician" bots as examples, the following use cases can experience the ability of natural language image generation.

When you use natural language to generate images, we recommend that you provide three types of information:

-   **Image content**: This determines the main subject and background elements of your picture.
    
-   **Image style**: This determines which stable diffusion checkpoint the robot will call for you to draw, and is closely related to the artistic style of the image.
    
-   **Image usage**: This determines the size and content quality enhancement template of your picture. Currently, we recommend that you use "Avatar", "Portrait", and "Banner". The first two usages are convenient for you to draw high-quality portraits for use as avatars and photo wall decorations, while the latter is good at drawing landscapes as banner accessories.
    

## ## **Parameters**

In addition to natural language image generation, MyShell also enables advanced users to adjust image generation through parameters.

### **Prompt**

-   Description: The main text instruction that guides the image generation process. It's the core input that the AI uses to generate images.
    

Enter a descriptive narrative or keywords that closely detail the desired outcome. The more specific and descriptive the prompt, the more accurate the generated image will be.

### **Negative Prompt**

-   Description: Instructions specifying what should be excluded from the generated image. This helps in refining the output by avoiding unwanted elements.
    

List elements you wish to avoid in the output, such as "Watermark, signature, motion blur, extra fingers, bad anatomy." This feature is particularly useful for achieving more precise results and avoiding common pitfalls in image generation.

### **Model**

-   Description: The image model used for generating the image. Different models may have different capabilities and specialties.
    
-   Usage: Choose from the available options. The choice of model can significantly impact the style and quality of the output.
    

MyShell supports a large number of drawing models, here are some of the most popular ones.

#### Popular Models

### **Image Size**

-   Description: The dimensions of the generated image. This determines the resolution and aspect ratio of the output.
    

In bot creation, we recommend the following sizes for you:

-   Avatar: 750\*750
    
-   Banner: 1000\*200
    
-   Photo wall: 750\*750, 600\*800, ...
    
-   Immersive background: 1000\*840, 1500 \* 1260, 2000\*1680...
    

### **Image Number**

-   Description: The number of images to generate in a single run. This allows for the creation of multiple variations of an image based on the same prompt.
    

Select a number to generate multiple variations. This is useful for exploring different interpretations of the same prompt. Maximum support for ten images.

## **Advanced Parameters**

### **Sampling Method**

-   Description: The algorithm that drives the transformation from noise to image. Different sampling methods can produce different styles and qualities of images.
    

Select from options like Euler, which affect the visual style and coherence. The choice of sampler can influence the smoothness, color distribution, and edge definition in the generated images. Different sampling methods will produce different image effects, and we recommend that you try them out.

### **Sampling Steps**

-   Description: The number of iterations in the image refinement process. This affects how gradually the image is developed from the initial noise.
    

Higher numbers typically result in more detailed images. However, too many steps might not always improve quality and can increase processing time.

### **CFG Scale**

-   Description: Balances between the AI's creativity and adherence to the prompt. It's a scale that determines how closely the AI should follow the prompt.
    

A higher scale makes the AI closely follow the prompt, while a lower scale allows more creative freedom. This parameter is crucial for controlling the balance between fidelity to the prompt and artistic interpretation.

### **Seed**

-   Description: Initializes the random noise pattern, affecting image uniqueness. It's a value that determines the starting point of the image generation process.
    

A specific seed value ensures reproducibility of results. This is useful for creating consistent results or variations of the same image. When you enter -1, a random seed will be used.