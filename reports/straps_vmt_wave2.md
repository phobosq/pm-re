# Straps/VMT Wave2 Hypothesis Draft (NVIDIA)

status: pre-transport-confirmation draft
evidence_policy: static-only claims remain strongly_inferred/hypothesis

## Preconditions (gate)
1. vmr parser->consumer path is mapped.
2. vmr transport path reaches DeviceIoControl/helper-driver interaction.
3. at least one vmr argument-to-transport causal chain is runtime-confirmed.

## Hypotheses
H04: straps and vmt1/2/3 reuse the same transport family as vmr
status: hypothesis
evidence: options are grouped in docs and low-level transport surface is shared globally
falsification: straps/vmt consumer bypasses DeviceIoControl/MMIO path used by vmr
next_experiment: A/B runs for straps and vmt values after vmr gate passes

H05: vmt fields map to staged parameterization before transport write
status: hypothesis
evidence: multiple vmt options imply multi-field or staged configuration
falsification: vmt options map directly to independent non-overlapping calls without shared staging
next_experiment: compare pre-transport state transitions for vmt1/vmt2/vmt3

H06: straps acts as preset selector while vmt fine-tunes subfields
status: hypothesis
evidence: documentation language suggests strap levels and optional fine controls
falsification: straps and vmt alter identical payload fields with no layering
next_experiment: differential payload analysis: straps-only vs vmt-only vs combined

## Planned artifacts after gate
- registers/vmt_field_map.csv (populate from runtime differentials)
- reports/straps_model.md
- traces/proof_straps_vmt.md

## Stop conditions
- no runtime confirmation of vmr transport => keep straps/vmt in hypothesis-only state
- unstable A/B traces => no promotion to confirmed
