# Script to set your Hugging Face token
# For setting ur token " .\set_token.ps1 <your-token> "

param(
    [Parameter(Mandatory=$true)]
    [string]$Token
)

$env:Path += ";$env:APPDATA\Python\Python313\Scripts"

# Set the token using the CLI
hf auth login --token $Token

Write-Host "Token has been set successfully!" -ForegroundColor Green
