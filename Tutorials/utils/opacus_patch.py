import torch

def apply_fsdp_patch():
    """
    Injects a dummy FSDPModule into PyTorch's namespace to prevent Opacus 
    from crashing during the backward pass in PyTorch 2.x environments.
    """
    try:
        import torch.distributed.fsdp
        # If FSDPModule is missing, create a harmless dummy class in its place
        if not hasattr(torch.distributed.fsdp, 'FSDPModule'):
            class DummyFSDPModule:
                pass
            torch.distributed.fsdp.FSDPModule = DummyFSDPModule
            print("🔧 FSDPModule dummy injected! Opacus compatibility secured.")
    except ImportError:
        pass # If distributed isn't installed at all, no patch is needed