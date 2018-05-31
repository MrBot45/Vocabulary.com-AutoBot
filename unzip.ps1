Add-Type -AssemblyName System.IO.Compression.FileSystem
function Unzip
{
    param([string]$zipfile, [string]$outpath)

    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
}

$path = [System.IO.Directory]::GetCurrentDirectory() + "\ffmpeg-4.0-win32-static.zip"
echo $path

Unzip $path "C:\ffmpeg2"