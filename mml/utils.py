import torch
import numpy as np


def init_exp_backend(*, device: str = "cpu", seed: int = 42):
    torch.manual_seed(seed)
    np.random.seed(seed)

    if device is None:
        if torch.cuda.is_available():
            device = "cuda"
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False
        else:
            device = "cpu"
    else:
        if device == "cuda":
            if torch.cuda.is_available():
                torch.backends.cudnn.deterministic = True
                torch.backends.cudnn.benchmark = False
            else:
                device = "cpu"
    return torch.device(device)


def freeze_params(model):
    for param in model.parameters():
        param.requires_grad = False


def unfreeze_params(model):
    for param in model.parameters():
        param.requires_grad = True


def guassian_noise(mean: float, scale: float, shape: tuple) -> torch.Tensor:
    data = np.random.normal(mean, scale, shape)
    return torch.from_numpy(data).float()


def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


def gaussian_noise(mean: float, scale: float, shape: tuple) -> torch.Tensor:
    data = np.random.normal(mean, scale, shape)
    return torch.from_numpy(data).float()
