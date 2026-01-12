# Setup script to add Hugging Face CLI to PATH permanently
# Run this once to add the Scripts directory to your user PATH

$scriptsPath = "$env:APPDATA\Python\Python313\Scripts"
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")

if ($currentPath -notlike "*$scriptsPath*") {
    [Environment]::SetEnvironmentVariable("Path", "$currentPath;$scriptsPath", "User")
    Write-Host "Successfully added Hugging Face CLI to PATH!" -ForegroundColor Green
    Write-Host "Please restart your terminal for changes to take effect." -ForegroundColor Yellow
} else {
    Write-Host "Hugging Face CLI is already in PATH." -ForegroundColor Green
}

Write-Host "`nYou can now use 'hf' command directly in new terminal sessions." -ForegroundColor Cyan
Write-Host "For current session, use: .\hf.ps1 <command>" -ForegroundColor Cyan

