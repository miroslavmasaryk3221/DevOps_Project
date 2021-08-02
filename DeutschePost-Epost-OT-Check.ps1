function CheckFolder {

param(
        [Parameter(Mandatory=$true,Position=0,ValueFromPipeline=$true)]
        [string]$server,

        [Parameter(Mandatory=$true,Position=0,ValueFromPipeline=$true)]
        [string]$WorkingPath,
        [Parameter(Mandatory=$true,Position=0,ValueFromPipeline=$true)]
        [string]$WorkingDir
        
        
    )

$directoryInfoDp = Get-ChildItem $WorkingPath | Measure-Object




 
 if ($directoryInfoDp.count -ge 1) 
    {
       Write-Host "$server  Deutsche-Post $WorkingDir folder is not empty"
       Write-Output "$server  Deutsche-Post $WorkingDir folder is not empty"
       Write-Output "False"
    }

   else  {                    
         Write-Host "$server  Deutsche-Post $WorkingDir folder is  empty"
         Write-Output "$server  Deutsche-Post $WorkingDir folder is  empty"
          Write-Output "True"
         }

}
clear
$Path = @(
          '\\ot\de-myfileservices\DeutschePost-ePost\work' 
          '\\ot\de-myfileservices\DeutschePost-ePost\Zip'
          '\\ot\de-myfileservices\DeutschePost-ePost\Proofed'
          '\\ot\de-myfileservices\DeutschePost-ePost\NotProofed'
          '\\ot\de-myfileservices\DeutschePost-ePost\Log'
          '\\ot\de-myfileservices\DeutschePost-ePost\GpG'
          '\\ot\de-myfileservices\DeutschePost-ePost\finished')

$Dir = @(        
                 '\\ot\de-myfileservices\DeutschePost-ePost\work'
                 '\\ot\de-myfileservices\DeutschePost-ePost\Zip'
                 '\\ot\de-myfileservices\DeutschePost-ePost\Proofed'
                 '\\ot\de-myfileservices\DeutschePost-ePost\NotProofed'
                 '\\ot\de-myfileservices\DeutschePost-ePost\Log'
                 '\\ot\de-myfileservices\DeutschePost-ePost\GpG'
                 '\\ot\de-myfileservices\DeutschePost-ePost\finished')
$array = 0,1,2,3,4,5,6 

$output = Checkfolder -server "ODEFMF01" -WorkingPath "\\odefmf01\ExtPrint_Prod" -WorkingDir "ExtPrintProd" 

$output1=foreach ($i in $array) 
{
$check1 = $Path[$i]
$check = $Dir[$i].split('\')[5]

      Checkfolder -server "ODEFMA08" -WorkingPath "$check1" -WorkingDir "$check" 
   
 }
  $output  | Out-File -FilePath C:\Users\MASARYK-A\Desktop\DevOps\Dpe_Post.txt
  $output1 | Out-File -FilePath C:\Users\MASARYK-A\Desktop\DevOps\Dpe_Post.txt -Append
  