# System Check Script for Hugging Face Hub and CUDA

Write-Host "=== Hugging Face Hub Check ===" -ForegroundColor Cyan
$env:Path += ";$env:APPDATA\Python\Python313\Scripts"

$hfVersion = hf version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Hugging Face CLI version: $hfVersion" -ForegroundColor Green
    
    $whoamiOutput = hf auth whoami 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Hugging Face authentication: Working" -ForegroundColor Green
        Write-Host "  Logged in as: $whoamiOutput" -ForegroundColor Gray
    } else {
        Write-Host "✗ Hugging Face authentication: FAILED" -ForegroundColor Red
        Write-Host "  Error: $whoamiOutput" -ForegroundColor Yellow
        Write-Host "  Run: .\set_token.ps1 YOUR_TOKEN" -ForegroundColor Yellow
    }
} else {
    Write-Host "✗ Hugging Face CLI error" -ForegroundColor Red
}

Write-Host "`n=== CUDA Check ===" -ForegroundColor Cyan

# Check nvidia-smi
$nvidiaSmiOutput = nvidia-smi --query-gpu=driver_version,cuda_version --format=csv,noheader 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ NVIDIA Driver detected" -ForegroundColor Green
    Write-Host "  $nvidiaSmiOutput" -ForegroundColor Gray
} else {
    Write-Host "✗ NVIDIA Driver not found" -ForegroundColor Red
}

# Check nvcc
$nvccOutput = nvcc --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ CUDA Toolkit (nvcc) installed" -ForegroundColor Green
    $nvccOutput | Select-String -Pattern "release" | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }
} else {
    Write-Host "✗ CUDA Toolkit (nvcc) NOT installed" -ForegroundColor Red
    Write-Host "  nvcc is not in PATH" -ForegroundColor Yellow
    Write-Host "  Install CUDA Toolkit from: https://developer.nvidia.com/cuda-downloads" -ForegroundColor Yellow
}

# Check CUDA_PATH
if ($env:CUDA_PATH) {
    Write-Host "✓ CUDA_PATH environment variable: $env:CUDA_PATH" -ForegroundColor Green
} else {
    Write-Host "✗ CUDA_PATH environment variable: Not set" -ForegroundColor Yellow
}

# Check PyTorch CUDA
Write-Host "`n=== PyTorch CUDA Check ===" -ForegroundColor Cyan
$pythonCmd = 'import torch; print("PyTorch:", torch.__version__); print("CUDA available:", torch.cuda.is_available()); print("CUDA version:", torch.version.cuda if torch.cuda.is_available() else "N/A")'
$pytorchCheck = python -c $pythonCmd 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host $pytorchCheck
} else {
    Write-Host "✗ PyTorch not installed or error checking CUDA" -ForegroundColor Red
    Write-Host "  $pytorchCheck" -ForegroundColor Yellow
}
