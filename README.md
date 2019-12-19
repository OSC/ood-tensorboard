# Tensorboard App

## Clone Repo and Set the Bin Scripts as executable

Version v0.0.1 is the current working version. The solution is brittle as it is coded against tensorboard included in tensorflow 1.9 and will need updated to work with later versions of tensorboard until we can cleanly deploy tensorboard as a Passenger app.

```shell
cd ~/ondemand/dev
git clone https://github.com/OSC/ood-tensorboard.git
git checkout v0.0.1
chmod 755 bin/setup bin/python 
```

## Run the setup script

```shell
bin/setup
```

Then access as a normal OnDemand Passenger app
