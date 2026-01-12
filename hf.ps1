# Hugging Face CLI wrapper script
# This script ensures the Hugging Face CLI is in PATH and runs the command

$scriptsPath = "$env:APPDATA\Python\Python313\Scripts"
if ($env:Path -notlike "*$scriptsPath*") {
    $env:Path += ";$scriptsPath"
}

& "$scriptsPath\hf.exe" $args

