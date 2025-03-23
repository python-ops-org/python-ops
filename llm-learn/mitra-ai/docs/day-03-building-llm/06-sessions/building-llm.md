
```

Outcome: Understand the underlying modules of LLMs are built and what they can and cannot achieve.

Objective: Explain how LLMs are built and can be used to solve various problems in NLP and cover the transformer architecture.

Key Activities:

LLM settings
Perplexity metric
Temperature and top-k predictions
Memory and continuation
The transformer model and how it works
Attention and various uses


```

50-55
-----



OpenAI Whisper
--------------




| **Point**                            | **Description**                                                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1. Automatic Speech Recognition** | Whisper is an open-source neural network by OpenAI designed for speech-to-text transcription, translation, and language identification.                     |
| **2. Multilingual Support**         | Trained on 680,000 hours of data, Whisper supports multiple languages and delivers high transcription accuracy across diverse languages and accents.       |
| **3. Noise Robustness**             | Whisper performs well even in noisy environments, handling background sounds, varied accents, and low-quality audio inputs effectively.                     |
| **4. Open Source & Extensible**     | Fully open-source and available on GitHub, Whisper can be integrated or fine-tuned for use in apps like voice assistants, transcription tools, and more.    |


```

LLMs - The cutting edge

- ALiBi - positional encoding
- Flash Attention
- Sparse Attention
- Multi-Query Attention vs Multi-head Attention
- Conditional Computation
- Mixed-precision training
- Model Quantization

```

Quantization - Less memory footprint
------------------------------------


| **Aspect**                   | **Description**                                                                                          |
|-----------------------------|----------------------------------------------------------------------------------------------------------|
| **Reduced Model Size**      | Quantization converts high-precision weights (e.g., FP32) to lower precision (e.g., INT8), reducing memory usage significantly. |
| **Faster Inference**        | Lower bit-width arithmetic operations lead to faster computation and lower latency during inference.     |
| **Hardware Optimization**   | Enables deployment on resource-constrained devices like mobile phones, edge devices, and microcontrollers.|


Flash Attention - Better than O(N^2)
-------------------------------------

| **Aspect**                     | **Description**                                                                                                      |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Efficient Memory Usage**     | Flash Attention reduces memory overhead by fusing operations and avoiding redundant memory reads/writes.            |
| **Sub-Quadratic Time Complexity** | Unlike standard attention with O(N²) complexity, Flash Attention uses optimized kernels for faster computation.     |
| **GPU-Accelerated**            | Designed to fully utilize GPU memory bandwidth and parallelism, significantly improving training and inference speed.|
| **Scalable for Long Sequences**| Allows handling of longer input sequences efficiently, making it ideal for large language models and transformers.   |


Alibi - Variable context windows
---------------------------------

| **Aspect**                       | **Description**                                                                                                   |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **Context-Aware Biasing**        | Alibi (Attention with Linear Biases) introduces position-based biases to the attention scores without embeddings. |
| **Supports Variable Window Sizes** | Enables models to handle inputs with variable context lengths without retraining positional encodings.           |
| **Lightweight & Efficient**      | Avoids the need for absolute or relative position embeddings, reducing overhead and improving generalization.     |
| **Improves Long-Context Handling** | Enhances transformer performance on tasks requiring long-term dependencies by biasing attention distribution.     |


LoRA – Efficient LLM Fine-tuning
---------------------------------

| **Aspect**                        | **Description**                                                                                                  |
|----------------------------------|------------------------------------------------------------------------------------------------------------------|
| **Parameter-Efficient Tuning**   | LoRA (Low-Rank Adaptation) freezes the original model weights and trains only a few added low-rank matrices.     |
| **Reduced Resource Usage**       | Significantly lowers GPU memory and compute requirements compared to full fine-tuning.                           |
| **Modular and Scalable**         | LoRA modules can be easily added or removed, enabling rapid experimentation and multi-task learning.             |
| **Maintains Base Model Integrity**| Original model weights remain unchanged, ensuring stability and reusability across different applications.        |



```

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load audio file
y, sr = librosa.load('sample.wav', sr=None)  # Replace with your file path

# Generate Mel spectrogram
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)

# Convert to log scale (dB)
S_dB = librosa.power_to_db(S, ref=np.max)

# Plot
plt.figure(figsize=(10, 4))
librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel Spectrogram')
plt.tight_layout()
plt.show()


```















































