# Avatar Generation

> AI Laboratory capability for generating talking-avatar and lip-synchronised video outputs.

## Architectural position

This module belongs to `ENGINEERING/LABS/AI_LAB` because it experiments with AI-based visual and speech-driven generation.

It is an optional AI capability, not part of BRAHMA CORE or the BRAHMA Runtime. The SadTalker implementation is treated as a replaceable backend adapter so that other avatar-generation engines can be evaluated later without changing BRAHMA's core architecture.

## Initial objective

Establish a reproducible Google Colab workflow that:

1. prepares a compatible Python/CUDA environment;
2. obtains the SadTalker source code;
3. restores model checkpoints from persistent storage;
4. validates user-provided image and audio inputs;
5. generates a talking-avatar video;
6. stores outputs and execution logs in persistent storage.

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

Colab's `/content` directory is temporary and can disappear when a runtime is reclaimed or reset. Therefore:

- GitHub stores notebooks, scripts, documentation, and configuration.
- Persistent storage (Google Drive or another user-controlled storage provider) stores model checkpoints and media.
- A bootstrap workflow reconstructs the temporary Colab environment from versioned setup instructions.
- Each stage must verify the existence and integrity (file size and preferably SHA-256) of restored assets before proceeding.

A successful copy command alone is not considered a verified backup. The workflow must list the destination files and compare checksums where practical.

## Security and privacy

- Never commit personal images, voice recordings, generated videos, API keys, access tokens, or private Drive paths.
- Keep storage containing a child's photo or voice private and share it only when necessary.
- Do not expose model downloads or generated media through public repository assets.
- Review third-party model and source licenses before redistribution or commercial use.

## Implementation status

**Phase 0 — Architecture and persistence design.** The module boundary and storage rules are documented. The reproducible Colab bootstrap, environment lock, validation scripts, and inference workflow are to be added and tested incrementally.

## Next milestones

1. Add a Colab bootstrap script with explicit Python, PyTorch, CUDA, and system-package checks.
2. Add a persistent-storage restore/verify script for checkpoints and input assets.
3. Add input validation and audio conversion helpers.
4. Add an inference wrapper based on the actual SadTalker CLI options in the pinned source revision.
5. Save the tested notebook and a run manifest (versions, commands, checksums, timestamps) to GitHub without personal media or model binaries.
