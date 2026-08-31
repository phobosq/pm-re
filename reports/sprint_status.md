# Sprint Status

- scope: NVIDIA vmr wave1, straps/vmt wave2
- sample_hash_status: confirmed
- inventory_status: completed
- pe_triage_status: updated with deep profile
- import_classification_status: enriched with function-level imports
- transport_status: helper-driver/MMIO path strongly inferred
- environment_interference: PhoenixMiner.exe and IOMap64.sys removed after unpack
- mitigation: static analysis from zip-stream .bin artifacts
- runtime_trace_status: pending isolated VM setup that preserves sample


- static_callsite_map: generated (1785 import callsites, 494 high-value)
- vmr_anchor_points: notes/vmr_rva_anchors.md
- local_runtime_status: blocked by Defender quarantine and missing debugger stack
- vmr_operational_block_filter: reports/vmr_candidate_blocks_operational.md
- wave2_plan: reports/straps_vmt_wave2.md
- current_best_transport_targets: B009,B015,B010,B011
- cloud_delegate_runbook: integrated
- new_runtime_templates: traces/experiment_matrix_vmr_wave1.csv; traces/capture_schema.md; reports/vmr_wave1_proof_template.md
- wave2_gate_doc: reports/straps_vmt_wave2_gates.md
