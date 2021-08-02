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
       Write-Host "$server  IMS $WorkingDir folder is not empty"
       Write-Output "$server  IMS $WorkingDir folder is not empty"
       Write-Output "False"
    }

   else  {                    
         Write-Host "$server  IMS $WorkingDir folder is  empty"
         Write-Output "$server  IMS $WorkingDir folder is  empty"
          Write-Output "True"
         }

}
clear


function CheckFolder1 {

param(
        [Parameter(Mandatory=$true,Position=0,ValueFromPipeline=$true)]
        [string]$server,

        [Parameter(Mandatory=$true,Position=0,ValueFromPipeline=$true)]
        [string]$WorkingPath,
        [Parameter(Mandatory=$true,Position=0,ValueFromPipeline=$true)]
        [string]$WorkingDir
        
        
    )

$directoryInfoDp = Get-ChildItem $WorkingPath -Exclude *bat,  *old, *log, *temp | Measure-Object




 
 if ($directoryInfoDp.count -ge 1) 
    {
       Write-Host "$server  IMS $WorkingDir folder is not empty"
       Write-Output "$server  IMS $WorkingDir folder is not empty"
       Write-Output "False"
    }

   else  {                    
         Write-Host "$server  IMS $WorkingDir folder is  empty"
         Write-Output "$server  IMS $WorkingDir folder is  empty"
          Write-Output "True"
         }

}
clear



$output = Checkfolder -server "ODEFMF01" -WorkingPath "\\odefmf01\ssi_prod\IMS" -WorkingDir "ODEFMF01 IMS" 
$output1 = Checkfolder1 -server "ODEFMA08" -WorkingPath "\\odefma08\IMS" -WorkingDir "ODEFMA08 IMS" 


   
 
  $output  | Out-File -FilePath C:\Users\MASARYK-A\Desktop\DevOps\IMS.txt
  $output1 | Out-File -FilePath C:\Users\MASARYK-A\Desktop\DevOps\IMS.txt -Append
  
  