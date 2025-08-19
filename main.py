import torch
import torchaudio
from einops import rearrange
import gradio as gr
import os
import uuid
import threading
import time
from stable_audio_tools import get_pretrained_model
from stable_audio_tools.inference.generation import generate_diffusion_cond

# PyTorch optimization for better performance
torch.backends.cudnn.benchmark = True
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True

device = "cuda" if torch.cuda.is_available() else "cpu"

# Global variables for model
model = None
model_config = None
sample_rate = None
sample_size = None
model_loading = False
model_ready = False

def load_model_in_background():
    """Loads model in background mode"""
    global model, model_config, sample_rate, sample_size, model_loading, model_ready
    
    model_loading = True
    print("Loading model in background...")
    
    try:
        # Download model
        model, model_config = get_pretrained_model("stabilityai/stable-audio-open-1.0")
        sample_rate = model_config["sample_rate"]
        sample_size = model_config["sample_size"]
        
        model = model.to(device)
        
        # Model optimization with torch.compile for acceleration
        print("Compiling model for optimization...")
        try:
            model = torch.compile(model, mode="reduce-overhead")
            print("Model compiled successfully!")
        except Exception as e:
            print(f"Model compilation failed: {e}, using original model")
        
        # Cache model in memory
        model.eval()
        print("Model loaded and ready!")
        
        model_ready = True
        model_loading = False
        
    except Exception as e:
        print(f"Error loading model: {e}")
        model_loading = False

def get_model_status():
    """Returns model loading status"""
    if model_ready:
        return "✅ Model ready! You can generate audio now."
    elif model_loading:
        return "⏳ Loading model... Please wait."
    else:
        return "❌ Model not loaded yet."

def generate_audio(prompt, seconds_total=15, steps=50, cfg_scale=7):
    """
    Optimized audio generation function
    """
    global model_ready
    
    # Check if model is ready
    if not model_ready:
        return None, "❌ Model is still loading. Please wait a moment and try again."
    
    # Optimized default parameters for fast generation
    if seconds_total > 20:
        print("Warning: Long audio generation (>20s) may be slow. Consider shorter duration for faster results.")
    
    # Set up text and timing conditioning
    conditioning = [{
        "prompt": prompt,
        "seconds_start": 0,
        "seconds_total": seconds_total
    }]
    print(f"Generating {seconds_total}s audio with {steps} steps...")

    try:
        # Generation with optimized settings
        with torch.no_grad():
            with torch.cuda.amp.autocast(dtype=torch.float16):  # Use mixed precision
                output = generate_diffusion_cond(
                    model,
                    steps=steps,
                    cfg_scale=cfg_scale,
                    conditioning=conditioning,
                    sample_size=sample_size,
                    sigma_min=0.3,
                    sigma_max=500,
                    sampler_type="dpmpp-3m-sde",  # One of the fastest samplers
                    device=device
                )

        # Optimized audio processing
        output = rearrange(output, "b d n -> d (b n)")
        
        # Fast normalization
        max_val = torch.max(torch.abs(output))
        if max_val > 0:
            output = output.div(max_val).clamp(-1, 1)
        
        # Convert to int16
        output = (output * 32767).to(torch.int16).cpu()

        # Generate filename
        unique_filename = f"output_{uuid.uuid4().hex}.wav"
        
        # Save
        torchaudio.save(unique_filename, output, sample_rate)
        print(f"Audio saved: {unique_filename}")
        
        return unique_filename, "✅ Audio generated successfully!"
        
    except Exception as e:
        return None, f"❌ Error generating audio: {str(e)}"

# Start model loading in background
model_thread = threading.Thread(target=load_model_in_background, daemon=True)
model_thread.start()

# Setting up the Gradio Interface
with gr.Blocks(title="Stable Audio Generator - Optimized Version") as demo:
    gr.Markdown("# 🎵 Stable Audio Generator - Optimized Version")
    gr.Markdown("Fast audio generation using Stable Audio Open 1.0. For best speed: use 15s duration and 50 steps.")
    
    # Model status
    status_text = gr.Textbox(
        value="⏳ Starting model loading...", 
        label="Model Status", 
        interactive=False
    )
    
    with gr.Row():
        with gr.Column():
            # Input parameters
            prompt_input = gr.Textbox(
                label="Prompt", 
                placeholder="Enter your text prompt here",
                lines=3
            )
            
            duration_slider = gr.Slider(
                5, 47, value=15, label="Duration in Seconds", step=1
            )
            
            steps_slider = gr.Slider(
                20, 200, value=50, step=5, label="Number of Diffusion Steps"
            )
            
            cfg_slider = gr.Slider(
                1, 15, value=7, step=0.1, label="CFG Scale"
            )
            
            generate_btn = gr.Button("🎵 Generate Audio", variant="primary")
        
        with gr.Column():
            # Output
            output_audio = gr.Audio(type="filepath", label="Generated Audio")
            output_text = gr.Textbox(label="Status", interactive=False)
    
    # Examples
    gr.Examples(
        examples=[
            ["Deep ambient focus music with rich low-end textures and evolving bass drones. Soft atmospheric layers, slow harmonic shifts, subtle sub-bass pulses, analog warmth, filtered noise. Inspired by early morning stillness and internal reflection. No melody, no vocals. Smooth, immersive, and grounding. Tempo: 60 BPM. Ideal for deep concentration, introspection, and flow state.", 15, 150, 13],
            ["A chilled, atmospheric lo-fi beat with warm vinyl crackle, soft piano chords, and mellow synth textures. Slow tempo. Dreamy and nostalgic mood. Subtle tape hiss and background ambiance. Suitable for studying, relaxing, or rainy late-night scenes.", 47, 180, 9],
            ["Recreate a gentle rainfall with distant thunder.", 15, 100, 7],
            ["Rock beat played in a treated studio, session drumming on an acoustic kit.", 15, 50, 7]
        ],
        inputs=[prompt_input, duration_slider, steps_slider, cfg_slider]
    )
    
    # Generation handler
    generate_btn.click(
        fn=generate_audio,
        inputs=[prompt_input, duration_slider, steps_slider, cfg_slider],
        outputs=[output_audio, output_text]
    )
    
    # Simple status update when loading page
    demo.load(
        fn=get_model_status,
        outputs=status_text
    )

# Launch interface
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8000)