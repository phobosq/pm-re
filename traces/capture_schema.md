# Trace Capture Schema

## CSV Columns
- timestamp_utc: ISO 8601, 100 us granularity
- event_type: CreateFileW|CreateFileA|DeviceIoControl|LoadLibrary|GetCommandLineW|CompareStringW|VirtualAlloc|other
- function_rva: RVA in PhoenixMiner payload, linked to function index
- control_code: DeviceIoControl code in hex
- buffer_first_512b: hex string, no whitespace
- retval: 32-bit hex
- ntstatus: 32-bit hex when available
- stack_depth: integer
- event_sequence_id: monotonically increasing integer
- evidence_link: claim id in reports/evidence_matrix.csv

## Notes
- Keep run window fixed for baseline and active runs.
- Capture exactly the same API set in each run.
- Do not promote to confirmed without parser-to-transport causal chain.

