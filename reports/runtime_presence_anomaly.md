# Runtime Presence Anomaly Report

timestamp_utc: 2026-08-31T22:55:49.8384626Z
zip_file: C:\temp\pm\samples\work\PhoenixMiner_6.2c_Windows.zip
unpacked_root: C:\temp\pm\samples\work\unpacked\PhoenixMiner_6.2c_Windows
total_files_in_zip: 44
missing_after_unpack: 2

missing_files:
- IOMap64.sys (zip_size=34064)
- PhoenixMiner.exe (zip_size=8477696)

assessment:
- PhoenixMiner.exe present in zip but absent on disk after unpack.
- This can break runtime trace pipeline and must be treated as environment interference.
- Static analysis can continue from PhoenixMiner.exe.bin extracted directly from zip stream.

