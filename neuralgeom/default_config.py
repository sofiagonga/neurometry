"""Default configuration for a run."""

import logging
from datetime import datetime
import torch
import os


os.environ["GEOMSTATS_BACKEND"] = "pytorch"
from geomstats.geometry.special_orthogonal import SpecialOrthogonal

run_name = "testing"

# Can be replaced by logging.DEBUG or logging.WARNING
logging.basicConfig(level=logging.INFO)

# Hardware
device = "cuda" if torch.cuda.is_available() else "cpu"


# Training
batch_size = 128
scheduler = False
log_interval = 20
checkpt_interval = 20
n_epochs = 120
learning_rate = 1e-3
sftbeta = 4.5
beta = 0.03
gamma = 10

# Dataset
dataset_name = "s1_synthetic"

if dataset_name == "experimental":
    expt_id = "34"  # hd: with head direction
    timestep_microsec = int(1e6)
    smooth = False
else:
    timestep_microsec, expt_id, smooth = [None for _ in range(3)]


if dataset_name == "s1_synthetic":
    distortion_func = "bump"
    n_times = 2000
    distortion_amp = 0.2
    radius = 1
    n_wiggles = 3
    embedding_dim = 2
    noise_var = 1e-3
    synthetic_rotation = SpecialOrthogonal(n=embedding_dim).random_point()
else:
    (
        n_times,
        distortion_amp,
        radius,
        n_wiggles,
        embedding_dim,
        noise_var,
        distortion_func,
        synthetic_rotation,
    ) = [None for _ in range(8)]

radius=1

# if dataset_name == "s2_synthetic":
#     distortion_func = "bump"
#     n_times = 2000
#     distortion_amp = 0.2
#     radius = 1
#     embedding_dim = 2
#     noise_var = 1e-3
# else:
#     (
#         n_times,
#         distortion_amp,
#         radius,
#         n_wiggles,
#         embedding_dim,
#         noise_var,
#         distortion_func,
#     ) = [None for _ in range(7)]


if dataset_name in ["images", "projected_images"]:
    img_size = 64

# Models
model_type = "neural_geom_vae"
encoder_width = 400
# decoder_width = 40
decoder_width = encoder_width
encoder_depth = 4
# decoder_depth = 4
decoder_depth = encoder_depth
latent_dim = 2
posterior_type = "hyperspherical"
gen_likelihood_type = "gaussian"

# Results
now = str(datetime.now().replace(second=0, microsecond=0))
results_prefix = f"{dataset_name}_{now}"
trained_model_path = None