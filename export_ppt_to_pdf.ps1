$ErrorActionPreference = "Stop"
Write-Host "[*] Starting PowerPoint COM to export PDF..."

$srcPptx = "D:\SAMVEDNA\SAMVEDNA_AI_SIH_Final_Presentation.pptx"
$dstPdf1 = "D:\SAMVEDNA\SAMVEDNA_AI_SIH_Final_Presentation.pdf"
$dstPdf2 = "C:\Users\hp\Downloads\SAMVEDNA_AI_SIH_Final_Presentation.pdf"
$dstPptx2 = "C:\Users\hp\Downloads\SAMVEDNA_AI_SIH_Final_Presentation.pptx"

$ppt = New-Object -ComObject PowerPoint.Application
$pres = $ppt.Presentations.Open($srcPptx, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)

# Export PDF
$pres.SaveAs($dstPdf1, 32)
Write-Host "[+] Exported PDF to: $dstPdf1"

$pres.SaveAs($dstPdf2, 32)
Write-Host "[+] Exported PDF to: $dstPdf2"

# Copy PPTX to Downloads as well
Copy-Item -Path $srcPptx -Destination $dstPptx2 -Force
Write-Host "[+] Copied PPTX to: $dstPptx2"

$pres.Close()
$ppt.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($ppt) | Out-Null
Write-Host "[+] Export Complete!"
