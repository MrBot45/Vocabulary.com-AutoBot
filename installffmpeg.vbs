Dim folderName
folderName = "./"

Dim fso
Set fso = CreateObject("Scripting.FileSystemObject")

Dim fullpath
fullpath = fso.GetAbsolutePathName(folderName)
Wscript.Echo "Downloading ffmpeg... (About 1 minute)"

' Set your settings
    strFileURL = "https://ffmpeg.zeranoe.com/builds/win32/static/ffmpeg-4.0-win32-static.zip"
    strHDLocation = fullpath + "/ffmpeg-4.0-win32-static.zip"

' Fetch the file
    Set objXMLHTTP = CreateObject("MSXML2.XMLHTTP")

    objXMLHTTP.open "GET", strFileURL, false
    objXMLHTTP.send()

If objXMLHTTP.Status = 200 Then
Set objADOStream = CreateObject("ADODB.Stream")
objADOStream.Open
objADOStream.Type = 1 'adTypeBinary

objADOStream.Write objXMLHTTP.ResponseBody
objADOStream.Position = 0    'Set the stream position to the start

Set objFSO = CreateObject("Scripting.FileSystemObject")
If objFSO.Fileexists(strHDLocation) Then objFSO.DeleteFile strHDLocation
Set objFSO = Nothing

objADOStream.SaveToFile strHDLocation
objADOStream.Close
Set objADOStream = Nothing
End if

Set objXMLHTTP = Nothing

Wscript.Echo "Done."
Wscript.Echo "Unzipping..."

'The location of the zip file.
ZipFile = fullpath + "/ffmpeg-4.0-win32-static.zip"
'The folder the contents should be extracted to.
ExtractTo="C:/ffmpeg2"

'If the extraction location does not exist create it.
Set fso = CreateObject("Scripting.FileSystemObject")
If NOT fso.FolderExists(ExtractTo) Then
   fso.CreateFolder(ExtractTo)
End If

Set fso = Nothing

Set objXMLHTTP = Nothing

Wscript.sleep(500)

Set shell = CreateObject("WScript.Shell")
shell.CurrentDirectory = fullpath
shell.Run "powershell unzip.ps1"

Wscript.sleep(5000)

Set shell = CreateObject("WScript.Shell")
shell.CurrentDirectory = fullpath
shell.Run "ffmpeg.bat"