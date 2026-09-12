$ppt = New-Object -ComObject PowerPoint.Application
$pres = $ppt.Presentations.Add([Microsoft.Office.Core.MsoTriState]::msoTrue)
$slide = $pres.Slides.Add(1, 12)
$tb = $slide.Shapes.AddTextbox(1, 50, 50, 400, 200)
$tr = $tb.TextFrame.TextRange
$tr.Text = "Line 1: bold part and normal part`r`nLine 2: another bold part and normal part"
Write-Host "Count:" $tr.Paragraphs().Count
for ($p = 1; $p -le $tr.Paragraphs().Count; $p++) {
    $para = $tr.Paragraphs($p)
    Write-Host "Para $($p):" $para.Text.Trim()
    $colonIdx = $para.Text.IndexOf(":")
    if ($colonIdx -gt 0) {
        $bold = $para.Characters(1, $colonIdx + 1)
        $bold.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
        Write-Host "  Bolding first" ($colonIdx + 1) "chars: " $bold.Text
    }
}
$pres.Close()
$ppt.Quit()
Write-Host "Test passed!"
