$ppt = New-Object -ComObject PowerPoint.Application
$pres = $ppt.Presentations.Add([Microsoft.Office.Core.MsoTriState]::msoTrue)
$slide = $pres.Slides.Add(1, 12)
$tb = $slide.Shapes.AddTextbox(1, 100, 100, 500, 100)
$tb.TextFrame.TextRange.Text = "SAMVEDNA AI TEST"
$pres.SaveAs("C:\Users\ACER\Downloads\test_ppt.pptx")
$pres.Close()
$ppt.Quit()
Write-Host "SUCCESSFULLY CREATED PPTX"
