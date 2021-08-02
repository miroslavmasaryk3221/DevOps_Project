function CheckAccount {

param(
        [Parameter(Mandatory=$true,Position=0,ValueFromPipeline=$true)]
        [string]$account
        
    )


Write-Output "$account"  
Get-ADUser $account -Properties * |  select -ExpandProperty LockedOut 
}
$data = @('s-qlik','s-runDB','s-runapp', 's-runsvc', 's-runcps', 's-runacc')
Checkaccount -account "s-archivDB"| Out-file "C:\scripts\Checkapp\psscripts_backend\accounts.txt"
foreach($account in $data){
Checkaccount -account "$account"| Out-file "C:\scripts\Checkapp\psscripts_backend\accounts.txt" -Append
}




