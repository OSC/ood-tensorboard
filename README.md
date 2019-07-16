# Tensorboard App

## Clone Repo and Set the Bin Scripts as executable

```shell
cd ./bin
chmod 755 setup python 
```

## Run the setup script

```shell
bin/setup
```

## Modify tensorboard.program

In /.venv/lib/python2.7/site-packages/tensorboard/program modify:

```python
tf.flags.DEFINE_string('logdir', '', """logdir specifies the directory where
TensorBoard will look to find TensorFlow event files that it can display.
TensorBoard will recursively walk the directory structure rooted at logdir,
looking for .*tfevents.* files.
```

To be:

```python
tf.flags.DEFINE_string('logdir', '/users/PZS0715/smansour/TensorboardTestbench/logs/', """logdir specifies the directory where
TensorBoard will look to find TensorFlow event files that it can display.
TensorBoard will recursively walk the directory structure rooted at logdir,
looking for .*tfevents.* files.

```

### Navigate to correct URL

Once you launch the app you must either go to

https://ondemand.osc.edu/pun/dev/Tensor/appone/

or 

https://ondemand.osc.edu/pun/dev/Tensor/apptwo/
