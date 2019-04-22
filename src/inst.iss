
[Setup]
AppName=Calculator
AppVersion=1.0
DefaultDirName={pf}\Calculator
DefaultGroupName=Calculator
UninstallDisplayIcon={app}\Uninstall.exe
Compression=lzma2
SolidCompression=yes
OutputDir=userdocs:Inno Setup Examples Output
LicenseFile=LICENSE.txt

[Files]
Source: "Calculator_tk.exe"; DestDir: "{app}"
Source: "icon.ico"; DestDir: "{app}"
Source: "LICENSE.txt"; DestDir: "{app}";
;Source: "Readme.txt"; DestDir: "{app}"; Flags: isreadme

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Icons]
Name: {userdesktop}\Calculator; Filename: "{app}\Calculator_tk.exe"; IconFilename: "{app}\icon.ico"; Tasks: desktopicon;

[Run]
Filename: {app}\Calculator_tk.exe; Description: {cm:LaunchProgram,Calculator}; Flags: nowait postinstall skipifsilent