$projectPath = $args[0]
$commitMessage = $args[1]
$branchName = $args[2]

Set-Location -Path $projectPath
git add .
git commit -m $commitMessage
git push origin $branchName