H01: vmr_parser_path_exists
status: open
evidence: docs show -vmr option; binary direct token visibility weak
falsification_test: no parser comparator/store path found after dynamic compare tracing
next_experiment: breakpoint on argument compare and track config writes
confidence: hypothesis

H02: vmr_uses_low_level_transport
status: open
evidence: EIO.dll exports include MMIO-like read/write symbols; DeviceIoControl patterns present
falsification_test: vmr consumer path does not reach IOCTL/MMIO/NVAPI write functions
next_experiment: vmr A/B trace with transport API breakpoints and stack correlation
confidence: strongly_inferred

H03: straps_vmt_depend_on_same_transport_family
status: open
evidence: docs cluster straps/vmt/vmr under timing controls
falsification_test: straps/vmt consumers use unrelated transport chain
next_experiment: after vmr confirmation, map straps/vmt consumer call graph
confidence: hypothesis

H04: straps_vmt_share_vmr_transport_family
status: open
evidence: docs grouping + shared low-level transport surface
falsification_test: straps/vmt bypass vmr transport family
next_experiment: post-vmr gate A/B straps and vmt traces
confidence: hypothesis

H05: vmt_is_staged_parameterization
status: open
evidence: multiple vmt knobs suggest staged fields
falsification_test: each vmt maps to isolated independent write path
next_experiment: compare vmt1/2/3 pre-transport state transitions
confidence: hypothesis

H06: vmr_transport_candidates_prioritized_by_pdata
status: active
evidence: transport shortlist ranges 0x001C4010..0x001C44E3, 0x001C1BB0..0x001C1CE0, 0x001C6BB0..0x001C6C93, 0x0028CA90..0x0028CB6B
falsification_test: none of shortlisted ranges participates in vmr path after code-flow validation
next_experiment: inspect these ranges first in disassembler and trace upward callers
confidence: strongly_inferred

H07: vmr_parser_entry_small_dispatcher
status: active
evidence: compact function range 0x003E16B0..0x003E16D5 contains GetCommandLineA/W
falsification_test: function is unrelated to CLI parsing after local code analysis
next_experiment: inspect immediate callers and downstream compare/config stores
confidence: strongly_inferred
