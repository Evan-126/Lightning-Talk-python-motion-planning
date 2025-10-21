## Common Issues we Stumbled Upon in Download Process

- Sometimes, `conda activate pmp` command fails, stating "conda init must be run first", and then running `conda init` gives no change. 
  In this case, Open PowerShell as Administrator and run:
  ``Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser``
  Then fully close and reopen powershell and try `conda activate pmp` again. 

- Be totally sure you have python-motion-planning version 1.1.1 installed, and NOT version 2.0.dev1
  can ensure this on download by running `pip install python-motion-planning==1.1.1` instead of simply `pip install python-motion-planning`
