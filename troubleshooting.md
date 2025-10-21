## Common Issues we Stumbled Upon in Download Process

- Sometimes, `conda activate pmp` command fails, stating "conda init must be run first", and then running `conda init` gives no change. 
  In this case, Open PowerShell as Administrator and run:
  ``Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser``
  Then fully close and reopen powershell and try `conda activate pmp` again. 
