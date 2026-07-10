def IT_2_Image():
    import torch
    from diffusers import AutoPipelineForImage2Image
    from diffusers.utils import make_image_grid, load_image
    pipeline = AutoPipelineForImage2Image.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
    )
    pipeline.enable_model_cpu_offload()

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "pdf"])
    init_image = ""
    init_image = Image.open(uploaded_file) 
    st.image(init_image, caption="Uploaded Image.", use_column_width=True)
    if uploaded_file is not None:
            prompt = st.text_input("Enter your prompt:")
            if prompt:
                image = pipeline(prompt, image=init_image).images[0]
                make_image_grid([init_image, image], rows=1, cols=2)

def Text_2_Image2():
    client = InferenceClient("stabilityai/stable-diffusion-3.5-large",token=os.environ.get("HUGGING_FACE_API_KEY"))
    prompt = st.text_input("Enter your prompt:")
  # output is a PIL.Image object
    if st.button("Generate Image"):   
     with st.spinner(text='Wait...I am generating image'):
      image = client.text_to_image(prompt)
      #print(image)
      st.image(image)
      #image.show()
      st.success("Done")

def Image_2_Image_Overlaping1():

    from diffusers import DiffusionPipeline
    pipe = DiffusionPipeline.from_pretrained()#"Lykon/absolute-reality-1.6525-inpainting")#("yisol/IDM-VTON")
    prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
    with st.sidebar:
         #prompt = st.text_input("Ask anything about the image")  
         uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "pdf"])
         image = ""
         if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image.", use_column_width=True)
    image = pipe(prompt).images[0]

def Image_2_Image_Overlaping():
    from diffusers import AutoPipelineForInpainting, DEISMultistepScheduler
    import torch
    from diffusers.utils import load_image

    pipe = AutoPipelineForInpainting.from_pretrained('lykon/absolute-reality-1.6525-inpainting', torch_dtype=torch.float16, variant="fp16")
    pipe.scheduler = DEISMultistepScheduler.from_config(pipe.scheduler.config) 
    pipe = pipe.to("cuda")

    img_url = "https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png"
    mask_url = "https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png"

    image = load_image(img_url)
    mask_image = load_image(mask_url)


    prompt = "a majestic tiger sitting on a park bench"

    generator = torch.manual_seed(33)
    image = pipe(prompt, image=image, mask_image=mask_image, generator=generator, num_inference_steps=25).images[0]  
    image.save("./image.png")
