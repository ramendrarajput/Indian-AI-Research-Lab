# Avatar Generation

> AI Laboratory capability for generating talking-avatar and lip-synchronised video outputs.

## Architectural position

This module belongs to `ENGINEERING/LABS/AI_LAB` because it experiments with AI-based visual and speech-driven generation.

It is an optional AI capability, not part of BRAHMA CORE or the BRAHMA Runtime. SadTalker is treated as a replaceable backend so other avatar-generation engines can be evaluated later without changing BRAHMA's core architecture.

## Current Colab workflow

The first reproducible SadTalker notebook is available here:

[`BRAHMA_SadTalker_Verified_Workflow.ipynb`](notebooks/BRAHMA_SadTalker_Verified_Workflow.ipynb)

The notebook documents the successful setup path used in Colab:

1. T4 GPU runtime verification.
2. Miniconda3 with Python 3.8.20.
3. PyTorch 2.0.1, torchvision 0.15.2, torchaudio 2.0.2 and CUDA 11.8.
4. OpenTalker/SadTalker source and Python requirements.
5. Four primary SadTalker model checkpoints.
6. Image/audio input checks and MP3-to-16 kHz mono WAV conversion.
7. 512-resolution inference using crop preprocessing.
8. Local MP4 preview and direct download to the user's computer.

**Validation note:** The inference command completed successfully in the working Colab session (`return code: 0`) and an MP4 was generated and played back. The notebook is an ordered reconstruction of those successful steps; a fresh-runtime end-to-end rerun is still recommended when validating future changes.

## Directory layout

```text
AVATAR_GENERATION/
├── README.md
├── .gitignore
├── notebooks/       # Reproducible Colab notebooks (code/config only)
├── scripts/         # Setup, validation, restore and inference helpers
├── configs/         # Versioned, non-secret configuration
├── docs/            # Setup notes, compatibility and decisions
├── checkpoints/     # Local model weights; never commit
├── inputs/          # Local user media; never commit
├── outputs/         # Generated media; never commit
└── logs/            # Runtime logs; never commit
```

Only source code, documentation, and non-sensitive configuration belong in Git. Model weights, personal photos, voice recordings, generated videos, credentials, and runtime caches must remain in private storage.

## Persistence strategy

Colab's `/content` directory is temporary and can disappear when a runtime is reclaimed or reset.

- GitHub stores notebooks, scripts, documentation, and non-sensitive configuration.
- Google Drive is used as the source for private input media and, when available, previously downloaded checkpoints.
- Missing model checkpoints are downloaded into Colab's temporary local storage by the notebook.
- Generated MP4 files are written to local Colab storage and downloaded directly to the user's computer. They are not uploaded to Drive by this workflow, avoiding failures when Drive storage quota is full.
- Download the final MP4 before ending the Colab session.
- Verify restored files before inference; add checksum verification as the workflow matures.

## Security and privacy

- Never commit personal images, voice recordings, generated videos, API keys, access tokens, or private Drive paths.
- Keep storage containing a child's photo or voice private and share it only when necessary.
- Do not expose model downloads or generated media through public repository assets.
- Review third-party model and source licenses before redistribution or commercial use.

## Implementation status

**Phase 1 — Initial reproducible notebook committed.** The ordered Colab notebook captures the environment, checkpoint, input preparation, inference, preview, and local-download steps used in the successful SadTalker run.

## Next milestones

1. Re-run the notebook from a fresh Colab runtime to validate end-to-end reproducibility.
2. Pin the SadTalker source revision and record dependency versions in a run manifest.
3. Add SHA-256 checksums for model checkpoints and restored inputs.
4. Extract reusable setup, validation, audio conversion, and inference helpers into `scripts/`.
5. Evaluate optional face enhancement and alternative avatar-generation backends independently of BRAHMA Core.
