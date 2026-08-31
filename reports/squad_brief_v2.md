# Squad Brief v2 (Address-Ranged)

scope: vmr wave1, straps/vmt wave2 (gated)

Helper 1 (Parser entry):
- focus range: 0x003E16B0..0x003E16D5
- task: verify cmdline acquisition path and immediate downstream branches
- artifact: notes/helper1_parser_entry.md

Helper 2 (Compare path A):
- focus range: 0x003B160C..0x003B16C8
- task: determine whether CompareStringW compares CLI tokens
- artifact: notes/helper2_compare_a.md

Helper 3 (Compare path B):
- focus range: 0x003F9610..0x003F96FF
- task: classify compare role and relation to parser/config path
- artifact: notes/helper3_compare_b.md

Helper 4 (Transport wrapper A):
- focus ranges: 0x001C4010..0x001C44E3 and 0x0028CA90..0x0028CB6B
- task: map CreateFile->DeviceIoControl wrapper shape and possible device handle flow
- artifact: notes/helper4_transport_wrappers.md

Helper 5 (IOCTL clusters):
- focus ranges: 0x001C1BB0..0x001C1CE0 and 0x001C6BB0..0x001C6C93
- task: classify repeated DeviceIoControl call pattern (probe/read/write hypothesis)
- artifact: notes/helper5_ioctl_clusters.md

Helper 6 (Evidence normalizer):
- inputs: reports/vmr_focus_functions.md, reports/vmr_candidate_blocks_operational.md, traces/transport_matrix.csv
- task: merge claims and ensure confidence taxonomy consistency
- artifact: reports/evidence_matrix.csv updates

PM gate:
- no straps/vmt semantic promotion before vmr transport confirmation.
- no confirmed label without direct code-flow or runtime evidence.
