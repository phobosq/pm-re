# Wave 1 Experiment Sequence

Run 1 (Baseline): --vmr=0, fixed window
Run 2 (Active-1): --vmr=100, fixed window
Run 3 (Active-2): --vmr=50, fixed window for quantitative diff

Between Run 1 and Run 2:
- verify parser anchors and expected branch divergence

Between Run 2 and Run 3:
- confirm transport wrapper consistency and IOCTL repeatability

Go/No-Go after Run 3:
- if parser plus transport plus payload-diff chain is stable: vmr confirmed
- else keep hypothesis open and iterate setup

