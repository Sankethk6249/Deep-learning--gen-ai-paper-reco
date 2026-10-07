"""
---
title: U-Net model for Denoising Diffusion Probabilistic Models (DDPM)
summary: >
  UNet model for Denoising Diffusion Probabilistic Models (DDPM)
---

# U-Net model for [Denoising Diffusion Probabilistic Models (DDPM)](index.html)

This is a [U-Net](../../unet/index.html) based model to predict noise
$\textcolor{lightgreen}{\epsilon_\theta}(x_t, t)$.

U-Net is a gets it's name from the U shape in the model diagram.
It processes a given image by progressively lowering (halving) the feature map resolution and then
increasing the resolution.
There are pass-through connection at each resolution.

![U-Net diagram from paper](../../unet/unet.png)

This implementation contains a bunch of modifications to original U-Net (residual blocks, multi-head attention)
 and also adds time-step embeddings $t$.
"""

import math
from typing import Optional, Tuple, Union, List
