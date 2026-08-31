# vmr RVA Anchors (Static)

source: notes/phoenix_callsites_focus.csv

## GetCommandLineA (1 callsites)
- 0x003E16B4 -> KERNEL32.dll!GetCommandLineA

## GetCommandLineW (1 callsites)
- 0x003E16C1 -> KERNEL32.dll!GetCommandLineW

## CompareStringW (2 callsites)
- 0x003B16A7 -> KERNEL32.dll!CompareStringW
- 0x003F96DE -> KERNEL32.dll!CompareStringW

## CreateFileW (10 callsites)
- 0x0022487C -> KERNEL32.dll!CreateFileW
- 0x0028CACC -> KERNEL32.dll!CreateFileW
- 0x0028CC24 -> KERNEL32.dll!CreateFileW
- 0x0028D43A -> KERNEL32.dll!CreateFileW
- 0x003EEE65 -> KERNEL32.dll!CreateFileW
- 0x003FF82D -> KERNEL32.dll!CreateFileW
- 0x00404EE9 -> KERNEL32.dll!CreateFileW
- 0x00404F45 -> KERNEL32.dll!CreateFileW
- 0x0040515C -> KERNEL32.dll!CreateFileW
- 0x00405C79 -> KERNEL32.dll!CreateFileW

## DeviceIoControl (10 callsites)
- 0x001C1C37 -> KERNEL32.dll!DeviceIoControl
- 0x001C1CA0 -> KERNEL32.dll!DeviceIoControl
- 0x001C1D58 -> KERNEL32.dll!DeviceIoControl
- 0x001C1E0E -> KERNEL32.dll!DeviceIoControl
- 0x001C1EAC -> KERNEL32.dll!DeviceIoControl
- 0x001C1F3E -> KERNEL32.dll!DeviceIoControl
- 0x001C44A1 -> KERNEL32.dll!DeviceIoControl
- 0x001C6C1C -> KERNEL32.dll!DeviceIoControl
- 0x001C6C65 -> KERNEL32.dll!DeviceIoControl
- 0x0028CB1F -> KERNEL32.dll!DeviceIoControl

## DeviceIoControl Clusters
- cluster size=6 range=0x001C1C37..0x001C1F3E
- cluster size=1 range=0x001C44A1..0x001C44A1
- cluster size=2 range=0x001C6C1C..0x001C6C65
- cluster size=1 range=0x0028CB1F..0x0028CB1F

## Priority order for vmr hunt
1. parser anchor: GetCommandLineA 0x003E16B4 and GetCommandLineW 0x003E16C1
2. normalization/compare anchor: CompareStringW 0x003B16A7 and 0x003F96DE
3. transport anchor cluster: DeviceIoControl around 0x001C1C37..0x001C6C65
4. late transport anchor: DeviceIoControl 0x0028CB1F with CreateFileW near 0x0028CACC and 0x0028CC24
5. bridge/loading anchors: LoadLibrary*/GetProcAddress dense resolver region at low RVA
