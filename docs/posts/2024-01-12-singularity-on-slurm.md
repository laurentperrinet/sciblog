In this post, I will disp)lay my configuration that I use to run [Singularity](https://sylabs.io/singularity/) on a [SLURM](https://slurm.schedmd.com/) cluster. 

My use case is mostly using a recent version of pyTorch on GPUs.

<!-- TEASER_END -->

# Initialization: creating the container

The initialization of the process consists in creating the image that will be used by singularity. This is done by creating a definition file (here `pytorch.def`) that will be used by singularity to create the image. The definition file `pytorch.def` is the following:

```
Bootstrap:docker
From:continuumio/miniconda3:23.3.1-0

%environment

%runscript
. /etc/profile
conda activate pytorch
exec make

%post
# Create some common mountpoints for systems without overlayfs
mkdir /scratch
mkdir /apps

. /etc/profile
conda create --name pytorch
conda activate pytorch
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia
# conda install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch
conda install matplotlib numpy pandas jupyter nbconvert make scipy -c conda-forge
python3 -m pip install MotionClouds
```

The first line indicates that the image will be created from a docker image. The second line indicates the docker image that will be used. The `%environment` section is used to define the environment variables that will be used by the container. The `%runscript` section is used to define the command that will be executed when the container is run. The `%post` section is used to define the commands that will be executed when the container is created.

The command to create the container is the following:

```

$ singularity build pytorch.sif pytorch.def

```

# Using the container

Once created, the container can be used by running a set of commands. 

- login to the head of the cluster,

- connect to one node of the cluster :

```

$ srun -p volta  -t 6-12 --gres=gpu:1 --cpus-per-task=12 --pty bash -i

```
- run the container created above by connecting the `/scratch` folder:

```

$ singularity shell --bind /scratch:/scratch --nv pytorch.sif

```

- apply the profile :

```

$ Apptainer> . /etc/profile

```

- activate conda :

```

$ conda activate pytorch

```

- you are good to go :

```

$ ipython

Python 3.10.11 (main, Apr 20 2023, 19:02:41) [GCC 11.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.14.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import torch
In [2]: torch.cuda.is_available()
Out[2]: True

```
